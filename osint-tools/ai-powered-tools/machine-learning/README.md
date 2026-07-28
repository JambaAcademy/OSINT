# Machine Learning

## Overview

This section covers general-purpose machine learning platforms and libraries applicable to OSINT analysis tasks such as clustering similar content, classification, and anomaly detection. See `text_similarity_clustering.py` in this folder for a ready-to-use script that groups similar text entries together, useful for identifying duplicate, templated, or coordinated content within a collected dataset.

---

## General ML Platforms and Libraries

| Tool | Description | Best For | Cost |
|---|---|---|---|
| scikit-learn | Widely used Python machine learning library covering classification, clustering, regression, and dimensionality reduction | General-purpose ML tasks with well-understood, interpretable algorithms | Free, open source |
| Hugging Face Hub | Repository of pre-trained models and datasets covering NLP, vision, and audio tasks | Accessing state-of-the-art pre-trained models without training from scratch | Free (open models); paid hosted inference available |
| Google Colab / Kaggle Notebooks | Free hosted Jupyter notebook environments with GPU access | Running ML experiments and scripts without local setup, including on larger datasets | Free tier available; paid tiers for more compute |
| TensorFlow / PyTorch | Leading deep learning frameworks | Custom model development and training for specialized tasks | Free, open source |
| AutoML platforms (e.g., Google Vertex AI AutoML, Azure AutoML) | Managed platforms that automate model selection and training | Non-specialist analysts who need a working model without deep ML expertise | Paid, usage-based |

## Anomaly and Outlier Detection

| Technique/Library | Description | Best For | Cost |
|---|---|---|---|
| Isolation Forest (scikit-learn) | Tree-based anomaly detection algorithm effective on high-dimensional data | Flagging unusual records in a large structured dataset (e.g., outlier transactions or accounts) | Free, open source |
| DBSCAN clustering (scikit-learn) | Density-based clustering that naturally identifies outliers as points that don't belong to any cluster | Identifying both natural groupings and anomalies simultaneously | Free, open source |

---

## Using the Included Text Similarity Clustering Script

`text_similarity_clustering.py` reads a list of text entries (for example, social media posts, comments, or article excerpts) from a CSV or plain text file, and groups them into clusters of similar content using TF-IDF vectorization and K-Means clustering. This is useful for identifying templated, copy-pasted, or coordinated messaging within a large collected dataset.

```bash
pip install scikit-learn --break-system-packages
python text_similarity_clustering.py --input posts.txt --clusters 5
python text_similarity_clustering.py --input posts.csv --text-column post_text --clusters auto
```

See the script's `--help` output for the full set of options, including automatic cluster count selection.

---

## Usage Notes

- Clustering algorithms group by textual/statistical similarity, not by verified meaning; always manually review a sample from each cluster to confirm the grouping makes sense before drawing conclusions, consistent with `osint-templates/ai-assisted-templates/machine-learning-insights.md`.
- Short text (single-sentence social media posts) clusters less reliably than longer documents; consider this when interpreting cluster cohesion for short-form content.

---

## Legal and Ethical Notes

- Machine learning techniques in this section are applied to data already lawfully collected as part of a documented investigation; this section does not cover techniques for lawfully or unlawfully obtaining the underlying data, which is addressed in the relevant collection-category folders (`social-media-intelligence/`, `search-and-discovery/`, and others).
- See `osint-templates/ai-assisted-templates/ai-pattern-analysis.md` for the required bias and fairness considerations before relying on an ML-identified pattern in a report.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
