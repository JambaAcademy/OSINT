# Contact Discovery

## Overview

Contact discovery tools help identify publicly associated email addresses and phone numbers for a person or organization, most commonly used in business development, recruiting, journalism (reaching a source for comment), and due diligence contexts. This section does not cover techniques for locating a person who is not seeking to be found; see the [people-investigation category overview](../README.md) for the boundary this repository draws around that use case.

---

## Business Email Discovery

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Hunter.io | Finds and verifies professional email addresses associated with a company domain, based on common naming pattern detection and public data | Locating a professional contact's business email address at a known company | Freemium/Paid |
| RocketReach | Aggregates professional contact information, including email and phone, primarily for business development use cases | Sales and recruiting outreach research | Freemium/Paid |
| Apollo.io | Sales intelligence platform combining contact discovery with company/role data | Business-to-business outreach list building | Freemium/Paid |
| Clearbit (Connect/Enrichment products) | Business contact and company data enrichment platform | Enriching an existing contact list with verified business contact details | Paid |

## Email Verification

| Tool | Description | Best For | Cost |
|---|---|---|---|
| NeverBounce | Email verification service that checks whether a given email address is currently valid and deliverable | Confirming a discovered or provided email address before relying on it | Paid, usage-based |
| ZeroBounce | Similar email verification and deliverability scoring service | Bulk email list validation | Paid, usage-based |
| Manual SMTP/MX record check | Checking a domain's mail server configuration to confirm it is actively configured to receive mail (does not confirm a specific mailbox exists) | Basic sanity-checking of a domain's email infrastructure | Free, using tools in `search-and-discovery` and `technical-reconnaissance/domain-analysis/` |

## Phone Number Research

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Carrier lookup services | Identify which telecommunications carrier a given phone number is registered to | Basic technical validation of a phone number's carrier and line type (mobile/landline/VoIP) | Free/Paid, varies by provider |
| Truecaller | Crowdsourced caller ID and spam-identification service | Checking whether a number is publicly associated with a name or flagged as spam by other users (accuracy depends on crowdsourced data quality) | Free (with paid premium features) |
| Reverse phone lookup aggregators (see also `background-checking/`) | General-purpose public record aggregators often include reverse phone lookup among their features | Cross-referencing a phone number against public record aggregation | Freemium/Paid, subject to the same FCRA and accuracy caveats as `background-checking/` |

---

## Verifying Business Association Before Outreach

Before relying on a discovered contact detail for professional outreach:

1. Confirm the person's current employment/role independently (see `search-and-discovery/` and professional networking platforms).
2. Verify the email address is currently valid using an email verification tool where the outreach is significant (e.g., time-sensitive journalism deadline).
3. Note the source and date of discovery for your own records, consistent with the documentation standard in `osint-templates/operational-planning/osint-collection-plan.md`.

---

## Usage Notes

- Business email discovery tools generally work by detecting an organization's email naming convention (e.g., firstname.lastname@company.com) from previously observed addresses and applying it to a target name; this is a strong inference, not a certainty, and should be verified before being relied upon for important outreach.
- Crowdsourced caller ID/spam databases (such as Truecaller) reflect other users' submissions and can be inaccurate, outdated, or reflect a shared/reassigned number's previous owner.

---

## Legal and Ethical Notes

- Contact discovery tools in this section are intended for legitimate professional outreach (business development, recruiting, journalism, due diligence), not for enabling unwanted contact with a private individual.
- Some jurisdictions regulate unsolicited commercial contact (for example, anti-spam and telemarketing regulations); ensure any outreach using discovered contact information complies with applicable marketing and communications law, separate from the OSINT collection question itself.
- Do not use phone or email discovery tools to locate or contact a person who has asked not to be contacted, or in the context of a personal dispute; see the [people-investigation category overview](../README.md) for the boundary this repository draws around that use case.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
