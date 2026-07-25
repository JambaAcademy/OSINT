# Source Verification Framework

## Purpose Statement

This framework provides a consistent methodology for rating the reliability of sources and the credibility of information during an OSINT investigation. Consistent application of this framework helps ensure that conclusions in the final report are appropriately qualified by the strength of the evidence behind them.

This framework adapts the widely used NATO Admiralty Code (source reliability and information credibility rating system) for open-source intelligence use.

---

## 1. Source Reliability Rating

Rate the source itself — the platform, publication, or entity providing the information — independent of the specific claim being evaluated.

| Rating | Label | Description |
|---|---|---|
| A | Completely reliable | Source has a long, consistent history of accuracy; primary/authoritative source (e.g., government registry, official company filing) |
| B | Usually reliable | Source has a good track record with occasional minor inaccuracies (e.g., established news organization with editorial standards) |
| C | Fairly reliable | Source has a mixed record or limited track record (e.g., a smaller publication or a professional networking profile with limited corroborating history) |
| D | Not usually reliable | Source has a history of inaccuracies or an unclear editorial/verification process (e.g., an anonymous forum post) |
| E | Unreliable | Source has a demonstrated history of fabrication or is designed to mislead (e.g., known disinformation outlet) |
| F | Reliability cannot be judged | Insufficient information exists to rate this source |

---

## 2. Information Credibility Rating

Rate the specific piece of information based on how well it is corroborated, independent of the source's general reliability.

| Rating | Label | Description |
|---|---|---|
| 1 | Confirmed | Corroborated by multiple independent, reliable sources, or verified through direct primary evidence |
| 2 | Probably true | Logical, consistent with other known information, but not fully independently corroborated |
| 3 | Possibly true | Reasonably logical but not corroborated |
| 4 | Doubtful | Not logical or consistent with other known reliable information |
| 5 | Improbable | Contradicted by reliable, corroborated information |
| 6 | Cannot be judged | Insufficient basis to assess |

---

## 3. Combined Rating Notation

Findings should be documented using a combined notation, for example "B2" (source usually reliable; information probably true), following each significant claim in working notes and, where appropriate, in the final report's methodology or confidence sections.

### Example Application

| Finding | Source | Source Reliability | Information Credibility | Combined Rating |
|---|---|---|---|---|
| [Subject's stated employer] | [LinkedIn profile, self-reported] | C | 2 | C2 |
| [Subject's registered business address] | [State corporate registry filing] | A | 1 | A1 |
| [Allegation from anonymous online post] | [Unverified forum post] | E | 4 | E4 |

---

## 4. Source Category Reference Guide

Use this general guidance as a starting point; individual sources within a category can vary significantly and should still be assessed on their own merits.

| Source Category | Typical Reliability Range | Notes |
|---|---|---|
| Government registries and official filings | A-B | Generally high reliability but can lag in currency |
| Court records | A-B | Authoritative for what was filed/ruled, but allegations within filings are not themselves proven facts |
| Established news organizations with editorial standards | B-C | Verify whether reporting or opinion content |
| Corporate self-published material (press releases, official websites) | B-C | Reliable for the organization's own claims about itself; may be promotional in framing |
| Professional networking profiles (self-reported) | C-D | Self-reported and unverified; useful for leads, not for confirmed fact absent corroboration |
| General social media posts | C-E | Highly variable; assess account history, verification status, and consistency |
| Anonymous forums and message boards | D-E | Useful for leads and monitoring, rarely sufficient alone for a finding |
| Data broker/aggregator compiled profiles | C-D | Often aggregate other sources with unclear currency; verify against primary sources where possible |
| Wikis and crowd-edited encyclopedic content | C-D | Useful for orientation and lead generation; verify against primary sources before citing as fact |

---

## 5. Corroboration Standards

### 5.1 Minimum Corroboration Requirements

| Finding Significance | Minimum Independent Sources Required |
|---|---|
| Central finding driving a major conclusion | Two or more independent sources, at least one rated B or higher |
| Supporting/contextual finding | One reliable source (B or higher), or two lower-reliability sources in agreement |
| Background/orientation information not central to conclusions | Single source acceptable, clearly labeled as such |

### 5.2 Independence Test

Two sources are only "independent" corroboration if they do not both trace back to the same original reporting or the same underlying self-reported claim. A claim repeated across many outlets that all cite the same original post is a single source, not multiple corroborating sources.

---

## 6. Handling Conflicting Information

When sources conflict:

1. Compare the reliability ratings of the conflicting sources.
2. Assess whether one source is a primary source and the other secondary/derivative.
3. Consider recency: has the underlying fact plausibly changed over time.
4. If the conflict cannot be resolved, document both versions in the report with their respective ratings and note the conflict explicitly rather than silently choosing one.

**Documentation format for unresolved conflicts:**

> "Source A (B2) reports [X]. Source B (C3) reports [Y], which conflicts with Source A. This discrepancy could not be resolved with available information."

---

## 7. Red Flags Requiring Additional Scrutiny

- [ ] Source is anonymous with no verifiable track record
- [ ] Source has a clear motive to mislead (competitor, disgruntled party, adversarial actor)
- [ ] Information appears designed to provoke an emotional reaction
- [ ] Claim lacks any specific, checkable detail
- [ ] Visual/media evidence shows signs of manipulation (inconsistent lighting, metadata anomalies, reused/recycled imagery found via reverse image search)
- [ ] Timing of publication coincides suspiciously with an event that would benefit from the narrative being pushed
- [ ] Information originates from a source with a documented history of the specific type of fabrication involved

---

## 8. Analyst Bias Mitigation

- [ ] Considered alternative explanations for ambiguous findings before settling on a conclusion
- [ ] Actively searched for disconfirming evidence, not only confirming evidence
- [ ] Distinguished clearly, in both notes and final report, between confirmed fact, inference, and speculation
- [ ] Had a second analyst review key conclusions where feasible (see [Investigation Workflow](investigation-workflow.md), Stage 9)

---

## 9. Documentation Requirements

Every source used in a final report should be logged with:

- Full URL or citation
- Date and time accessed
- Source reliability rating (A-F)
- Archived copy reference (screenshot, saved page, or hash), where feasible

---

## 10. Version Control

**Version:** [Version number]
**Last Updated:** [Date]

---

*This framework adapts a long-established intelligence community rating methodology for OSINT practice. Ratings involve analyst judgment and should be applied consistently and documented transparently so that report consumers can understand the basis for each conclusion's confidence level.*
