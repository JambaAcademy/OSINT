# 📄 Changelog

All notable changes to the OSINT Mastery Guide repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) (`MAJOR.MINOR.PATCH`).

---

## [Unreleased]

### Planned
- Expansion of `osint-tools/` subfolders with curated, annotated tool directories for every category in the repository structure
- Python automation scripts for lawful, public-API-based OSINT workflows in `scripts-and-automation/`
- Additional language translations for the eight core investigation report templates
- Interactive dashboard templates for `data-visualization/`

See the [README Roadmap](README.md#-roadmap) for the full forward-looking plan.

---

## [2.0.0] — 2025-11-03

### Added
- Complete restructure of the repository into six top-level areas: `osint-templates/`, `osint-tools/`, `documentation/`, `scripts-and-automation/`, and `community/`
- `ai-assisted-templates/` subfolder with five new templates covering AI-assisted pattern analysis, automated correlation, sentiment analysis, predictive intelligence, and machine learning insight reporting
- `specialized-formats/` subfolder covering court-ready reporting, regulatory compliance, insurance investigation, academic research, and journalism fact-checking formats
- Full book chapter breakdown (16 chapters) cross-referenced against repository components in the README
- Repository architecture diagram (Mermaid) illustrating how templates, tools, scripts, and documentation relate

### Changed
- Renamed several first-generation templates to align with a consistent `subject-purpose-report.md` naming convention
- Rewrote the README's "About This Repository" and "Book Overview" sections for clarity and to reflect the second edition of the companion book
- Expanded the Legal and Ethical Considerations section with jurisdiction-aware guidance

### Fixed
- Corrected inconsistent heading levels across the original eight investigation-report templates
- Repaired broken anchor links introduced by earlier heading renumbering

---

## [1.3.0] — 2025-06-18

### Added
- `operational-planning/` template set: OSINT collection plan, investigation workflow, risk assessment matrix, legal compliance checklist, source verification framework, and evidence chain-of-custody documentation
- MIT License file formalizing reuse terms for all templates and tools
- Initial `CONTRIBUTING.md` draft (superseded by the current version)

### Changed
- Migrated all templates to a consistent Executive-Summary-first structure
- Updated tool category descriptions to reflect early-2025 platform changes (several social media APIs updated authentication requirements)

---

## [1.2.0] — 2025-03-22

### Added
- `technical-assessments/` template set: network reconnaissance, domain/website analysis, infrastructure assessment, vulnerability intelligence, malware analysis, and incident response documentation
- MITRE ATT&CK mapping sections added to threat-intelligence-oriented templates
- YARA and Sigma rule scaffolding blocks in technical templates for analysts producing detection content alongside OSINT findings

### Fixed
- Corrected several placeholder inconsistencies in the breach analysis template flagged by early community reviewers

---

## [1.1.0] — 2025-01-14

### Added
- Three additional investigation report templates: digital footprint assessment, asset investigation report, and comprehensive background check
- Confidence-level rating tables (`High/Medium/Low`) standardized across all investigation templates
- Book purchase links and chapter-alignment notes in the README

### Changed
- Expanded the person-investigation-report and business-intelligence-report templates with additional sourcing and verification sections based on early reader feedback

---

## [1.0.0] — 2024-11-05

### Added
- Initial public release of the repository as the official companion to *A Complete Guide to Mastering Open-Source Intelligence (OSINT)*
- First four investigation report templates: person investigation report, business intelligence report, social media analysis report, and threat intelligence report
- Base repository README with project objectives and disclaimer
- MIT License

---

## Versioning Notes

- **MAJOR** versions indicate structural changes to the repository (folder reorganization, naming convention changes) that may require contributors and users to update local references.
- **MINOR** versions indicate new templates, tools, or documentation added without breaking existing structure.
- **PATCH** versions (not separately itemized above prior to 1.0.0 general availability) indicate typo fixes, broken-link repairs, and minor clarifications, and are tracked in individual pull request history.

[Unreleased]: https://github.com/JambaAcademy/OSINT/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/JambaAcademy/OSINT/compare/v1.3.0...v2.0.0
[1.3.0]: https://github.com/JambaAcademy/OSINT/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/JambaAcademy/OSINT/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/JambaAcademy/OSINT/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/JambaAcademy/OSINT/releases/tag/v1.0.0
