#!/usr/bin/env python3
"""
iot_banner_classifier.py

Classify discovered internet-facing devices (from a CSV export of
host/port/banner data, such as one exported from Shodan or a similar
internet-wide scan index) into likely device categories using common
port and banner-text signature patterns.

Purpose in an OSINT context:
    Helps triage a large list of discovered internet-facing hosts by
    likely device type (webcam/DVR, router, industrial control system,
    printer, media server) before manual review. See
    osint-tools/mobile-and-iot/iot-discovery/README.md for important
    limitations: this is a heuristic classifier, not a certainty.

Requirements:
    Python 3.8+ (standard library only, no third-party packages required)

Usage:
    python iot_banner_classifier.py --input scan_export.csv

Input CSV format (header row required):
    ip,port,banner
    203.0.113.10,554,RTSP/1.0 200 OK Server: Hikvision-Webs
    203.0.113.11,502,Modbus TCP response
"""

import argparse
import csv
import sys
from collections import defaultdict

# Each category maps to: a set of "signature" ports strongly associated with
# it, and a list of case-insensitive keywords to look for in the banner text.
# A match on port OR keyword contributes to that category's score; a match
# on both contributes more strongly.
CATEGORY_SIGNATURES = {
    "Webcam / DVR / NVR": {
        "ports": {554, 8000, 8080, 37777},
        "keywords": ["dvr", "nvr", "webcam", "ip camera", "hikvision", "dahua",
                     "rtsp", "onvif", "axis communications"],
    },
    "Router / Networking Equipment": {
        "ports": {23, 80, 443, 7547, 8291},
        "keywords": ["router", "rompager", "netgear", "tp-link", "d-link",
                     "mikrotik", "tr-069", "busybox"],
    },
    "Industrial Control System (ICS/SCADA)": {
        "ports": {502, 102, 20000, 44818, 47808},
        "keywords": ["modbus", "s7comm", "dnp3", "ethernet/ip", "siemens",
                     "schneider", "bacnet", "scada", "plc"],
    },
    "Printer": {
        "ports": {515, 631, 9100},
        "keywords": ["jetdirect", "printer", "ipp", "hp laserjet", "epson", "brother"],
    },
    "Media Server": {
        "ports": {8200, 32400, 32469, 1900},
        "keywords": ["dlna", "plex", "upnp", "minidlna", "media server"],
    },
}


def classify_entry(port: int, banner: str) -> dict:
    banner_lower = (banner or "").lower()
    scores = {}

    for category, sig in CATEGORY_SIGNATURES.items():
        score = 0
        matched_signals = []
        if port in sig["ports"]:
            score += 2
            matched_signals.append(f"port {port}")
        for keyword in sig["keywords"]:
            if keyword in banner_lower:
                score += 3
                matched_signals.append(f"keyword '{keyword}'")
        if score > 0:
            scores[category] = {"score": score, "signals": matched_signals}

    if not scores:
        return {"category": "Unclassified", "confidence": "Low", "signals": []}

    best_category = max(scores, key=lambda c: scores[c]["score"])
    best_score = scores[best_category]["score"]

    if best_score >= 5:
        confidence = "High"
    elif best_score >= 3:
        confidence = "Medium"
    else:
        confidence = "Low"

    return {
        "category": best_category,
        "confidence": confidence,
        "signals": scores[best_category]["signals"],
    }


def load_entries(path: str) -> list:
    entries = []
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        required = {"ip", "port", "banner"}
        if not required.issubset(set(reader.fieldnames or [])):
            sys.exit(f"CSV must contain columns: {required}. Found: {reader.fieldnames}")
        for row in reader:
            try:
                port = int(row["port"])
            except ValueError:
                print(f"Warning: skipping row with non-numeric port: {row}")
                continue
            entries.append({"ip": row["ip"].strip(), "port": port, "banner": row["banner"].strip()})
    return entries


def main():
    parser = argparse.ArgumentParser(
        description="Classify discovered devices by likely IoT category using port and banner signatures."
    )
    parser.add_argument("--input", required=True, help="Path to a CSV file with ip,port,banner columns")
    args = parser.parse_args()

    entries = load_entries(args.input)
    if not entries:
        sys.exit("No entries loaded from the input file.")

    category_counts = defaultdict(int)

    print(f"\n{'IP':<16}{'Port':<8}{'Category':<32}{'Confidence':<12}Signals")
    print("-" * 100)
    for entry in entries:
        result = classify_entry(entry["port"], entry["banner"])
        category_counts[result["category"]] += 1
        signals = ", ".join(result["signals"]) if result["signals"] else "-"
        print(f"{entry['ip']:<16}{entry['port']:<8}{result['category']:<32}{result['confidence']:<12}{signals}")

    print("\nSummary by category:\n")
    for category, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        print(f"  {category}: {count}")

    print(
        "\nReminder: this is a heuristic classification based on port and banner text patterns. "
        "A device can run services on non-standard ports or present an altered/generic banner. "
        "Treat results as a starting point for manual verification, not a final determination, "
        "and do not attempt to access any classified device without explicit written authorization."
    )


if __name__ == "__main__":
    main()
