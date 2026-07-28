# Network Diagrams

## Overview

This section covers hierarchical and technical diagramming — organizational charts, corporate ownership structures, and network/infrastructure topology diagrams — as distinct from the general entity-relationship graphs covered in `link-analysis/`. Network diagrams in this sense typically have a clearer hierarchical or directional structure (parent-child, upstream-downstream) than a general link analysis graph. See `network_diagram_generator.py` in this folder for a ready-to-use script that renders a clean hierarchical diagram from a simple text description, using Graphviz.

---

## Diagramming Tools

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Graphviz | Open-source graph visualization software with strong support for clean, automatic hierarchical layouts | Programmatic generation of organizational charts, ownership structures, and network topology diagrams | Free, open source |
| draw.io / diagrams.net | Free, browser-based diagramming tool with network and infrastructure shape libraries | Manually created, presentation-polished diagrams | Free |
| Lucidchart | Commercial diagramming platform with collaboration features | Team-based diagram creation and maintenance | Freemium/Paid |
| Microsoft Visio | Established commercial diagramming software with extensive network/infrastructure stencil libraries | Enterprise-standard technical diagramming | Paid |

---

## Using the Included Network Diagram Generator

`network_diagram_generator.py` reads a simple text file describing a hierarchy (one relationship per line, in the form `parent -> child`) and renders a clean, automatically laid-out diagram as a PNG using Graphviz. This is well suited to corporate ownership structures, organizational charts, and network topology diagrams where relationships have a clear direction.

```bash
pip install graphviz --break-system-packages
# The Graphviz system binary is also required:
#   Debian/Ubuntu: sudo apt-get install graphviz
#   macOS (Homebrew): brew install graphviz

python network_diagram_generator.py --input hierarchy.txt --output diagram.png
```

See `sample_hierarchy.txt` in this folder for the expected input format.

---

## When to Use a Hierarchical Diagram vs. a General Link Analysis Graph

| Use a hierarchical diagram (this folder) when... | Use a general link analysis graph (`link-analysis/`) when... |
|---|---|
| Relationships have a clear direction (parent company owns subsidiary; server connects to database) | Relationships are non-directional or the direction is not analytically significant |
| You want automatic, clean top-down or left-right layout | You want the layout algorithm to reveal clustering and centrality patterns |
| The structure is a tree or near-tree (each node has one clear "parent") | The structure is a dense, cyclical, or many-to-many web of connections |

---

## Usage Notes

- Graphviz's automatic layout works best for genuinely hierarchical data; a highly interconnected, non-hierarchical dataset will render more clearly using the force-directed layout in `link-analysis/link_analysis_graph_builder.py` instead.
- For technical infrastructure diagrams specifically, pair this tool with the findings from `technical-reconnaissance/infrastructure-mapping/` and document the diagram alongside `osint-templates/technical-assessments/infrastructure-assessment.md`.

---

## Legal and Ethical Notes

- Diagramming a corporate ownership or organizational structure from public registry data is a standard, lawful due diligence technique (see `business-intelligence/company-research/`).
- Where a hierarchy diagram includes named private individuals, apply the elevated standard in `people-investigation/README.md`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
