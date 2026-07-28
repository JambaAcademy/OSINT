# Network Scanning

## Overview

This section covers tools for discovering hosts, open ports, and running services on network infrastructure. It is split between internet-wide scan index services, which are queried passively, and direct scanning tools, which actively send traffic to a target and therefore require explicit written authorization before use against any asset you do not own.

**Authorization requirement:** Do not use any active scanning tool listed in this section against a system unless you own it or have documented, written authorization to test it, as described in `osint-templates/technical-assessments/network-reconnaissance-report.md`, Section 1.1. Unauthorized scanning of systems you do not own or have permission to test may violate computer misuse laws in most jurisdictions.

---

## Internet-Wide Scan Index Services (Queried Passively)

These platforms conduct their own internet-wide scanning on an ongoing basis and make the results searchable. Querying their existing index does not send any traffic to the target system yourself, which is why these are generally treated as passive OSINT tools despite surfacing data originally gathered through active scanning performed by the service operator.

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Shodan | Searchable index of internet-connected devices and services, including banners, geolocation, and vulnerability tags | Discovering an organization's or device type's internet-facing footprint without scanning it yourself | Freemium/Paid |
| Censys | Similar internet-wide scan index to Shodan, with strong certificate and structured host data | Cross-referencing Shodan results and certificate-linked host discovery | Freemium/Paid |
| ZoomEye | Internet-wide scan index with strong coverage of Chinese and Asia-Pacific infrastructure | Regional coverage that may differ from Shodan/Censys | Freemium/Paid |
| FOFA | Internet-wide scan index and search platform, notable for coverage in the Chinese security research community | Cross-referencing device/service exposure across an additional independent index | Freemium/Paid |

## Direct Scanning Tools (Active — Authorization Required)

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Nmap | The standard open-source network discovery and port-scanning utility, supporting host discovery, port scanning, and service/version detection | Authorized reconnaissance of your own or a client's network as part of a documented engagement | Free, open source |
| Masscan | High-speed port scanner designed for scanning very large address ranges quickly | Authorized, large-scale internet-facing asset inventory scans | Free, open source |
| Nessus / OpenVAS | Vulnerability scanning platforms that go beyond port discovery to assess known vulnerabilities on discovered services | Authorized vulnerability assessment as part of a security engagement | Nessus: paid (limited free version); OpenVAS: free, open source |

---

## Choosing Between Passive Index Services and Direct Scanning

| Consideration | Favor Passive Index Services When... | Favor Direct Scanning When... |
|---|---|---|
| Authorization | You do not have explicit authorization to scan the target | You have documented, written authorization |
| Timing | You need results immediately without a scan window | You need current, real-time results and can schedule a scan |
| Stealth | You want to avoid alerting the target to your reconnaissance activity | Detectability is not a concern, or the engagement is an announced assessment |
| Coverage | The target may have services not indexed by any scan service | You need guaranteed coverage of the specific target's current state |

---

## Usage Notes

- Passive index services (Shodan, Censys, and similar) still require an account and, for meaningful query volume, typically a paid subscription; free tiers are usually sufficient only for light, occasional lookups.
- Internet-wide scan indices are not real-time; a host's listed open ports and banners reflect the date of the service's last scan of that host, which can be days to weeks old.
- When conducting authorized direct scanning, always scope the scan precisely to the addresses and ports covered by your authorization, and document the scan window in your report per `osint-templates/technical-assessments/network-reconnaissance-report.md`.

---

## Legal and Ethical Notes

- Direct scanning tools in this section are standard, widely used, legitimate network administration and security assessment utilities. Their inclusion here is not an endorsement of using them against any system without authorization.
- Some jurisdictions treat even non-disruptive port scanning of a system you do not own as a potential computer misuse offense regardless of intent; always confirm your authorization basis in writing before beginning.
- Rate-limit and scope any scan to avoid unintended denial-of-service impact on the target, even within an authorized engagement.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
