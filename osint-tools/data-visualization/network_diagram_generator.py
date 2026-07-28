#!/usr/bin/env python3
"""
network_diagram_generator.py

Render a clean, automatically laid-out hierarchical diagram (organizational
chart, corporate ownership structure, or network topology diagram) from a
simple text file describing parent-child relationships, using Graphviz.

Purpose in an OSINT context:
    Well suited to visualizing corporate ownership structures, reporting
    hierarchies, or network/infrastructure topology, where relationships
    have a clear direction. See
    osint-tools/data-visualization/network-diagrams/README.md for when to
    use this versus the general-purpose link analysis graph builder.

Requirements:
    Python 3.8+
    graphviz Python package (pip install graphviz --break-system-packages)
    The Graphviz system binary must also be installed separately:
        Debian/Ubuntu: sudo apt-get install graphviz
        macOS (Homebrew): brew install graphviz

Usage:
    python network_diagram_generator.py --input hierarchy.txt --output diagram.png
    python network_diagram_generator.py --input hierarchy.txt --output diagram.png --direction LR

Input file format (one relationship per line):
    Parent Entity -> Child Entity
    # Lines starting with # are treated as comments and ignored
    # Blank lines are ignored
"""

import argparse
import sys

try:
    import graphviz
except ImportError:
    sys.exit(
        "This script requires the 'graphviz' Python package.\n"
        "Install it with: pip install graphviz --break-system-packages\n"
        "You must also install the Graphviz system binary separately (see this "
        "script's header comment for OS-specific instructions)."
    )


def parse_hierarchy(path: str) -> list:
    edges = []
    with open(path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "->" not in line:
                print(f"Warning: skipping line {line_num} (no '->' found): {line!r}")
                continue
            parent, child = line.split("->", 1)
            parent, child = parent.strip(), child.strip()
            if parent and child:
                edges.append((parent, child))
    return edges


def build_diagram(edges: list, direction: str = "TB") -> graphviz.Digraph:
    dot = graphviz.Digraph(format="png")
    dot.attr(rankdir=direction)
    dot.attr("node", shape="box", style="filled,rounded", fillcolor="#1f4e78",
             fontcolor="white", fontname="Helvetica", color="#1f4e78")
    dot.attr("edge", color="#666666", fontname="Helvetica", fontsize="9")

    seen_nodes = set()
    for parent, child in edges:
        for node in (parent, child):
            if node not in seen_nodes:
                dot.node(node)
                seen_nodes.add(node)
        dot.edge(parent, child)

    return dot


def main():
    parser = argparse.ArgumentParser(
        description="Render a hierarchical network/organizational diagram from a text file of parent -> child relationships."
    )
    parser.add_argument("--input", required=True, help="Path to a text file with 'Parent -> Child' lines")
    parser.add_argument("--output", required=True, help="Output image path (extension determines format, e.g. .png, .svg, .pdf)")
    parser.add_argument(
        "--direction", default="TB", choices=["TB", "LR", "BT", "RL"],
        help="Layout direction: TB (top-bottom, default), LR (left-right), BT, or RL",
    )
    args = parser.parse_args()

    edges = parse_hierarchy(args.input)
    if not edges:
        sys.exit("No valid relationships were parsed from the input file.")

    print(f"Loaded {len(edges)} relationship(s).")

    dot = build_diagram(edges, direction=args.direction)

    # graphviz.render() appends the format extension automatically; strip a
    # matching extension from the requested output path first if present.
    output_base = args.output
    fmt = "png"
    for ext in ("png", "svg", "pdf"):
        if output_base.lower().endswith(f".{ext}"):
            output_base = output_base[: -(len(ext) + 1)]
            fmt = ext
            break
    dot.format = fmt

    rendered_path = dot.render(filename=output_base, cleanup=True)
    print(f"Diagram written to {rendered_path}")

    print(
        "\nReminder: verify each relationship against its original source (e.g. a corporate "
        "registry filing) before relying on this diagram in a report, per "
        "osint-templates/operational-planning/source-verification-framework.md."
    )


if __name__ == "__main__":
    main()
