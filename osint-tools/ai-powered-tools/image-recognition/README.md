# Image Recognition

## Overview

This section covers object detection, optical character recognition (OCR), and image classification tools. See `ocr_extract_text.py` in this folder for a ready-to-use script that extracts text from an image (such as a screenshot, scanned document, or photographed sign) using Tesseract OCR.

Reverse image search (finding where else an image appears online) is covered in `social-media-intelligence/cross-platform-analyzers/README.md` rather than here, since it is a search/correlation technique rather than an image content-recognition technique.

---

## Optical Character Recognition (OCR)

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Tesseract OCR | Widely used open-source OCR engine supporting over 100 languages | Extracting text from screenshots, scanned documents, and photographed signage | Free, open source |
| Google Cloud Vision API (OCR) | Managed cloud OCR service with strong accuracy on difficult/low-quality images | Higher-accuracy OCR at scale, or for challenging source images | Paid, usage-based |
| Amazon Textract | Managed cloud OCR service with strong structured-document extraction (tables, forms) | Extracting structured data from forms and tables, not just plain text | Paid, usage-based |
| ABBYY FineReader | Commercial desktop OCR software with strong accuracy and layout preservation | Professional document digitization workflows | Paid |

## Object and Scene Detection

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Google Cloud Vision API (object/label detection) | Managed cloud service for general object, label, and landmark detection in images | Identifying general objects, scenes, and some landmarks in an image | Paid, usage-based |
| YOLO (You Only Look Once) family of models | Open-source real-time object detection models | Custom or offline object detection pipelines | Free, open source (compute required) |
| Google Cloud Vision API (landmark detection) | Identifies well-known landmarks visible in an image | Supporting geolocation verification when a recognizable landmark is present (see `geospatial-intelligence/`) | Paid, usage-based |

## Image Classification and Content Moderation Signals

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Google Cloud Vision API (SafeSearch) | Flags images for adult, violent, or otherwise sensitive content categories | Pre-screening large image sets before manual review | Paid, usage-based |
| Hugging Face vision models | Pre-trained image classification models across many categories | Custom classification tasks using open models | Free (open models); compute cost applies |

---

## Using the Included OCR Script

`ocr_extract_text.py` extracts text from an image file using the Tesseract OCR engine via the `pytesseract` Python wrapper. Tesseract must be installed separately as a system package (it is a compiled binary, not a Python package).

```bash
# Install the Tesseract binary (varies by OS)
# Debian/Ubuntu: sudo apt-get install tesseract-ocr
# macOS (Homebrew): brew install tesseract

pip install pytesseract Pillow --break-system-packages
python ocr_extract_text.py --file screenshot.png
python ocr_extract_text.py --file screenshot.png --lang eng+fra
```

---

## Usage Notes

- OCR accuracy depends heavily on image quality, resolution, and contrast; low-resolution screenshots or photographs taken at an angle will produce more errors. Consider basic image preprocessing (contrast enhancement, deskewing) for difficult source images before running OCR.
- Always manually verify OCR output against the source image before relying on extracted text in a report, particularly for numbers, dates, and names, which OCR engines commonly misread (e.g., confusing "0" and "O", or "1" and "l").
- Multi-language documents require specifying the correct language pack(s) (`--lang`); Tesseract's default English model will produce poor results on non-English text.

---

## Legal and Ethical Notes

- OCR and image recognition techniques in this section operate on images already lawfully obtained as part of a documented investigation.
- Facial recognition search is addressed separately and with additional caution in `social-media-intelligence/cross-platform-analyzers/README.md`, given its heightened privacy sensitivity; this section's object/scene/text recognition tools do not identify specific individuals and carry substantially lower sensitivity.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
