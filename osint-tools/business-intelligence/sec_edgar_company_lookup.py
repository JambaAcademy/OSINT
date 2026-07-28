#!/usr/bin/env python3
"""
sec_edgar_company_lookup.py

Look up a U.S. public company's SEC filing history and standardized
financial facts using the Securities and Exchange Commission's official,
free, publicly documented EDGAR data APIs:

    - Company ticker-to-CIK mapping: https://www.sec.gov/files/company_tickers.json
    - Filing history (submissions): https://data.sec.gov/submissions/CIK##########.json
    - Standardized XBRL financial facts: https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json

This script only queries publicly available government data and does not
require an API key. The SEC asks that all automated requests to its data
APIs include a descriptive User-Agent header identifying the requester
(name and contact email), and that request volume stay within its published
fair-access guidelines (a conservative default delay is applied between
requests in this script). See https://www.sec.gov/os/webmaster-faq#developers
for the SEC's current access guidelines before heavy or repeated use.

Legal and ethical scope:
    This script is intended for legitimate financial research, journalism,
    academic study, and business intelligence purposes, consistent with
    osint-templates/operational-planning/legal-compliance-checklist.md.
    It does not provide investment advice, and financial data retrieved
    with it should not be used to trade on the basis of anything that is
    not yet publicly disclosed.

Requirements:
    Python 3.8+
    requests (pip install requests --break-system-packages)

Usage:
    python sec_edgar_company_lookup.py --ticker AAPL
    python sec_edgar_company_lookup.py --name "Example Technologies"
    python sec_edgar_company_lookup.py --ticker MSFT --facts revenue
    python sec_edgar_company_lookup.py --ticker MSFT --output msft_filings.csv

Configuration:
    Set your contact identification via the --contact argument or the
    SEC_EDGAR_CONTACT environment variable, e.g.:
        export SEC_EDGAR_CONTACT="Jane Analyst janeanalyst@example.com"
    Do not hardcode personal contact details directly into this file if you
    plan to share or commit it; use the environment variable instead.
"""

import argparse
import csv
import json
import os
import sys
import time
from urllib.parse import quote

try:
    import requests
except ImportError:
    sys.exit(
        "This script requires the 'requests' package.\n"
        "Install it with: pip install requests --break-system-packages"
    )

TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL_TEMPLATE = "https://data.sec.gov/submissions/CIK{cik:0>10}.json"
COMPANY_FACTS_URL_TEMPLATE = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:0>10}.json"

# Conservative delay between requests, well within SEC's published rate guidance.
REQUEST_DELAY_SECONDS = 0.3

# A short list of commonly requested standardized XBRL financial concepts.
# Full concept names follow the "us-gaap" taxonomy used by SEC EDGAR.
COMMON_FACT_ALIASES = {
    "revenue": "Revenues",
    "net_income": "NetIncomeLoss",
    "total_assets": "Assets",
    "total_liabilities": "Liabilities",
    "cash": "CashAndCashEquivalentsAtCarryingValue",
    "eps": "EarningsPerShareDiluted",
}


def build_headers(contact: str) -> dict:
    """Build the required User-Agent header identifying the requester."""
    if not contact:
        sys.exit(
            "A contact identifier is required by SEC's fair-access guidelines.\n"
            "Pass --contact 'Your Name your.email@example.com' or set the "
            "SEC_EDGAR_CONTACT environment variable."
        )
    return {"User-Agent": contact, "Accept-Encoding": "gzip, deflate"}


def load_ticker_map(headers: dict) -> dict:
    """Download and return the SEC's ticker-to-CIK mapping as {TICKER: cik_int}."""
    response = requests.get(TICKER_MAP_URL, headers=headers, timeout=15)
    response.raise_for_status()
    raw = response.json()
    ticker_map = {}
    for entry in raw.values():
        ticker_map[entry["ticker"].upper()] = entry["cik_str"]
    return ticker_map


def find_cik_by_name(name_query: str, headers: dict) -> list:
    """Return a list of (ticker, title, cik) tuples whose title contains name_query."""
    response = requests.get(TICKER_MAP_URL, headers=headers, timeout=15)
    response.raise_for_status()
    raw = response.json()
    query_lower = name_query.lower()
    matches = []
    for entry in raw.values():
        if query_lower in entry["title"].lower():
            matches.append((entry["ticker"], entry["title"], entry["cik_str"]))
    return matches


def get_submissions(cik: int, headers: dict) -> dict:
    """Fetch the filing history / submissions record for a given CIK."""
    url = SUBMISSIONS_URL_TEMPLATE.format(cik=cik)
    time.sleep(REQUEST_DELAY_SECONDS)
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()


def get_company_facts(cik: int, headers: dict) -> dict:
    """Fetch standardized XBRL company facts for a given CIK."""
    url = COMPANY_FACTS_URL_TEMPLATE.format(cik=cik)
    time.sleep(REQUEST_DELAY_SECONDS)
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()


def summarize_recent_filings(submissions: dict, limit: int = 15) -> list:
    """Return a list of dicts summarizing the most recent filings."""
    recent = submissions.get("filings", {}).get("recent", {})
    rows = []
    forms = recent.get("form", [])
    for i in range(min(limit, len(forms))):
        rows.append({
            "form": forms[i],
            "filing_date": recent.get("filingDate", [])[i],
            "report_date": recent.get("reportDate", [])[i] if i < len(recent.get("reportDate", [])) else "",
            "accession_number": recent.get("accessionNumber", [])[i],
            "primary_document": recent.get("primaryDocument", [])[i],
        })
    return rows


def print_filing_summary(company_title: str, rows: list) -> None:
    print(f"\nMost recent filings for {company_title}:\n")
    print(f"{'Form':<10}{'Filing Date':<14}{'Report Date':<14}{'Accession Number':<24}")
    print("-" * 62)
    for row in rows:
        print(f"{row['form']:<10}{row['filing_date']:<14}{row['report_date']:<14}{row['accession_number']:<24}")


def print_fact_summary(company_facts: dict, fact_key: str) -> None:
    concept = COMMON_FACT_ALIASES.get(fact_key, fact_key)
    us_gaap = company_facts.get("facts", {}).get("us-gaap", {})
    if concept not in us_gaap:
        print(f"\nConcept '{concept}' was not found in this company's reported XBRL facts.")
        print(f"Available concepts (first 20 shown): {list(us_gaap.keys())[:20]}")
        return

    units = us_gaap[concept].get("units", {})
    print(f"\nReported values for {concept}:\n")
    for unit, entries in units.items():
        print(f"Unit: {unit}")
        # Only show annual (10-K) figures with a full fiscal period, most recent first
        annual_entries = [e for e in entries if e.get("form") == "10-K" and e.get("fp") == "FY"]
        annual_entries.sort(key=lambda e: e.get("end", ""), reverse=True)
        for entry in annual_entries[:8]:
            print(f"  FY ending {entry.get('end')}: {entry.get('val'):,} "
                  f"(filed {entry.get('filed')}, accession {entry.get('accn')})")


def write_csv(rows: list, output_path: str) -> None:
    if not rows:
        print("No rows to write.")
        return
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nWrote {len(rows)} rows to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Look up a company's SEC EDGAR filing history and financial facts."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--ticker", help="Stock ticker symbol, e.g. AAPL")
    group.add_argument("--name", help="Company name search query, e.g. 'Example Technologies'")
    parser.add_argument(
        "--contact",
        default=os.environ.get("SEC_EDGAR_CONTACT", ""),
        help="Contact identifier required by SEC (e.g. 'Jane Analyst jane@example.com'). "
             "Defaults to the SEC_EDGAR_CONTACT environment variable if set.",
    )
    parser.add_argument(
        "--facts",
        help="Alias or exact us-gaap concept name to summarize (e.g. revenue, net_income, "
             "total_assets, cash, eps, or an exact XBRL concept name).",
    )
    parser.add_argument(
        "--limit", type=int, default=15, help="Number of recent filings to display (default 15)."
    )
    parser.add_argument(
        "--output", help="Optional path to write the recent filings list as a CSV file."
    )
    args = parser.parse_args()

    headers = build_headers(args.contact)

    if args.ticker:
        ticker_map = load_ticker_map(headers)
        ticker = args.ticker.upper()
        if ticker not in ticker_map:
            sys.exit(f"Ticker '{ticker}' was not found in the SEC's ticker mapping.")
        cik = ticker_map[ticker]
        company_title = ticker
    else:
        matches = find_cik_by_name(args.name, headers)
        if not matches:
            sys.exit(f"No company titles matched '{args.name}'.")
        if len(matches) > 1:
            print(f"Multiple matches found for '{args.name}':\n")
            for ticker, title, cik in matches[:15]:
                print(f"  {ticker:<8} {title} (CIK {cik})")
            print("\nRe-run with --ticker using the specific ticker you want.")
            sys.exit(0)
        ticker, company_title, cik = matches[0]

    submissions = get_submissions(cik, headers)
    company_title = submissions.get("name", company_title)
    rows = summarize_recent_filings(submissions, limit=args.limit)
    print_filing_summary(company_title, rows)

    if args.output:
        write_csv(rows, args.output)

    if args.facts:
        company_facts = get_company_facts(cik, headers)
        print_fact_summary(company_facts, args.facts)


if __name__ == "__main__":
    main()
