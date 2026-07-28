# Technical Reconnaissance

## Overview

This category covers tools used to analyze domains, network infrastructure, digital certificates, and hosting environments. Passive techniques (WHOIS, passive DNS, certificate transparency) are appropriate for general OSINT work using only publicly available data. Active techniques (port scanning, service enumeration) require explicit authorization, as described in `osint-templates/technical-assessments/network-reconnaissance-report.md`, and should only be performed against assets you own or have written permission to test.

---

## Subfolders

| Subfolder | Description |
|---|---|
| [`domain-analysis/`](domain-analysis/README.md) | WHOIS, DNS, and passive domain research tools |
| [`network-scanning/`](network-scanning/README.md) | Active and passive service/port discovery tools (authorized use only) |
| [`certificate-analysis/`](certificate-analysis/README.md) | TLS/SSL certificate and certificate transparency log tools |
| [`infrastructure-mapping/`](infrastructure-mapping/README.md) | Hosting provider, CDN, and cloud infrastructure identification tools |

---

## Passive vs. Active Techniques: A Critical Distinction

| Technique Type | Examples | Authorization Required? |
|---|---|---|
| Passive | WHOIS lookup, passive DNS history, certificate transparency log search, publicly available internet-wide scan indices (e.g., previously published scan results) | No — relies solely on already-public data |
| Active | Port scanning, direct service banner grabbing, vulnerability scanning, any technique that sends traffic directly to the target for the purpose of probing it | Yes — requires written authorization from the asset owner or an equivalent lawful basis |

This repository documents both categories because both are legitimate parts of authorized security assessment practice, but the authorization requirement for active techniques is not optional. See `osint-templates/technical-assessments/network-reconnaissance-report.md` Section 1.1 for the authorization documentation this repository expects before active scanning is performed.

---

## When to Use This Category

- Assessing your own organization's external attack surface as part of an authorized security review.
- Investigating a domain's legitimacy or ownership as part of a fraud or brand-protection investigation (passive techniques only).
- Supporting an authorized penetration test or red team engagement's reconnaissance phase.
- Correlating infrastructure across multiple domains to support attribution in a threat intelligence investigation (passive techniques only).

---

## Related Categories

- For assessing overall hosting/vendor dependency posture, see `business-intelligence/` for the organizational context and `osint-templates/technical-assessments/infrastructure-assessment.md` for the report format.
- For AI-assisted correlation of technical indicators, see `ai-powered-tools/pattern-analysis/`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
