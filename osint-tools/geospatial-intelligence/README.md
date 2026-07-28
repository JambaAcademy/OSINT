# Geospatial Intelligence

## Overview

This category covers tools and techniques for location-based analysis: interactive mapping platforms, satellite and aerial imagery, tracking publicly broadcast location data (aircraft, vessels), and correlating multiple location-related data points to verify or establish a place, time, or movement pattern. Geospatial techniques are frequently used alongside the verification workflow in `osint-templates/specialized-formats/journalism-fact-check.md`.

Alongside tool directories, this category includes four ready-to-use working scripts/templates covering geocoding, sun-position-based chronolocation, image geolocation extraction, and cross-point geographic correlation.

---

## Subfolders

| Subfolder | Description | Includes Working Files |
|---|---|---|
| [`mapping-platforms/`](mapping-platforms/README.md) | Interactive maps, geocoding, and street-level imagery | Geocoding/reverse geocoding script (Python) |
| [`satellite-imagery/`](satellite-imagery/README.md) | Satellite and aerial imagery sources and change detection | Sun position calculator for chronolocation (Python) |
| [`location-tracking/`](location-tracking/README.md) | Publicly broadcast location data and image geolocation metadata | Image EXIF geolocation extractor (Python) |
| [`geographic-correlation/`](geographic-correlation/README.md) | Cross-referencing multiple location data points for consistency | Distance/bearing/feasibility calculator (Python) plus a verification worksheet (Markdown) |

---

## When to Use This Category

- Verifying the claimed location of a photo, video, or reported event as part of a fact-check or investigation (see `osint-templates/specialized-formats/journalism-fact-check.md`).
- Assessing change over time at a physical location (construction, environmental change, damage assessment).
- Establishing whether two reported sightings of the same subject are geographically and temporally consistent with each other.
- Understanding an organization's physical footprint as part of due diligence (see `business-intelligence/company-research/`).

---

## Legal and Ethical Notes for This Category

- Publicly broadcast location data (aircraft ADS-B transponder signals, vessel AIS signals) is legal to receive and aggregate in most jurisdictions and is commonly used for legitimate purposes (aviation safety research, maritime safety, journalism); some jurisdictions and platforms restrict redistribution of tracking data for certain categories of aircraft (for example, government or VIP aircraft that have requested blocking). Respect platform-level blocking requests and any applicable local restrictions.
- Satellite and aerial imagery providers vary in their licensing terms for derivative use (republishing, commercial use); confirm the specific provider's terms before republishing imagery.
- Location correlation techniques applied to a specific individual should be used consistent with the elevated standard described in `people-investigation/README.md`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
