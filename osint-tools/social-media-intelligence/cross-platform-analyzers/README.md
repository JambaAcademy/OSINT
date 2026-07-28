# Cross-Platform Analyzers

## Overview

Cross-platform analyzers help correlate a single identifier, such as a username, email address, or profile photo, across many different social media and web platforms simultaneously. These tools are typically the fastest way to build an initial map of a subject's online footprint before moving into deeper platform-specific research.

---

## Username Correlation Tools

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Sherlock (open source) | Command-line tool that checks a given username's existence across several hundred websites and platforms | Broad, fast username footprint discovery | Free, self-hosted/run locally |
| WhatsMyName | Web-based and command-line tool checking username presence across a large, actively maintained site list | Cross-platform username discovery with an actively maintained target list | Free |
| Maigret | Open-source tool similar in purpose to Sherlock, with additional profile data extraction from discovered accounts | Deeper profile detail extraction once accounts are found, not just existence confirmation | Free, self-hosted/run locally |
| Namechk-style checkers | Web-based username availability checkers, primarily built for branding/domain purposes but usable for OSINT footprint checks | Quick manual spot-check across a smaller set of major platforms | Free |

## Email-Based Correlation

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Holehe (open source) | Checks whether an email address is registered on numerous online services by testing each service's account-recovery or registration-check endpoint | Determining which platforms an email address is associated with | Free, self-hosted/run locally |
| Have I Been Pwned | Checks whether an email address has appeared in known public data breaches | Assessing exposure and corroborating account existence via breach data | Free |

## Reverse Image Search

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Google Images (reverse search) | Upload or link an image to find visually similar or identical images elsewhere on the indexed web | General-purpose reverse image search | Free |
| Yandex Images | Widely regarded as particularly strong for facial similarity matching and Eastern European content | Reverse image search where Google's results are insufficient, especially for faces | Free |
| TinEye | Dedicated reverse image search engine with a focus on exact and near-exact match detection | Finding the earliest known appearance of an image online | Free tier; paid tiers for bulk use |
| PimEyes | Facial recognition-based reverse image search | Investigative use only where a strong, documented legal basis and authorization exists; carries significant privacy and legal sensitivity | Freemium/Paid |

## Multi-Platform Profile Aggregators

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Social-searcher-style aggregators | Web-based tools that search public posts across multiple platforms for a given keyword or handle in one query | Quick multi-platform keyword/mention monitoring | Freemium |
| OSINT Framework (osintframework.com) | Not a tool itself, but a curated, categorized directory linking out to hundreds of OSINT tools, including many cross-platform analyzers | Discovering additional tools beyond this repository's curated list | Free |

---

## Usage Notes

- Username correlation tools work by checking whether a given username *exists* on a target site, which is different from *confirming* that two accounts with the same username belong to the same person. Treat a username match as a lead requiring corroboration, not a confirmed identity link, consistent with `osint-templates/ai-assisted-templates/automated-data-correlation.md`.
- Facial recognition-based reverse image search tools (such as PimEyes) carry substantially higher privacy sensitivity than traditional reverse image search and, in some jurisdictions, specific legal restrictions on their use for identifying private individuals. Confirm your legal basis and organizational policy before using facial recognition search on a real person, and see `osint-templates/operational-planning/legal-compliance-checklist.md`.
- Many self-hosted correlation tools (Sherlock, Maigret, Holehe) are community-maintained open source projects; their site-coverage lists require periodic updates as platforms change their detection-evasion measures, so results should be spot-checked against manual verification.

---

## Legal and Ethical Notes

- Cross-platform correlation should be limited to information relevant to a documented, legitimate investigative purpose; running broad correlation sweeps on individuals without a specific investigative basis raises the proportionality concerns addressed in the [Code of Conduct](../../../CODE_OF_CONDUCT.md).
- Facial recognition search results should never be treated as a definitive identity match without independent corroborating evidence, given documented accuracy variance across demographic groups in facial recognition technology generally.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
