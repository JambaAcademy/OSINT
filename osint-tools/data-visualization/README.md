# Data Visualization

## Overview

This category covers tools and techniques for visually presenting OSINT analysis and findings: entity relationship graphs, chronological timelines, technical network diagrams, and interactive dashboards. Effective visualization often reveals patterns and relationships that are difficult to see in tabular or narrative form, and supports clearer communication of findings to non-technical stakeholders.

Each subfolder includes a ready-to-use, tested working script or template.

---

## Subfolders

| Subfolder | Description | Includes Working Files |
|---|---|---|
| [`link-analysis/`](link-analysis/README.md) | Entity relationship graphs from tabular relationship data | Link analysis graph builder (Python, NetworkX) |
| [`timeline-creation/`](timeline-creation/README.md) | Chronological event timeline visualization | Investigation timeline generator (Python, Matplotlib) |
| [`network-diagrams/`](network-diagrams/README.md) | Hierarchical and technical infrastructure diagrams | Network diagram generator (Python, Graphviz) |
| [`interactive-dashboards/`](interactive-dashboards/README.md) | Browser-based interactive findings dashboards | Self-contained HTML dashboard template |

---

## When to Use This Category

- Presenting a complex web of relationships (people, organizations, accounts, transactions) in a way that is easier to grasp than a table.
- Establishing and communicating a chronological sequence of events in an investigation.
- Documenting a technical infrastructure's structure for a report (see `osint-templates/technical-assessments/infrastructure-assessment.md`).
- Providing an interactive, explorable view of findings for a stakeholder audience, rather than a static document.

---

## Related Categories

- Raw relationship and network data is typically gathered using tools in `social-media-intelligence/network-mapping/` or `technical-reconnaissance/infrastructure-mapping/` before being visualized here.
- For AI-assisted pattern identification that might feed into a visualization, see `ai-powered-tools/pattern-analysis/`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
