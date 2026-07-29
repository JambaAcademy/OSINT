#!/usr/bin/env python3
"""
csv_deduplicator_normalizer.py

Normalize commonly inconsistent field formats (phone numbers, email
addresses, whitespace) in a CSV file and remove duplicate rows based on
one or more configurable key columns, producing a cleaned output CSV and
a summary report of what was changed.

Purpose in an OSINT context:
    Useful for cleaning up merged exports from multiple sources covering
    overlapping subjects (for example, combining several people-search
    or company-registry exports). See
    scripts-and-automation/data-processing/README.md for important
    limitations: this script performs exact matching on normalized
    fields only, not fuzzy identity correlation.

Requirements:
    Python 3.8+ (standard library only, no third-party packages required)

Usage:
    python csv_deduplicator_normalizer.py --input merged_export.csv --output cleaned.csv --key-columns email,phone
"""

import argparse
import csv
import re
import sys

PHONE_STRIP_PATTERN = re.compile(r"[^\d+]")


def normalize_value(value: str, column_name: str) -> str:
    """Apply column-appropriate normalization to a single field value."""
    value = (value or "").strip()
    lower_col = column_name.lower()

    if "email" in lower_col:
        return value.lower()
    if "phone" in lower_col:
        return PHONE_STRIP_PATTERN.sub("", value)
    return value


def normalize_row(row: dict) -> dict:
    return {col: normalize_value(val, col) for col, val in row.items()}


def load_and_normalize(path: str) -> tuple:
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = [normalize_row(row) for row in reader]
    return fieldnames, rows


def deduplicate(rows: list, key_columns: list) -> tuple:
    """
    Remove rows that are duplicates of an earlier row based on the given
    key columns (compared on their already-normalized values). Returns
    (deduplicated_rows, list_of_removed_row_indices_with_reason).
    """
    seen_keys = {}
    deduplicated = []
    removed = []

    for i, row in enumerate(rows):
        key = tuple(row.get(col, "") for col in key_columns)
        if key in seen_keys:
            removed.append({"row_index": i, "duplicate_of_row_index": seen_keys[key], "key": key})
        else:
            seen_keys[key] = i
            deduplicated.append(row)

    return deduplicated, removed


def write_csv(path: str, fieldnames: list, rows: list) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(
        description="Normalize field formats and remove duplicate rows from a CSV file."
    )
    parser.add_argument("--input", required=True, help="Path to the input CSV file")
    parser.add_argument("--output", required=True, help="Path to write the cleaned output CSV file")
    parser.add_argument(
        "--key-columns", required=True,
        help="Comma-separated list of column names to use for duplicate detection, e.g. 'email,phone'",
    )
    args = parser.parse_args()

    key_columns = [c.strip() for c in args.key_columns.split(",") if c.strip()]

    fieldnames, rows = load_and_normalize(args.input)

    missing_columns = [c for c in key_columns if c not in fieldnames]
    if missing_columns:
        sys.exit(f"Key column(s) not found in the input CSV: {missing_columns}. Available columns: {fieldnames}")

    print(f"Loaded {len(rows)} row(s) from {args.input}.")

    deduplicated, removed = deduplicate(rows, key_columns)

    write_csv(args.output, fieldnames, deduplicated)

    print(f"Wrote {len(deduplicated)} deduplicated row(s) to {args.output}.")
    print(f"Removed {len(removed)} duplicate row(s) based on key column(s): {key_columns}")

    if removed:
        print("\nDuplicate removal detail (first 10 shown):")
        for r in removed[:10]:
            print(f"  Row {r['row_index']} was a duplicate of row {r['duplicate_of_row_index']} "
                  f"(matching key: {r['key']})")
        if len(removed) > 10:
            print(f"  ... and {len(removed) - 10} more")

    print(
        "\nReminder: this script performs exact matching on normalized fields only, not fuzzy "
        "identity correlation. Review the duplicate removal detail above before treating the "
        "cleaned output as final, especially for datasets with common names or shared contact "
        "details across genuinely different individuals/entities."
    )


if __name__ == "__main__":
    main()
