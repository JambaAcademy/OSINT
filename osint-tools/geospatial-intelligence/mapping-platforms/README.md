# Mapping Platforms

## Overview

This section covers interactive mapping platforms, geocoding services, and street-level imagery tools. See `geocode_lookup.py` in this folder for a ready-to-use script that converts addresses to coordinates and back using a free, public geocoding API.

---

## General Mapping Platforms

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Google Maps / Google Earth | Widely used mapping platform with satellite view, street view, and a very large points-of-interest database | General-purpose mapping and street-level visual reconnaissance | Free (API usage beyond free tier is paid) |
| Google Earth Pro | Desktop application with historical imagery, measurement tools, and KML support | Historical imagery comparison and detailed measurement | Free |
| OpenStreetMap | Free, open, crowd-sourced mapping platform | Base mapping data, especially useful where Google's coverage is weaker (some regions have more detailed OSM data) | Free |
| Bing Maps | Microsoft's mapping platform, including Bird's Eye oblique aerial imagery in some regions | Alternative aerial angle not available on other platforms | Free |
| Yandex Maps | Russian mapping platform with strong coverage of Russia and Eastern Europe, including street-level panoramas | Investigations involving Russian/CIS locations | Free |
| Baidu Maps | Leading Chinese mapping platform | Investigations involving locations in China | Free |
| what3words | Divides the world into 3x3 meter squares, each with a unique three-word address | Precise location-sharing/reference, increasingly used in emergency services and logistics | Free |

## Street-Level and Crowd-Sourced Imagery

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Google Street View | Street-level panoramic imagery integrated into Google Maps | Ground-level visual verification of a location's appearance | Free |
| Mapillary | Crowd-sourced street-level imagery platform (owned by Meta), with strong coverage contributed by volunteers | Alternative or supplementary street-level imagery, particularly in areas with limited Street View coverage or where more recent images have been contributed | Free |
| Wikimapia | Crowd-sourced platform layering user-contributed place descriptions and boundaries onto a map | Identifying informally known names/uses for a location beyond official mapping data | Free |

## Geocoding Services

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Nominatim (OpenStreetMap) | Free, open-source geocoding service built on OpenStreetMap data | Programmatic address-to-coordinate and coordinate-to-address lookups without an API key (subject to fair-use policy) | Free |
| Google Geocoding API | Commercial geocoding API with strong global address coverage | High-volume or high-accuracy commercial geocoding needs | Paid, with a limited free tier |
| What3Words API | Programmatic conversion between what3words addresses and coordinates | Integrating what3words references into a broader workflow | Freemium/Paid |

---

## Using the Included Geocoding Script

`geocode_lookup.py` uses the free, public OpenStreetMap Nominatim API to convert an address to coordinates (geocoding) or coordinates to an address (reverse geocoding), requiring only Python's standard library plus the `requests` package.

```bash
pip install requests --break-system-packages
python geocode_lookup.py --address "1600 Pennsylvania Avenue NW, Washington, DC"
python geocode_lookup.py --lat 38.8977 --lon -77.0365
```

See the script's header comment for Nominatim's usage policy, including its rate limit and required identification header, before running it at any volume.

---

## Usage Notes

- Different mapping platforms have different imagery capture dates for a given location; cross-reference the "imagery date" shown by the platform (where available) rather than assuming the displayed image reflects the current state of a location.
- Crowd-sourced platforms (OpenStreetMap, Mapillary, Wikimapia) can have gaps or inaccuracies in less-traveled areas; corroborate a crowd-sourced finding against an official/commercial platform where the finding is significant.

---

## Legal and Ethical Notes

- Free geocoding services such as Nominatim have usage policies (typically a maximum of one request per second and a requirement to identify your application) that must be respected; the included script is written to comply with this by default.
- Street-level imagery services capture publicly visible areas; using them to specifically track a private individual's residence or routine in a way that facilitates stalking is inconsistent with this repository's [Code of Conduct](../../../CODE_OF_CONDUCT.md) and the elevated standard in `people-investigation/README.md`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
