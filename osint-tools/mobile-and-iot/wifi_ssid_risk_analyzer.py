#!/usr/bin/env python3
"""
wifi_ssid_risk_analyzer.py

Flag Wi-Fi network names (SSIDs) matching common factory-default naming
patterns from major manufacturers and internet service providers, using
data from an authorized wireless site survey export.

Purpose in an OSINT/security-assessment context:
    A network still broadcasting its factory-default SSID is a widely
    used proxy indicator that other default settings (most importantly,
    the administrative password) may also be unchanged, since changing
    the SSID and changing the admin password are typically both part of
    the same basic router setup process. See
    osint-tools/mobile-and-iot/wireless-intelligence/README.md for the
    authorization requirement and important limitations of this
    heuristic before relying on it.

Requirements:
    Python 3.8+ (standard library only, no third-party packages required)

Usage:
    python wifi_ssid_risk_analyzer.py --input ssid_survey.csv

Input CSV format (header row required):
    ssid,signal_strength_dbm,encryption
    NETGEAR23,-45,WPA2
    TheOffice_5G,-52,WPA2
"""

import argparse
import csv
import re
import sys

# Each entry: (compiled regex, human-readable description, severity)
# Patterns are illustrative of common factory-default naming conventions
# from major manufacturers and ISPs; they are not exhaustive.
DEFAULT_SSID_PATTERNS = [
    (re.compile(r"^NETGEAR\d{2}$"), "Netgear factory default", "High"),
    (re.compile(r"^Linksys[-_]?[0-9A-Fa-f]{4,6}$"), "Linksys factory default", "High"),
    (re.compile(r"^(TP-LINK|TP_LINK)[_-][0-9A-Fa-f]{4,6}$", re.IGNORECASE), "TP-Link factory default", "High"),
    (re.compile(r"^ASUS(_[0-9A-Fa-f]{2,4})?$"), "ASUS factory default", "Medium"),
    (re.compile(r"^dlink[-_]?[0-9A-Fa-f]{4,6}$", re.IGNORECASE), "D-Link factory default", "High"),
    (re.compile(r"^Xfinity", re.IGNORECASE), "Comcast Xfinity default/ISP-provided naming", "Medium"),
    (re.compile(r"^(ATT|AT&T)[- ]?[0-9A-Za-z]{4,6}$", re.IGNORECASE), "AT&T default naming", "High"),
    (re.compile(r"^SpectrumSetup-[0-9A-Za-z]{2}$"), "Spectrum default naming", "High"),
    (re.compile(r"^CenturyLink[0-9A-Fa-f]{4,6}$", re.IGNORECASE), "CenturyLink default naming", "High"),
    (re.compile(r"^Verizon[-_]?[0-9A-Za-z]{4,6}$", re.IGNORECASE), "Verizon default naming", "High"),
    (re.compile(r"^Optimum_?WiFi", re.IGNORECASE), "Optimum default naming", "Medium"),
    (re.compile(r"^belkin\.?[0-9A-Fa-f]{4,6}$", re.IGNORECASE), "Belkin factory default", "High"),
    (re.compile(r"^(Wireless|WiFi|Home Network|Default|Network)$", re.IGNORECASE),
     "Generic default/unconfigured name", "Medium"),
]

WEAK_ENCRYPTION_VALUES = {"none", "open", "wep"}


def classify_ssid(ssid: str, encryption: str = "") -> dict:
    for pattern, description, severity in DEFAULT_SSID_PATTERNS:
        if pattern.match(ssid.strip()):
            return {"flagged": True, "reason": description, "severity": severity}
    return {"flagged": False, "reason": None, "severity": None}


def load_networks(path: str) -> list:
    networks = []
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if "ssid" not in (reader.fieldnames or []):
            sys.exit(f"CSV must contain an 'ssid' column. Found: {reader.fieldnames}")
        for row in reader:
            networks.append({
                "ssid": row.get("ssid", "").strip(),
                "signal_strength_dbm": row.get("signal_strength_dbm", "").strip(),
                "encryption": row.get("encryption", "").strip(),
            })
    return networks


def main():
    parser = argparse.ArgumentParser(
        description="Flag Wi-Fi SSIDs matching common factory-default naming patterns."
    )
    parser.add_argument("--input", required=True, help="Path to a CSV file with an 'ssid' column")
    args = parser.parse_args()

    networks = load_networks(args.input)
    if not networks:
        sys.exit("No networks loaded from the input file.")

    flagged_count = 0
    weak_encryption_count = 0

    print(f"\n{'SSID':<28}{'Encryption':<12}{'Default Name Flag':<40}")
    print("-" * 90)
    for net in networks:
        result = classify_ssid(net["ssid"], net["encryption"])
        flag_text = f"{result['reason']} ({result['severity']})" if result["flagged"] else "-"
        encryption_display = net["encryption"] or "unknown"
        if net["encryption"].lower() in WEAK_ENCRYPTION_VALUES:
            encryption_display += " [WEAK]"
            weak_encryption_count += 1
        if result["flagged"]:
            flagged_count += 1
        print(f"{net['ssid']:<28}{encryption_display:<12}{flag_text:<40}")

    print(f"\nSummary: {flagged_count} of {len(networks)} network(s) flagged for default-style naming.")
    if weak_encryption_count:
        print(f"WARNING: {weak_encryption_count} network(s) reported open or WEP encryption, "
              "which is considered cryptographically weak/broken regardless of SSID naming.")

    print(
        "\nReminder: a default-style SSID is a proxy indicator, not direct evidence of a specific "
        "vulnerability. Confirm findings through an authorized, in-scope technical assessment "
        "before drawing conclusions, and never attempt to access a network or its administrative "
        "interface without explicit authorization, per this folder's README."
    )


if __name__ == "__main__":
    main()
