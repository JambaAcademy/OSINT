# Scripts and Automation

## Overview

This directory contains standalone automation scripts and utilities that support the OSINT workflow described throughout this repository, organized by language and purpose rather than by investigation type. Tool-specific scripts (SEC EDGAR lookups, OFAC screening, geolocation calculators, and others) live alongside their relevant tool category in `osint-tools/`; this directory holds general-purpose automation that supports the workflow as a whole — case setup, evidence handling, API integration patterns, and data cleaning.

---

## Subfolders

| Subfolder | Description |
|---|---|
| [`python-scripts/`](python-scripts/README.md) | General-purpose Python automation for investigation workflow management |
| [`bash-utilities/`](bash-utilities/README.md) | Shell scripts for evidence handling and file management tasks |
| [`api-integrations/`](api-integrations/README.md) | Example integrations with free, publicly documented security/OSINT APIs |
| [`data-processing/`](data-processing/README.md) | Data cleaning, deduplication, and normalization utilities |

---

## Coding Standards for This Directory

All scripts in this directory, and throughout the repository, follow the standards in [CONTRIBUTING.md](../CONTRIBUTING.md): PEP 8 for Python, a module-level docstring describing purpose and legal scope, no hardcoded credentials, and interaction only with publicly accessible or properly authorized/authenticated data sources.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
