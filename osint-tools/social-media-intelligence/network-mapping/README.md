# Network Mapping Tools

## Overview

Network mapping tools visualize relationships between accounts, individuals, or organizations, such as follower/following graphs, retweet/amplification networks, or co-mention relationships. These tools help identify influential nodes, community clusters, and coordination patterns that are difficult to see by reviewing individual posts alone.

---

## Graph Analysis and Visualization Platforms

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Gephi | Open-source network analysis and visualization software widely used for social network graphs | Detailed, customizable network visualization and centrality analysis | Free, open source |
| NodeXL | Network analysis add-in for Microsoft Excel, with built-in social media data importers for some platforms | Analysts already comfortable in a spreadsheet environment who want graph analysis without learning dedicated graph software | Freemium (basic version free; Pro version paid) |
| Cytoscape | Open-source network visualization platform originally built for biological network analysis, widely adapted for general graph/social network use | Large, complex network visualization with extensive plugin ecosystem | Free, open source |
| Maltego | Commercial link-analysis platform with transforms for pulling and connecting OSINT data from many sources into a single graph | End-to-end OSINT investigation graphing, from initial entity to multi-hop relationship mapping | Freemium (community edition available; paid tiers for full transform library) |

## Social Graph-Specific Tools

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Platform-native network export/analysis (where available via official API) | Some platforms' APIs expose follower/following or interaction data that can be exported and analyzed in a general graph tool | Building an accurate, terms-of-service-compliant social graph directly from platform data | Free/Paid, depends on API tier |
| Academic/research network analysis toolkits (e.g., NetworkX for Python) | Programming libraries for constructing and analyzing graphs computationally | Analysts with coding capability who want to build custom network metrics (centrality, community detection) | Free, open source |

## Coordination and Inauthentic Behavior Detection

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Botometer | Academic tool assessing the likelihood that a given account exhibits automated/bot-like behavior | Screening accounts for potential inauthentic/automated activity before including them in network analysis | Free (research-oriented; rate limited) |
| Custom co-activity analysis (via graph tools above) | Identifying clusters of accounts that post near-identical content in tight time windows, a common signature of coordinated inauthentic behavior | Detecting potential coordination in an amplification network | Free, using the general graph tools above |

---

## Usage Notes

- **Centrality metrics matter more than raw connection counts.** A node with fewer connections but high "betweenness centrality" (bridging otherwise unconnected clusters) is often more analytically significant than a node with many connections within a single tight cluster.
- **Distinguish organic from inauthentic structure.** A dense, tightly interconnected cluster of accounts created around the same time, all amplifying the same content, is a common signature worth flagging for further review rather than treating as organic influence.
- **Combine with the [Source Verification Framework](../../../osint-templates/operational-planning/source-verification-framework.md).** A network diagram is a hypothesis-generation tool; specific relationships it suggests should be corroborated before being asserted as fact in a final report.

---

## Legal and Ethical Notes

- Building a network map should stay within the bounds of the investigation's documented scope; broad, exploratory network mapping of individuals not directly relevant to the investigation's objective raises proportionality concerns under this repository's [Code of Conduct](../../../CODE_OF_CONDUCT.md).
- Where network mapping draws on platform APIs, ensure the specific data fields collected and their intended use are consistent with that platform's developer terms of service.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
