# Bash Utilities

## Overview

This section contains shell scripts for evidence handling and file management tasks that are simpler to express as portable shell scripts than as Python. See `evidence_hash_logger.sh` for a ready-to-use script that computes cryptographic hashes for every file in an evidence directory and appends them to a chain-of-custody log, directly automating the hash-verification requirement in `osint-templates/operational-planning/evidence-chain-custody.md`.

---

## Using the Included Evidence Hash Logger

`evidence_hash_logger.sh` walks a directory of collected evidence files, computes a SHA-256 hash for each, and appends a timestamped record to a CSV log — creating an auditable, tamper-evident record of exactly what was collected and when, consistent with `osint-templates/operational-planning/evidence-chain-custody.md`.

```bash
chmod +x evidence_hash_logger.sh
./evidence_hash_logger.sh /path/to/evidence/directory /path/to/evidence_hash_log.csv
```

Run this script each time you add new evidence to a case's evidence folder; it appends to the log rather than overwriting it, and skips files already recorded with an unchanged hash.

---

## Usage Notes

- This script requires `sha256sum` (standard on Linux) or `shasum` (standard on macOS); it detects which is available automatically.
- Re-running the script after adding new files to the evidence directory will only add new entries; files already logged with an identical hash are not re-added, keeping the log clean across repeated runs.
- If a previously logged file's hash changes on a later run, the script flags this prominently — this should never happen to genuine, unaltered evidence, and any such result requires immediate investigation per `osint-templates/operational-planning/evidence-chain-custody.md`, Section 7.

---

## Legal and Ethical Notes

- Hashing files you have already lawfully collected has no independent legal or ethical considerations; it is a standard integrity-verification practice.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
