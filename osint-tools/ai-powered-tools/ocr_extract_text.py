#!/usr/bin/env python3
"""
ocr_extract_text.py

Extract text from an image file (screenshot, scanned document, or
photographed sign) using the Tesseract OCR engine via the pytesseract
Python wrapper.

Purpose in an OSINT context:
    Useful for extracting readable text from a screenshot, a photographed
    document, or signage visible in a photo, as part of a broader
    investigation. See
    osint-tools/ai-powered-tools/image-recognition/README.md for
    accuracy notes and alternatives for higher-accuracy or large-scale
    needs.

Requirements:
    Python 3.8+
    pytesseract (pip install pytesseract --break-system-packages)
    Pillow (pip install Pillow --break-system-packages)
    The Tesseract OCR binary must also be installed separately as a
    system package (it is not a Python package):
        Debian/Ubuntu: sudo apt-get install tesseract-ocr
        macOS (Homebrew): brew install tesseract
        Windows: see https://github.com/tesseract-ocr/tesseract

Usage:
    python ocr_extract_text.py --file screenshot.png
    python ocr_extract_text.py --file screenshot.png --lang eng+fra
    python ocr_extract_text.py --file screenshot.png --confidence
"""

import argparse
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit(
        "This script requires the 'Pillow' package.\n"
        "Install it with: pip install Pillow --break-system-packages"
    )

try:
    import pytesseract
except ImportError:
    sys.exit(
        "This script requires the 'pytesseract' package.\n"
        "Install it with: pip install pytesseract --break-system-packages\n"
        "You must also install the Tesseract OCR binary separately (see this "
        "script's header comment for OS-specific instructions)."
    )


def extract_text(image_path: str, lang: str = "eng") -> str:
    image = Image.open(image_path)
    return pytesseract.image_to_string(image, lang=lang)


def extract_with_confidence(image_path: str, lang: str = "eng", min_confidence: int = 0) -> list:
    """Return a list of (text, confidence) tuples for each recognized word above min_confidence."""
    image = Image.open(image_path)
    data = pytesseract.image_to_data(image, lang=lang, output_type=pytesseract.Output.DICT)
    results = []
    for text, conf in zip(data["text"], data["conf"]):
        text = text.strip()
        try:
            conf_val = int(conf)
        except (TypeError, ValueError):
            conf_val = -1
        if text and conf_val >= min_confidence:
            results.append((text, conf_val))
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from an image using Tesseract OCR."
    )
    parser.add_argument("--file", required=True, help="Path to the image file")
    parser.add_argument(
        "--lang", default="eng",
        help="Tesseract language code(s), e.g. 'eng', 'fra', or 'eng+fra' for multiple. Default 'eng'.",
    )
    parser.add_argument(
        "--confidence", action="store_true",
        help="Show per-word confidence scores instead of plain extracted text",
    )
    parser.add_argument(
        "--min-confidence", type=int, default=0,
        help="When used with --confidence, only show words at or above this confidence (0-100). Default 0.",
    )
    args = parser.parse_args()

    try:
        if args.confidence:
            results = extract_with_confidence(args.file, lang=args.lang, min_confidence=args.min_confidence)
            print(f"\nRecognized words with confidence scores (image: {args.file}):\n")
            for text, conf in results:
                print(f"  [{conf:3d}%] {text}")
            low_conf_count = sum(1 for _, c in results if 0 <= c < 60)
            if low_conf_count:
                print(
                    f"\n{low_conf_count} word(s) had confidence below 60%; manually verify these "
                    "against the source image before relying on them."
                )
        else:
            text = extract_text(args.file, lang=args.lang)
            print(f"\nExtracted text from {args.file}:\n")
            print(text if text.strip() else "(no text recognized)")
    except FileNotFoundError:
        sys.exit(f"File not found: {args.file}")
    except pytesseract.TesseractNotFoundError:
        sys.exit(
            "Tesseract OCR binary not found. Install it separately from pytesseract:\n"
            "  Debian/Ubuntu: sudo apt-get install tesseract-ocr\n"
            "  macOS (Homebrew): brew install tesseract"
        )

    print(
        "\nReminder: manually verify extracted text against the source image before use in a "
        "report, particularly for numbers, dates, and names, which OCR commonly misreads."
    )


if __name__ == "__main__":
    main()
