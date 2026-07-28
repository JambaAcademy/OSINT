# Operational Security

## Overview

This section covers general operational security (OPSEC) principles for OSINT investigators: compartmentalizing investigative activity from personal identity, managing investigative personas responsibly, and avoiding inadvertent disclosure of an investigation to its subject. See `investigation_persona_tracker.csv` in this folder for a ready-to-use tracker for managing the metadata of investigative accounts/personas — deliberately excluding any actual credentials, which belong in a password manager, not this file.

---

## Core OPSEC Principles for OSINT Work

| Principle | Description |
|---|---|
| Compartmentalization | Keep investigative activity (accounts, browsing, devices/VMs) separate from personal identity and, where feasible, separate between unrelated cases |
| Minimal footprint | Interact with a subject's environment (visiting their website, viewing their public profile) only as much as necessary; excessive interaction increases detection risk and can itself alert the subject |
| Attribution awareness | Understand what each action you take could reveal about you — an account creation, a direct message, a "like," or even a page view can sometimes be visible to the subject depending on the platform |
| Consistent persona hygiene | If using an investigative persona (see below), maintain consistent, plausible details rather than an account that raises suspicion through inconsistency |
| Least-privilege access | Use only the access level and tools necessary for the specific task, reducing the potential impact if an account or device is compromised |
| Documented authorization | Ensure OPSEC practices (including persona use) are consistent with your organization's policy and the authorization documented in your collection plan (see `osint-templates/operational-planning/legal-compliance-checklist.md`) |

---

## Investigative Personas: Scope and Boundaries

Maintaining a separate, non-attributable account for investigative research (sometimes called a "sock puppet" in tradecraft literature) is standard practice in professional OSINT, security research, and journalism, distinct from creating a fake identity to deceive, harass, or manipulate a specific individual.

**Appropriate use:**

- Creating a professional research account to view public content on a platform without exposing your personal or organizational identity.
- Using a persona to observe public groups, forums, or channels relevant to an investigation.

**Inappropriate use (outside the scope of this repository):**

- Impersonating a specific real person.
- Using a persona to send friend/connection requests specifically to gain access to a subject's private or restricted content.
- Using a persona to interact with, manipulate, or deceive a specific individual for the purpose of extracting information from them.

See this repository's [Code of Conduct](../../../CODE_OF_CONDUCT.md) and the [Legal Compliance Checklist](../../../osint-templates/operational-planning/legal-compliance-checklist.md) for the governing standard.

---

## Using the Included Investigation Persona Tracker

`investigation_persona_tracker.csv` tracks the non-sensitive metadata of investigative personas/accounts your organization maintains: which platform, purpose, creation date, associated case(s), and review status. It deliberately does not include a field for passwords or security question answers — store those in a dedicated password manager, never in a plain spreadsheet.

---

## Additional OPSEC Practices

- [ ] Separate investigation devices, VMs, or browser profiles from personal use (see `anonymization-tools/README.md`)
- [ ] VPN/Tor configuration verified per `vpn-tor-setup/opsec-verification-checklist.md`
- [ ] Sensitive communications conducted per `secure-communications/README.md`
- [ ] Investigative personas reviewed periodically for continued necessity and appropriateness (retire personas no longer in active use)
- [ ] Case-specific access reviewed and revoked at case closure, consistent with `osint-templates/operational-planning/investigation-workflow.md`, Stage 11

---

## Legal and Ethical Notes

- Persona and OPSEC practices in this section are intended to protect the investigator's safety and the confidentiality of lawful, authorized research, not to enable deception, harassment, or manipulation of a specific individual.
- Confirm your organization's specific policy on persona creation and use before establishing a new investigative account, as policies and platform terms of service vary.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
