# Background Checking

## Overview

Background checking covers verifying a person's criminal history, employment history, education, and other biographical facts. This section distinguishes between regulated consumer reporting agencies (appropriate for decisions about employment, housing, credit, or insurance) and general-purpose public record aggregators (appropriate for general research but not for regulated eligibility decisions without proper compliance). Read the parent category's [Fair Credit Reporting Act notice](../README.md#the-fair-credit-reporting-act-united-states--why-this-matters-here) before using any tool in this section.

---

## Regulated Employment and Tenant Screening Providers (United States)

These providers operate as FCRA-compliant consumer reporting agencies and are the appropriate choice when the outcome of the check will inform an employment, tenancy, credit, or insurance decision in the United States.

| Provider | Description | Best For | Cost |
|---|---|---|---|
| Checkr | FCRA-compliant background screening platform widely used for employment screening, including criminal history and employment/education verification | Employment background checks with compliant adjudication workflow | Paid |
| Sterling | Established employment background screening provider offering criminal history, drug testing coordination, and verification services | Enterprise employment screening programs | Paid |
| HireRight | FCRA-compliant employment screening provider with global screening capability | Multinational employment screening programs | Paid |
| First Advantage | Employment and tenant screening provider offering criminal history and verification services | Employment and rental/tenant screening | Paid |

**Important:** Using any of these providers still requires the employer/requester to follow FCRA notice and consent obligations (providing the applicant with a clear disclosure and obtaining written authorization before running a check, and following adverse action procedures if the check influences a negative decision). These providers support but do not replace your organization's own compliance obligations.

---

## Public Record Sources (Free, Direct)

For research not governed by FCRA-style eligibility decisions, direct public record sources are often more accurate and current than aggregator services, though typically require more manual effort.

| Resource | Description | Best For | Cost |
|---|---|---|---|
| State/county court record portals | See `search-and-discovery/government-databases/` for jurisdiction-specific court record resources | Direct verification of a specific criminal or civil case | Free/Paid, varies |
| State sex offender registries | Publicly mandated registries maintained by government agencies | Legally mandated public safety lookups | Free |
| Professional licensing board registries | See `search-and-discovery/government-databases/` | Verifying a specific professional license or disciplinary history | Free, varies by board |
| Direct employer/institution verification | Contacting the claimed employer or school's official verification service | Authoritative confirmation of a specific claimed employment or education history | Free/Paid, varies |

## General-Purpose Public Record Aggregators (Consumer "People Search" Services)

These commercial services compile information from public records and marketing databases into a consolidated profile. They are widely used for general research purposes (reconnecting with contacts, general due diligence, self-monitoring) but are **not** FCRA-compliant consumer reporting agencies and should not be used to inform employment, housing, credit, or insurance decisions in the United States.

| Service | Description | Notes |
|---|---|---|
| Whitepages | Aggregates contact and public record information into person profiles | Widely used baseline lookup; offers a self-service opt-out for individuals who want their own listing removed |
| Spokeo | Aggregates public records, social media, and marketing data into person profiles | Subscription-based; accuracy and currency vary by record type |
| BeenVerified | Aggregates public records into background-style reports | Subscription-based; explicitly states it is not a consumer reporting agency and should not be used for FCRA-covered purposes |
| Intelius | Aggregates public records into background-style reports | Subscription-based; same FCRA limitation applies |
| TruthFinder | Aggregates public records into background-style reports | Subscription-based; same FCRA limitation applies |
| PeopleFinders | Aggregates public records into person and background-style reports | Subscription-based; same FCRA limitation applies |

**Accuracy caveat:** All aggregator services compile data from many underlying sources with varying currency and can contain outdated, mismatched, or simply incorrect information, particularly for individuals with common names. Treat aggregator output as a lead requiring independent corroboration (see the [Source Verification Framework](../../../osint-templates/operational-planning/source-verification-framework.md)), not as a verified fact.

**Opt-out note:** Most of these services offer a self-service data removal process for individuals who want their own information removed from public listing. If you are reviewing this section to understand your own exposure, see `privacy-and-security/anonymization-tools/` for broader guidance on managing your personal data footprint.

---

## Usage Notes

- Common names create a substantial false-positive/mismatch risk across all background checking sources; always cross-check with at least one additional unique identifier (date of birth, middle name, prior address) before attributing a record to a specific individual.
- International background checking varies enormously by country in terms of what records are publicly available at all; do not assume U.S.-style public record availability applies elsewhere.

---

## Legal and Ethical Notes

- Confirm which regulatory framework applies to your specific use case before selecting a tool: regulated screening providers for eligibility decisions, versus general research tools for other legitimate purposes.
- Review `osint-templates/operational-planning/legal-compliance-checklist.md` and the elevated standards in the [people-investigation category overview](../README.md) before beginning any background check on a specific individual.
- Background checking tools should never be used to locate a person who has taken steps to avoid contact with a specific individual, given the substantial risk of facilitating harassment.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
