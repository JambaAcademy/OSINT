# Location Tracking

## Overview

This section covers tools for working with publicly broadcast location data (aircraft, marine vessels) and location metadata embedded in digital files. See `extract_image_geolocation.py` in this folder for a ready-to-use script that extracts GPS coordinates embedded in an image's EXIF metadata.

---

## Aircraft Tracking

| Tool | Description | Best For | Cost |
|---|---|---|---|
| ADS-B Exchange | Aggregates unfiltered ADS-B aircraft transponder data from a global network of volunteer receivers | Tracking aircraft movements, including some aircraft filtered from other trackers | Free (with a paid API tier for high-volume programmatic access) |
| FlightRadar24 | Widely used flight tracking platform with a large receiver network and historical playback | General-purpose flight tracking and route history | Freemium/Paid |
| FlightAware | Flight tracking platform with strong North American coverage and historical data | Flight tracking, delay/route analysis | Freemium/Paid |

## Marine Vessel Tracking

| Tool | Description | Best For | Cost |
|---|---|---|---|
| MarineTraffic | Aggregates AIS (Automatic Identification System) vessel transponder data globally | Tracking commercial vessel movements and port calls | Freemium/Paid |
| VesselFinder | Similar AIS-based vessel tracking platform | Cross-checking vessel position and history against another independent source | Freemium/Paid |

## Image and Video Geolocation Metadata

| Tool | Description | Best For | Cost |
|---|---|---|---|
| ExifTool | Comprehensive command-line metadata reading/writing tool supporting a very wide range of file formats | Detailed, authoritative metadata extraction, including GPS, camera model, and timestamp fields | Free, open source |
| Built-in OS/photo app metadata viewers | Most operating systems and photo management apps display basic embedded location metadata | Quick manual check without installing additional tools | Free, built-in |
| Online EXIF viewers | Various web-based tools allow uploading an image to view its embedded metadata | Quick one-off checks without local tool installation (be mindful of uploading sensitive images to third-party sites) | Free |

---

## Using the Included EXIF Geolocation Extractor

`extract_image_geolocation.py` reads an image file's embedded EXIF metadata and extracts GPS coordinates (if present), along with the camera timestamp and basic camera/device information. It requires only the `Pillow` Python package.

```bash
pip install Pillow --break-system-packages
python extract_image_geolocation.py --file photo.jpg
```

Many images no longer contain GPS metadata by the time they reach an OSINT analyst, because major social media and messaging platforms strip EXIF data on upload as a privacy protection measure. This script is most useful for images obtained directly (e.g., provided by a source, downloaded from a personal website or blog, or received via email) rather than images downloaded from major social platforms.

---

## Usage Notes

- The absence of GPS metadata in an image does not mean the image lacks location context; it may simply have been stripped by the platform it passed through, or the capturing device may not have had location services enabled. Rely on the visual geolocation techniques cross-referenced in `osint-templates/specialized-formats/journalism-fact-check.md` as a fallback.
- Public flight and vessel tracking data can be delayed, filtered (some operators request their aircraft/vessel be excluded from public trackers), or occasionally spoofed (particularly AIS data, which is self-reported by the vessel); treat unusually anomalous tracking data with appropriate skepticism and cross-reference against a second provider where the finding is significant.
- EXIF timestamps reflect the camera's internal clock setting, which may not be accurate or may not reflect the correct time zone; do not assume the embedded timestamp is authoritative without cross-verification.

---

## Legal and Ethical Notes

- Extracting metadata from an image you have lawfully obtained access to is a standard and appropriate OSINT/verification technique.
- Using image geolocation extraction specifically to determine a private individual's home address, workplace, or routine location from images they did not intend to share publicly (for example, images obtained through a private/restricted account) falls outside the scope of lawful, ethical OSINT and is inconsistent with this repository's [Code of Conduct](../../../CODE_OF_CONDUCT.md).
- Public flight and vessel tracking data is broadcast for safety purposes and its aggregation for tracking is common and lawful in most jurisdictions; some jurisdictions restrict republishing tracking data for specific aircraft categories (for example, certain government aircraft), which reputable trackers already filter by default.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
