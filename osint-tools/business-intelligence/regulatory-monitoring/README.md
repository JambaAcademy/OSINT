# Regulatory Monitoring

## Overview

This section covers tools for monitoring regulatory filings, sanctions designations, and compliance-relevant public announcements. See `ofac_sanctions_check.py` in this folder for a ready-to-use script that screens a name against the U.S. Treasury's official, publicly downloadable sanctions list data.

---

## Sanctions and Watchlist Sources

| Resource | Description | Best For | Cost |
|---|---|---|---|
| OFAC Specially Designated Nationals (SDN) List | The U.S. Treasury's primary sanctions list, publicly published and updated regularly | Screening for U.S. sanctions exposure | Free |
| OFAC Consolidated Sanctions List | Combines the SDN list with several other OFAC sanctions programs into one dataset | Comprehensive U.S. sanctions screening | Free |
| UN Security Council Consolidated List | United Nations global sanctions list | International sanctions screening | Free |
| EU Consolidated Sanctions List | European Union sanctions list | EU sanctions screening | Free |
| UK OFSI Consolidated List | UK Office of Financial Sanctions Implementation sanctions list | UK sanctions screening | Free |
| World Bank Debarred Firms and Individuals | List of entities debarred from World Bank-financed projects due to fraud or corruption findings | Development finance and anti-corruption due diligence | Free |

## Regulatory Filing and Enforcement Monitoring

| Resource | Description | Best For | Cost |
|---|---|---|---|
| SEC EDGAR full-text search alerts | SEC EDGAR supports full-text search across filings; combine with the script in `financial-analysis/` for programmatic monitoring | Monitoring a company's or individual's mentions across new filings | Free |
| Regulator press release/enforcement action pages | Most financial, environmental, and safety regulators publish enforcement actions publicly (see `search-and-discovery/government-databases/`) | Tracking enforcement history relevant to due diligence | Free |
| RSS/news aggregation of regulatory announcements | Many regulators offer RSS feeds or email alert subscriptions for new announcements | Ongoing passive monitoring without manual re-checking | Free |

## Commercial Compliance Screening Platforms

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Refinitiv World-Check | Commercial politically exposed persons (PEP) and sanctions screening database | Enterprise-grade compliance screening with PEP coverage beyond raw sanctions lists | Paid, enterprise |
| Dow Jones Risk & Compliance | Commercial adverse media, PEP, and sanctions screening platform | Enterprise compliance screening integrated with adverse media search | Paid, enterprise |
| ComplyAdvantage | Compliance screening platform combining sanctions, PEP, and adverse media data with API access | Programmatic compliance screening integration | Paid |

---

## Using the Included OFAC Screening Script

`ofac_sanctions_check.py` downloads the U.S. Treasury's current, publicly published SDN list data and performs a local, fuzzy name match against a name you provide. It requires only Python's standard library plus the `requests` and `rapidfuzz` packages.

```bash
pip install requests rapidfuzz --break-system-packages
python ofac_sanctions_check.py --name "Jordan A. Sample"
python ofac_sanctions_check.py --name "Example Trading Company" --threshold 85
```

See the script's header comment for full usage details and important limitations, including that this script is a screening aid, not a substitute for a compliance department's official sanctions screening process.

---

## Usage Notes

- Sanctions list screening is prone to both false positives (common names) and false negatives (alternate name spellings, transliterations); any potential match should be manually reviewed against secondary identifiers (date of birth, nationality, other listed aliases) before any action is taken, consistent with `osint-templates/specialized-formats/regulatory-compliance-report.md` Section 4.1.
- Sanctions lists are updated frequently, sometimes with same-day effect; always confirm you are screening against the most current published list rather than a cached copy.

---

## Legal and Ethical Notes

- All sanctions list sources in this section are official government publications, free to download and use for screening purposes.
- A name match against a sanctions list carries significant legal and reputational consequence; organizations should have a documented escalation and review process before treating a match as confirmed, and should generally involve compliance/legal functions rather than relying on an automated script's output alone.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
