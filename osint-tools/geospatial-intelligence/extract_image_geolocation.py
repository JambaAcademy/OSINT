#!/usr/bin/env python3
"""
extract_image_geolocation.py

Extract GPS coordinates and other relevant metadata (timestamp, camera
make/model) embedded in an image file's EXIF data, using the Pillow
library.

Purpose in an OSINT context:
    Many cameras and smartphones embed GPS coordinates and a capture
    timestamp directly into a photo's EXIF metadata. When present, this
    is one of the most direct forms of geolocation and chronolocation
    evidence available, and should be corroborated against other sources
    before being relied upon (see
    osint-templates/operational-planning/source-verification-framework.md).

Important limitation:
    Most major social media and messaging platforms strip EXIF metadata,
    including GPS data, from images on upload as a privacy protection
    measure. This script will typically only find GPS data in images
    obtained directly from a source, a personal website, camera export,
    or unprocessed email attachment — not in images downloaded from
    platforms like Instagram, X, Facebook, or WhatsApp.

Legal and ethical scope:
    Extracting metadata from an image you have lawfully obtained access
    to is a standard OSINT/verification technique. See
    osint-tools/geospatial-intelligence/location-tracking/README.md for
    the boundary this repository draws around using this technique
    against a private individual's non-public images.

Requirements:
    Python 3.8+
    Pillow (pip install Pillow --break-system-packages)

Usage:
    python extract_image_geolocation.py --file photo.jpg
    python extract_image_geolocation.py --file photo.jpg --json
"""

import argparse
import json
import sys

try:
    from PIL import Image, ExifTags
except ImportError:
    sys.exit(
        "This script requires the 'Pillow' package.\n"
        "Install it with: pip install Pillow --break-system-packages"
    )

# Build reverse lookup tables from Pillow's tag ID constants to human-readable names.
TAG_NAMES = {v: k for k, v in ExifTags.TAGS.items()}
GPS_TAG_NAMES = {v: k for k, v in ExifTags.GPSTAGS.items()}


def dms_to_decimal(dms, ref) -> float:
    """Convert an EXIF GPS coordinate (degrees, minutes, seconds tuple) to decimal degrees."""
    degrees, minutes, seconds = dms
    decimal = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
    if ref in ("S", "W"):
        decimal = -decimal
    return decimal


def extract_metadata(image_path: str) -> dict:
    """Extract EXIF metadata, including GPS coordinates if present, from an image file."""
    image = Image.open(image_path)
    exif_data = image.getexif()

    result = {
        "file": image_path,
        "camera_make": None,
        "camera_model": None,
        "datetime_original": None,
        "gps_latitude": None,
        "gps_longitude": None,
        "gps_altitude_m": None,
        "raw_gps_tags": {},
    }

    if not exif_data:
        return result

    readable = {}
    for tag_id, value in exif_data.items():
        tag_name = ExifTags.TAGS.get(tag_id, tag_id)
        readable[tag_name] = value

    result["camera_make"] = readable.get("Make")
    result["camera_model"] = readable.get("Model")
    result["datetime_original"] = readable.get("DateTimeOriginal") or readable.get("DateTime")

    # DateTimeOriginal typically lives in the Exif sub-IFD, not the top-level
    # IFD, so fall back to reading it there if not already found above.
    if result["datetime_original"] is None and hasattr(ExifTags, "IFD"):
        try:
            exif_sub_ifd = exif_data.get_ifd(ExifTags.IFD.Exif)
        except (KeyError, AttributeError):
            exif_sub_ifd = {}
        for tag_id, value in exif_sub_ifd.items():
            tag_name = ExifTags.TAGS.get(tag_id, tag_id)
            if tag_name == "DateTimeOriginal":
                result["datetime_original"] = value
                break

    # GPS data lives in a nested IFD (Image File Directory).
    gps_ifd = exif_data.get_ifd(ExifTags.IFD.GPSInfo) if hasattr(ExifTags, "IFD") else None
    if not gps_ifd:
        # Fallback for older Pillow versions: GPS tag ID 34853 holds the GPS IFD directly.
        gps_ifd = exif_data.get(34853)

    if gps_ifd:
        gps_readable = {}
        for tag_id, value in gps_ifd.items():
            tag_name = ExifTags.GPSTAGS.get(tag_id, tag_id)
            gps_readable[tag_name] = value
        result["raw_gps_tags"] = gps_readable

        lat = gps_readable.get("GPSLatitude")
        lat_ref = gps_readable.get("GPSLatitudeRef")
        lon = gps_readable.get("GPSLongitude")
        lon_ref = gps_readable.get("GPSLongitudeRef")

        if lat and lat_ref and lon and lon_ref:
            result["gps_latitude"] = round(dms_to_decimal(lat, lat_ref), 6)
            result["gps_longitude"] = round(dms_to_decimal(lon, lon_ref), 6)

        altitude = gps_readable.get("GPSAltitude")
        if altitude is not None:
            try:
                result["gps_altitude_m"] = round(float(altitude), 1)
            except (TypeError, ValueError):
                pass

    return result


def print_human_readable(result: dict) -> None:
    print(f"\nMetadata for: {result['file']}\n")
    print(f"Camera make/model: {result['camera_make'] or 'Not present'} / {result['camera_model'] or 'Not present'}")
    print(f"Capture timestamp (from EXIF, unverified): {result['datetime_original'] or 'Not present'}")

    if result["gps_latitude"] is not None:
        print(f"\nGPS coordinates found: {result['gps_latitude']}, {result['gps_longitude']}")
        if result["gps_altitude_m"] is not None:
            print(f"GPS altitude: {result['gps_altitude_m']} meters")
        print(
            f"\nMap link for manual verification: "
            f"https://www.openstreetmap.org/?mlat={result['gps_latitude']}&mlon={result['gps_longitude']}&zoom=16"
        )
        print(
            "\nCross-reference this location against visual landmarks in the image "
            "before relying on it, per osint-templates/operational-planning/"
            "source-verification-framework.md."
        )
    else:
        print(
            "\nNo GPS coordinates found in this image's EXIF metadata. This is common for "
            "images downloaded from social media platforms, which typically strip this data "
            "on upload. See this folder's README for alternative geolocation techniques."
        )


def main():
    parser = argparse.ArgumentParser(
        description="Extract GPS coordinates and other metadata from an image's EXIF data."
    )
    parser.add_argument("--file", required=True, help="Path to the image file to inspect")
    parser.add_argument("--json", action="store_true", help="Output raw results as JSON instead of a human-readable summary")
    args = parser.parse_args()

    try:
        result = extract_metadata(args.file)
    except FileNotFoundError:
        sys.exit(f"File not found: {args.file}")
    except Exception as exc:
        sys.exit(f"Could not read metadata from {args.file}: {exc}")

    if args.json:
        # raw_gps_tags may contain non-JSON-serializable IFDRational types; stringify defensively.
        safe_result = dict(result)
        safe_result["raw_gps_tags"] = {k: str(v) for k, v in result["raw_gps_tags"].items()}
        print(json.dumps(safe_result, indent=2, default=str))
    else:
        print_human_readable(result)


if __name__ == "__main__":
    main()
