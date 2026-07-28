# Anonymization Tools

## Overview

This section covers tools and practices for reducing an investigator's identifiable digital footprint while conducting research, and for managing one's own personal data exposure to commercial data brokers. See `data_broker_optout_tracker.csv` in this folder for a ready-to-use tracker for managing opt-out requests to the consumer data aggregator services listed in `people-investigation/background-checking/README.md`.

---

## Browser and Session Isolation

| Tool/Technique | Description | Best For | Cost |
|---|---|---|---|
| Dedicated investigation virtual machine | A separate VM (e.g., using VirtualBox or VMware) used only for investigative browsing, kept isolated from personal accounts and browsing history | Preventing cross-contamination between an analyst's personal identity and investigative activity | Free (VM software) |
| Browser profiles/containers | Most modern browsers support separate profiles or containerized tabs that isolate cookies and login state | Lightweight isolation between investigative and personal browsing without a full VM | Free, built-in |
| Privacy-focused browsers (e.g., Tor Browser, Brave) | Browsers with built-in tracker blocking and fingerprint resistance | Reducing tracking and fingerprinting during research | Free |
| Disposable/temporary email services | Services providing a short-lived email address for one-time account verification | Creating a research account without exposing a personal or organizational email address | Free (basic tiers) |

## Fingerprinting Awareness

| Resource | Description | Best For | Cost |
|---|---|---|---|
| Browser fingerprint check tools (e.g., Cover Your Tracks by EFF) | Free tools that show how uniquely identifiable your browser configuration is | Understanding and reducing your own browser's fingerprinting surface before investigative browsing | Free |

---

## Using the Included Data Broker Opt-Out Tracker

`data_broker_optout_tracker.csv` provides a structured way to track opt-out requests submitted to the consumer data aggregator services documented in `people-investigation/background-checking/README.md` (Whitepages, Spokeo, BeenVerified, Intelius, TruthFinder, PeopleFinders, and others). This is useful both for an analyst managing their own personal exposure and as a template to offer an investigation subject who requests guidance on removing their own public data footprint.

Open the CSV in any spreadsheet application and fill in the status columns as you submit and confirm each opt-out request. Most services require periodic re-submission, as data is often re-aggregated from public records over time.

---

## Usage Notes

- Data broker opt-out is typically a per-service, manual process; there is no single action that removes a person's data from every aggregator at once. Paid "reputation management" services exist that automate this across many sites, but the CSV in this folder allows managing the process manually at no cost.
- A dedicated investigation VM or browser profile substantially reduces, but does not eliminate, the risk of an analyst's identity becoming linked to their research; combine this with the broader practices in `operational-security/README.md`.

---

## Legal and Ethical Notes

- These tools and techniques protect the investigator's own privacy and operational security during lawful research; they are not intended to facilitate anonymous harassment or evasion of legitimate accountability.
- Using anonymization tools to access a platform in a way that circumvents an explicit ban or access restriction placed on the investigator personally (as opposed to general privacy-preserving browsing) may violate that platform's terms of service; consider this distinction before proceeding.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
