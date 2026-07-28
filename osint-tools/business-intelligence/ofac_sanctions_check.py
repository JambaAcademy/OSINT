#!/usr/bin/env python3
"""
ofac_sanctions_check.py

Screen a name against the U.S. Treasury Office of Foreign Assets Control's
(OFAC) Specially Designated Nationals (SDN) List, using OFAC's official,
free, publicly documented Sanctions List Service (SLS) data files.

Official data source:
    https://ofac.treasury.gov/sanctions-list-service
    File download endpoint pattern: https://sanctionslistservice.ofac.treas.gov/api/download/{filename}
    (e.g. SDN.CSV). OFAC can change file names or endpoints without notice;
    if this script's requests start failing, check the page above and the
    service's own /sanctions-lists endpoint for the current file names
    before assuming your code is at fault.

This is a SCREENING AID, not a replacement for a compliance department's
official sanctions screening process. It performs local fuzzy name
matching against OFAC's own published data and does not call any
third-party paid screening API. It does not screen the UN, EU, UK, or
other non-U.S. sanctions lists; see osint-tools/business-intelligence/
regulatory-monitoring/README.md for those sources.

IMPORTANT LIMITATIONS:
    - This script checks name similarity only. It does not check secondary
      identifiers (date of birth, nationality, address) that OFAC's SDN
      data also includes in its Advanced XML format. Any potential match
      MUST be manually reviewed against those additional identifiers
      before any action is taken, per
      osint-templates/specialized-formats/regulatory-compliance-report.md,
      Section 4.1.
    - A "no match" result from this script is not a compliance clearance.
      Organizations with a regulatory obligation to screen for sanctions
      exposure should use a properly validated, maintained compliance
      screening process or vendor, not a standalone research script.
    - The SDN List is one of several OFAC lists. See
      osint-tools/business-intelligence/regulatory-monitoring/README.md
      for the Consolidated List and other sanctions programs this script
      does not cover.

Requirements:
    Python 3.8+
    requests (pip install requests --break-system-packages)
    rapidfuzz (pip install rapidfuzz --break-system-packages)

Usage:
    python ofac_sanctions_check.py --name "Jordan A. Sample"
    python ofac_sanctions_check.py --name "Example Trading Company" --threshold 85
    python ofac_sanctions_check.py --name "Jordan Sample" --cache sdn_cache.csv

Configuration:
    Set your contact identification via the --contact argument or the
    OFAC_SLS_CONTACT environment variable. A descriptive User-Agent is
    good practice for any automated access to a government data service.
"""

import argparse
import csv
import io
import os
import sys
import time

try:
    import requests
except ImportError:
    sys.exit(
        "This script requires the 'requests' package.\n"
        "Install it with: pip install requests --break-system-packages"
    )

try:
    from rapidfuzz import fuzz
except ImportError:
    sys.exit(
        "This script requires the 'rapidfuzz' package.\n"
        "Install it with: pip install rapidfuzz --break-system-packages"
    )

SDN_CSV_URL = "https://sanctionslistservice.ofac.treas.gov/api/download/SDN.CSV"

# Documented OFAC SDN.CSV column layout (the file itself has no header row).
SDN_COLUMNS = [
    "ent_num", "sdn_name", "sdn_type", "program", "title",
    "call_sign", "vess_type", "tonnage", "grt", "vess_flag",
    "vess_owner", "remarks",
]


def build_headers(contact: str) -> dict:
    """Build a descriptive User-Agent header for the request."""
    contact = contact or "OSINT-Mastery-Guide-User (please set --contact or OFAC_SLS_CONTACT)"
    return {"User-Agent": contact}


def download_sdn_list(headers: dict, cache_path: str = None) -> list:
    """
    Download the current SDN.CSV file and return a list of dict records.
    If cache_path is given and exists, read from the cache instead of
    downloading again (useful for repeated runs during development/testing
    to avoid unnecessary load on OFAC's service).
    """
    if cache_path and os.path.exists(cache_path):
        print(f"Using cached SDN list at {cache_path} (delete this file to force a fresh download).")
        with open(cache_path, "r", encoding="utf-8", errors="replace") as f:
            raw_text = f.read()
    else:
        print("Downloading current SDN list from OFAC's Sanctions List Service...")
        response = requests.get(SDN_CSV_URL, headers=headers, timeout=30)
        response.raise_for_status()
        raw_text = response.text
        if cache_path:
            with open(cache_path, "w", encoding="utf-8") as f:
                f.write(raw_text)
            print(f"Cached raw SDN list to {cache_path}")

    reader = csv.reader(io.StringIO(raw_text))
    records = []
    for row in reader:
        if not row:
            continue
        # Pad or trim to the expected column count defensively, since OFAC's
        # remarks field can itself contain embedded commas in edge cases.
        row = (row + [""] * len(SDN_COLUMNS))[: len(SDN_COLUMNS)]
        records.append(dict(zip(SDN_COLUMNS, row)))
    return records


def screen_name(query_name: str, records: list, threshold: int) -> list:
    """Return records whose sdn_name fuzzy-matches query_name at or above threshold."""
    matches = []
    for record in records:
        score = fuzz.token_sort_ratio(query_name.lower(), record["sdn_name"].lower())
        if score >= threshold:
            matches.append((score, record))
    matches.sort(key=lambda pair: pair[0], reverse=True)
    return matches


def print_matches(query_name: str, matches: list) -> None:
    if not matches:
        print(f"\nNo matches at or above the specified threshold for '{query_name}'.")
        print("This is not a compliance clearance; see the script's limitations notice above.")
        return

    print(f"\n{len(matches)} potential match(es) found for '{query_name}':\n")
    for score, record in matches:
        print(f"Score: {score:.1f}  |  Name: {record['sdn_name']}  |  Type: {record['sdn_type']}  |  "
              f"Program: {record['program']}  |  Entity #: {record['ent_num']}")
        if record["remarks"]:
            print(f"    Remarks: {record['remarks'][:200]}")
    print(
        "\nManually review each potential match against secondary identifiers "
        "(date of birth, nationality, address, other listed aliases) before "
        "treating it as a confirmed match. Consider also checking OFAC's own "
        "Sanctions List Search tool at https://sanctionslist.ofac.treas.gov/ "
        "which includes fuzzy logic and additional identifying fields not "
        "present in the flat SDN.CSV file."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Screen a name against OFAC's Specially Designated Nationals (SDN) List."
    )
    parser.add_argument("--name", required=True, help="Name to screen, e.g. 'Jordan A. Sample'")
    parser.add_argument(
        "--threshold", type=int, default=80,
        help="Minimum fuzzy match score (0-100) to report as a potential match. Default 80.",
    )
    parser.add_argument(
        "--contact",
        default=os.environ.get("OFAC_SLS_CONTACT", ""),
        help="Contact identifier for the User-Agent header (e.g. 'Jane Analyst jane@example.com'). "
             "Defaults to the OFAC_SLS_CONTACT environment variable if set.",
    )
    parser.add_argument(
        "--cache",
        help="Optional local file path to cache the downloaded SDN list for reuse across runs.",
    )
    args = parser.parse_args()

    headers = build_headers(args.contact)
    start = time.time()
    records = download_sdn_list(headers, cache_path=args.cache)
    print(f"Loaded {len(records)} SDN records in {time.time() - start:.1f} seconds.")

    matches = screen_name(args.name, records, threshold=args.threshold)
    print_matches(args.name, matches)


if __name__ == "__main__":
    main()
