# Geographic Correlation

## Overview

This section covers techniques for cross-referencing multiple location-related data points to assess consistency, such as verifying whether two reported sightings of the same subject are geographically and temporally feasible, or correlating a set of location clues to narrow down a search area. See `geolocation_correlation_calculator.py` for a distance/bearing/travel-feasibility calculator, and `geolocation-verification-worksheet.md` for a structured worksheet to document a full geolocation verification exercise.

---

## Techniques and Concepts

| Technique | Description | Best For |
|---|---|---|
| Distance and bearing calculation | Computing the straight-line distance and compass bearing between two coordinate pairs | Assessing whether two locations are close enough to be relevant, or determining direction of travel |
| Travel-time feasibility analysis | Comparing the distance between two claimed sighting locations against the time elapsed and plausible travel modes/speeds | Assessing whether two reported sightings of the same subject are physically possible |
| Landmark triangulation | Using multiple identifiable landmarks visible in an image to narrow down a specific location | Precise geolocation of a photo or video without embedded GPS data |
| Timezone cross-referencing | Confirming that a claimed local time is consistent with the timezone of the claimed location | Detecting inconsistencies in a claimed timeline |
| Multi-source convergence | Combining independent geolocation methods (EXIF data, visual landmarks, shadow analysis, claimed statements) and checking whether they converge on the same location | Building higher-confidence geolocation conclusions from imperfect individual signals |

---

## Supporting Tools

| Tool | Description | Best For | Cost |
|---|---|---|---|
| GeoHack / Wikipedia coordinate templates | Aggregates links to multiple mapping services for a given coordinate pair | Quickly cross-checking a coordinate across several map providers at once | Free |
| SunCalc | Web-based sun and moon position visualizer for a given location and date | Visual, interactive alternative/supplement to `satellite-imagery/sun_position_calculator.py` | Free |
| Overpass Turbo (OpenStreetMap query tool) | Query OpenStreetMap data for specific feature types within an area (e.g., all gas stations within a radius) | Narrowing down a location based on visible landmark types and their relative arrangement | Free |

---

## Using the Included Correlation Calculator

`geolocation_correlation_calculator.py` computes the great-circle distance and initial compass bearing between two coordinate pairs, and assesses whether the distance is feasible given an elapsed time and a chosen travel mode's typical speed range. It requires only Python's standard library.

```bash
python geolocation_correlation_calculator.py \\
    --lat1 48.8584 --lon1 2.2945 --time1 "2026-06-15T09:00:00" \\
    --lat2 51.5074 --lon2 -0.1278 --time2 "2026-06-15T12:00:00" \\
    --mode commercial_flight
```

---

## Using the Geolocation Verification Worksheet

`geolocation-verification-worksheet.md` provides a structured, fillable worksheet for documenting a full geolocation verification exercise: initial claim, candidate locations, supporting/contradicting evidence for each, and a final confidence assessment. It follows the same source-rating conventions as `osint-templates/operational-planning/source-verification-framework.md`.

---

## Usage Notes

- Great-circle distance calculations assume travel "as the crow flies"; actual travel distance by road, rail, or sea will typically be longer, so use the great-circle distance as a lower bound on required travel time, not an exact prediction.
- Travel-time feasibility analysis is a falsification tool: it is most useful for ruling out an impossible claim (insufficient time for any plausible travel mode to cover the distance) rather than confirming a claim is true, since satisfying the minimum time requirement does not prove the claimed travel actually occurred.

---

## Legal and Ethical Notes

- Geographic correlation techniques applied to establish a specific individual's movements should be used consistent with the elevated standard in `people-investigation/README.md`; this is a category where the same technique can serve legitimate verification (confirming a public figure's whereabouts for a news story) or improper surveillance (tracking a private individual's movements) depending entirely on the purpose and target.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
