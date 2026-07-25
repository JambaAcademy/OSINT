# Changelog

All notable changes to the OSINT Mastery Guide repository will be documented in this file.

The format is based on Keep a Changelog (keepachangelog.com), and this project adheres to Semantic Versioning (MAJOR.MINOR.PATCH).

---

## [Unreleased]

### Planned

- Expansion of osint-tools/ subfolders with curated, annotated tool directories for every category in the repository structure.
- Python automation scripts for lawful, public-API-based OSINT workflows in scripts-and-automation/.
- Additional language translations for the eight core investigation report templates.
- Interactive dashboard templates for data-visualization/.

See the README roadmap section for the full forward-looking plan.

---

## [2.0.0] - 2025-11-03

### Added

- Complete restructure of the repository into five top-level areas: osint-templates/, osint-tools/, documentation/, scripts-and-automation/, and community/.
- ai-assisted-templates/ subfolder with five new templates covering AI-assisted pattern analysis, automated correlation, sentiment analysis, predictive intelligence, and machine learning insight reporting.
- specialized-formats/ subfolder covering court-ready reporting, regulatory compliance, insurance investigation, academic research, and journalism fact-checking formats.
- Full book chapter breakdown, sixteen chapters, cross-referenced against repository components in the README.
- Repository architecture diagram illustrating how templates, tools, scripts, and documentation relate.

### Changed

- Renamed several first-generation templates to align with a consistent subject-purpose-report.md naming convention.
- Rewrote the README's "About This Repository" and "Book Overview" sections for clarity and to reflect the second edition of the companion book.
- Expanded the legal and ethical considerations section with jurisdiction-aware guidance.

### Fixed

- Corrected inconsistent heading levels across the original eight investigation-report templates.
- Repaired broken anchor links introduced by earlier heading renumbering.

---

## [1.3.0] - 2025-06-18

### Added

- operational-planning/ template set: OSINT collection plan, investigation workflow, risk assessment matrix, legal compliance checklist, source verification framework, and evidence chain-of-custody documentation.
- MIT License file formalizing reuse terms for all templates and tools.
- Initial CONTRIBUTING.md draft, since superseded by the current version.

### Changed

- Migrated all templates to a consistent executive-summary-first structure.
- Updated tool category descriptions to reflect early-2025 platform changes, including updated authentication requirements on several social media APIs.

---

## [1.2.0] - 2025-03-22

### Added

- technical-assessments/ template set: network reconnaissance, domain and website analysis, infrastructure assessment, vulnerability intelligence, malware analysis, and incident response documentation.
- MITRE ATT&CK mapping sections added to threat-intelligence-oriented templates.
- YARA and Sigma rule scaffolding blocks in technical templates for analysts producing detection content alongside OSINT findings.

### Fixed

- Corrected several placeholder inconsistencies in the breach analysis template flagged by early community reviewers.

---

## [1.1.0] - 2025-01-14

### Added

- Three additional investigation report templates: digital footprint assessment, asset investigation report, and comprehensive background check.
- Confidence-level rating tables (high, medium, low) standardized across all investigation templates.
- Book purchase links and chapter-alignment notes in the README.

### Changed

- Expanded the person-investigation-report and business-intelligence-report templates with additional sourcing and verification sections based on early reader feedback.

---

## [1.0.0] - 2024-11-05

### Added

- Initial public release of the repository as the official companion to "A Complete Guide to Mastering Open-Source Intelligence (OSINT)."
- First four investigation report templates: person investigation report, business intelligence report, social media analysis report, and threat intelligence report.
- Base repository README with project objectives and disclaimer.
- MIT License.

---

## Versioning Notes

- MAJOR versions indicate structural changes to the repository, such as folder reorganization or naming convention changes, that may require contributors and users to update local references.
- MINOR versions indicate new templates, tools, or documentation added without breaking the existing structure.
- PATCH versions indicate typo fixes, broken-link repairs, and minor clarifications, and are tracked in individual pull request history rather than itemized separately above prior to the 1.0.0 general availability release.

[Unreleased]: https://github.com/JambaAcademy/OSINT/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/JambaAcademy/OSINT/compare/v1.3.0...v2.0.0
[1.3.0]: https://github.com/JambaAcademy/OSINT/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/JambaAcademy/OSINT/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/JambaAcademy/OSINT/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/JambaAcademy/OSINT/releases/tag/v1.0.0
