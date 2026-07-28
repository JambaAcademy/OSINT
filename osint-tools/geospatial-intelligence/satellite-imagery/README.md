# Satellite Imagery

## Overview

This section covers sources of satellite and aerial imagery, along with change-detection technique guidance. See `sun_position_calculator.py` in this folder for a ready-to-use script that calculates the sun's position (elevation and azimuth) for a given location, date, and time — useful for verifying whether shadows visible in a photo or satellite image are consistent with its claimed capture date and time (a technique often called chronolocation).

---

## Satellite Imagery Sources

| Resource | Description | Best For | Cost |
|---|---|---|---|
| Google Earth Pro | Desktop application with a historical imagery slider showing past satellite captures for many locations | Comparing a location's appearance across multiple past dates | Free |
| Sentinel Hub / Copernicus Browser | Access to European Space Agency Sentinel satellite imagery, including multispectral data | Recent, relatively high-frequency satellite imagery with spectral analysis options | Free tier available; paid for higher volume/resolution |
| NASA Worldview | Near-real-time and historical NASA satellite imagery browser | Environmental and large-scale change monitoring | Free |
| USGS EarthExplorer | Access to Landsat and other USGS-managed satellite imagery archives | Long-term historical imagery archives (Landsat coverage extends back decades) | Free |
| Planet Labs | Commercial satellite imagery provider with frequent (near-daily) revisit rates | High-frequency commercial monitoring of a specific location | Paid, with limited free/educational access programs |
| Maxar / commercial high-resolution providers | Very high-resolution commercial satellite imagery, often used in conflict/disaster reporting | High-detail imagery for significant events, typically licensed per image or via subscription | Paid |

## Historical and Comparative Imagery Tools

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Google Earth Pro historical imagery | Built-in slider for viewing past captures at the same location | Quick, free before/after comparison | Free |
| Sentinel Hub EO Browser time-lapse tools | Generate time-lapse comparisons from Sentinel archive imagery | Visualizing gradual change over months/years | Free tier available |

---

## Chronolocation: Verifying Time and Date Using Shadows

Chronolocation is the technique of estimating or verifying the time of day (and, combined with other clues, the date) an image was captured by analyzing shadow length and direction relative to known landmarks. Combined with geolocation (establishing where an image was taken), this helps verify or refute a claimed timestamp.

### Using the Included Sun Position Calculator

`sun_position_calculator.py` computes the sun's elevation and azimuth angle for a given latitude, longitude, date, and UTC time, using standard solar position formulas. It requires only Python's standard library.

```bash
python sun_position_calculator.py --lat 48.8584 --lon 2.2945 --datetime "2026-06-15T14:30:00" --utc-offset 2
```

Compare the script's computed sun azimuth and elevation against the shadow direction and length visible in the image or satellite frame under review: a shadow points opposite the sun's azimuth, and its length relative to object height corresponds to the sun's elevation angle (lower elevation produces longer shadows). A significant mismatch between the computed sun position and the observed shadow is evidence the claimed date/time may be inaccurate, though local terrain, elevation, and atmospheric refraction introduce some margin of error worth accounting for.

---

## Usage Notes

- Satellite imagery capture dates are frequently not the same as the date you are viewing the imagery; always confirm the specific capture date shown by the platform (where available) rather than assuming "current" imagery reflects the present state of a location.
- Cloud cover, seasonal vegetation change, and sensor resolution all affect how reliably a satellite image can be compared across dates; note these limitations explicitly in any report drawing conclusions from satellite imagery comparison.
- Chronolocation using the sun position calculator provides a plausibility check, not absolute proof; combine it with other verification steps in `osint-templates/specialized-formats/journalism-fact-check.md`.

---

## Legal and Ethical Notes

- Satellite imagery providers vary in licensing terms for reproduction and redistribution; confirm the specific provider's license before republishing imagery in a report intended for external distribution.
- High-resolution commercial satellite imagery of a specific private individual's property, obtained and used to facilitate surveillance of that individual, is inconsistent with this repository's [Code of Conduct](../../../CODE_OF_CONDUCT.md); this section is intended for general geographic, environmental, and public-interest analysis.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
