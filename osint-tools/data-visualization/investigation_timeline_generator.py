#!/usr/bin/env python3
"""
investigation_timeline_generator.py

Render a horizontal visual timeline from a CSV file of dated events,
with optional category-based color coding, using Matplotlib.

Purpose in an OSINT context:
    Visualizing a chronological sequence of events makes it easier to
    spot gaps, overlaps, or inconsistencies in a reported narrative. See
    osint-tools/data-visualization/timeline-creation/README.md for
    guidance on building a defensible investigative timeline.

Requirements:
    Python 3.8+
    matplotlib (pip install matplotlib --break-system-packages)

Usage:
    python investigation_timeline_generator.py --input events.csv --output timeline.png

Input CSV format (header row required):
    date,event,category
    2026-01-15,Company incorporated in Delaware,Corporate
    2026-02-01,Domain registered,Technical
    2026-03-10,First public statement issued,Communications

The 'category' column is optional; if omitted, all events are shown in a
single color.
"""

import argparse
import csv
import datetime
import sys

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
except ImportError:
    sys.exit(
        "This script requires matplotlib.\n"
        "Install it with: pip install matplotlib --break-system-packages"
    )

CATEGORY_COLORS = [
    "#1f4e78", "#c00000", "#2e7d32", "#e65100", "#6a1b9a",
    "#00838f", "#827717", "#4527a0", "#ad1457", "#37474f",
]


def load_events(csv_path: str) -> list:
    events = []
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if "date" not in (reader.fieldnames or []) or "event" not in (reader.fieldnames or []):
            sys.exit(f"CSV must contain at least 'date' and 'event' columns. Found: {reader.fieldnames}")
        has_category = "category" in (reader.fieldnames or [])
        for row in reader:
            try:
                date = datetime.datetime.fromisoformat(row["date"].strip())
            except ValueError:
                print(f"Warning: skipping row with unparseable date: {row['date']!r}")
                continue
            events.append({
                "date": date,
                "event": row["event"].strip(),
                "category": row.get("category", "").strip() if has_category else "",
            })
    events.sort(key=lambda e: e["date"])
    return events


def render_timeline(events: list, output_path: str, title: str = "Investigation Timeline") -> None:
    if not events:
        sys.exit("No valid events were loaded; nothing to render.")

    categories = sorted({e["category"] for e in events if e["category"]})
    color_map = {cat: CATEGORY_COLORS[i % len(CATEGORY_COLORS)] for i, cat in enumerate(categories)}
    default_color = "#1f4e78"

    dates = [e["date"] for e in events]
    fig_width = max(12, len(events) * 0.9)
    fig, ax = plt.subplots(figsize=(fig_width, 6))

    # Alternate label vertical offset (up/down) to reduce overlap on a dense timeline.
    levels = [1 if i % 2 == 0 else -1 for i in range(len(events))]

    ax.axhline(0, color="#999999", linewidth=1.5, zorder=1)

    for event, level in zip(events, levels):
        color = color_map.get(event["category"], default_color)
        ax.scatter(event["date"], 0, s=80, color=color, zorder=3, edgecolor="white", linewidth=1)
        ax.plot([event["date"], event["date"]], [0, level * 0.5], color=color, linewidth=1, zorder=2)
        label = event["event"]
        if event["category"]:
            label = f"[{event['category']}] {label}"
        ax.annotate(
            f"{event['date'].date()}\n{label}",
            xy=(event["date"], level * 0.5),
            xytext=(0, 10 if level > 0 else -10),
            textcoords="offset points",
            ha="center",
            va="bottom" if level > 0 else "top",
            fontsize=8,
            rotation=0,
            wrap=True,
        )

    ax.set_ylim(-2, 2)
    ax.get_yaxis().set_visible(False)
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    fig.autofmt_xdate()

    if categories:
        handles = [plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=color_map[c],
                               markersize=8, label=c) for c in categories]
        ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.15),
                  ncol=min(len(categories), 5), frameon=False)

    plt.title(title, fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description="Render a visual timeline from a CSV of dated events."
    )
    parser.add_argument("--input", required=True, help="Path to a CSV file with date,event[,category] columns")
    parser.add_argument("--output", required=True, help="Path to write the rendered PNG image")
    parser.add_argument("--title", default="Investigation Timeline", help="Title displayed on the timeline")
    args = parser.parse_args()

    events = load_events(args.input)
    print(f"Loaded {len(events)} event(s) spanning {events[0]['date'].date()} to {events[-1]['date'].date()}.")

    render_timeline(events, args.output, title=args.title)
    print(f"Timeline image written to {args.output}")

    print(
        "\nReminder: verify each event's date against its original source before relying on "
        "this timeline in a report, and note any significant gaps between events explicitly "
        "in your accompanying narrative."
    )


if __name__ == "__main__":
    main()
