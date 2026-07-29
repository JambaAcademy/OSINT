# Data Processing

## Overview

This section contains data cleaning, deduplication, and normalization utilities for handling the tabular data commonly produced when merging results from multiple OSINT sources (for example, combining several people-search or company-registry exports covering overlapping subjects). See `csv_deduplicator_normalizer.py` for a ready-to-use script that normalizes common field formats and removes duplicate records based on configurable key columns.

---

## Using the Included CSV Deduplicator and Normalizer

`csv_deduplicator_normalizer.py` reads a CSV file, normalizes commonly inconsistent field formats (phone numbers, email addresses, and surrounding whitespace), and removes duplicate rows based on one or more key columns you specify, producing both a cleaned output CSV and a summary of what was changed.

```bash
python csv_deduplicator_normalizer.py --input merged_export.csv --output cleaned.csv --key-columns email,phone
```

---

## What Normalization Is Applied

- **Phone numbers:** Non-numeric characters (spaces, dashes, parentheses, dots) are stripped for comparison purposes, so `"(415) 555-0199"` and `"415-555-0199"` are recognized as the same value. The output CSV retains a normalized, consistently formatted version.
- **Email addresses:** Converted to lowercase and stripped of surrounding whitespace for comparison, since email addresses are conventionally case-insensitive at the domain level and often effectively so in practice at the local-part level.
- **General whitespace:** Leading/trailing whitespace is stripped from every field.

---

## Usage Notes

- Choose key columns carefully: deduplicating on a single common field like a first name will merge unrelated records; a combination of fields (e.g., email address and phone number together) produces safer deduplication.
- Review the summary report before trusting the deduplicated output blindly, especially for a dataset where you plan to use the result in a report — false-merge risk (treating two different people/entities as the same record) is the main failure mode to watch for, particularly with common names.
- This script does not attempt fuzzy/approximate matching (e.g., recognizing "Bob Smith" and "Robert Smith" as potentially the same person); it performs exact matching on the normalized key columns only. For fuzzy identity correlation, see `osint-templates/ai-assisted-templates/automated-data-correlation.md` and the associated tooling in `osint-tools/social-media-intelligence/cross-platform-analyzers/`.

---

## Legal and Ethical Notes

- Deduplicating and normalizing data you have already lawfully collected has no independent legal or ethical considerations beyond those governing the original collection itself.
- Where merged data includes personal information from multiple sources, review `osint-templates/operational-planning/legal-compliance-checklist.md` for data minimization guidance — a merge operation is a good opportunity to also discard fields not relevant to your investigation's stated purpose.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
