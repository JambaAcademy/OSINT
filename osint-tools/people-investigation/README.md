# People Investigation

## Overview

This category covers tools for identity verification, background research, contact discovery, and relationship mapping regarding individuals. It carries the highest ethical and legal sensitivity of any category in this repository, because its subject matter is, by definition, personal information about real people.

**Read this section before using any tool documented in this category.**

---

## Elevated Standard for This Category

Every other category in `osint-tools/` asks you to confirm authorization or legal basis before use. This category requires that, in addition:

1. **You have a specific, legitimate, documented purpose** for investigating this particular individual, established before you begin (see `osint-templates/operational-planning/osint-collection-plan.md`).
2. **Your collection is proportionate** to that purpose. Broad, exploratory research into a person's life beyond what your stated purpose requires is not appropriate, even if every individual technique used is itself lawful.
3. **You have confirmed the applicable legal framework** for your specific use case, particularly where the investigation could affect a person's employment, housing, credit, or insurance eligibility (see the Fair Credit Reporting Act notes below and `osint-templates/operational-planning/legal-compliance-checklist.md`).
4. **You are not using these tools to facilitate stalking, harassment, intimidation, or unauthorized surveillance of any individual**, consistent with this repository's [Code of Conduct](../../CODE_OF_CONDUCT.md). This applies regardless of your relationship to the subject, including in personal disputes, and regardless of how the request is framed.

If you are investigating a private individual and are not confident you can satisfy all four points above, stop and reconsider before proceeding, or consult legal counsel.

---

## Subfolders

| Subfolder | Description |
|---|---|
| [`identity-verification/`](identity-verification/README.md) | Confirming a claimed identity is genuine |
| [`background-checking/`](background-checking/README.md) | Criminal history, employment, and education verification tools |
| [`contact-discovery/`](contact-discovery/README.md) | Finding publicly associated email addresses and phone numbers |
| [`relationship-mapping/`](relationship-mapping/README.md) | Mapping family, professional, and associational connections |

---

## The Fair Credit Reporting Act (United States) — Why This Matters Here

Many tools in this category are marketed for general "background check" or "people search" purposes, but if the result of your search will be used, in whole or part, to make a decision about a person's **employment, tenancy, credit, or insurance eligibility**, U.S. federal law (the Fair Credit Reporting Act) likely applies. Under the FCRA, using consumer report information for these purposes typically requires the report to come from a properly regulated consumer reporting agency, with specific notice, consent, and dispute-process obligations attached, rather than an unregulated consumer "people search" website. Consult qualified legal counsel before using any tool in this category to inform an employment, housing, credit, or insurance decision. This awareness point is U.S.-specific; other jurisdictions have their own frameworks governing background screening, which are addressed generally in `osint-templates/operational-planning/legal-compliance-checklist.md`.

---

## When to Use This Category

- Legitimate due diligence on a business counterparty's key personnel, with a documented business purpose.
- Employment background screening conducted through a properly regulated process.
- Fraud, insurance, or security investigations with a documented legal basis (see `osint-templates/specialized-formats/insurance-investigation.md`).
- Journalistic or academic research into a public figure's publicly documented activities, proportionate to the public interest involved.
- Missing person or safety-related investigations conducted by or in coordination with appropriate authorities.

## When Not to Use This Category

- To investigate a private individual out of personal curiosity, suspicion, or interpersonal conflict without a legitimate, documented purpose.
- To locate a person who has taken deliberate steps to be unreachable by someone (e.g., a former partner, given the substantial risk that this facilitates harassment or worse).
- To compile a comprehensive personal dossier on someone when your actual information need is narrow and specific.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
