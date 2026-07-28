# International Legal Frameworks Guide

## Purpose Statement

This guide provides a comparative, educational overview of data protection and OSINT-relevant legal frameworks across several major jurisdictions. It is designed to build general awareness of how these frameworks differ, not to serve as authoritative legal guidance for any specific investigation. Laws in this area change frequently; always confirm current requirements with qualified legal counsel licensed in the relevant jurisdiction(s) before relying on any statement below for an actual investigation.

---

## 1. European Union / European Economic Area — GDPR

The General Data Protection Regulation is among the most comprehensive data protection frameworks globally and applies broadly whenever personal data of individuals in the EU/EEA is processed, regardless of where the processing organization is based.

**Key concepts relevant to OSINT:**

- **Lawful basis requirement:** Processing personal data requires a documented lawful basis; for most OSINT investigative purposes, this is typically "legitimate interest," which requires a documented balancing test weighing the investigator's interest against the data subject's rights.
- **Data minimization:** Only data necessary for the stated purpose should be collected and retained.
- **Data subject rights:** Individuals generally have rights to be informed, to access their data, and to erasure, subject to exemptions (including exemptions relevant to legal claims and certain journalistic/research purposes).
- **Cross-border transfer restrictions:** Moving personal data outside the EEA requires an approved transfer mechanism.

**Practical implication:** An OSINT investigation touching EU/EEA individuals should document its legitimate interest assessment before beginning collection, per `osint-templates/operational-planning/legal-compliance-checklist.md` Section 3.1.

---

## 2. United States — Sectoral Approach

Unlike the EU's comprehensive framework, the United States regulates data protection through a patchwork of sector-specific federal laws and an increasing number of state-level comprehensive privacy laws.

**Key federal frameworks relevant to OSINT:**

- **Fair Credit Reporting Act (FCRA):** Governs the use of "consumer reports" for employment, credit, housing, and insurance decisions; see `osint-tools/people-investigation/README.md` for how this applies to background-check-style investigations.
- **Driver's Privacy Protection Act (DPPA):** Restricts permissible uses of motor vehicle record data.
- **Health Insurance Portability and Accountability Act (HIPAA):** Governs protected health information held by covered entities.

**State-level frameworks:**

- **California (CCPA/CPRA):** A comprehensive consumer privacy law with its own set of individual rights and business obligations, including a specific exemption relevant to publicly available information that OSINT practitioners should understand carefully rather than assume applies broadly.
- **A growing number of other states** (e.g., Virginia, Colorado, Connecticut, Utah, and others as of this writing) have enacted their own comprehensive privacy statutes with varying requirements; confirm the current state of the law for any state relevant to your investigation, as this list continues to grow.

**Practical implication:** A U.S.-focused investigation should identify every state whose law may apply (based on the data subject's residency, not just the investigating organization's location) rather than assuming federal law alone governs.

---

## 3. United Kingdom — UK GDPR and Data Protection Act 2018

Following its withdrawal from the EU, the UK maintains its own version of GDPR (the "UK GDPR") alongside the Data Protection Act 2018, which are substantially similar to the EU framework but administered independently by the UK's Information Commissioner's Office rather than an EU supervisory authority.

**Key difference from EU GDPR:** Transferring data between the UK and EU/EEA requires its own transfer mechanism consideration, separate from the EU's own cross-border transfer rules, since the UK is now a "third country" from the EU's perspective (and vice versa).

---

## 4. Canada — PIPEDA

The Personal Information Protection and Electronic Documents Act governs private-sector data handling nationally, with some provinces maintaining their own substantially similar legislation that can apply instead of the federal law for organizations operating solely within that province.

**Key concept:** PIPEDA's consent-based framework generally requires knowledge and consent for collection, use, or disclosure of personal information, with exceptions including publicly available information as defined by regulation — a narrower category than "anything findable via a search engine."

---

## 5. Brazil — LGPD

The Lei Geral de Proteção de Dados closely mirrors the GDPR's structure and is generally considered Latin America's most comprehensive data protection framework, with similar lawful-basis and data-subject-rights concepts.

---

## 6. Singapore — PDPA

The Personal Data Protection Act governs private-sector data handling with a consent-based framework, including specific provisions relevant to publicly available data and legitimate business purposes.

---

## 7. Cross-Cutting Themes Across Frameworks

| Theme | Common Pattern Across Jurisdictions |
|---|---|
| Lawful basis requirement | Most comprehensive frameworks require identifying a specific lawful basis before processing personal data, not just a general sense that the purpose is legitimate |
| "Publicly available" is not a blanket exemption | Nearly every framework treats "publicly available" information as narrower than "anything found via OSINT techniques" — being technically accessible does not automatically remove all legal protection |
| Data minimization | A consistent theme: collect only what is necessary for the stated purpose |
| Cross-border transfer restrictions | Increasingly common as more jurisdictions adopt comprehensive frameworks, creating a growing web of transfer considerations for multi-jurisdictional investigations |
| Special/sensitive category data | Most frameworks impose a higher bar for health, biometric, religious, political, or similar sensitive data categories |

---

## 8. Practical Guidance for Multi-Jurisdictional Investigations

1. Identify every jurisdiction with a potential connection to the investigation: the data subject's residence/nationality, the investigating organization's location(s), and where any data will be stored or processed.
2. Do not assume the most familiar framework (e.g., your home jurisdiction's law) is the only one that applies.
3. Document your lawful basis analysis for the framework(s) most likely to apply, using `osint-templates/operational-planning/legal-compliance-checklist.md` as your working document.
4. For any investigation with meaningful legal risk or genuine jurisdictional complexity, consult qualified legal counsel rather than relying on this guide alone.

---

## Disclaimer

This guide reflects a general, educational overview of legal frameworks as broadly understood at the time of writing and is not exhaustive, is not legal advice, and may not reflect subsequent legal developments. Data protection law is one of the most actively evolving areas of law globally; always verify current requirements with qualified legal counsel for any specific investigation.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
