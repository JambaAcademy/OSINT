#!/usr/bin/env python3
"""
text_similarity_clustering.py

Group a collection of text entries (e.g., social media posts, comments,
or article excerpts) into clusters of similar content using TF-IDF
vectorization and K-Means clustering.

Purpose in an OSINT context:
    Useful for identifying templated, copy-pasted, or coordinated
    messaging within a large collected dataset — a common signature of
    inauthentic amplification campaigns (see
    osint-tools/social-media-intelligence/network-mapping/README.md) or
    for simply organizing a large volume of collected text before manual
    review.

Important limitation:
    Clustering groups text by statistical similarity, not by verified
    meaning. Always manually review a sample from each cluster before
    drawing conclusions, per
    osint-templates/ai-assisted-templates/machine-learning-insights.md.

Requirements:
    Python 3.8+
    scikit-learn (pip install scikit-learn --break-system-packages)

Usage:
    python text_similarity_clustering.py --input posts.txt --clusters 5
    python text_similarity_clustering.py --input posts.csv --text-column post_text --clusters auto
"""

import argparse
import csv
import sys

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
except ImportError:
    sys.exit(
        "This script requires scikit-learn.\n"
        "Install it with: pip install scikit-learn --break-system-packages"
    )


def load_texts(input_path: str, text_column: str = None) -> list:
    """Load text entries from a .txt (one per line) or .csv (with a named column) file."""
    if input_path.lower().endswith(".csv"):
        if not text_column:
            sys.exit("--text-column is required when --input is a CSV file.")
        texts = []
        with open(input_path, "r", encoding="utf-8", errors="replace", newline="") as f:
            reader = csv.DictReader(f)
            if text_column not in reader.fieldnames:
                sys.exit(f"Column '{text_column}' not found. Available columns: {reader.fieldnames}")
            for row in reader:
                value = (row.get(text_column) or "").strip()
                if value:
                    texts.append(value)
        return texts
    else:
        with open(input_path, "r", encoding="utf-8", errors="replace") as f:
            return [line.strip() for line in f if line.strip()]


def choose_best_k(tfidf_matrix, max_k: int = 10, min_k: int = 2) -> int:
    """Pick the number of clusters with the best silhouette score over a small search range."""
    n_samples = tfidf_matrix.shape[0]
    # Cap the search range relative to sample size as well as max_k, so that
    # small datasets aren't fragmented into mostly-singleton clusters.
    upper = min(max_k, n_samples - 1, max(min_k, n_samples // 2))
    if upper < min_k:
        return min_k

    best_k, best_score = min_k, -1.0
    for k in range(min_k, upper + 1):
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = model.fit_predict(tfidf_matrix)
        if len(set(labels)) < 2:
            continue
        score = silhouette_score(tfidf_matrix, labels)
        if score > best_score:
            best_k, best_score = k, score
    return best_k


def top_terms_per_cluster(vectorizer, model, n_terms: int = 6) -> dict:
    """Return the top TF-IDF terms for each cluster's centroid, for human interpretability."""
    feature_names = vectorizer.get_feature_names_out()
    result = {}
    for cluster_id, centroid in enumerate(model.cluster_centers_):
        top_indices = centroid.argsort()[::-1][:n_terms]
        result[cluster_id] = [feature_names[i] for i in top_indices]
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Cluster similar text entries using TF-IDF and K-Means."
    )
    parser.add_argument("--input", required=True, help="Path to a .txt (one entry per line) or .csv file")
    parser.add_argument("--text-column", help="Column name containing text (required for CSV input)")
    parser.add_argument(
        "--clusters", default="auto",
        help="Number of clusters, or 'auto' to select automatically via silhouette score (default: auto)",
    )
    parser.add_argument("--max-entries-shown", type=int, default=5, help="Max entries to print per cluster (default 5)")
    args = parser.parse_args()

    texts = load_texts(args.input, args.text_column)
    if len(texts) < 2:
        sys.exit("Need at least 2 non-empty text entries to cluster.")

    print(f"Loaded {len(texts)} text entries.")

    vectorizer = TfidfVectorizer(stop_words="english", max_df=0.95, min_df=1)
    tfidf_matrix = vectorizer.fit_transform(texts)

    if args.clusters == "auto":
        k = choose_best_k(tfidf_matrix)
        print(f"Automatically selected {k} clusters based on silhouette score.")
    else:
        try:
            k = int(args.clusters)
        except ValueError:
            sys.exit("--clusters must be an integer or 'auto'.")
        k = max(1, min(k, len(texts)))

    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(tfidf_matrix)
    terms = top_terms_per_cluster(vectorizer, model)

    clusters = {i: [] for i in range(k)}
    for text, label in zip(texts, labels):
        clusters[label].append(text)

    print(f"\n{k} cluster(s) found:\n")
    for cluster_id in sorted(clusters, key=lambda c: -len(clusters[c])):
        members = clusters[cluster_id]
        print(f"--- Cluster {cluster_id} ({len(members)} entries) ---")
        print(f"Top terms: {', '.join(terms[cluster_id])}")
        for text in members[: args.max_entries_shown]:
            preview = text if len(text) <= 100 else text[:97] + "..."
            print(f"  - {preview}")
        if len(members) > args.max_entries_shown:
            print(f"  ... and {len(members) - args.max_entries_shown} more")
        print()

    print(
        "Reminder: this groups text by statistical similarity, not verified meaning. "
        "Manually review a sample from each cluster before drawing conclusions, per "
        "osint-templates/ai-assisted-templates/machine-learning-insights.md."
    )


if __name__ == "__main__":
    main()
