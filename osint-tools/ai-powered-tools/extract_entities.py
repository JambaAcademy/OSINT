#!/usr/bin/env python3
"""
extract_entities.py

Perform a fast, dependency-free first-pass extraction of common entity
types from a block of text: email addresses, phone numbers, URLs, dates,
monetary amounts, and candidate proper names (capitalized word sequences).

This is a HEURISTIC, pattern-matching tool, not a trained machine learning
named-entity-recognition (NER) model. It requires no downloads and no
third-party packages, making it useful for quick triage of a document
before deciding whether a full NER pipeline (spaCy, Hugging Face) is
warranted for a larger corpus. See
osint-tools/ai-powered-tools/natural-language-processing/README.md for
the tradeoffs and the more accurate ML-based alternatives.

Known limitations:
    - Candidate proper names include false positives (e.g., sentence-
      initial capitalized words, capitalized common nouns) and are NOT
      classified as person/organization/location.
    - Phone number and date patterns cover common formats but are not
      exhaustive across all international formats.
    - This script does not understand context, so it cannot resolve
      whether "Washington" refers to a person, a city, or a state.

Legal and ethical scope:
    Use this script only on text you have lawfully obtained access to as
    part of a documented investigation. See
    osint-templates/operational-planning/legal-compliance-checklist.md
    for handling requirements when extracted entities include personal
    information about identifiable individuals.

Requirements:
    Python 3.8+ (standard library only, no third-party packages required)

Usage:
    python extract_entities.py --file document.txt
    python extract_entities.py --file document.txt --json
"""

import argparse
import json
import re
import sys

EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")

URL_PATTERN = re.compile(r"\bhttps?://[^\s<>\"']+", re.IGNORECASE)

# Common phone formats: (123) 456-7890, 123-456-7890, 123.456.7890, +1 123 456 7890
PHONE_PATTERN = re.compile(
    r"(?:\+\d{1,3}[\s.-]?)?"
    r"(?:\(\d{2,4}\)[\s.-]?\d{3,4}[\s.-]\d{3,4}"   # (202) 555-0173 style
    r"|\d{2,4}[\s.-]\d{3,4}[\s.-]\d{3,4})\b"        # 202-555-0173 style
)

# Common date formats: 2026-06-15, 06/15/2026, 15 June 2026, June 15, 2026
DATE_PATTERNS = [
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),
    re.compile(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b"),
    re.compile(
        r"\b\d{1,2}\s+(?:January|February|March|April|May|June|July|August|"
        r"September|October|November|December)\s+\d{4}\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:January|February|March|April|May|June|July|August|September|"
        r"October|November|December)\s+\d{1,2},?\s+\d{4}\b",
        re.IGNORECASE,
    ),
]

# Monetary amounts: $1,000, $1,000.50, 1,000 USD, €500, £250
MONEY_PATTERN = re.compile(
    r"(?:[$€£¥]\s?\d[\d,]*(?:\.\d{1,2})?)|(?:\d[\d,]*(?:\.\d{1,2})?\s?(?:USD|EUR|GBP|JPY))"
)

# Candidate proper names: sequences of two or more capitalized words, matched
# within a single sentence at a time (see extract_entities()) so a match
# never crosses a sentence-ending period into the next sentence.
PROPER_NAME_PATTERN = re.compile(r"\b(?:[A-Z][a-z]+\s+){1,4}[A-Z][a-z]+\b")

# A rough sentence splitter: break after '.', '!', or '?' followed by whitespace.
SENTENCE_SPLIT_PATTERN = re.compile(r"(?<=[.!?])\s+")

# Common words that are capitalized for reasons other than being a name
# (sentence-initial function words), used to reduce obvious false positives.
COMMON_FALSE_POSITIVE_STARTS = {
    "The", "This", "That", "These", "Those", "A", "An", "It", "He", "She",
    "They", "We", "I", "In", "On", "At", "For", "With", "After", "Before",
}


def dedupe_preserve_order(items: list) -> list:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def extract_entities(text: str) -> dict:
    emails = dedupe_preserve_order(EMAIL_PATTERN.findall(text))
    urls = dedupe_preserve_order(URL_PATTERN.findall(text))
    phones = dedupe_preserve_order(PHONE_PATTERN.findall(text))

    dates = []
    for pattern in DATE_PATTERNS:
        dates.extend(pattern.findall(text))
    dates = dedupe_preserve_order(dates)

    money = dedupe_preserve_order(MONEY_PATTERN.findall(text))

    names = []
    for sentence in SENTENCE_SPLIT_PATTERN.split(text):
        for match in PROPER_NAME_PATTERN.findall(sentence):
            name = match.strip()
            first_word = name.split()[0]
            if first_word in COMMON_FALSE_POSITIVE_STARTS:
                continue
            names.append(name)
    names = dedupe_preserve_order(names)

    return {
        "emails": emails,
        "urls": urls,
        "phone_numbers": phones,
        "dates": dates,
        "monetary_amounts": money,
        "candidate_proper_names": names,
    }


def print_human_readable(entities: dict) -> None:
    labels = {
        "emails": "Email addresses",
        "urls": "URLs",
        "phone_numbers": "Phone numbers",
        "dates": "Dates",
        "monetary_amounts": "Monetary amounts",
        "candidate_proper_names": "Candidate proper names (unclassified — review manually)",
    }
    for key, label in labels.items():
        values = entities[key]
        print(f"\n{label} ({len(values)} found):")
        if not values:
            print("  (none found)")
        for v in values:
            print(f"  - {v}")

    print(
        "\nReminder: this is a heuristic, pattern-matching extractor, not a trained NER model. "
        "Candidate proper names are NOT classified as person/organization/location and will "
        "include false positives. Review results manually before use in a report."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Extract common entity types from a text document using pattern matching."
    )
    parser.add_argument("--file", required=True, help="Path to a plain text file to analyze")
    parser.add_argument("--json", action="store_true", help="Output results as JSON instead of a human-readable summary")
    args = parser.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except FileNotFoundError:
        sys.exit(f"File not found: {args.file}")

    entities = extract_entities(text)

    if args.json:
        print(json.dumps(entities, indent=2))
    else:
        print_human_readable(entities)


if __name__ == "__main__":
    main()
