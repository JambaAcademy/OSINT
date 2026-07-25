# OSINT Templates

## Overview

This directory contains the complete library of professional OSINT documentation templates referenced throughout "A Complete Guide to Mastering Open-Source Intelligence (OSINT)." Templates are organized into five categories based on their purpose: general investigation reporting, technical security assessments, operational planning and governance, specialized audience-specific formats, and AI-assisted analysis documentation.

All templates follow a consistent design philosophy:

- Bracketed placeholders in the form `[Description of expected content]` mark where case-specific information should be entered. No template contains pre-filled fictional data that could be mistaken for a real case.
- Every template includes an executive summary block, numbered major sections, and a closing classification/version-control block.
- Every template includes, where relevant, an explicit legal and ethical considerations component consistent with the guidance in `operational-planning/legal-compliance-checklist.md`.
- Templates cross-reference one another rather than duplicating content; for example, most templates defer detailed source-reliability rating methodology to `operational-planning/source-verification-framework.md` rather than restating it.

---

## How to Use These Templates

1. Identify the template category matching your investigation type using the table below.
2. Copy the relevant template file into your case working directory rather than editing the master copy in this repository.
3. Complete the [OSINT Collection Plan](operational-planning/osint-collection-plan.md) and [Legal Compliance Checklist](operational-planning/legal-compliance-checklist.md) before beginning active collection, regardless of which report template you ultimately intend to produce.
4. Follow the [Investigation Workflow](operational-planning/investigation-workflow.md) stages as you progress from collection through delivery.
5. Fill in bracketed placeholders with case-specific content; remove any sections that are genuinely not applicable to your investigation, but document why in your working notes.
6. Apply the [Source Verification Framework](operational-planning/source-verification-framework.md) rating to significant findings before finalizing any report.

---

## Template Categories

### 1. Investigation Reports (`investigation-reports/`)

General-purpose templates for the most common OSINT investigation types.

| Template | Use Case |
|---|---|
| `person-investigation-report.md` | Individual background and identity investigation |
| `business-intelligence-report.md` | Corporate research and competitive analysis |
| `social-media-analysis-report.md` | Platform-specific social media intelligence |
| `digital-footprint-assessment.md` | Online presence and exposure analysis |
| `asset-investigation-report.md` | Financial and property intelligence |
| `threat-intelligence-report.md` | Security-focused threat assessment |
| `breach-analysis-report.md` | Data breach investigation and impact analysis |
| `comprehensive-background-check.md` | Multi-source verification investigation |

### 2. Technical Assessments (`technical-assessments/`)

Templates for technical, infrastructure-focused, and security-oriented investigations, intended for use within an authorized engagement.

| Template | Use Case |
|---|---|
| `network-reconnaissance-report.md` | Authorized external attack surface and asset discovery |
| `domain-website-analysis-report.md` | Domain, DNS, and website legitimacy analysis |
| `infrastructure-assessment.md` | Cloud, vendor, and technology stack review |
| `vulnerability-intelligence-report.md` | CVE-centric vulnerability and exploitation landscape reporting |
| `malware-analysis-report.md` | Correlation of public threat intelligence on a malware family |
| `incident-response-template.md` | Full security incident lifecycle documentation |

### 3. Operational Planning (`operational-planning/`)

Governance and process templates used across every investigation, regardless of type.

| Template | Use Case |
|---|---|
| `osint-collection-plan.md` | Pre-collection scoping and methodology planning |
| `investigation-workflow.md` | End-to-end process checklist from intake to closure |
| `risk-assessment-matrix.md` | Legal, ethical, operational security, and data-handling risk scoring |
| `legal-compliance-checklist.md` | Data protection and regulatory awareness checklist |
| `source-verification-framework.md` | Source reliability and information credibility rating system |
| `evidence-chain-custody.md` | Evidence collection, storage, and custody tracking |

### 4. Specialized Formats (`specialized-formats/`)

Templates adapted for specific professional audiences and use contexts.

| Template | Use Case |
|---|---|
| `court-ready-report.md` | Litigation support and formal evidentiary reporting |
| `executive-summary.md` | One-to-two-page condensation for senior stakeholders |
| `regulatory-compliance-report.md` | Sanctions screening, beneficial ownership, and regulatory review |
| `insurance-investigation.md` | Special Investigation Unit claims and underwriting review |
| `academic-research-template.md` | Research-ethics-compliant academic OSINT methodology documentation |
| `journalism-fact-check.md` | Claim verification and media authentication for publication |

### 5. AI-Assisted Templates (`ai-assisted-templates/`)

Templates for documenting analysis performed with the assistance of AI and machine learning tools, with an emphasis on human verification and transparent limitation reporting.

| Template | Use Case |
|---|---|
| `ai-pattern-analysis.md` | AI-assisted pattern and anomaly identification |
| `automated-data-correlation.md` | Cross-platform identifier correlation with false-positive risk assessment |
| `sentiment-analysis-report.md` | Automated opinion mining with manual validation |
| `predictive-intelligence.md` | Structured forecasting and trend analysis |
| `machine-learning-insights.md` | General ML model findings with validation reporting |

---

## Choosing the Right Template

| If your investigation involves... | Start with... |
|---|---|
| A specific individual | `investigation-reports/person-investigation-report.md` |
| A company or organization | `investigation-reports/business-intelligence-report.md` |
| A domain, website, or network asset (authorized engagement) | `technical-assessments/domain-website-analysis-report.md` or `network-reconnaissance-report.md` |
| A security incident already in progress | `technical-assessments/incident-response-template.md` |
| Output intended for a court or legal proceeding | `specialized-formats/court-ready-report.md` |
| A finding that needs to go to senior leadership | `specialized-formats/executive-summary.md`, paired with your full report |
| Regulatory, sanctions, or beneficial ownership review | `specialized-formats/regulatory-compliance-report.md` |
| An insurance claim or application | `specialized-formats/insurance-investigation.md` |
| Academic research using public social data | `specialized-formats/academic-research-template.md` |
| Verifying a viral claim or piece of media | `specialized-formats/journalism-fact-check.md` |
| Any use of AI/ML tools in your analysis | The relevant `ai-assisted-templates/` template, in addition to your primary report template |

Every investigation, regardless of type, should also make use of the `operational-planning/` templates as governing process documents.

---

## Template Maintenance

Templates in this directory are versioned individually; see the version-control block at the end of each file for its current version and last-updated date. Proposed changes to any template should follow the process described in the repository's [CONTRIBUTING.md](../CONTRIBUTING.md), including the content standards and legal/ethical requirements that apply to all submissions.

---

## Legal and Ethical Notice

All templates in this directory are designed for use in lawful, authorized, and ethically conducted investigations. They assume the user has an appropriate legal basis for the investigation and, where required, proper authorization. See `operational-planning/legal-compliance-checklist.md` for further guidance. These templates do not constitute legal advice.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
