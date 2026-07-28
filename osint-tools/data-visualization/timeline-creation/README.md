# Timeline Creation

## Overview

Chronological timelines help establish and communicate the sequence of events in an investigation, making it easier to spot gaps, overlaps, or inconsistencies in a reported narrative. See `investigation_timeline_generator.py` in this folder for a ready-to-use script that renders a labeled visual timeline from a simple CSV of dated events.

---

## Timeline Tools

| Tool | Description | Best For | Cost |
|---|---|---|---|
| TimelineJS (Knight Lab) | Free, embeddable, web-based timeline tool driven by a Google Sheet or JSON data source | Interactive, shareable web timelines for a public-facing report | Free, open source |
| Aeon Timeline | Commercial desktop application for building detailed, filterable investigative timelines | Complex investigations with many interrelated events and entities | Paid |
| Tableau / Power BI (timeline/Gantt views) | General-purpose business intelligence platforms with timeline/Gantt chart capability | Integrating a timeline view alongside other data visualizations | Paid (with free tiers/trial) |
| Spreadsheet Gantt/timeline templates | Standard spreadsheet software can build a basic timeline or Gantt-style chart | Quick, no-code timeline for a modest number of events | Free (with common spreadsheet software) |

---

## Using the Included Timeline Generator

`investigation_timeline_generator.py` reads a CSV file of dated events and renders a horizontal visual timeline as a PNG image, with events grouped and color-coded by category if a category column is present. It requires only the `matplotlib` Python package.

```bash
pip install matplotlib --break-system-packages
python investigation_timeline_generator.py --input events.csv --output timeline.png
```

See `sample_events.csv` in this folder for the expected input format: `date,event,category`.

---

## Building a Good Investigative Timeline

- **Use precise dates where known**, and clearly mark estimated or approximate dates as such (e.g., in the event label) rather than presenting an estimate with the same visual weight as a confirmed date.
- **Cite the source for each event** in your underlying data (even if not shown directly on the visual timeline itself, keep it in your working notes) so the timeline can be defended if challenged.
- **Group related events by category** (e.g., financial events, communications, travel) using color coding to make patterns easier to spot.
- **Note gaps deliberately.** A period with no documented events is itself potentially significant and worth flagging in the accompanying narrative report.

---

## Usage Notes

- Very dense timelines (50+ events) become difficult to read as a single static image; consider splitting into multiple timelines by category or time period, or using an interactive tool such as TimelineJS for a large event set.
- This script renders a static image suitable for inclusion in a written report; for an interactive, explorable timeline, consider TimelineJS or pairing this data with the dashboard template in `interactive-dashboards/`.

---

## Legal and Ethical Notes

- Timelines documenting a specific individual's activities should be built and used consistent with the elevated standard in `people-investigation/README.md`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
