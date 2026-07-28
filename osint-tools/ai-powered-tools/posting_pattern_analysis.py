#!/usr/bin/env python3
"""
posting_pattern_analysis.py

Analyze a list of UTC post/activity timestamps to build an hourly
activity histogram, identify the longest sustained low-activity ("quiet")
window, and rank candidate UTC offsets (timezones) by how well that quiet
window aligns with a typical local nighttime sleep period.

Purpose in an OSINT context:
    A common technique for narrowing down an account's likely timezone
    (and therefore general geographic region) is analyzing when it is
    typically active versus quiet, on the assumption that most individual
    accounts are quieter during their local nighttime. See
    osint-tools/ai-powered-tools/pattern-analysis/README.md for the
    important limitations of this technique before relying on its output.

Requirements:
    Python 3.8+ (standard library only, no third-party packages required)

Usage:
    python posting_pattern_analysis.py --file timestamps.txt
    python posting_pattern_analysis.py --file timestamps.csv --timestamp-column posted_at

Input format:
    .txt: one ISO-8601 UTC timestamp per line, e.g. 2026-06-15T14:32:00
    .csv: a CSV file with a header row; specify the timestamp column
          with --timestamp-column
"""

import argparse
import csv
import datetime
import sys

TYPICAL_LOCAL_SLEEP_MIDPOINT_HOUR = 3  # 3:00 AM local time, a common sleep-window midpoint


def load_timestamps(path: str, timestamp_column: str = None) -> list:
    timestamps = []
    if path.lower().endswith(".csv"):
        if not timestamp_column:
            sys.exit("--timestamp-column is required when --file is a CSV file.")
        with open(path, "r", encoding="utf-8", errors="replace", newline="") as f:
            reader = csv.DictReader(f)
            if timestamp_column not in reader.fieldnames:
                sys.exit(f"Column '{timestamp_column}' not found. Available columns: {reader.fieldnames}")
            for row in reader:
                raw = (row.get(timestamp_column) or "").strip()
                if raw:
                    timestamps.append(raw)
    else:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            timestamps = [line.strip() for line in f if line.strip()]

    parsed = []
    skipped = 0
    for raw in timestamps:
        try:
            parsed.append(datetime.datetime.fromisoformat(raw.replace("Z", "+00:00")))
        except ValueError:
            skipped += 1
    if skipped:
        print(f"Warning: skipped {skipped} timestamp(s) that could not be parsed as ISO-8601.")
    return parsed


def build_hourly_histogram(timestamps: list) -> list:
    """Return a 24-element list of activity counts by UTC hour (0-23)."""
    counts = [0] * 24
    for ts in timestamps:
        counts[ts.hour] += 1
    return counts


def find_quiet_window(counts: list, min_size: int = 3, max_size: int = 12) -> dict:
    """
    Find the longest contiguous circular run of "quiet" hours (activity at
    or below a low threshold), treating the 24-hour histogram as wrapping
    around midnight. If no hours are at the minimum threshold, the
    threshold is relaxed upward until at least one candidate run is found.
    Returns the best run's start hour, size, and total activity within it.
    """
    total_activity = sum(counts)
    doubled = counts + counts  # lets a circular run be read as a simple slice

    # Try increasingly permissive thresholds (starting at "zero activity")
    # until we find at least one qualifying run of an acceptable size.
    distinct_levels = sorted(set(counts))
    for threshold in distinct_levels:
        # Find every maximal run (in the doubled array) where every hour's
        # count is <= threshold, then keep the longest such run that fits
        # within one 24-hour cycle.
        best_run = None
        run_start = None
        for i in range(len(doubled)):
            if counts[i % 24] <= threshold:
                if run_start is None:
                    run_start = i
            else:
                if run_start is not None:
                    length = i - run_start
                    if length <= 24 and (best_run is None or length > best_run[1]):
                        best_run = (run_start % 24, length)
                run_start = None
        if run_start is not None:
            length = len(doubled) - run_start
            if length <= 24 and (best_run is None or length > best_run[1]):
                best_run = (run_start % 24, length)

        if best_run and min_size <= best_run[1] <= max_size:
            start_hour, size = best_run
            window_total = sum(doubled[start_hour:start_hour + size])
            return {"start_hour": start_hour, "size": size, "total": window_total}
        elif best_run and best_run[1] > max_size:
            # Cap runs that are implausibly long (e.g. a nearly-inactive
            # account) at max_size, keeping the sub-window with lowest sum.
            start_hour, size = best_run
            best_sub = None
            for offset in range(size - max_size + 1):
                sub_start = (start_hour + offset) % 24
                sub_sum = sum(doubled[start_hour + offset:start_hour + offset + max_size])
                if best_sub is None or sub_sum < best_sub[1]:
                    best_sub = (sub_start, sub_sum)
            return {"start_hour": best_sub[0], "size": max_size, "total": best_sub[1]}

    # Fallback: no run met min_size at any threshold (very evenly distributed
    # activity); report the single quietest hour.
    quietest_hour = counts.index(min(counts))
    return {"start_hour": quietest_hour, "size": 1, "total": counts[quietest_hour]}


def rank_utc_offsets(quiet_center_utc_hour: float, top_n: int = 5) -> list:
    """
    For each whole-hour UTC offset from -12 to +14, compute the local hour
    that the quiet window's center would fall on, and rank offsets by how
    close that local hour is to a typical sleep-window midpoint.
    """
    scored = []
    for offset in range(-12, 15):
        local_hour = (quiet_center_utc_hour + offset) % 24
        # circular distance from the typical sleep midpoint
        diff = abs(local_hour - TYPICAL_LOCAL_SLEEP_MIDPOINT_HOUR)
        circular_diff = min(diff, 24 - diff)
        scored.append((circular_diff, offset, local_hour))
    scored.sort(key=lambda x: x[0])
    return scored[:top_n]


def main():
    parser = argparse.ArgumentParser(
        description="Analyze posting timestamps to identify activity patterns and candidate timezones."
    )
    parser.add_argument("--file", required=True, help="Path to a .txt (one ISO timestamp per line) or .csv file")
    parser.add_argument("--timestamp-column", help="Column name containing timestamps (required for CSV input)")
    args = parser.parse_args()

    timestamps = load_timestamps(args.file, args.timestamp_column)
    if len(timestamps) < 5:
        sys.exit("Need at least 5 valid timestamps for a meaningful pattern analysis.")

    print(f"Loaded {len(timestamps)} valid timestamps.\n")

    counts = build_hourly_histogram(timestamps)
    max_count = max(counts) or 1

    print("Hourly activity histogram (UTC), each # represents relative activity:\n")
    for hour in range(24):
        bar = "#" * int(round(30 * counts[hour] / max_count))
        print(f"  {hour:02d}:00  {bar} ({counts[hour]})")

    quiet = find_quiet_window(counts)
    quiet_center = (quiet["start_hour"] + quiet["size"] / 2) % 24
    quiet_end = (quiet["start_hour"] + quiet["size"]) % 24

    print(
        f"\nLongest low-activity window: {quiet['start_hour']:02d}:00 to {quiet_end:02d}:00 UTC "
        f"({quiet['size']} hours, {quiet['total']} of {sum(counts)} total posts fall in this window)"
    )

    print(
        "\nCandidate UTC offsets, ranked by how well this quiet window aligns with a "
        f"typical local sleep midpoint (~{TYPICAL_LOCAL_SLEEP_MIDPOINT_HOUR}:00 local time):\n"
    )
    for circular_diff, offset, local_hour in rank_utc_offsets(quiet_center):
        sign = "+" if offset >= 0 else ""
        print(f"  UTC{sign}{offset:<4} would place the quiet window's center at {local_hour:04.1f} local time")

    print(
        "\nReminder: this is a plausibility indicator based on assumed 'normal' sleep hours, "
        "not a confirmed timezone. People keep irregular schedules and may use scheduling "
        "tools; corroborate with other evidence (language, cultural references, explicit "
        "profile information) before relying on this in a report, per "
        "osint-tools/ai-powered-tools/pattern-analysis/README.md."
    )


if __name__ == "__main__":
    main()
