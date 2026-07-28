# AI-Powered Tools

## Overview

This category covers artificial intelligence and machine learning platforms and techniques applicable to OSINT workflows: general machine learning, natural language processing, image recognition, pattern analysis, and automated report generation. Every tool and script in this category is an aid to human analytical judgment, not a replacement for it — see `osint-templates/ai-assisted-templates/` for the reporting templates that require human verification of any AI-assisted finding before it is presented as a conclusion.

Each subfolder includes a ready-to-use, tested working script demonstrating the relevant technique using freely available libraries.

---

## Subfolders

| Subfolder | Description | Includes Working Files |
|---|---|---|
| [`machine-learning/`](machine-learning/README.md) | General ML platforms and techniques | Text similarity clustering script (Python, scikit-learn) |
| [`natural-language-processing/`](natural-language-processing/README.md) | Text analysis and entity extraction | Heuristic entity extraction script (Python, no heavy dependencies) |
| [`image-recognition/`](image-recognition/README.md) | Object detection, OCR, and image classification | OCR text extraction script (Python, Tesseract) |
| [`pattern-analysis/`](pattern-analysis/README.md) | Temporal and behavioral pattern detection | Posting-time/timezone inference script (Python) |
| [`automated-reporting/`](automated-reporting/README.md) | AI-assisted report drafting and generation | Findings-to-report generator script (Python) |

---

## Foundational Principle for This Category

Every script and tool in this category produces a *lead*, not a *finding*. Before any AI/ML-assisted output is included in a final report, it should be independently verified by a human analyst, consistent with:

- `osint-templates/ai-assisted-templates/ai-pattern-analysis.md`
- `osint-templates/ai-assisted-templates/machine-learning-insights.md`
- `osint-templates/ai-assisted-templates/sentiment-analysis-report.md` (see also `social-media-intelligence/sentiment-analysis/`)
- `osint-templates/ai-assisted-templates/predictive-intelligence.md`

---

## When to Use This Category

- Processing a large volume of collected text, images, or data points beyond what manual review can reasonably cover, to prioritize what a human analyst reviews first.
- Extracting structured entities (names, organizations, dates, contact details) from unstructured documents as a first-pass triage step.
- Detecting patterns (timing, similarity, anomaly) that would be difficult to spot manually across a large dataset.
- Speeding up the drafting of a report's boilerplate structure from structured findings data, leaving the analyst to focus on interpretation and verification.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
