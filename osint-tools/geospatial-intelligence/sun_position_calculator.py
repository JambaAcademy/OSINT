#!/usr/bin/env python3
"""
sun_position_calculator.py

Calculate the sun's elevation and azimuth angle for a given latitude,
longitude, date, and time, using the standard solar position formulas
published by NOAA's Global Monitoring Laboratory (a public-domain
government reference algorithm, commonly known as the NOAA Solar
Position Calculator method). No network access or external data is
required; this is a self-contained astronomical calculation.

Purpose in an OSINT context:
    This script supports "chronolocation" — verifying whether a claimed
    date and time for a photo, video, or satellite image are consistent
    with the shadows visible in it, as documented in
    osint-tools/geospatial-intelligence/satellite-imagery/README.md and
    osint-templates/specialized-formats/journalism-fact-check.md.

Accuracy note:
    This implementation uses the standard (non-elliptical-refraction-
    corrected) NOAA formulas, which are accurate to within a fraction of
    a degree for most dates — sufficient for chronolocation plausibility
    checking, but not intended for precision astronomical or navigational
    use. Atmospheric refraction near the horizon is not modeled.

Requirements:
    Python 3.8+ (standard library only, no third-party packages required)

Usage:
    python sun_position_calculator.py --lat 48.8584 --lon 2.2945 \\
        --datetime "2026-06-15T14:30:00" --utc-offset 2

    (Latitude/longitude for the Eiffel Tower, Paris; local time 14:30,
    Central European Summer Time is UTC+2.)

    If your date/time is already in UTC, omit --utc-offset or set it to 0.
"""

import argparse
import datetime
import math
import sys


def to_julian_day(dt_utc: datetime.datetime) -> float:
    """Convert a UTC datetime to a Julian Day number."""
    year = dt_utc.year
    month = dt_utc.month
    day = dt_utc.day + (dt_utc.hour + dt_utc.minute / 60 + dt_utc.second / 3600) / 24

    if month <= 2:
        year -= 1
        month += 12

    A = math.floor(year / 100)
    B = 2 - A + math.floor(A / 4)

    jd = (math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1))
          + day + B - 1524.5)
    return jd


def solar_position(lat_deg: float, lon_deg: float, dt_utc: datetime.datetime) -> dict:
    """
    Compute solar elevation and azimuth for a given latitude/longitude (degrees)
    and a UTC datetime, using the NOAA solar position formulas.

    Returns a dict with keys: elevation_deg, azimuth_deg, declination_deg,
    equation_of_time_min, hour_angle_deg.
    """
    jd = to_julian_day(dt_utc)
    T = (jd - 2451545.0) / 36525.0  # Julian century

    # Geometric mean longitude of the sun (degrees)
    L0 = (280.46646 + T * (36000.76983 + T * 0.0003032)) % 360

    # Geometric mean anomaly of the sun (degrees)
    M = 357.52911 + T * (35999.05029 - 0.0001537 * T)
    M_rad = math.radians(M)

    # Eccentricity of Earth's orbit
    e = 0.016708634 - T * (0.000042037 + 0.0000001267 * T)

    # Sun's equation of center
    C = (math.sin(M_rad) * (1.914602 - T * (0.004817 + 0.000014 * T))
         + math.sin(2 * M_rad) * (0.019993 - 0.000101 * T)
         + math.sin(3 * M_rad) * 0.000289)

    # Sun's true longitude and true anomaly
    true_long = L0 + C

    # Sun's apparent longitude (degrees), corrected for nutation/aberration
    omega = 125.04 - 1934.136 * T
    apparent_long = true_long - 0.00569 - 0.00478 * math.sin(math.radians(omega))

    # Mean obliquity of the ecliptic (degrees)
    mean_obliq = (23 + (26 + ((21.448 - T * (46.815 + T * (0.00059 - T * 0.001813)))) / 60) / 60)
    obliq_corr = mean_obliq + 0.00256 * math.cos(math.radians(omega))

    # Sun's declination (degrees)
    decl_rad = math.asin(math.sin(math.radians(obliq_corr)) * math.sin(math.radians(apparent_long)))
    declination = math.degrees(decl_rad)

    # Equation of time (minutes)
    y = math.tan(math.radians(obliq_corr / 2)) ** 2
    eot = 4 * math.degrees(
        y * math.sin(2 * math.radians(L0))
        - 2 * e * math.sin(M_rad)
        + 4 * e * y * math.sin(M_rad) * math.cos(2 * math.radians(L0))
        - 0.5 * y * y * math.sin(4 * math.radians(L0))
        - 1.25 * e * e * math.sin(2 * M_rad)
    )

    # True solar time (minutes) and hour angle (degrees)
    time_minutes = dt_utc.hour * 60 + dt_utc.minute + dt_utc.second / 60
    true_solar_time = (time_minutes + eot + 4 * lon_deg) % 1440

    if true_solar_time / 4 < 0:
        hour_angle = true_solar_time / 4 + 180
    else:
        hour_angle = true_solar_time / 4 - 180

    # Solar zenith angle
    lat_rad = math.radians(lat_deg)
    ha_rad = math.radians(hour_angle)

    cos_zenith = (math.sin(lat_rad) * math.sin(decl_rad)
                  + math.cos(lat_rad) * math.cos(decl_rad) * math.cos(ha_rad))
    cos_zenith = max(-1.0, min(1.0, cos_zenith))
    zenith = math.degrees(math.acos(cos_zenith))
    elevation = 90 - zenith

    # Solar azimuth angle (degrees clockwise from north)
    zenith_rad = math.radians(zenith)
    denom = math.cos(lat_rad) * math.sin(zenith_rad)
    if abs(denom) < 1e-6:
        azimuth = 0.0
    else:
        cos_az = (math.sin(lat_rad) * math.cos(zenith_rad) - math.sin(decl_rad)) / denom
        cos_az = max(-1.0, min(1.0, cos_az))
        azimuth = math.degrees(math.acos(cos_az))
        if hour_angle > 0:
            azimuth = 360 - azimuth

    return {
        "elevation_deg": elevation,
        "azimuth_deg": azimuth,
        "declination_deg": declination,
        "equation_of_time_min": eot,
        "hour_angle_deg": hour_angle,
    }


def describe_shadow(elevation_deg: float, azimuth_deg: float) -> str:
    if elevation_deg <= 0:
        return "The sun is below the horizon at this date/time/location; no direct shadow would be cast."
    shadow_direction = (azimuth_deg + 180) % 360
    shadow_length_multiplier = 1 / math.tan(math.radians(elevation_deg))
    return (
        f"Shadows would point toward approximately {shadow_direction:.1f} degrees "
        f"(measured clockwise from north), i.e. away from the sun. "
        f"An object's shadow length would be roughly {shadow_length_multiplier:.2f} times "
        f"its height (shorter near solar noon, longer near sunrise/sunset)."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Calculate solar elevation and azimuth for chronolocation verification."
    )
    parser.add_argument("--lat", type=float, required=True, help="Latitude in decimal degrees (positive = North)")
    parser.add_argument("--lon", type=float, required=True, help="Longitude in decimal degrees (positive = East)")
    parser.add_argument(
        "--datetime", required=True,
        help="Local date and time in ISO format, e.g. '2026-06-15T14:30:00'",
    )
    parser.add_argument(
        "--utc-offset", type=float, default=0.0,
        help="Offset in hours from UTC for the provided datetime (e.g. 2 for CEST, -5 for EST). Default 0 (already UTC).",
    )
    args = parser.parse_args()

    try:
        local_dt = datetime.datetime.fromisoformat(args.datetime)
    except ValueError:
        sys.exit("Could not parse --datetime. Use ISO format, e.g. '2026-06-15T14:30:00'.")

    utc_dt = local_dt - datetime.timedelta(hours=args.utc_offset)

    result = solar_position(args.lat, args.lon, utc_dt)

    print(f"\nSolar position for latitude {args.lat}, longitude {args.lon}")
    print(f"Local time: {local_dt.isoformat()} (UTC offset {args.utc_offset:+.1f}h)")
    print(f"UTC time used for calculation: {utc_dt.isoformat()}\n")
    print(f"Solar elevation: {result['elevation_deg']:.2f} degrees above the horizon")
    print(f"Solar azimuth:   {result['azimuth_deg']:.2f} degrees (clockwise from true north)")
    print(f"Solar declination: {result['declination_deg']:.2f} degrees")
    print(f"Equation of time: {result['equation_of_time_min']:.2f} minutes\n")
    print(describe_shadow(result["elevation_deg"], result["azimuth_deg"]))
    print(
        "\nCompare this to the shadow direction and length observed in the image or "
        "satellite frame under review. A significant mismatch suggests the claimed "
        "date/time may be inaccurate; note that local terrain, building height, lens "
        "distortion, and atmospheric refraction near the horizon introduce some margin "
        "of error."
    )


if __name__ == "__main__":
    main()
