# Sentiment Analysis Tools

## Overview

Sentiment analysis tools apply natural language processing to classify the emotional tone or opinion expressed in text, commonly used in OSINT for gauging public reaction to a brand, event, individual, or piece of content at scale. This section covers commercial and open-source sentiment analysis platforms; see `osint-templates/ai-assisted-templates/sentiment-analysis-report.md` for the reporting template and required limitations disclosure that should accompany any use of these tools.

---

## Commercial Social Listening and Sentiment Platforms

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Brandwatch | Enterprise social listening platform with sentiment classification, trend detection, and audience analysis | Large-scale, ongoing brand or topic monitoring | Paid, enterprise pricing |
| Talkwalker | Social listening and analytics platform covering social media, news, and blogs with sentiment scoring | Cross-source (social plus traditional media) sentiment tracking | Paid, enterprise pricing |
| Meltwater | Media and social monitoring platform with sentiment and influencer identification features | PR and communications-focused monitoring | Paid, enterprise pricing |
| Sprout Social | Social media management platform with built-in sentiment and engagement analytics | Brand-focused sentiment tracking integrated with social account management | Paid, tiered pricing |

## Open Source and Developer Libraries

| Tool | Description | Best For | Cost |
|---|---|---|---|
| VADER (Valence Aware Dictionary and sEntiment Reasoner) | Lexicon- and rule-based sentiment analysis tool tuned specifically for social media text, including slang and emoji | Lightweight, fast sentiment scoring of social media-style short text | Free, open source |
| TextBlob | Python library providing simple sentiment polarity and subjectivity scoring | Quick prototyping and small-scale sentiment analysis tasks | Free, open source |
| Hugging Face Transformers (sentiment models) | Access to a wide range of pre-trained transformer-based sentiment and emotion classification models | Higher-accuracy sentiment classification, including multilingual and domain-specific models | Free (open models); compute cost applies for hosting/inference |
| spaCy (with sentiment extensions) | General-purpose NLP library that can be extended with sentiment classification components | Sentiment analysis integrated into a broader NLP pipeline (entity extraction, etc.) | Free, open source |

## Multilingual Considerations

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Multilingual transformer models (e.g., XLM-R-based sentiment models) | Pre-trained models supporting sentiment classification across dozens of languages | Investigations spanning non-English content | Free (open models); compute cost applies |
| Machine translation plus English-model classification (fallback approach) | Translating source text before applying an English-tuned sentiment model | A pragmatic fallback when no adequate native-language model is available, with awareness that translation can distort sentiment-bearing nuance (sarcasm, idiom) | Varies by translation service used |

---

## Usage Notes

- No automated sentiment tool reliably handles sarcasm, irony, or culturally specific expression; always pair automated scoring with the manual validation sampling described in `osint-templates/ai-assisted-templates/sentiment-analysis-report.md`.
- Lexicon-based tools (VADER) are fast and transparent in their reasoning but less accurate on nuanced or novel language than modern transformer-based models, which are more accurate but harder to interpret directly.
- Aggregate sentiment percentages can obscure meaningful subgroup variation; where the investigation's objective calls for it, break results down by relevant subgroup (platform, region, time period) rather than reporting only a single blended figure.

---

## Legal and Ethical Notes

- Large-scale social listening tools that collect content in bulk should be configured and used consistent with the terms of service of each source platform they draw from.
- Where sentiment analysis is applied to content involving identifiable private individuals rather than aggregate public opinion, review `osint-templates/operational-planning/legal-compliance-checklist.md` for applicable data protection considerations.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
