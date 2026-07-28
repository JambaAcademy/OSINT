# Link Analysis

## Overview

Link analysis visualizes relationships between entities (people, organizations, accounts, addresses, transactions) as a graph of nodes and edges, making complex webs of connection easier to interpret than a table. See `link_analysis_graph_builder.py` in this folder for a ready-to-use script that builds and renders a relationship graph from a simple CSV file.

---

## Dedicated Link Analysis Platforms

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Maltego (also listed in `social-media-intelligence/network-mapping/`) | Commercial link-analysis platform with built-in OSINT data-source transforms | End-to-end investigation graphing from initial entity to multi-hop relationships | Freemium/Paid |
| Gephi | Open-source graph visualization and analysis platform | Detailed, customizable graph visualization with centrality analysis | Free, open source |
| i2 Analyst's Notebook | Established commercial link-analysis platform widely used in law enforcement and intelligence contexts | Formal, presentation-ready link charts for investigative and legal contexts | Paid, enterprise |
| Linkurious | Commercial graph visualization platform built on graph databases | Large-scale, database-backed relationship visualization | Paid, enterprise |

---

## Using the Included Link Analysis Graph Builder

`link_analysis_graph_builder.py` reads a CSV file describing relationships between entities and renders a labeled network graph as a PNG image, using NetworkX and Matplotlib. It also exports a GraphML file that can be opened in Gephi or other dedicated graph tools for further, more detailed analysis.

```bash
pip install networkx matplotlib --break-system-packages
python link_analysis_graph_builder.py --input relationships.csv --output link_graph.png
```

See `sample_relationships.csv` in this folder for the expected input format: `entity_a,entity_b,relationship_type`.

---

## Interpreting a Link Analysis Graph

- **Node size/centrality:** Nodes with more connections (higher "degree") are typically drawn larger or more prominently; these are often, but not always, the most significant entities in the network.
- **Edge labels:** Label edges with the nature of the relationship (e.g., "co-owner," "family member," "same registered address") rather than leaving them unlabeled, so the diagram remains interpretable without the underlying data.
- **Clusters:** Tightly interconnected clusters can indicate a genuinely close-knit group, but can also reflect an artifact of how data was collected (e.g., all entities sharing a common intermediary such as a registered agent).

---

## Usage Notes

- A link analysis diagram is a hypothesis-generation and communication tool; treat any specific relationship it depicts as requiring the same source verification as any other finding, per `osint-templates/operational-planning/source-verification-framework.md`.
- Large graphs (100+ nodes) become visually cluttered quickly; consider filtering to the most relevant subset of entities for a presentation-ready diagram, while retaining the full dataset in the GraphML export for deeper analysis.

---

## Legal and Ethical Notes

- Link analysis diagrams involving named private individuals should be handled consistent with the elevated standard in `people-investigation/README.md`, particularly regarding proportionate scope (see also `people-investigation/relationship-mapping/README.md`).

---

**Version:** 1.0
**Last Updated:** 2026-07-25
