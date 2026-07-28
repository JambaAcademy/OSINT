#!/usr/bin/env python3
"""
geolocation_correlation_calculator.py

Compute the great-circle distance and initial compass bearing between two
coordinate pairs, and assess whether travel between them is feasible given
an elapsed time and a selected travel mode's typical speed range.

Purpose in an OSINT context:
    Supports geographic correlation analysis as documented in
    osint-tools/geospatial-intelligence/geographic-correlation/README.md —
    for example, assessing whether two reported sightings of the same
    subject, at two different times and places, are physically consistent
    with each other. This is primarily a falsification tool: it is most
    useful for ruling out a claim as impossible, not for confirming a
    claim is true.

Requirements:
    Python 3.8+ (standard library only, no third-party packages required)

Usage:
    python geolocation_correlation_calculator.py \\
        --lat1 48.8584 --lon1 2.2945 --time1 "2026-06-15T09:00:00" \\
        --lat2 51.5074 --lon2 -0.1278 --time2 "2026-06-15T12:00:00" \\
        --mode commercial_flight

    Run with --list-modes to see all supported travel modes and their
    assumed speed ranges.
"""

import argparse
import datetime
import math
import sys

EARTH_RADIUS_KM = 6371.0088

# Conservative typical speed ranges (km/h) used for feasibility checking.
# These are deliberately generous (a wide low-to-high range) since this is a
# plausibility check, not a precise transit-time prediction.
TRAVEL_MODES = {
    "walking": (3, 6),
    "cycling": (10, 25),
    "car_urban": (20, 60),
    "car_highway": (60, 130),
    "train_regional": (60, 120),
    "train_highspeed": (150, 320),
    "commercial_flight": (700, 950),  # includes typical cruise speed; does not add airport/ground time
    "private_jet": (700, 900),
    "ship_commercial": (15, 45),
}


def haversine_distance_km(lat1, lon1, lat2, lon2) -> float:
    """Great-circle distance between two points in kilometers."""
    lat1_r, lon1_r, lat2_r, lon2_r = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2_r - lat1_r
    dlon = lon2_r - lon1_r
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_r) * math.cos(lat2_r) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(min(1, math.sqrt(a)))
    return EARTH_RADIUS_KM * c


def initial_bearing_deg(lat1, lon1, lat2, lon2) -> float:
    """Initial compass bearing (degrees, clockwise from true north) from point 1 to point 2."""
    lat1_r, lat2_r = math.radians(lat1), math.radians(lat2)
    dlon_r = math.radians(lon2 - lon1)
    x = math.sin(dlon_r) * math.cos(lat2_r)
    y = math.cos(lat1_r) * math.sin(lat2_r) - math.sin(lat1_r) * math.cos(lat2_r) * math.cos(dlon_r)
    bearing = math.degrees(math.atan2(x, y))
    return (bearing + 360) % 360


def bearing_to_compass(bearing_deg: float) -> str:
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = round(bearing_deg / 22.5) % 16
    return directions[index]


def assess_feasibility(distance_km: float, elapsed_hours: float, mode: str) -> dict:
    low_speed, high_speed = TRAVEL_MODES[mode]
    min_hours_needed = distance_km / high_speed
    max_reasonable_hours = distance_km / low_speed

    if elapsed_hours <= 0:
        feasible = False
        note = "Elapsed time is zero or negative; travel between distinct locations is not possible."
    elif elapsed_hours < min_hours_needed:
        feasible = False
        note = (
            f"Not feasible: even at the high end of typical {mode.replace('_', ' ')} speed "
            f"({high_speed} km/h), this distance would require at least {min_hours_needed:.2f} hours, "
            f"more than the {elapsed_hours:.2f} hours elapsed."
        )
    elif elapsed_hours > max_reasonable_hours * 3:
        feasible = True
        note = (
            f"Feasible, with substantial time to spare. At typical {mode.replace('_', ' ')} speeds, "
            f"this trip would take roughly {min_hours_needed:.2f}-{max_reasonable_hours:.2f} hours, "
            f"well within the {elapsed_hours:.2f} hours elapsed."
        )
    else:
        feasible = True
        note = (
            f"Feasible. At typical {mode.replace('_', ' ')} speeds, this trip would take roughly "
            f"{min_hours_needed:.2f}-{max_reasonable_hours:.2f} hours, consistent with the "
            f"{elapsed_hours:.2f} hours elapsed."
        )

    return {
        "feasible": feasible,
        "min_hours_needed": min_hours_needed,
        "typical_max_hours": max_reasonable_hours,
        "note": note,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Assess geographic and temporal consistency between two location/time data points."
    )
    parser.add_argument("--list-modes", action="store_true", help="List supported travel modes and speed ranges, then exit")
    parser.add_argument("--lat1", type=float, help="Latitude of point 1")
    parser.add_argument("--lon1", type=float, help="Longitude of point 1")
    parser.add_argument("--time1", help="ISO datetime at point 1, e.g. '2026-06-15T09:00:00' (assumed same timezone as --time2 unless both include UTC offsets)")
    parser.add_argument("--lat2", type=float, help="Latitude of point 2")
    parser.add_argument("--lon2", type=float, help="Longitude of point 2")
    parser.add_argument("--time2", help="ISO datetime at point 2")
    parser.add_argument(
        "--mode", choices=list(TRAVEL_MODES.keys()), default="car_highway",
        help="Assumed travel mode for feasibility checking (default: car_highway)",
    )
    args = parser.parse_args()

    if args.list_modes:
        print("\nSupported travel modes and assumed speed ranges (km/h):\n")
        for mode, (low, high) in TRAVEL_MODES.items():
            print(f"  {mode:<20} {low}-{high} km/h")
        print(
            "\nThese are deliberately wide, conservative ranges for plausibility checking, "
            "not precise transit-time prediction, and do not account for boarding, "
            "connection, or ground transportation time for flights."
        )
        return

    required = [args.lat1, args.lon1, args.time1, args.lat2, args.lon2, args.time2]
    if any(v is None for v in required):
        sys.exit("All of --lat1, --lon1, --time1, --lat2, --lon2, --time2 are required (or use --list-modes).")

    try:
        t1 = datetime.datetime.fromisoformat(args.time1)
        t2 = datetime.datetime.fromisoformat(args.time2)
    except ValueError:
        sys.exit("Could not parse --time1/--time2. Use ISO format, e.g. '2026-06-15T09:00:00'.")

    distance = haversine_distance_km(args.lat1, args.lon1, args.lat2, args.lon2)
    bearing = initial_bearing_deg(args.lat1, args.lon1, args.lat2, args.lon2)
    compass = bearing_to_compass(bearing)
    elapsed_hours = abs((t2 - t1).total_seconds()) / 3600

    print(f"\nPoint 1: ({args.lat1}, {args.lon1}) at {t1.isoformat()}")
    print(f"Point 2: ({args.lat2}, {args.lon2}) at {t2.isoformat()}\n")
    print(f"Great-circle distance: {distance:.1f} km ({distance * 0.621371:.1f} miles)")
    print(f"Initial bearing from point 1 to point 2: {bearing:.1f} degrees ({compass})")
    print(f"Elapsed time between the two timestamps: {elapsed_hours:.2f} hours\n")

    result = assess_feasibility(distance, elapsed_hours, args.mode)
    print(f"Feasibility assessment (assumed mode: {args.mode}):")
    print(f"  {result['note']}\n")
    print(
        "Note: great-circle distance is a straight-line lower bound. Actual travel "
        "distance by road, rail, or sea is typically longer. This assessment does not "
        "account for boarding time, connections, customs/immigration, or ground transport "
        "to/from airports and stations. Use this to rule out clearly impossible claims, "
        "not to confirm a claim is true — meeting the minimum time requirement does not "
        "prove the claimed travel actually took place."
    )


if __name__ == "__main__":
    main()
