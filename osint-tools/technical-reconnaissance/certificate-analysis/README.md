# Certificate Analysis

## Overview

TLS/SSL certificate data is one of the richest passive sources of infrastructure intelligence available: certificates reveal subdomains through Subject Alternative Names, can link seemingly unrelated domains through shared certificate issuance patterns, and provide a timeline of a domain's operational history through certificate transparency logs. All techniques in this section are passive and rely on publicly logged, already-public certificate data.

---

## Certificate Transparency Log Search

| Tool | Description | Best For | Cost |
|---|---|---|---|
| crt.sh | Free, widely used web interface for searching certificate transparency logs by domain, organization, or certificate fingerprint | Passive subdomain discovery and certificate issuance history | Free |
| Censys Certificates | Certificate search integrated into the broader Censys platform, with structured filtering | Advanced certificate search with additional structured metadata | Freemium/Paid |
| Google Certificate Transparency Search tools / community CT search frontends | Various frontends built on the underlying certificate transparency log network | Cross-checking crt.sh results against an independent frontend | Free |

## Direct Certificate Inspection

| Tool/Technique | Description | Best For | Cost |
|---|---|---|---|
| Browser certificate viewer | Every modern browser allows direct inspection of a site's presented certificate, including issuer, validity dates, and Subject Alternative Names | Quick, no-tool-needed manual certificate inspection during general browsing | Free, built-in |
| OpenSSL command-line tool | Standard open-source toolkit that can retrieve and parse a certificate directly from a live server | Scriptable, detailed certificate inspection as part of an authorized technical assessment | Free, open source |
| SSL Labs (Qualys SSL Server Test) | Free web-based tool providing a detailed grade and configuration analysis of a server's TLS setup | Assessing TLS configuration quality/security posture of a public-facing server you are authorized to assess | Free |

---

## Using Certificates for Infrastructure Correlation

### Subject Alternative Name (SAN) Analysis

A single certificate frequently covers multiple subdomains or even multiple distinct domains via its Subject Alternative Names field. Reviewing SAN entries on a certificate is one of the fastest ways to discover related infrastructure that would not otherwise be found through search engines.

### Certificate Reuse and Shared Infrastructure

Organizations that manage many domains sometimes reuse the same certificate, the same issuing pattern, or the same certificate authority account across otherwise unrelated-looking domains. Consistent patterns in issuance timing, issuer, or SAN grouping across domains can indicate common ownership or management, though this should be treated as a lead requiring corroboration rather than proof on its own, consistent with `osint-templates/technical-assessments/domain-website-analysis-report.md`.

### Certificate Issuance Timeline

Certificate transparency logs provide a reliable, tamper-evident timeline of when a domain's certificates were issued and renewed, which can help establish when a domain became operationally active or when its infrastructure changed hands, particularly useful when WHOIS data has been altered or is privacy-protected.

---

## Usage Notes

- Certificate transparency logging has been standard practice among major certificate authorities and is enforced by modern browsers, meaning nearly any certificate issued in recent years will appear in a CT log search; the absence of any CT log entry for a domain claiming to use HTTPS is itself a notable finding worth investigating further.
- Wildcard certificates (covering an entire subdomain space with a single entry) will not reveal individual subdomain names through SAN inspection; in that case, rely on the passive subdomain enumeration tools documented in `domain-analysis/README.md` instead.

---

## Legal and Ethical Notes

- Certificate transparency log data and direct inspection of a certificate presented to any visitor during normal browsing are both fully public and passive; no special authorization is required to search or inspect this data.
- Direct certificate retrieval via OpenSSL against a live server, while low-impact, still constitutes a direct interaction with the target and should be scoped consistently with any active-technique authorization requirements documented for the broader engagement.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
