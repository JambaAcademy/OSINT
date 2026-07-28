# Platform-Specific Tools

## Overview

This section covers tools and techniques built around a single major social media platform's specific structure, search capability, and API. Platform-specific tools generally provide deeper access to that platform's data than a general cross-platform aggregator, at the cost of only covering one platform.

---

## Facebook / Meta

| Tool/Technique | Description | Best For | Cost |
|---|---|---|---|
| Facebook Graph API (via Meta for Developers) | Official API for accessing public Page data, with authentication and rate limits | Programmatic access to public Page posts and metadata | Free, requires developer account |
| Meta Ad Library | Searchable public archive of active and historical ads run on Meta platforms, including spend and targeting ranges for political/issue ads | Investigating an organization's or campaign's advertising activity | Free |
| Native platform search | Facebook's built-in search for people, Pages, groups, and posts | Baseline discovery of public profiles and Pages | Free |

## X (formerly Twitter)

| Tool/Technique | Description | Best For | Cost |
|---|---|---|---|
| X API | Official API with tiered access levels for programmatic search and data collection | Structured data collection within API rate/cost limits | Freemium/Paid, tiered |
| Advanced search operators (native) | Built-in operators such as `from:`, `to:`, `since:`, `until:`, `filter:` | Precise search of public post history | Free |
| Third-party archive/analysis tools | Various community-maintained tools track deleted posts, historical account activity, and posting patterns from public data | Reviewing an account's historical public activity, including content later deleted | Varies, confirm current availability and terms before use |

## LinkedIn

| Tool/Technique | Description | Best For | Cost |
|---|---|---|---|
| Native LinkedIn search | Built-in search for people, companies, and posts, with filtering by location, industry, and connection degree | Professional background and current role verification | Free (enhanced filters with paid tiers) |
| LinkedIn Sales Navigator | Paid LinkedIn product with advanced search filters | Business intelligence and lead-style research applied to OSINT contexts | Paid |
| Company Page "People" tab | Aggregated view of employees who list a given company on their public profile | Estimating headcount and identifying relevant personnel | Free |

## Instagram

| Tool/Technique | Description | Best For | Cost |
|---|---|---|---|
| Native search and hashtag browsing | Built-in search for accounts, hashtags, and locations | Discovering public content associated with a person, brand, or location tag | Free |
| Meta Ad Library (shared with Facebook) | Covers Instagram ad activity as well | Advertising activity investigation | Free |

## TikTok

| Tool/Technique | Description | Best For | Cost |
|---|---|---|---|
| Native search and Creative Center | TikTok's built-in search plus its public Creative Center trend-discovery tool | Trend research and public content discovery | Free |
| TikTok Commercial Content Library | Public library of paid commercial and political ad content, similar in spirit to Meta's Ad Library | Investigating paid promotional activity on the platform | Free |

## Reddit

| Tool/Technique | Description | Best For | Cost |
|---|---|---|---|
| Native search and search operators | Built-in search supports operators such as `subreddit:`, `author:`, `title:` | Locating discussion threads and a user's public post/comment history | Free |
| Pushshift-successor archives / academic Reddit datasets | Various research-oriented archives index historical Reddit content beyond native search's retention | Historical research on deleted or older content, subject to current availability | Varies, confirm current terms of access |

## Telegram

| Tool/Technique | Description | Best For | Cost |
|---|---|---|---|
| Native search and public channel/group browsing | Telegram's public channels and groups are searchable and joinable without special access | Monitoring public channel activity | Free |
| Telegram API (for developers) | Official API for building tools that interact with public channels a user has joined | Programmatic monitoring of public channel content | Free, requires developer registration |

---

## General Platform-Specific Usage Notes

- API access tiers, pricing, and rate limits change frequently across all major platforms; confirm current terms directly with the platform before building a workflow around a specific API tier.
- Native in-platform search is often underused; before reaching for a third-party tool, confirm what the platform's own advanced search or operators can already provide.
- Ad transparency libraries (Meta Ad Library, TikTok Commercial Content Library, and similar tools maintained by other platforms) are a particularly high-value and underused OSINT resource for understanding an organization's messaging and targeting strategy.

---

## Legal and Ethical Notes

- Do not create fake accounts, "sock puppets," or impersonation accounts to gain access to non-public content or to deceive a subject into connecting with you. This is inconsistent with most platforms' terms of service and with the ethical standards in this repository's [Code of Conduct](../../../CODE_OF_CONDUCT.md).
- Automated collection against any platform should respect documented rate limits and terms of service; excessive automated querying can result in account suspension and, in some cases, legal liability under computer misuse statutes.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
