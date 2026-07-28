#!/usr/bin/env python3
"""
link_analysis_graph_builder.py

Build and render a labeled relationship graph (link analysis diagram)
from a simple CSV file describing entities and the relationships between
them, using NetworkX for graph construction and Matplotlib for rendering.
Also exports a GraphML file for further analysis in dedicated tools such
as Gephi.

Purpose in an OSINT context:
    Visualizing relationships between people, organizations, accounts, or
    other entities often reveals structure (hubs, clusters, bridges) that
    is difficult to see in a table. See
    osint-tools/data-visualization/link-analysis/README.md for
    interpretation guidance and limitations.

Requirements:
    Python 3.8+
    networkx (pip install networkx --break-system-packages)
    matplotlib (pip install matplotlib --break-system-packages)

Usage:
    python link_analysis_graph_builder.py --input relationships.csv --output link_graph.png
    python link_analysis_graph_builder.py --input relationships.csv --output link_graph.png --graphml link_graph.graphml

Input CSV format (header row required):
    entity_a,entity_b,relationship_type
    Jordan Sample,Example Trading Co.,officer_of
    Jordan Sample,Sample Holdings LLC,officer_of
    Example Trading Co.,123 Main St Registered Agent,shares_registered_agent
"""

import argparse
import csv
import sys

try:
    import networkx as nx
except ImportError:
    sys.exit(
        "This script requires networkx.\n"
        "Install it with: pip install networkx --break-system-packages"
    )

try:
    import matplotlib
    matplotlib.use("Agg")  # non-interactive backend suitable for saving to file
    import matplotlib.pyplot as plt
except ImportError:
    sys.exit(
        "This script requires matplotlib.\n"
        "Install it with: pip install matplotlib --break-system-packages"
    )


def load_graph(csv_path: str) -> nx.Graph:
    graph = nx.Graph()
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        required_cols = {"entity_a", "entity_b", "relationship_type"}
        if not required_cols.issubset(set(reader.fieldnames or [])):
            sys.exit(f"CSV must contain columns: {required_cols}. Found: {reader.fieldnames}")
        for row in reader:
            a = row["entity_a"].strip()
            b = row["entity_b"].strip()
            rel = row["relationship_type"].strip()
            if a and b:
                graph.add_edge(a, b, relationship=rel)
    return graph


def render_graph(graph: nx.Graph, output_path: str, title: str = "Link Analysis Diagram") -> None:
    if graph.number_of_nodes() == 0:
        sys.exit("No relationships were loaded from the input file; nothing to render.")

    # Scale figure size and node size with graph size for readability.
    n = graph.number_of_nodes()
    fig_size = max(8, min(20, n * 0.8))
    plt.figure(figsize=(fig_size, fig_size))

    layout = nx.spring_layout(graph, seed=42, k=1.2 / (n ** 0.5) if n > 1 else 1)

    degrees = dict(graph.degree())
    max_degree = max(degrees.values()) if degrees else 1
    node_sizes = [800 + 1600 * (degrees[node] / max_degree) for node in graph.nodes()]

    nx.draw_networkx_nodes(graph, layout, node_size=node_sizes, node_color="#1f4e78", alpha=0.9)
    nx.draw_networkx_edges(graph, layout, width=1.5, alpha=0.6, edge_color="#666666")
    nx.draw_networkx_labels(graph, layout, font_size=9, font_color="white", font_weight="bold")

    edge_labels = nx.get_edge_attributes(graph, "relationship")
    nx.draw_networkx_edge_labels(graph, layout, edge_labels=edge_labels, font_size=7, font_color="#333333")

    plt.title(title, fontsize=14, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()


def print_centrality_summary(graph: nx.Graph) -> None:
    degrees = dict(graph.degree())
    ranked = sorted(degrees.items(), key=lambda x: -x[1])
    print("\nEntities ranked by number of connections (degree centrality):\n")
    for entity, degree in ranked[:15]:
        print(f"  {entity}: {degree} connection(s)")
    if len(ranked) > 15:
        print(f"  ... and {len(ranked) - 15} more entities")


def main():
    parser = argparse.ArgumentParser(
        description="Build and render a link analysis graph from a CSV of entity relationships."
    )
    parser.add_argument("--input", required=True, help="Path to a CSV file with entity_a,entity_b,relationship_type columns")
    parser.add_argument("--output", required=True, help="Path to write the rendered PNG image")
    parser.add_argument("--graphml", help="Optional path to also export a GraphML file for use in Gephi or similar tools")
    parser.add_argument("--title", default="Link Analysis Diagram", help="Title displayed on the rendered graph")
    args = parser.parse_args()

    graph = load_graph(args.input)
    print(f"Loaded {graph.number_of_nodes()} entities and {graph.number_of_edges()} relationships.")

    render_graph(graph, args.output, title=args.title)
    print(f"Graph image written to {args.output}")

    if args.graphml:
        nx.write_graphml(graph, args.graphml)
        print(f"GraphML file written to {args.graphml} (importable into Gephi and similar tools)")

    print_centrality_summary(graph)

    print(
        "\nReminder: this diagram visualizes relationships from the data you provided. "
        "Verify each significant relationship against its original source before relying "
        "on this diagram in a report, per "
        "osint-templates/operational-planning/source-verification-framework.md."
    )


if __name__ == "__main__":
    main()
