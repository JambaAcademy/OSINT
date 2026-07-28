# Geolocation Verification Worksheet

## Purpose Statement

This worksheet structures the process of verifying or determining the location depicted in an image, video, or claimed in a statement, by systematically documenting candidate locations and the evidence for and against each. It complements `osint-templates/specialized-formats/journalism-fact-check.md` and uses the same source-rating conventions as `osint-templates/operational-planning/source-verification-framework.md`.

---

## 1. Case Information

**Case/Project ID:** [Unique identifier]
**Media/Claim Under Review:** [Brief description; reference the file or claim text]
**Claimed Location:** [As stated by the source, if any]
**Claimed Date/Time:** [As stated by the source, if any]
**Analyst:** [Name]
**Date of Analysis:** [Date]

---

## 2. Initial Observations from the Media Itself

### 2.1 Embedded Metadata

- **EXIF GPS Data Present:** [Yes/No — see `location-tracking/extract_image_geolocation.py`]
- **Coordinates (if present):** [Lat, Lon]
- **Embedded Timestamp (if present):** [Value, and note that camera clocks can be inaccurate]

### 2.2 Visual Landmarks Identified

| Landmark | Description | Distinctiveness (High/Medium/Low) |
|---|---|---|
| [Landmark 1] | [Description] | [Rating] |
| [Landmark 2] | [Description] | [Rating] |
| [Landmark 3] | [Description] | [Rating] |

### 2.3 Environmental Clues

- **Language(s) visible on signage:** [List]
- **Vehicle types/license plate style:** [Description]
- **Architecture style:** [Description]
- **Vegetation/climate indicators:** [Description]
- **Traffic direction (left/right-hand):** [Observation]

### 2.4 Shadow and Lighting Analysis (Chronolocation)

- **Shadow direction observed:** [Description or approximate compass bearing]
- **Shadow length relative to object height:** [Description]
- **Computed sun position for claimed date/time/location (via `satellite-imagery/sun_position_calculator.py`):** [Elevation/azimuth]
- **Consistency assessment:** [Consistent / Inconsistent / Inconclusive]

---

## 3. Candidate Locations

List each candidate location under consideration, with supporting and contradicting evidence for each.

### Candidate 3.1: [Location Name/Description]

**Coordinates:** [Lat, Lon]

**Supporting Evidence:**

- [Evidence item] — Source: [Citation] — Reliability: [A-F per source-verification-framework.md]

**Contradicting Evidence:**

- [Evidence item] — Source: [Citation] — Reliability: [A-F]

**Confidence in This Candidate:** [High/Medium/Low]

---

### Candidate 3.2: [Location Name/Description]

[Repeat structure for each additional candidate]

---

## 4. Cross-Referencing Tools Used

- [ ] Reverse image search (see `social-media-intelligence/cross-platform-analyzers/README.md`)
- [ ] Mapping platform street-level imagery comparison (see `mapping-platforms/README.md`)
- [ ] Satellite imagery comparison (see `satellite-imagery/README.md`)
- [ ] Geocoding of a candidate address (see `mapping-platforms/geocode_lookup.py`)
- [ ] Sun position / chronolocation check (see `satellite-imagery/sun_position_calculator.py`)
- [ ] Distance/feasibility check against another claimed sighting (see `geolocation_correlation_calculator.py`)

---

## 5. Final Assessment

**Determined Location:** [Best-supported candidate, or "Undetermined" if evidence is insufficient]

**Overall Confidence:** [High/Medium/Low]

**Reasoning:** [Narrative synthesis of why this candidate is best supported, referencing the strongest corroborating evidence and explaining why alternative candidates were less well supported]

**Unresolved Questions:** [Note anything that remains uncertain]

---

## 6. Source List

- [Source 1]: [Citation] — [Access date]
- [Source 2]: [Citation] — [Access date]

---

## 7. Version Control

**Version:** [Version number]
**Last Updated:** [Date]

---

*This worksheet documents a geolocation verification process for internal analytical use. When findings from this worksheet are included in a final report, use the appropriate report template (e.g., `osint-templates/specialized-formats/journalism-fact-check.md`) rather than distributing this worksheet directly.*
