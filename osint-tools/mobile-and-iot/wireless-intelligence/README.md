# Wireless Intelligence

## Overview

This section covers analysis of wireless network configuration and naming data collected through an authorized wireless site survey (surveying your own network, or a network you have explicit permission to assess). See `wifi_ssid_risk_analyzer.py` in this folder for a ready-to-use script that flags Wi-Fi network names (SSIDs) matching common factory-default naming patterns, a well-established indicator of an unconfigured or minimally secured network.

**Authorization requirement:** This section covers analysis of wireless network data you have lawfully collected through an authorized site survey. It does not cover techniques for intercepting or decoding the content of wireless communications, which requires specific legal authorization in virtually every jurisdiction and is outside the scope of this repository.

---

## Wireless Site Survey Tools

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Kismet | Open-source wireless network detector and site survey tool, capable of passively observing broadcast network names and signal metadata | Authorized wireless site surveys and network inventory | Free, open source |
| Wireshark (in monitor mode, on an authorized network) | Widely used network protocol analyzer, usable for wireless site survey analysis on networks you are authorized to assess | Detailed protocol-level wireless network analysis on an authorized network | Free, open source |
| Built-in OS Wi-Fi scanning tools | Most operating systems can passively list nearby broadcast network names and signal strength without special software | Quick, basic wireless network inventory | Free, built-in |
| WiGLE | Crowd-sourced global database of wireless network observations, primarily used for research and coverage mapping | Understanding general wireless network density/patterns in a public dataset context | Free (registration required) |

---

## Using the Included SSID Risk Analyzer

`wifi_ssid_risk_analyzer.py` reads a CSV of observed network names (SSIDs) from an authorized site survey export and flags any that match common factory-default naming patterns (for example, a default SSID containing a manufacturer name and a partial MAC address, which typically indicates the network's administrator has never changed the router's default configuration, and may also still be using default administrative credentials).

```bash
python wifi_ssid_risk_analyzer.py --input ssid_survey.csv
```

See `sample_ssid_survey.csv` in this folder for the expected input format.

---

## Why Default SSIDs Matter

A network still using its factory-default SSID is a widely used proxy indicator that the network's administrator has likely not changed other default settings either, including the administrative password — since changing the SSID and changing the admin password are both steps in the same basic setup process that a factory-default SSID suggests was skipped. This is a standard, well-documented heuristic in wireless security assessment, not a guarantee.

---

## Usage Notes

- SSID naming pattern analysis is a proxy indicator, not direct evidence of a specific vulnerability; always confirm through an authorized, in-scope technical assessment before drawing conclusions about a specific network's actual security posture.
- Some organizations deliberately use a manufacturer-style default-looking SSID as a decoy while running a properly secured configuration; treat a flagged SSID as worth further authorized investigation, not as a confirmed finding.

---

## Legal and Ethical Notes

- Passively observing broadcast SSID names (which any Wi-Fi-enabled device does automatically to show available networks) is a normal and lawful part of using Wi-Fi technology.
- Connecting to a network without authorization, and any use of a discovered or default credential to access a network administrative interface without authorization, is unlawful in virtually every jurisdiction under computer misuse and unauthorized access statutes, regardless of how weak the network's security appears to be.
- This section does not cover, and this repository does not provide, techniques for capturing or decoding wireless traffic content (as opposed to passively observing broadcast network names), which requires specific legal authorization.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
