# Evidence Chain of Custody

## Purpose Statement

This document tracks the chain of custody for evidence collected during an OSINT investigation, establishing an unbroken record of who collected each item of evidence, how it was handled, and where it has been stored. Proper chain-of-custody documentation is essential if findings may later be relied upon in litigation, regulatory proceedings, internal disciplinary action, or any context where the integrity of the evidence could be challenged.

---

## 1. Case Information

**Case/Project ID:** [Unique identifier]
**Lead Analyst:** [Name]
**Case Opened:** [Date]
**Classification:** [Confidential / Restricted, per organizational policy]

---

## 2. Evidence Collection Principles

- [ ] Original evidence is preserved unaltered; all analysis is performed on working copies
- [ ] Every item of evidence is logged at the time of collection, not retroactively
- [ ] Collection method is documented in enough detail to be reproduced or defended if challenged
- [ ] Digital evidence integrity is verified using cryptographic hashing where feasible
- [ ] Access to stored evidence is restricted and logged

---

## 3. Evidence Log

| Evidence ID | Description | Source URL/Location | Collection Date/Time | Collected By | Collection Method | Hash Value (SHA-256) |
|---|---|---|---|---|---|---|
| [EV-001] | [Screenshot of subject's public profile page] | [URL] | [DateTime] | [Name] | [Screenshot with timestamp overlay tool] | [Hash] |
| [EV-002] | [Archived copy of news article] | [URL] | [DateTime] | [Name] | [Full-page web archive] | [Hash] |
| [EV-003] | [Downloaded public filing document] | [URL/registry reference] | [DateTime] | [Name] | [Direct download] | [Hash] |

---

## 4. Collection Method Standards

### 4.1 Screenshots

- [ ] Full browser window captured, including visible URL bar and system clock/timestamp where possible
- [ ] Screenshot taken immediately upon viewing; not reconstructed from memory or edited after capture
- [ ] File saved in a non-editable or integrity-verifiable format
- [ ] Hash generated immediately after capture

### 4.2 Web Page Archiving

- [ ] Full-page archival tool used to preserve complete page state (not just visible viewport)
- [ ] Archive timestamp recorded
- [ ] Archive stored in the case evidence repository, not solely relying on third-party archive availability

### 4.3 Document Downloads

- [ ] Document downloaded directly from the original source where possible
- [ ] Source URL and access date recorded alongside the file
- [ ] File renamed according to the evidence ID convention without altering file content

### 4.4 Video/Audio Evidence

- [ ] Full, unedited recording preserved as the primary evidence copy
- [ ] Any clipped/edited versions created for reporting purposes clearly marked as derivative and linked to the original
- [ ] Metadata preserved where the platform provides it

---

## 5. Custody Transfer Log

Record every instance in which evidence is accessed, copied, or transferred between individuals or systems.

| Evidence ID | Transferred From | Transferred To | Date/Time | Purpose | Method |
|---|---|---|---|---|---|
| [EV-001] | [Name/system] | [Name/system] | [DateTime] | [e.g., handed to legal counsel for review] | [Secure file transfer/physical media] |

---

## 6. Storage and Access Control

### 6.1 Storage Details

- **Primary Storage Location:** [Secure repository name/system]
- **Backup Storage Location:** [If applicable]
- **Encryption Status:** [At-rest encryption method used]
- **Access Control Method:** [Role-based access, specific individuals authorized]

### 6.2 Authorized Access List

| Name | Role | Access Level | Date Access Granted |
|---|---|---|---|
| [Name] | [Role] | [Read/Write/Admin] | [Date] |

### 6.3 Access Log

| Evidence ID | Accessed By | Date/Time | Purpose |
|---|---|---|---|
| [EV-001] | [Name] | [DateTime] | [Purpose, e.g., report drafting] |

---

## 7. Integrity Verification

| Evidence ID | Original Hash | Verification Date | Verified Hash | Match Confirmed |
|---|---|---|---|---|
| [EV-001] | [Hash] | [Date] | [Hash] | [Yes/No] |

If a hash mismatch is discovered, document the discrepancy immediately, halt reliance on the affected evidence item, and escalate to the lead analyst and, where applicable, legal counsel.

---

## 8. Evidence Disposition

| Evidence ID | Disposition | Date | Authorized By |
|---|---|---|---|
| [EV-001] | [Retained per policy / Disposed of / Transferred to external party] | [Date] | [Name] |

---

## 9. Retention and Legal Hold

- **Standard Retention Period:** [Duration per organizational policy]
- **Legal Hold in Effect:** [Yes/No — if yes, reference the legal hold notice and do not dispose of evidence until released]
- **Scheduled Review Date:** [Date]

---

## 10. Chain of Custody Certification

By signing below, each individual confirms that evidence was handled in accordance with the procedures described in this document during the period of their custody.

| Name | Role | Custody Period | Signature | Date |
|---|---|---|---|---|
| [Name] | [Role] | [Date range] | [Signature] | [Date] |

---

## 11. Version Control

**Version:** [Version number]
**Last Updated:** [Date]

---

*This document should be maintained contemporaneously throughout the investigation rather than reconstructed afterward. Where findings may be used in legal proceedings, consult legal counsel regarding jurisdiction-specific evidentiary requirements, which may impose additional formalities beyond this general template.*
