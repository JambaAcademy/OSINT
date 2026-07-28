# Identity Verification

## Overview

Identity verification tools help confirm that a claimed identity is genuine and internally consistent, commonly used in Know Your Customer (KYC) compliance, hiring verification, and fraud prevention contexts. This is distinct from background checking (which looks into a verified person's history) and from contact discovery (which locates ways to reach a person); identity verification asks the narrower question of whether the person is who they claim to be.

---

## Document and Identity Verification Platforms

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Jumio | Commercial identity verification platform combining document authentication and biometric liveness/face matching | Regulated KYC/onboarding workflows in financial services and other regulated industries | Paid, enterprise |
| Onfido | Commercial identity verification platform with document and biometric verification, widely used in fintech | Automated identity verification integrated into a digital onboarding flow | Paid, enterprise |
| ID.me | Identity verification service used widely for government and enterprise identity proofing in the United States | Verifying identity against government-recognized standards for benefit/service access contexts | Free to individuals verifying their own identity; paid for organizations integrating the service |

## Public Record Cross-Verification (Manual, Passive)

| Technique | Description | Best For | Cost |
|---|---|---|---|
| Cross-referencing name, address, and date of birth across independent public records | Comparing a claimed identity's details against independently sourced public records (property records, voter registration where publicly available, business filings) | Manual identity consistency checking without a commercial verification vendor | Free (using sources documented in `search-and-discovery/government-databases/`) |
| Professional license registry cross-check | Verifying a claimed professional credential against the relevant licensing board's public registry | Confirming a specific claimed professional identity/credential | Free, varies by licensing board |
| Employer/institution direct verification | Contacting the claimed employer or educational institution's official verification service directly | Authoritative confirmation of claimed current or past employment/education | Free/Paid, depends on institution |

## Social and Digital Identity Consistency Checks

| Technique | Description | Best For | Cost |
|---|---|---|---|
| Cross-platform profile consistency review | Comparing how a claimed identity presents itself (photos, biographical details, timeline) across multiple public platforms for internal consistency | Assessing whether a digital identity is internally coherent versus assembled from mismatched or stolen elements | Free, using tools in `social-media-intelligence/cross-platform-analyzers/` |
| Reverse image search on profile photographs | Checking whether a profile photo appears elsewhere online under a different name, which can indicate a fabricated or stolen identity | Detecting fabricated profiles using stock or stolen photographs | Free, using tools documented in `social-media-intelligence/cross-platform-analyzers/` |

---

## Identity Verification Confidence Framework

| Verification Level | What It Confirms | What It Does Not Confirm |
|---|---|---|
| Document verification only | The presented document appears to be a genuine, unaltered document of its claimed type | That the document belongs to the person presenting it |
| Document plus biometric/liveness check | The person presenting the document is physically consistent with the document's photo and is present live (not a static image) | That the underlying document itself was not fraudulently obtained in the first place |
| Document, biometric, and independent public record cross-check | A higher-confidence composite verification | Absolute certainty; no verification method is infallible |

---

## Usage Notes

- No single identity verification technique is conclusive on its own; commercial platforms typically combine several signals (document authenticity, biometric liveness, and database cross-checks) precisely because each individual signal can be circumvented or can produce false results in isolation.
- Biometric/facial verification technology has documented accuracy variance across demographic groups; treat any single biometric match or mismatch as one input into a broader assessment rather than a final determination, particularly in a consequential decision context.

---

## Legal and Ethical Notes

- Commercial identity verification platforms (Jumio, Onfido, and similar) typically require the verified individual's knowing participation (they submit their own document and biometric data); this repository does not document covert identity verification techniques that bypass a subject's awareness or consent.
- Where identity verification is conducted as part of a regulated process (KYC/AML, employment eligibility verification), ensure your organization's use of any tool in this section complies with the specific regulatory framework governing that process, in addition to the general guidance in `osint-templates/operational-planning/legal-compliance-checklist.md`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
