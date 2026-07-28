# OSINT Quick Reference Card

*Keep this open during active work. See linked templates/tools for full detail.*

---

## Before You Start Any Investigation

- [ ] Objective is specific and answerable (not "find out everything about X")
- [ ] Legal basis documented — `osint-templates/operational-planning/legal-compliance-checklist.md`
- [ ] Collection plan completed — `osint-templates/operational-planning/osint-collection-plan.md`
- [ ] Risk assessed — `osint-templates/operational-planning/risk-assessment-matrix.md`
- [ ] If investigating a person: elevated standard reviewed — `osint-tools/people-investigation/README.md`

---

## Search Operators (Google-Style)

| Operator | Function |
|---|---|
| `site:example.com` | Restrict to a domain |
| `filetype:pdf` | Restrict to a file type |
| `intitle:"term"` | Term must be in page title |
| `inurl:term` | Term must be in URL |
| `"exact phrase"` | Exact phrase match |
| `-term` | Exclude a term |
| `OR` | Match either term |

Full reference: `osint-tools/search-and-discovery/advanced-search-engines/README.md`

---

## Source Reliability Rating (Admiralty Code)

**Source reliability:** A (completely reliable) → F (cannot be judged)
**Information credibility:** 1 (confirmed) → 6 (cannot be judged)

Combine as e.g. "B2." Full framework: `osint-templates/operational-planning/source-verification-framework.md`

**Minimum corroboration:** central findings need 2+ independent sources (one B+); background info can use 1.

---

## Passive vs. Active Technique Reminder

| Passive (no special authorization) | Active (written authorization required) |
|---|---|
| WHOIS, passive DNS, certificate transparency, Shodan/Censys index queries | Port scanning, direct service probing, vulnerability scanning |

Full detail: `osint-tools/technical-reconnaissance/README.md`

---

## Confidence Language Cheat Sheet

| Confidence | When to Use |
|---|---|
| High | Multiple independent, reliable sources; alternatives clearly less supported |
| Medium | Credible sources but some gaps or a competitive alternative explanation |
| Low | Limited/ambiguous information; substantial uncertainty remains |

Full framework: `osint-templates/ai-assisted-templates/predictive-intelligence.md`

---

## Red Flags Requiring Extra Scrutiny

- Anonymous source with no verifiable track record
- Source has an evident motive to mislead
- Claim lacks any specific, checkable detail
- Timing coincides suspiciously with a beneficiary's interest
- Visual media shows signs of manipulation (check via reverse image search)

Full list: `osint-templates/operational-planning/source-verification-framework.md`, Section 7

---

## Before You Finalize Any Report

- [ ] Every claim traces to a logged, dated, rated source
- [ ] Alternative explanations considered and documented, not just the leading theory
- [ ] Confidence levels stated explicitly, not implied
- [ ] Legal/ethical considerations section completed
- [ ] Peer review completed — `osint-templates/operational-planning/investigation-workflow.md`, Stage 9
- [ ] Classification level assigned

---

## Emergency Reminders

- **Never** access non-public data via deception, fake accounts, or circumventing access controls.
- **Never** use these tools to locate someone avoiding contact with a specific individual.
- **Always** stop and reconsider proportionality before broad research into a private individual.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
