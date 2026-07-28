#!/usr/bin/env python3
"""
chat_export_analyzer.py

Parse a WhatsApp-style plain text chat export and produce participant
activity statistics, a daily message timeline, and basic entity
extraction (emails, phone numbers, URLs) across all messages.

Purpose in an OSINT/mobile-forensics context:
    Chat exports are one of the most common forms of consented or
    authorized mobile evidence an analyst will work with. See
    osint-tools/mobile-and-iot/mobile-forensics/README.md for the
    authorization requirement that applies before analyzing any such
    export, and for notes on the format's limitations.

Supported input formats (common WhatsApp export variants):
    1/15/26, 9:41 AM - Jordan Sample: Hey, are we still on for tomorrow?
    [1/15/26, 9:41:00 AM] Jordan Sample: Hey, are we still on for tomorrow?

Requirements:
    Python 3.8+ (standard library only, no third-party packages required)

Usage:
    python chat_export_analyzer.py --file chat_export.txt
    python chat_export_analyzer.py --file chat_export.txt --json
"""

import argparse
import json
import re
import sys
from collections import defaultdict

# Matches: "1/15/26, 9:41 AM - Sender: Message" or "[1/15/26, 9:41:00 AM] Sender: Message"
MESSAGE_LINE_PATTERN = re.compile(
    r"^\[?(?P<date>\d{1,2}/\d{1,2}/\d{2,4}),\s*(?P<time>\d{1,2}:\d{2}(?::\d{2})?\s?[APap]?[Mm]?)\]?"
    r"\s*-?\s*(?P<sender>[^:]+):\s?(?P<message>.*)$"
)

EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
URL_PATTERN = re.compile(r"\bhttps?://[^\s<>\"']+", re.IGNORECASE)
PHONE_PATTERN = re.compile(
    r"(?:\+\d{1,3}[\s.-]?)?"
    r"(?:\(\d{2,4}\)[\s.-]?\d{3,4}[\s.-]\d{3,4}"
    r"|\d{2,4}[\s.-]\d{3,4}[\s.-]\d{3,4})\b"
)


def parse_chat_export(path: str) -> list:
    """
    Parse a chat export file into a list of message dicts:
    {"date": str, "time": str, "sender": str, "message": str}.
    Lines that don't match a new-message pattern are treated as a
    continuation of the previous message (common for multi-line messages).
    """
    messages = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n")
            match = MESSAGE_LINE_PATTERN.match(line)
            if match:
                messages.append({
                    "date": match.group("date"),
                    "time": match.group("time"),
                    "sender": match.group("sender").strip(),
                    "message": match.group("message").strip(),
                })
            elif messages and line.strip():
                # Continuation of the previous message (e.g. a line break within one message)
                messages[-1]["message"] += " " + line.strip()
    return messages


def summarize_participants(messages: list) -> dict:
    counts = defaultdict(int)
    for m in messages:
        counts[m["sender"]] += 1
    return dict(sorted(counts.items(), key=lambda x: -x[1]))


def summarize_timeline(messages: list) -> dict:
    counts = defaultdict(int)
    for m in messages:
        counts[m["date"]] += 1
    # Preserve encounter order of dates as they appear in the export (typically chronological)
    return dict(counts)


def extract_entities(messages: list) -> dict:
    all_text = " ".join(m["message"] for m in messages)
    return {
        "emails": sorted(set(EMAIL_PATTERN.findall(all_text))),
        "urls": sorted(set(URL_PATTERN.findall(all_text))),
        "phone_numbers": sorted(set(PHONE_PATTERN.findall(all_text))),
    }


def print_summary(messages: list, participants: dict, timeline: dict, entities: dict) -> None:
    if not messages:
        print("No messages could be parsed from this file. Check that the export format matches "
              "one of the patterns documented in this script's header comment.")
        return

    print(f"\nTotal messages parsed: {len(messages)}")
    print(f"Date range: {messages[0]['date']} to {messages[-1]['date']}")

    print(f"\nMessages per participant:\n")
    for sender, count in participants.items():
        pct = 100 * count / len(messages)
        print(f"  {sender}: {count} messages ({pct:.1f}%)")

    print(f"\nMessages per day (first 20 days shown):\n")
    for i, (date, count) in enumerate(timeline.items()):
        if i >= 20:
            print(f"  ... and {len(timeline) - 20} more day(s)")
            break
        bar = "#" * min(50, count)
        print(f"  {date}: {bar} ({count})")

    print(f"\nEntities found across all messages:")
    print(f"  Email addresses: {entities['emails'] or '(none)'}")
    print(f"  URLs: {entities['urls'] or '(none)'}")
    print(f"  Phone numbers: {entities['phone_numbers'] or '(none)'}")

    print(
        "\nReminder: only analyze chat exports you have lawfully obtained access to. A chat "
        "export reflects only the exporting participant's device copy and may be incomplete; "
        "corroborate significant findings against other evidence where possible."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a WhatsApp-style plain text chat export for participant activity and entities."
    )
    parser.add_argument("--file", required=True, help="Path to the chat export .txt file")
    parser.add_argument("--json", action="store_true", help="Output results as JSON instead of a human-readable summary")
    args = parser.parse_args()

    try:
        messages = parse_chat_export(args.file)
    except FileNotFoundError:
        sys.exit(f"File not found: {args.file}")

    participants = summarize_participants(messages)
    timeline = summarize_timeline(messages)
    entities = extract_entities(messages)

    if args.json:
        print(json.dumps({
            "total_messages": len(messages),
            "participants": participants,
            "messages_per_day": timeline,
            "entities": entities,
        }, indent=2))
    else:
        print_summary(messages, participants, timeline, entities)


if __name__ == "__main__":
    main()
