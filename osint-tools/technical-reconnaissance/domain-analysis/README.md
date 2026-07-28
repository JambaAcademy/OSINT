# Domain Analysis

## Overview

Domain analysis tools cover WHOIS registration lookup, DNS record analysis, and passive historical domain research. These are entirely passive techniques that rely on already-public registry and DNS data, making them appropriate for general-purpose OSINT investigations without special authorization, subject to each specific database's terms of use.

---

## WHOIS Lookup Tools

| Tool | Description | Best For | Cost |
|---|---|---|---|
| ICANN Lookup | Official ICANN WHOIS lookup portal covering generic top-level domains | Authoritative baseline WHOIS lookup | Free |
| Registrar-specific WHOIS tools | Most domain registrars provide their own WHOIS lookup interface | Cross-checking results against the registrar of record | Free |
| WhoisXML API | Commercial WHOIS data provider with historical WHOIS records and bulk lookup capability | Historical WHOIS lookups, since current WHOIS often no longer shows change history directly | Freemium/Paid |
| DomainTools | Commercial domain intelligence platform with WHOIS history, reverse WHOIS, and risk scoring | Professional-grade domain investigation with historical ownership tracking | Paid |

## DNS Record Analysis Tools

| Tool | Description | Best For | Cost |
|---|---|---|---|
| dig / nslookup (command-line utilities) | Standard command-line DNS query tools available on most operating systems | Direct, precise DNS record lookups (A, MX, TXT, NS, and others) | Free, built-in |
| MXToolbox | Web-based DNS and mail server diagnostic tool suite | Quick DNS/MX/SPF/DKIM/DMARC checks without command-line access | Free (with paid monitoring tiers) |
| SecurityTrails | DNS and domain intelligence platform with historical DNS record data | Historical DNS resolution tracking (passive DNS) | Freemium/Paid |
| ViewDNS.info | Collection of free web-based DNS and domain lookup utilities | Quick, no-signup DNS and reverse lookup checks | Free |

## Passive DNS and Historical Resolution

| Tool | Description | Best For | Cost |
|---|---|---|---|
| SecurityTrails (also listed above) | Maintains historical passive DNS records showing prior IP resolutions for a domain | Tracing a domain's infrastructure history and hosting migrations | Freemium/Paid |
| RiskIQ / Microsoft Defender Threat Intelligence (passive DNS component) | Enterprise threat intelligence platform with passive DNS and infrastructure history | Deep infrastructure attribution research, typically in an enterprise security context | Paid |
| Farsight DNSDB (or similar passive DNS providers) | Widely used passive DNS data provider in the threat intelligence community | Historical DNS research at scale for security research purposes | Paid, with research access tiers in some cases |

## Subdomain Enumeration (Passive)

| Tool | Description | Best For | Cost |
|---|---|---|---|
| crt.sh | Free web interface for searching certificate transparency logs, frequently used to enumerate subdomains that have had a certificate issued | Passive subdomain discovery without touching the target directly | Free |
| Subfinder (open source) | Command-line tool aggregating multiple passive subdomain data sources into one query | Efficient passive subdomain enumeration for authorized assessments or your own assets | Free, open source |
| Amass (open source, OWASP project) | Comprehensive passive (and optionally active) attack surface mapping tool | In-depth passive reconnaissance combining many data sources | Free, open source |

---

## Usage Notes

- WHOIS privacy protection services are extremely common; the absence of registrant detail in WHOIS is not itself suspicious and should not be treated as an indicator of malicious intent on its own (see `osint-templates/technical-assessments/domain-website-analysis-report.md` for a fuller framework on assessing domain legitimacy).
- Passive DNS data providers vary in their historical depth and geographic/registrar coverage; cross-check findings across at least two providers where the finding is significant to an investigation's conclusions.
- Command-line DNS tools (dig, nslookup) query DNS resolvers directly and are effectively invisible to the domain owner; they carry no meaningful passive/active distinction concern since DNS resolution is a normal, expected part of internet functioning.

---

## Legal and Ethical Notes

- All tools in this section rely on publicly published registry and DNS data and do not require special authorization to use for research purposes.
- Some commercial domain intelligence platforms restrict permissible use of their historical WHOIS data in their terms of service (for example, restricting resale or certain automated bulk uses); review the specific platform's terms before building a recurring workflow around it.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
