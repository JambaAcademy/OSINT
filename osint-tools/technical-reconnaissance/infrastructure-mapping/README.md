# Infrastructure Mapping

## Overview

Infrastructure mapping tools help identify which cloud provider, content delivery network, or hosting company an organization relies on, and how its technology stack fits together. This information supports due diligence, vendor concentration risk assessment, and general technical attribution work, largely through passive analysis of publicly observable indicators.

---

## Autonomous System and IP Range Lookup

| Tool | Description | Best For | Cost |
|---|---|---|---|
| BGP.he.net (Hurricane Electric BGP Toolkit) | Free lookup of autonomous system numbers, announced IP ranges, and peering relationships | Identifying which organization or ISP controls a given IP range | Free |
| RIPEstat | RIPE NCC's free tool for querying IP address and ASN registration data, primarily for European ranges | Detailed regional internet registry lookups for European IP space | Free |
| ARIN Whois | American Registry for Internet Numbers' lookup tool for IP allocation in the Americas | Confirming IP block ownership in North American ranges | Free |
| IPinfo.io | Commercial IP geolocation and ASN lookup API/service | Quick programmatic IP-to-organization and geolocation lookups | Freemium/Paid |

## CDN and Cloud Provider Identification

| Tool/Technique | Description | Best For | Cost |
|---|---|---|---|
| HTTP response header inspection | Many CDNs and cloud providers leave identifying headers (e.g., server headers, specific caching headers) in HTTP responses | Quick manual identification of CDN/cloud usage during general browsing or authorized assessment | Free, built-in (browser developer tools) |
| BuiltWith | Web-based technology profiler that identifies CDN, hosting, analytics, and many other technology categories used by a website | Broad technology stack fingerprinting from a single lookup | Freemium/Paid |
| Wappalyzer | Browser extension and API that identifies web technologies in use on a given site | Quick technology identification while browsing | Freemium/Paid |
| Cloud provider IP range publications | Major cloud providers (AWS, Azure, Google Cloud, and others) publish their own current IP address ranges | Confirming whether a given IP address belongs to a specific cloud provider's published range | Free |

## Hosting and Data Center Attribution

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Shodan / Censys (also listed in `network-scanning/`) | Internet-wide scan indices that include hosting provider and organization metadata alongside service data | Cross-referencing a host's technical footprint with its hosting attribution | Freemium/Paid |
| MaxMind GeoIP | Widely used IP geolocation database and lookup service | Approximate geographic attribution of an IP address (noting inherent accuracy limits of IP geolocation) | Freemium/Paid |

---

## Building an Infrastructure Map

A typical infrastructure mapping workflow combines several of the tools above:

1. Enumerate the organization's domains and subdomains (see `domain-analysis/`).
2. Resolve each to its current IP address and identify the owning ASN/organization (BGP.he.net, RIPEstat, ARIN Whois).
3. Identify CDN or cloud provider usage through header inspection or a technology profiler (BuiltWith, Wappalyzer).
4. Cross-reference against internet-wide scan indices for additional service and certificate metadata (Shodan, Censys).
5. Document findings using `osint-templates/technical-assessments/infrastructure-assessment.md`.

---

## Usage Notes

- IP geolocation accuracy varies considerably and is frequently inaccurate at the city level, even when reasonably accurate at the country level; avoid over-stating confidence in geolocation-derived findings.
- Technology profiler tools (BuiltWith, Wappalyzer) rely on detectable fingerprints and can miss technologies that have been deliberately obscured or that lack a distinctive fingerprint; treat their output as a strong lead rather than an exhaustive inventory.
- Cloud provider-published IP ranges update periodically; confirm you are checking against the current published range rather than a cached or outdated copy.

---

## Legal and Ethical Notes

- All techniques in this section rely on publicly available registry data, publicly observable HTTP responses, or vendor-published data, and do not require special authorization for passive research use.
- When infrastructure mapping is conducted as part of a due diligence or competitive intelligence exercise, ensure the scope remains proportionate to the stated business purpose, consistent with `osint-templates/operational-planning/osint-collection-plan.md`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
