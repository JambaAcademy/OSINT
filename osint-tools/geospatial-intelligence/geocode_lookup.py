#!/usr/bin/env python3
"""
geocode_lookup.py

Convert an address to coordinates (geocoding) or coordinates to an address
(reverse geocoding) using the free, public OpenStreetMap Nominatim API.

Official data source and usage policy:
    https://nominatim.org/release-docs/latest/api/Overview/
    https://operations.osmfoundation.org/policies/nominatim/

Nominatim's public instance usage policy requires:
    - No more than 1 request per second (this script enforces a minimum
      delay between requests by default).
    - A valid HTTP Referer or descriptive User-Agent identifying your
      application (set via --contact below).
    - No heavy/bulk usage of the public instance; for high-volume geocoding,
      run your own Nominatim instance or use a commercial geocoding API
      instead, per Nominatim's policy.

Legal and ethical scope:
    This script queries only publicly available, open mapping data.
    Geocoding a specific individual's home address obtained from another
    source, or reverse-geocoding coordinates to locate someone, should
    only be done consistent with the elevated standard described in
    osint-tools/people-investigation/README.md.

Requirements:
    Python 3.8+
    requests (pip install requests --break-system-packages)

Usage:
    python geocode_lookup.py --address "1600 Pennsylvania Avenue NW, Washington, DC"
    python geocode_lookup.py --lat 38.8977 --lon -77.0365
    python geocode_lookup.py --address "Eiffel Tower, Paris" --contact "Jane Analyst jane@example.com"
"""

import argparse
import os
import sys
import time

try:
    import requests
except ImportError:
    sys.exit(
        "This script requires the 'requests' package.\n"
        "Install it with: pip install requests --break-system-packages"
    )

NOMINATIM_BASE = "https://nominatim.openstreetmap.org"
MIN_REQUEST_INTERVAL_SECONDS = 1.0


def build_headers(contact: str) -> dict:
    contact = contact or "OSINT-Mastery-Guide-User (please set --contact or NOMINATIM_CONTACT)"
    return {"User-Agent": contact}


def geocode(address: str, headers: dict) -> list:
    """Forward geocode an address string to one or more candidate locations."""
    params = {"q": address, "format": "jsonv2", "addressdetails": 1, "limit": 5}
    response = requests.get(f"{NOMINATIM_BASE}/search", params=params, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()


def reverse_geocode(lat: float, lon: float, headers: dict) -> dict:
    """Reverse geocode a latitude/longitude pair to a place description."""
    params = {"lat": lat, "lon": lon, "format": "jsonv2", "addressdetails": 1}
    response = requests.get(f"{NOMINATIM_BASE}/reverse", params=params, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()


def print_geocode_results(results: list) -> None:
    if not results:
        print("No results found for that address.")
        return
    print(f"\n{len(results)} result(s) found:\n")
    for i, r in enumerate(results, start=1):
        print(f"{i}. {r.get('display_name')}")
        print(f"   Latitude: {r.get('lat')}  Longitude: {r.get('lon')}")
        print(f"   Place type: {r.get('type')}  Class: {r.get('class')}")
        print(f"   OpenStreetMap ID: {r.get('osm_type')}/{r.get('osm_id')}")
        print()


def print_reverse_result(result: dict) -> None:
    if "error" in result:
        print(f"No result found: {result['error']}")
        return
    print(f"\nAddress for the given coordinates:\n")
    print(f"  {result.get('display_name')}")
    address = result.get("address", {})
    for key in ["road", "neighbourhood", "suburb", "city", "county", "state", "postcode", "country"]:
        if key in address:
            print(f"  {key.capitalize()}: {address[key]}")


def main():
    parser = argparse.ArgumentParser(
        description="Geocode an address or reverse geocode coordinates using OpenStreetMap Nominatim."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--address", help="Address or place name to geocode")
    group.add_argument("--lat", type=float, help="Latitude for reverse geocoding (requires --lon)")
    parser.add_argument("--lon", type=float, help="Longitude for reverse geocoding (requires --lat)")
    parser.add_argument(
        "--contact",
        default=os.environ.get("NOMINATIM_CONTACT", ""),
        help="Contact identifier for the User-Agent header, e.g. 'Jane Analyst jane@example.com'. "
             "Defaults to the NOMINATIM_CONTACT environment variable if set. Required by Nominatim's usage policy.",
    )
    args = parser.parse_args()

    if args.lat is not None and args.lon is None:
        parser.error("--lat requires --lon")

    headers = build_headers(args.contact)

    # Respect Nominatim's public instance rate limit even for a single call,
    # in case this script is invoked in a loop by the calling environment.
    time.sleep(MIN_REQUEST_INTERVAL_SECONDS)

    if args.address:
        results = geocode(args.address, headers)
        print_geocode_results(results)
    else:
        result = reverse_geocode(args.lat, args.lon, headers)
        print_reverse_result(result)


if __name__ == "__main__":
    main()
