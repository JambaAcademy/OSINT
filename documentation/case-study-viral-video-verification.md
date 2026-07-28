# Case Study: Verifying a Viral Video's Authenticity

## Disclaimer

This case study is entirely fictional. All names, locations, and identifying details are invented for illustrative purposes. Any resemblance to real events is coincidental.

---

## Background

A video began circulating on social media claiming to show severe storm damage in "Rivermouth" (a fictional coastal town), allegedly filmed "this morning." A regional news outlet's verification desk was asked to confirm whether the video was genuine and current before the outlet reported on it, following `osint-templates/specialized-formats/journalism-fact-check.md`.

---

## Stage 1: Claim Breakdown

The fact-checker broke the claim into its component, individually verifiable parts, per `osint-templates/specialized-formats/journalism-fact-check.md` Section 3:

1. The footage shows real storm damage (not staged or digitally altered).
2. The footage was filmed in Rivermouth specifically.
3. The footage was filmed "this morning" (i.e., matches the claimed recent timeframe).

---

## Stage 2: Reverse Image Search

Using the tools in `osint-tools/social-media-intelligence/cross-platform-analyzers/README.md`, the fact-checker extracted several video frames and ran them through reverse image search.

**Finding:** No earlier appearance of this specific footage was found — a good sign for authenticity (it did not appear to be recycled footage from a past, unrelated event), though the fact-checker noted this is not conclusive on its own, since genuinely new footage would also produce no prior matches.

---

## Stage 3: Geolocation

Using the techniques in `osint-tools/geospatial-intelligence/geographic-correlation/README.md`, the fact-checker identified a distinctive building facade and a partial street sign visible in the footage.

- Cross-referencing the building facade against Google Street View imagery for Rivermouth's waterfront district using `osint-tools/geospatial-intelligence/mapping-platforms/README.md` confirmed a strong visual match to a specific intersection.
- The `geolocation-verification-worksheet.md` template was used to formally document this candidate location, its supporting evidence, and confidence rating (assessed as **High** — a distinctive, multi-story building with an unusual roofline is a strong, low-ambiguity match).

**Claim component 2 (location) assessed as: Confirmed, high confidence.**

---

## Stage 4: Chronolocation

This is where the investigation became most interesting. Using `osint-tools/geospatial-intelligence/satellite-imagery/sun_position_calculator.py`, the fact-checker calculated the expected sun position for Rivermouth's coordinates at the claimed filming time ("this morning," interpreted as approximately 8:00 AM local time based on the accompanying social media post's timestamp).

- The calculated sun azimuth and elevation implied shadows should fall toward the northwest at a moderate length.
- The actual shadows visible in the footage fell toward the southeast and were notably short — consistent with an early afternoon sun position, not an early morning one.

**This is a genuine discrepancy, not a minor detail.** The fact-checker used the [Distance/Bearing/Feasibility framework's sibling tool] alongside standard newsroom practice: rather than assuming malice, the fact-checker searched for the same footage with alternative timestamps and found an earlier, unrelated post of what appeared to be the same footage, timestamped two days prior, in the early afternoon.

**Claim component 3 (timing) assessed as: False.** The footage appears to be genuine storm damage from Rivermouth, but from two days before the claimed "this morning," not current footage.

---

## Stage 5: Verdict and Reporting

Following `osint-templates/specialized-formats/journalism-fact-check.md`, the fact-checker issued a verdict of **"Misleading — Missing Context"** rather than "False" outright, since the underlying footage does appear to show genuine storm damage in the correct location; only the currency claim was inaccurate. The published fact-check:

- Confirmed the location match with supporting reasoning
- Explained the chronolocation methodology and shadow discrepancy in accessible terms for a general audience
- Linked to the earlier, correctly-dated original post
- Avoided any claim about who added the false "this morning" framing or why, since that could not be established from the available evidence

---

## What This Case Study Demonstrates

- **Breaking a compound claim into independently verifiable parts** (genuineness, location, timing) allowed for a nuanced verdict rather than a blunt true/false call on the whole claim.
- **Chronolocation via sun-position calculation** caught a discrepancy that reverse image search and geolocation alone would have missed entirely.
- **Appropriate verdict calibration:** "Misleading — Missing Context" more accurately reflected the evidence than a simple "False" label would have, since the footage's content and location were genuinely accurate.
- **Restraint in the write-up:** the fact-checker reported what the evidence supported (a timing discrepancy) without speculating about intent or attribution beyond what could be established.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
