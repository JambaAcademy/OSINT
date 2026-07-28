# Privacy and Security

## Overview

This category covers tools and practices that protect the investigator, their organization, and their sources: anonymization and browser isolation, VPN/Tor configuration, secure communications, and general operational security (OPSEC) discipline. Every technique in this category is oriented toward defending the analyst's own security and the confidentiality of an investigation, not toward evading accountability or facilitating harm.

Each subfolder includes a ready-to-use working file: a data broker opt-out tracker, an OPSEC verification checklist, a PGP key verification script, and an investigation persona tracker.

---

## Subfolders

| Subfolder | Description | Includes Working Files |
|---|---|---|
| [`anonymization-tools/`](anonymization-tools/README.md) | Browser isolation, disposable accounts, and personal data exposure reduction | Data broker opt-out tracker (CSV) |
| [`vpn-tor-setup/`](vpn-tor-setup/README.md) | VPN and Tor configuration for investigative browsing | OPSEC verification checklist (Markdown) |
| [`secure-communications/`](secure-communications/README.md) | Encrypted messaging, email, and source verification | PGP public key verification script (Python) |
| [`operational-security/`](operational-security/README.md) | General OPSEC principles and investigative persona management | Investigation persona tracker (CSV) |

---

## Why This Category Matters

OSINT investigation carries operational security risk in both directions: an analyst's own online activity can inadvertently expose their identity, employer, or investigative interest to the subject of an investigation (see the operational security risk section of `osint-templates/operational-planning/risk-assessment-matrix.md`), and communications with sensitive sources (whistleblowers, at-risk individuals) require genuine confidentiality. This category documents standard, widely used protective practices for both situations.

---

## Foundational Principle for This Category

Every tool and technique documented here is intended to:

- Protect the investigator's identity and safety while conducting lawful, authorized research.
- Protect the confidentiality of sensitive sources and communications.
- Prevent inadvertent disclosure of an ongoing investigation to its subject before appropriate.

None of the techniques in this category are intended to, and should not be used to, evade lawful accountability, conceal wrongdoing, or facilitate unauthorized access to systems. See the [Legal Compliance Checklist](../../osint-templates/operational-planning/legal-compliance-checklist.md) and this repository's [Code of Conduct](../../CODE_OF_CONDUCT.md).

---

**Version:** 1.0
**Last Updated:** 2026-07-25
