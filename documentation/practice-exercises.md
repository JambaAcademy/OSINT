# OSINT Practice Exercises

## Purpose Statement

These exercises are designed to build OSINT skills progressively, from foundational search techniques through multi-source correlation. Complete them using the templates and tools in this repository, and time-box each one to build efficient habits.

---

## Before You Begin

- Review the guidance in `README.md` (this folder) on practicing safely and ethically.
- Complete `../getting-started/first-investigation-walkthrough.md` before attempting Exercise 3 or later.
- For any exercise involving a "subject," use a public organization, a well-known public figure's already-public information, your own information, or a consenting colleague's — never a private individual without consent.

---

## Beginner Exercises

### Exercise 1: Advanced Search Operators

**Task:** Using only the search operators documented in `osint-tools/search-and-discovery/advanced-search-engines/README.md`, find three publicly available PDF documents published by a well-known public university relating to a topic of your choice.

**Time limit:** 15 minutes

**Skills practiced:** `filetype:`, `site:`, and phrase-matching operators.

**Success criteria:** You can explain which specific operator combination found each document and why a plain keyword search would have been less precise.

---

### Exercise 2: Source Reliability Rating

**Task:** Pick any well-known current news topic. Find three different sources reporting on it: one from an established news organization, one from a social media post, and one from a corporate press release. Rate each using `osint-templates/operational-planning/source-verification-framework.md`.

**Time limit:** 20 minutes

**Skills practiced:** Applying the Admiralty Code rating system consistently.

**Success criteria:** You can articulate why the three sources received different ratings, referencing the framework's criteria specifically rather than general impressions.

---

## Intermediate Exercises

### Exercise 3: Company Due Diligence

**Task:** Choose any publicly traded company. Using `osint-templates/investigation-reports/business-intelligence-report.md` as your template and `osint-tools/business-intelligence/` for tools, complete a basic profile covering: corporate structure, most recent public financial filing highlights, and any recent news coverage.

**Time limit:** 60 minutes

**Skills practiced:** Registry research, SEC EDGAR lookup (see `osint-tools/business-intelligence/financial-analysis/sec_edgar_company_lookup.py`), and structured reporting.

**Success criteria:** A completed report with every claim traceable to a cited, dated source.

---

### Exercise 4: Domain Legitimacy Assessment

**Task:** Choose any three websites you don't already know well (for example, from a list of small businesses in your area, with their consent, or from a public directory). Using `osint-templates/technical-assessments/domain-website-analysis-report.md`, assess each site's WHOIS history, certificate transparency log entries, and general legitimacy indicators.

**Time limit:** 45 minutes

**Skills practiced:** WHOIS/DNS lookup tools in `osint-tools/technical-reconnaissance/domain-analysis/README.md`, certificate transparency search.

**Success criteria:** A completed assessment for each site with an explicit legitimacy rating and supporting reasoning.

---

### Exercise 5: Geolocation Verification

**Task:** Find a publicly posted travel or news photo (from a source you have permission to use, such as a stock photo site or your own photos) that does not have an obvious location caption. Attempt to geolocate it using the tools in `osint-tools/geospatial-intelligence/` and document your process using `geolocation-verification-worksheet.md`.

**Time limit:** 30 minutes

**Skills practiced:** Visual landmark identification, reverse image search, mapping cross-reference.

**Success criteria:** A completed worksheet with a confidence-rated conclusion, even if the conclusion is "undetermined."

---

## Advanced Exercises

### Exercise 6: Multi-Source Correlation

**Task:** Using a publicly known historical event with well-documented, multiple independent sources (for example, a notable corporate merger or a significant public event), practice the correlation methodology in `../advanced-techniques/multi-source-correlation-methodology.md`. Identify at least three genuinely independent signals relevant to one specific factual question about the event, and write a calibrated confidence statement per the framework in that guide.

**Time limit:** 60 minutes

**Skills practiced:** Independence testing, alternative explanation analysis, confidence calibration.

**Success criteria:** You can clearly explain why your chosen signals are independent of each other (not just repetitions of the same original source) and have documented at least one alternative explanation you considered and assessed.

---

### Exercise 7: Full Investigation Simulation

**Task:** Choose a publicly traded company as a simulated business intelligence client request. Complete the full workflow in `osint-templates/operational-planning/investigation-workflow.md`, from intake through closure, producing a complete `osint-templates/investigation-reports/business-intelligence-report.md`.

**Time limit:** 3 hours (can be split across sessions)

**Skills practiced:** End-to-end workflow discipline, collection planning, source verification, structured reporting, and quality review (recruit a colleague to peer-review your draft per the workflow's Stage 9).

**Success criteria:** A complete report that would pass a peer review against the checklist in `osint-templates/operational-planning/investigation-workflow.md`, Stage 9.

---

## Self-Assessment Questions After Each Exercise

- Did I define a specific, answerable objective before starting, or did I search without a clear target?
- Did I log my sources as I went, or did I have to reconstruct them afterward?
- Did I rate source reliability consistently, or did I skip this step under time pressure?
- Would a colleague reviewing my work be able to independently verify my key claims from what I documented?

---

**Version:** 1.0
**Last Updated:** 2026-07-25
