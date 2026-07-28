# Pattern Analysis

## Overview

This section covers temporal and behavioral pattern detection techniques, such as analyzing when a social media account is typically active to infer a likely timezone or sleep/wake schedule. See `posting_pattern_analysis.py` in this folder for a ready-to-use script that analyzes a list of post timestamps and estimates likely activity windows and probable timezone candidates.

---

## Temporal Pattern Analysis Concepts

| Concept | Description | Typical Use |
|---|---|---|
| Activity histogram by hour | Distribution of activity (posts, logins, messages) across the 24-hour clock | Identifying an account's typical "awake" hours |
| Quiet-window inference | The longest sustained period of low/no activity, often corresponding to sleep | Estimating a plausible timezone or sleep schedule |
| Day-of-week pattern | Distribution of activity across days of the week | Distinguishing a personal account (weekday/weekend variation) from an automated or professionally managed account (more uniform activity) |
| Posting frequency burstiness | Whether activity is evenly spaced or clustered in tight bursts | Identifying automated posting or coordinated campaign activity (see `social-media-intelligence/network-mapping/README.md`) |
| Cadence consistency over time | Whether an account's activity pattern is stable or has shifted significantly | Detecting a possible change in operator, location, or account compromise |

## Supporting Platforms

| Tool | Description | Best For | Cost |
|---|---|---|---|
| General social media analytics platforms (see `social-media-intelligence/`) | Many platform-specific and cross-platform tools include basic posting-time analytics | Quick visual activity pattern review without custom scripting | Varies |
| Spreadsheet pivot tables/charts | Standard spreadsheet software can bin and chart timestamp data manually | Quick, no-code pattern visualization for a modest dataset | Free (with common spreadsheet software) |

---

## Using the Included Posting Pattern Analysis Script

`posting_pattern_analysis.py` takes a list of UTC timestamps (for example, exported post times from a social media account) and produces an hourly activity histogram, identifies the longest quiet window, and lists which UTC offsets would place that quiet window during typical local nighttime hours — a common technique for narrowing down an account's likely timezone. It requires only Python's standard library.

```bash
python posting_pattern_analysis.py --file timestamps.txt
python posting_pattern_analysis.py --file timestamps.csv --timestamp-column posted_at
```

Input should be one ISO-format UTC timestamp per line (.txt) or a CSV with a named timestamp column.

---

## Usage Notes

- Timezone inference from posting patterns is a plausibility indicator, not a proof: people keep irregular schedules, use scheduling tools to post outside their own waking hours, or deliberately post at unusual times. Treat the inferred timezone range as a lead to corroborate with other evidence (language, cultural references, explicit profile information), not a standalone conclusion.
- A very evenly distributed activity pattern with no clear quiet window can itself be a signal worth noting — it may indicate an account managed by a team across time zones, an automated posting schedule, or a scheduling tool, rather than a single individual's organic activity.

---

## Legal and Ethical Notes

- Timing pattern analysis applied to infer a specific individual's likely location or timezone should be used consistent with the elevated standard in `people-investigation/README.md`; this technique narrows a search space and should not be treated as pinpointing a precise location.
- This technique relies on publicly available or lawfully collected activity timestamps only.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
