# Financial Analysis

## Overview

This section covers tools for locating and analyzing company financial filings and statements. See `sec_edgar_company_lookup.py` in this folder for a ready-to-use script that queries the SEC's official, free, public EDGAR data API.

---

## Public Filing Sources

| Resource | Description | Best For | Cost |
|---|---|---|---|
| SEC EDGAR | Full-text and structured search of U.S. public company filings (10-K, 10-Q, 8-K, proxy statements, Forms 3/4/5, Schedule 13D/G) | Authoritative U.S. public company financial and ownership filings | Free |
| SEC EDGAR company facts API | Structured, machine-readable API providing standardized financial data extracted from filings | Programmatic financial data retrieval without manual filing parsing | Free |
| SEDAR+ | Canadian public company filing system | Canadian public company filings | Free |
| Companies House (UK) accounts filings | UK company registry includes filed annual accounts for many company types | UK company financial statement lookup | Free |
| Annual report archives (company investor relations pages) | Primary-source annual/integrated reports, often with more narrative detail than regulatory filings alone | Understanding management's own framing of financial performance | Free |

## Financial Data Aggregators and Analysis Platforms

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Yahoo Finance / Google Finance | Free financial data aggregators with historical price data, basic financial statements, and news | Quick, free baseline financial snapshot | Free |
| Morningstar | Financial data and analysis platform, including fund and equity research | Investment-oriented financial analysis with analyst commentary | Freemium/Paid |
| Bloomberg Terminal | Institutional-grade financial data and analytics platform | Comprehensive, real-time financial market and company data | Paid, enterprise |
| S&P Capital IQ | Institutional financial data and screening platform | Detailed comparable-company and financial screening analysis | Paid, enterprise |

## Financial Ratio and Statement Analysis Concepts

| Concept | What It Measures | Typical Use |
|---|---|---|
| Liquidity ratios (current ratio, quick ratio) | Ability to meet short-term obligations | Assessing short-term financial health |
| Leverage ratios (debt-to-equity, interest coverage) | Reliance on debt financing and ability to service it | Assessing financial risk and capital structure |
| Profitability ratios (gross margin, net margin, ROE, ROA) | Efficiency of converting revenue/assets into profit | Assessing operational performance |
| Valuation multiples (P/E, EV/EBITDA) | Market valuation relative to earnings/cash flow | Comparing valuation across similar companies |

---

## Using the Included SEC EDGAR Script

`sec_edgar_company_lookup.py` queries the SEC's public, unauthenticated EDGAR data API to retrieve a company's filing history and standardized financial facts by ticker or company name. It requires only Python's standard library plus the `requests` package.

```bash
pip install requests --break-system-packages
python sec_edgar_company_lookup.py --ticker AAPL
python sec_edgar_company_lookup.py --name "Example Technologies"
```

See the script's header comment for full usage details, including the SEC's requirement that all API requests include a descriptive `User-Agent` header identifying the requester, per SEC's published fair-access guidelines.

---

## Usage Notes

- SEC EDGAR's structured company facts API standardizes data across companies using XBRL tagging, which makes cross-company comparison easier but occasionally differs slightly from the "headline" figures a company emphasizes in its own press releases; when the two differ, the filed figure is the authoritative one for compliance purposes.
- Financial ratios are most meaningful compared against industry peers and the company's own historical trend, not evaluated in isolation.

---

## Legal and Ethical Notes

- SEC EDGAR and other government filing systems are fully public and free to query; the included script respects SEC's published access guidelines regarding request identification and rate limiting.
- Do not use financial analysis findings to make trading decisions based on any information that is not yet public (material non-public information); this repository's tools and templates are for research and reporting purposes and do not constitute investment advice.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
