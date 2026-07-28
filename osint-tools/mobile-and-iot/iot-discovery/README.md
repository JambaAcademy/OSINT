# IoT Discovery

## Overview

This section covers identifying and categorizing internet-connected devices (cameras, routers, industrial control systems, and other embedded devices) using passive, already-public internet-wide scan data — the same category of data source documented in `technical-reconnaissance/network-scanning/README.md`, applied specifically to IoT device identification. See `iot_banner_classifier.py` in this folder for a ready-to-use script that categorizes a list of discovered device banners/ports (for example, exported from a Shodan search) by likely device type, using common signature patterns.

**Authorization requirement:** As with all internet-wide scan index tools, querying an existing passive index (Shodan, Censys) is generally treated as passive. Any active probing of a specific IoT device requires the same written authorization as any other active network scanning; see `technical-reconnaissance/network-scanning/README.md`.

---

## IoT-Specific Search Platforms

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Shodan (also listed in `technical-reconnaissance/network-scanning/`) | Internet-wide scan index with strong IoT and industrial control system device coverage, including dedicated search filters for device categories | Discovering internet-facing IoT devices by type, manufacturer, or default banner | Freemium/Paid |
| Censys (also listed in `technical-reconnaissance/network-scanning/`) | Internet-wide scan index with structured device and certificate data | Cross-referencing Shodan IoT findings with an independent index | Freemium/Paid |
| ZoomEye (also listed in `technical-reconnaissance/network-scanning/`) | Internet-wide scan index with strong device and IoT coverage | Regional coverage cross-reference | Freemium/Paid |

## IoT Device Databases and Fingerprint References

| Resource | Description | Best For | Cost |
|---|---|---|---|
| Manufacturer default credential/banner databases | Various community-maintained references document default banners, ports, and credentials for common IoT device models | Identifying whether a discovered device is likely running factory-default configuration | Free, varies by source |
| IANA port number registry | Official registry of well-known and registered port numbers | Confirming the conventional purpose of a given port before assuming a device type | Free |

---

## Using the Included IoT Banner Classifier

`iot_banner_classifier.py` reads a CSV of discovered host/port/banner data (in the structure typically exported from Shodan or a similar internet-wide scan index) and classifies each entry into a likely device category (webcam/DVR, router/networking equipment, industrial control system, printer, media server, or unclassified) using common port and banner-text signature patterns.

```bash
python iot_banner_classifier.py --input scan_export.csv
```

See `sample_scan_export.csv` in this folder for the expected input format.

---

## Usage Notes

- Banner and port-based classification is a heuristic, not a certainty; a device can run a service on a non-standard port, or a banner can be altered or generic. Treat classification results as a starting point for further verification, not a final determination.
- Internet-wide scan index data reflects the date of the indexing service's last scan of that host, which can be days to weeks old; a device's exposure may have changed since.

---

## Legal and Ethical Notes

- Querying an existing internet-wide scan index is passive and does not require special authorization; directly connecting to or attempting to log into a discovered device does require explicit authorization, exactly as with any other active technique.
- Do not attempt to access a discovered IoT device using default or guessed credentials without explicit written authorization; doing so is likely to violate computer misuse laws regardless of how weak the device's security appears to be.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
