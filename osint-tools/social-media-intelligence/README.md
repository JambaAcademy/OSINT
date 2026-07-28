# Social Media Intelligence

## Overview

Social media intelligence (SOCMINT) covers the collection and analysis of publicly available social media content to support an investigation. This category is organized into platform-specific tools, tools that work across multiple platforms at once, sentiment/opinion mining tools, and tools for mapping social networks and relationships.

All tools in this category are intended for use against publicly accessible content only. None of the tools documented here are intended to access private, friends-only, or otherwise access-restricted content without the account holder's authorization.

---

## Subfolders

| Subfolder | Description |
|---|---|
| [`platform-specific-tools/`](platform-specific-tools/README.md) | Tools built for a single major platform's specific data structure and API |
| [`cross-platform-analyzers/`](cross-platform-analyzers/README.md) | Username correlation, reverse image search, and multi-platform aggregation tools |
| [`sentiment-analysis/`](sentiment-analysis/README.md) | Opinion mining and sentiment classification tools |
| [`network-mapping/`](network-mapping/README.md) | Tools for visualizing follower/following graphs and social relationships |

---

## When to Use This Category

- Investigating an individual's or organization's public online presence and activity.
- Assessing public sentiment toward a brand, topic, or event.
- Tracing an identifier (username, handle, profile photo) across multiple platforms.
- Understanding the structure of a social network relevant to an investigation (who follows whom, who amplifies whose content).

---

## Foundational Principles for This Category

- **Respect platform terms of service.** Every tool listed here should be used in a manner consistent with the terms of service of the platform whose data it accesses. Automated collection that violates a platform's terms carries both legal and account-suspension risk.
- **Public content only.** Do not use these tools, or any technique, to access content behind a privacy wall (friends-only posts, private accounts, direct messages) without proper authorization such as a legal process or the account holder's consent.
- **Corroborate before concluding.** Social media content is easily fabricated, exaggerated, or taken out of context; apply the [Source Verification Framework](../../osint-templates/operational-planning/source-verification-framework.md) before treating any single post as established fact.
- **Data currency.** Social media platforms change their features, APIs, and privacy controls frequently; a technique that worked previously may no longer function, and platform-specific tools in particular can break with little notice.

---

## Related Categories

- For finding a person's identity across platforms as part of a broader investigation, see also `people-investigation/contact-discovery/`.
- For visualizing findings once collected, see `data-visualization/network-diagrams/`.
- For AI-assisted analysis of large volumes of collected social content, see `ai-powered-tools/`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
