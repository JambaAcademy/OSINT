# Natural Language Processing

## Overview

This section covers text analysis techniques including entity extraction, language detection, and text summarization. See `extract_entities.py` in this folder for a ready-to-use, dependency-light script that performs a first-pass extraction of common entity types (email addresses, phone numbers, URLs, dates, monetary amounts, and candidate proper names) from a block of text.

---

## Named Entity Recognition (NER) Platforms and Libraries

| Tool | Description | Best For | Cost |
|---|---|---|---|
| spaCy | Widely used production NLP library with pre-trained NER models across many languages | High-accuracy entity extraction (people, organizations, locations, dates) integrated into a larger pipeline | Free, open source |
| Hugging Face Transformers (NER models) | Access to pre-trained transformer-based NER models, often more accurate than traditional NER for complex text | Higher-accuracy entity extraction where compute resources allow | Free (open models); compute cost applies |
| Amazon Comprehend | Managed cloud NLP service including entity recognition, key phrase extraction, and sentiment | Scalable, managed NLP without hosting your own models | Paid, usage-based |
| Google Cloud Natural Language API | Managed cloud NLP service with entity recognition and syntax analysis | Scalable, managed NLP with strong multilingual support | Paid, usage-based |

## Language Detection and Translation

| Tool | Description | Best For | Cost |
|---|---|---|---|
| langdetect / fastText language identification | Lightweight language identification libraries | Quickly determining the language(s) present in a collected dataset before further processing | Free, open source |
| DeepL / Google Translate (API) | Machine translation services | Translating non-English source material for analysis (see the multilingual note in `social-media-intelligence/sentiment-analysis/README.md`) | Freemium/Paid |

## Text Summarization

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Hugging Face summarization models (e.g., BART, T5-based models) | Pre-trained abstractive summarization models | Condensing long documents for faster analyst triage | Free (open models); compute cost applies |
| Large language model APIs (used with a clear, scoped prompt) | General-purpose language models can summarize and extract structure from text given a clear prompt | Flexible summarization and structured extraction tasks | Paid, usage-based |

---

## Using the Included Entity Extraction Script

`extract_entities.py` uses pattern-matching (regular expressions) and capitalization heuristics rather than a trained machine learning model, so it requires no additional downloads and runs instantly on any machine with Python installed. It is a fast, no-dependency **first-pass triage tool**, not a substitute for a trained NER model like spaCy when working with a large corpus or where higher accuracy is required.

```bash
python extract_entities.py --file document.txt
python extract_entities.py --file document.txt --json
```

It extracts: email addresses, phone numbers (common formats), URLs, dates (several common formats), monetary amounts, and candidate proper names (capitalized word sequences, which will include some false positives such as sentence-initial capitalized words).

---

## Usage Notes

- The included heuristic extractor is intentionally lightweight and will produce more false positives (and some false negatives) than a trained NER model such as spaCy; use it for quick triage of a document, and use spaCy or a Hugging Face model for a large corpus or a final, more precise extraction pass.
- Candidate proper names extracted by the heuristic script are not classified as person/organization/location; a human analyst (or a full NER model) is needed to categorize them.
- Always corroborate any entity extracted by an automated tool against the source document directly before using it in a report, consistent with `osint-templates/ai-assisted-templates/ai-pattern-analysis.md`.

---

## Legal and Ethical Notes

- Text analysis techniques in this section operate on text already lawfully obtained as part of a documented investigation.
- Where entity extraction surfaces personal information about identifiable individuals, handle and report on that information consistent with `osint-templates/operational-planning/legal-compliance-checklist.md`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
