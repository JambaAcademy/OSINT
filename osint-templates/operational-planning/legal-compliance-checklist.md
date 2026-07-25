# Legal Compliance Checklist

## Purpose Statement

This checklist helps analysts identify the legal frameworks potentially relevant to an OSINT investigation and confirm that basic compliance steps have been considered before and during collection. It is an operational aid, not a substitute for advice from qualified legal counsel. Laws vary significantly by jurisdiction and by the nature of the investigation; when in doubt, consult legal counsel before proceeding.

---

## 1. Investigation Details

**Case/Project ID:** [Unique identifier]
**Analyst(s):** [Name(s)]
**Review Date:** [Date]
**Jurisdictions Involved:** [List all relevant jurisdictions — subject location, analyst location, organization location, and data storage location may all differ]

---

## 2. General Legal Basis Checklist

- [ ] The purpose of the investigation is documented and legitimate (e.g., due diligence, fraud investigation, security research, journalism, legal proceeding)
- [ ] The investigation is proportionate to its stated purpose (the scope and depth of collection is no broader than necessary)
- [ ] A documented legal basis exists for processing personal data, appropriate to the applicable jurisdiction (see Section 3)
- [ ] The investigation does not target a subject based on a protected characteristic in a manner inconsistent with anti-discrimination law
- [ ] Internal authorization has been obtained per organizational policy

---

## 3. Data Protection Framework Considerations

> The items below are general awareness points, not an exhaustive legal analysis. Confirm current requirements with counsel, as data protection law changes frequently.

### 3.1 General Data Protection Regulation (GDPR) — European Union / European Economic Area

- [ ] Confirm whether the subject or the processing activity falls within GDPR's territorial scope
- [ ] Identify and document the lawful basis for processing (e.g., legitimate interest, with a documented legitimate interest assessment)
- [ ] Confirm data minimization: only data necessary for the purpose is collected
- [ ] Consider whether the subject has a right to be informed, and whether an exemption applies (e.g., disproportionate effort, or investigation/legal-claim contexts)
- [ ] Confirm data retention period is defined and proportionate
- [ ] Confirm cross-border transfer mechanisms are in place if data will leave the EEA

### 3.2 California Consumer Privacy Act / California Privacy Rights Act (CCPA/CPRA) — United States

- [ ] Confirm whether the organization and the data subject fall within CCPA/CPRA's scope
- [ ] Confirm whether an applicable exemption applies (e.g., employment context, publicly available information exemption)
- [ ] Document purpose limitation and retention schedule

### 3.3 Other Regional Frameworks

- [ ] Identify any other applicable state, provincial, or national privacy law (e.g., other U.S. state privacy laws, PIPEDA in Canada, LGPD in Brazil, POPIA in South Africa, PDPA in Singapore)
- [ ] Confirm requirements specific to that framework have been reviewed

### 3.4 Sector-Specific Regulation (United States Examples)

- [ ] **Fair Credit Reporting Act (FCRA):** If this investigation could be used, in whole or part, for employment, tenancy, credit, or insurance eligibility decisions about an individual, confirm whether FCRA applies and whether the organization is acting as, or using, a "consumer reporting agency," which carries specific notice, consent, and accuracy obligations
- [ ] **Health Insurance Portability and Accountability Act (HIPAA):** Confirm whether any health information encountered is subject to HIPAA and handled accordingly
- [ ] **Gramm-Leach-Bliley Act (GLBA):** Confirm applicability if the investigation involves financial institution customer data

---

## 4. Platform and Source Terms of Service

- [ ] Reviewed the terms of service of each major platform to be used for collection
- [ ] Confirmed that planned collection methods (manual browsing, authorized API use) are consistent with those terms
- [ ] Avoided use of fake accounts, impersonation, or deceptive tactics to gain access to non-public information, where such tactics would violate platform terms or applicable law
- [ ] Confirmed that any automated collection (scripts, scrapers) complies with the platform's terms of service and robots.txt directives where applicable
- [ ] Avoided circumventing technical access controls (e.g., paywalls, authentication) without authorization

---

## 5. Public Records Access Considerations

- [ ] Confirmed the specific public record source's access rules (some government databases restrict use of retrieved data to specific purposes, such as the U.S. Driver's Privacy Protection Act restricting DMV record use)
- [ ] Confirmed whether a permissible-purpose declaration or similar attestation is required and has been completed accurately
- [ ] Confirmed that court record access complies with any sealing, redaction, or juvenile-record restrictions applicable in that jurisdiction

---

## 6. Evidence Admissibility Considerations (If Findings May Be Used in Legal Proceedings)

- [ ] Chain of custody procedures followed from point of collection (see [Evidence Chain of Custody](evidence-chain-custody.md))
- [ ] Collection methods documented in sufficient detail to be described and defended if challenged
- [ ] Original, unaltered copies of evidence preserved, separate from any working/annotated copies
- [ ] Hash values or equivalent integrity verification generated for digital evidence, where appropriate to the jurisdiction's evidentiary standards

---

## 7. International and Cross-Border Considerations

- [ ] Confirmed whether the investigation involves data transfer across borders and what mechanism authorizes that transfer
- [ ] Confirmed whether the subject's home jurisdiction imposes restrictions on OSINT collection about its nationals or residents (some jurisdictions restrict certain categories of investigation)
- [ ] Confirmed export control or sanctions considerations do not apply to the investigation or its subject

---

## 8. Special Category / Sensitive Data Considerations

- [ ] Confirmed whether the investigation may surface special category data (health, religious belief, sexual orientation, political opinion, trade union membership, biometric or genetic data, criminal history)
- [ ] If so, confirmed a specific, documented legal basis exists for processing this category of data, which is typically held to a higher standard than general personal data
- [ ] Considered whether such data can and should be excluded from the final work product if not directly relevant to the investigation's legitimate purpose

---

## 9. Documentation and Sign-Off

| Item | Confirmed By | Date |
|---|---|---|
| Legal basis documented | [Name] | [Date] |
| Data protection framework review completed | [Name] | [Date] |
| Platform terms of service reviewed | [Name] | [Date] |
| Public records access rules confirmed | [Name] | [Date] |
| Overall compliance sign-off | [Name/role] | [Date] |

**Legal Counsel Consulted:** [Yes/No — name and date, if applicable]
**Outcome:** [Cleared to proceed / Cleared with conditions / Escalated for further review]

---

## 10. Version Control

**Version:** [Version number]
**Last Updated:** [Date]

---

*This checklist reflects general, non-exhaustive awareness points regarding commonly encountered legal frameworks as of the time of writing. Laws and their interpretation change frequently and vary by jurisdiction. This document does not constitute legal advice. Organizations should consult qualified legal counsel to confirm compliance obligations applicable to their specific investigation, jurisdiction, and use case.*
