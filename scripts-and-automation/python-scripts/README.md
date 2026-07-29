# Python Scripts

## Overview

This section contains general-purpose Python automation for managing the OSINT investigation workflow itself, as opposed to tool-specific scripts (which live alongside their relevant category in `osint-tools/`). See `case_folder_initializer.py` for a ready-to-use script that sets up a standardized case directory structure and starter files for a new investigation.

---

## Using the Included Case Folder Initializer

`case_folder_initializer.py` creates a standardized directory structure for a new investigation case: subfolders for evidence, source logs, working notes, and the final report, plus a starter collection log CSV and a copy of the pre-investigation checklist. Using a consistent structure across every case makes it easier to hand off, review, or retrieve a case later.

```bash
python case_folder_initializer.py --case-id OSINT-2026-0142 --output-dir ./cases
```

This creates:

```
cases/OSINT-2026-0142/
├── evidence/
├── source_log.csv
├── working_notes/
├── report/
└── pre_investigation_checklist.md
```

---

## Usage Notes

- Run this script at the very start of a new case, before any collection begins, so that source logging habits (see `osint-templates/operational-planning/osint-collection-plan.md`) start on day one rather than being reconstructed later.
- The generated `pre_investigation_checklist.md` is a condensed checklist; complete the full templates in `osint-templates/operational-planning/` as your authoritative documentation.

---

## Legal and Ethical Notes

- This script only creates local directory structure and starter files; it does not collect any data itself and has no special legal or ethical considerations beyond standard file system use.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
