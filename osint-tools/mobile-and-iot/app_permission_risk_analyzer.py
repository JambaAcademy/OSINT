#!/usr/bin/env python3
"""
app_permission_risk_analyzer.py

Flag mobile app permission requests that appear disproportionate to the
app's declared category, using a reference mapping of commonly expected
permissions per category. A flashlight app requesting contacts and
precise location access is a well-documented example of this kind of
red flag in mobile app security research and journalism.

Purpose in an OSINT context:
    Supports a first-pass triage of an app's declared permissions
    (recorded from a public app store listing, an APK analysis tool, or
    an installed app's settings) to identify requests worth further
    investigation. See
    osint-tools/mobile-and-iot/app-analysis/README.md for important
    limitations: a flagged permission is a prompt for further
    investigation, not proof of malicious intent.

Requirements:
    Python 3.8+ (standard library only, no third-party packages required)

Usage:
    python app_permission_risk_analyzer.py --input app_permissions.json
    python app_permission_risk_analyzer.py --input app_permissions.csv

Input JSON structure (see sample_app_permissions.json for a full example):
    {
        "apps": [
            {
                "app_name": "...",
                "category": "Flashlight/Utility",
                "requested_permissions": ["CAMERA", "INTERNET", "CONTACTS", "SMS"]
            }
        ]
    }

Input CSV structure (one row per app; permissions semicolon-separated):
    app_name,category,requested_permissions
    Sample Flashlight,Flashlight/Utility,CAMERA;INTERNET;CONTACTS;SMS

Recognized permission labels (platform-agnostic; map your platform's
specific permission strings to these before use):
    CAMERA, MICROPHONE, LOCATION_PRECISE, LOCATION_APPROXIMATE, CONTACTS,
    SMS, CALL_LOG, STORAGE, PHOTOS, CALENDAR, BLUETOOTH, INTERNET,
    BODY_SENSORS, DEVICE_ID, ACCOUNTS, NOTIFICATIONS

Recognized categories (apps in an unlisted category are still analyzed,
using a minimal generic baseline, with a note that results are less
precise):
    Flashlight/Utility, Camera, Messaging, Social Media, Games,
    Productivity, Health & Fitness, Navigation/Maps, Finance, Shopping
"""

import argparse
import csv
import json
import sys

# Reference mapping of permissions ordinarily expected for each app category.
# This is a general-purpose heuristic baseline, not an exhaustive or
# authoritative standard; treat flagged permissions as a lead, not a verdict.
CATEGORY_EXPECTED_PERMISSIONS = {
    "Flashlight/Utility": {"CAMERA", "INTERNET"},
    "Camera": {"CAMERA", "STORAGE", "PHOTOS", "INTERNET"},
    "Messaging": {"CONTACTS", "SMS", "CAMERA", "MICROPHONE", "STORAGE", "INTERNET", "NOTIFICATIONS"},
    "Social Media": {"CAMERA", "MICROPHONE", "STORAGE", "PHOTOS", "CONTACTS",
                      "LOCATION_APPROXIMATE", "INTERNET", "NOTIFICATIONS"},
    "Games": {"STORAGE", "INTERNET", "NOTIFICATIONS"},
    "Productivity": {"STORAGE", "CALENDAR", "ACCOUNTS", "INTERNET", "NOTIFICATIONS"},
    "Health & Fitness": {"BODY_SENSORS", "LOCATION_APPROXIMATE", "STORAGE", "INTERNET", "NOTIFICATIONS"},
    "Navigation/Maps": {"LOCATION_PRECISE", "INTERNET", "STORAGE"},
    "Finance": {"CAMERA", "STORAGE", "INTERNET", "ACCOUNTS", "NOTIFICATIONS"},
    "Shopping": {"STORAGE", "INTERNET", "NOTIFICATIONS", "CAMERA"},
}

GENERIC_BASELINE_PERMISSIONS = {"INTERNET", "STORAGE", "NOTIFICATIONS"}

HIGH_SENSITIVITY_PERMISSIONS = {
    "CONTACTS", "SMS", "CALL_LOG", "LOCATION_PRECISE", "MICROPHONE",
    "CAMERA", "BODY_SENSORS", "ACCOUNTS", "DEVICE_ID",
}


def load_apps(path: str) -> list:
    if path.lower().endswith(".json"):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("apps", [])
    elif path.lower().endswith(".csv"):
        apps = []
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                perms = [p.strip() for p in row.get("requested_permissions", "").split(";") if p.strip()]
                apps.append({
                    "app_name": row.get("app_name", "").strip(),
                    "category": row.get("category", "").strip(),
                    "requested_permissions": perms,
                })
        return apps
    else:
        sys.exit("Input file must be .json or .csv")


def analyze_app(app: dict) -> dict:
    category = app.get("category", "")
    requested = set(app.get("requested_permissions", []))

    if category in CATEGORY_EXPECTED_PERMISSIONS:
        expected = CATEGORY_EXPECTED_PERMISSIONS[category]
        category_recognized = True
    else:
        expected = GENERIC_BASELINE_PERMISSIONS
        category_recognized = False

    unexpected = requested - expected
    flagged = []
    for perm in sorted(unexpected):
        severity = "High" if perm in HIGH_SENSITIVITY_PERMISSIONS else "Medium"
        flagged.append({"permission": perm, "severity": severity})

    high_count = sum(1 for f in flagged if f["severity"] == "High")

    if high_count >= 2:
        overall_risk = "High"
    elif high_count == 1 or len(flagged) >= 2:
        overall_risk = "Medium"
    elif flagged:
        overall_risk = "Low"
    else:
        overall_risk = "None"

    return {
        "app_name": app.get("app_name", "Unnamed app"),
        "category": category or "Unspecified",
        "category_recognized": category_recognized,
        "requested_permissions": sorted(requested),
        "flagged_permissions": flagged,
        "overall_risk": overall_risk,
    }


def print_report(results: list) -> None:
    for r in results:
        print(f"\n=== {r['app_name']} ({r['category']}) ===")
        if not r["category_recognized"]:
            print("  Note: category not in reference mapping; using a minimal generic baseline "
                  "(results are less precise for this app).")
        print(f"  Requested permissions: {', '.join(r['requested_permissions']) or '(none)'}")
        if r["flagged_permissions"]:
            print(f"  Flagged (unexpected for this category):")
            for f in r["flagged_permissions"]:
                print(f"    - {f['permission']} (severity: {f['severity']})")
        else:
            print("  No unexpected permissions flagged relative to this category's baseline.")
        print(f"  Overall risk assessment: {r['overall_risk']}")

    print(
        "\nReminder: a flagged permission is a prompt for further investigation, not proof of "
        "malicious intent. Check the developer's stated justification for any flagged permission "
        "before drawing a conclusion, per this folder's README."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Flag mobile app permissions that appear disproportionate to the app's declared category."
    )
    parser.add_argument("--input", required=True, help="Path to an app permissions .json or .csv file")
    args = parser.parse_args()

    apps = load_apps(args.input)
    if not apps:
        sys.exit("No apps found in the input file.")

    results = [analyze_app(app) for app in apps]
    print_report(results)


if __name__ == "__main__":
    main()
