# Mobile and IoT

## Overview

This category covers mobile device data analysis (with proper authorization or consent), mobile application permission analysis, Internet of Things (IoT) device discovery, and wireless network intelligence. This is a technically sensitive category: several of the underlying data types (device backups, app permissions, network scan data) can only be lawfully analyzed with proper authorization, consent, or reliance on already-public data. Every tool and script in this category is scoped to analyzing data you have lawfully obtained access to, not to capturing or intercepting it.

Each subfolder includes a ready-to-use, tested working script that analyzes data already collected through an authorized process (a consented chat export, a recorded app permission list, a Shodan-style export, or an authorized wireless site survey).

---

## Subfolders

| Subfolder | Description | Includes Working Files |
|---|---|---|
| [`mobile-forensics/`](mobile-forensics/README.md) | Analysis of consented/authorized mobile data exports | Chat export analyzer (Python) |
| [`app-analysis/`](app-analysis/README.md) | Mobile app permission and metadata analysis | App permission risk analyzer (Python) |
| [`iot-discovery/`](iot-discovery/README.md) | Identifying and categorizing internet-connected devices | IoT device banner classifier (Python) |
| [`wireless-intelligence/`](wireless-intelligence/README.md) | Wireless network configuration and naming analysis | Wi-Fi SSID risk analyzer (Python) |

---

## Authorization Requirements for This Category

- **Mobile device data** (backups, chat exports, call logs): only analyze data you own, or that you have the device owner's informed consent to analyze, or that you are authorized to examine under a documented legal process (e.g., a warrant, or an employer's device policy with appropriate legal basis).
- **App permission analysis**: this category covers analysis of publicly disclosed app store information and locally examined app manifests from apps you have legitimately installed or downloaded; it does not cover reverse engineering an app in violation of its terms of service.
- **IoT device discovery**: relies on passive, already-public internet-wide scan indices (see `technical-reconnaissance/network-scanning/README.md`); active probing of a specific IoT device requires the same authorization as any other active network scanning.
- **Wireless intelligence**: relies on data from an authorized wireless site survey (surveying your own network, or a network you have permission to assess); intercepting or decoding the content of wireless communications without authorization is both outside the scope of this repository and unlawful in most jurisdictions.

---

## Related Categories

- For the underlying passive/active network scanning distinction, see `technical-reconnaissance/network-scanning/README.md`.
- For general operational security while conducting device or app analysis, see `privacy-and-security/operational-security/README.md`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
