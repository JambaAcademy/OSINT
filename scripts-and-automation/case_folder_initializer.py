#!/usr/bin/env python3
"""
case_folder_initializer.py

Create a standardized directory structure and starter files for a new
OSINT investigation case: subfolders for evidence, working notes, and
the final report, plus a starter source log CSV and a condensed
pre-investigation checklist.

Purpose in an OSINT context:
    Using a consistent case folder structure from the very start of an
    investigation, before any collection begins, makes source-logging
    habits automatic rather than something reconstructed after the fact,
    and makes cases easier to hand off, review, or retrieve later. See
    scripts-and-automation/python-scripts/README.md for usage notes.

Requirements:
    Python 3.8+ (standard library only, no third-party packages required)

Usage:
    python case_folder_initializer.py --case-id OSINT-2026-0142 --output-dir ./cases
"""

import argparse
import datetime
import sys
from pathlib import Path

SOURCE_LOG_HEADER = "date_accessed,source_url,description,source_reliability,analyst,notes\n"

CHECKLIST_TEMPLATE = """# Pre-Investigation Checklist — Case {case_id}

Generated: {generated_date}

This is a condensed checklist. Complete the full templates in
`osint-templates/operational-planning/` as your authoritative documentation.

## Before Starting Collection

- [ ] Objective is specific and answerable (see `osint-templates/operational-planning/osint-collection-plan.md`)
- [ ] Legal basis documented (see `osint-templates/operational-planning/legal-compliance-checklist.md`)
- [ ] Risk assessed (see `osint-templates/operational-planning/risk-assessment-matrix.md`)
- [ ] If investigating a person: elevated standard reviewed (see `osint-tools/people-investigation/README.md`)
- [ ] Authorization confirmed and documented

## During Collection

- [ ] Every source logged in `source_log.csv` as you go (not reconstructed later)
- [ ] Evidence captured per `osint-templates/operational-planning/evidence-chain-custody.md`
- [ ] Scope deviations flagged for re-approval rather than silently expanded

## Before Finalizing

- [ ] Every claim traces to a logged, rated source
- [ ] Alternative explanations considered and documented
- [ ] Appropriate report template selected from `osint-templates/`
- [ ] Peer review completed

## Case Metadata

- **Case ID:** {case_id}
- **Opened:** {generated_date}
- **Lead Analyst:** [Fill in]
- **Investigation Type:** [Fill in]
"""


def create_case_structure(case_id: str, output_dir: str) -> Path:
    base_path = Path(output_dir) / case_id

    if base_path.exists():
        sys.exit(f"Directory already exists: {base_path}. Choose a different case ID or output directory.")

    (base_path / "evidence").mkdir(parents=True)
    (base_path / "working_notes").mkdir(parents=True)
    (base_path / "report").mkdir(parents=True)

    source_log_path = base_path / "source_log.csv"
    source_log_path.write_text(SOURCE_LOG_HEADER, encoding="utf-8")

    checklist_path = base_path / "pre_investigation_checklist.md"
    checklist_content = CHECKLIST_TEMPLATE.format(
        case_id=case_id,
        generated_date=datetime.date.today().isoformat(),
    )
    checklist_path.write_text(checklist_content, encoding="utf-8")

    return base_path


def main():
    parser = argparse.ArgumentParser(
        description="Create a standardized case folder structure for a new OSINT investigation."
    )
    parser.add_argument("--case-id", required=True, help="Unique case identifier, e.g. OSINT-2026-0142")
    parser.add_argument("--output-dir", default=".", help="Directory in which to create the case folder (default: current directory)")
    args = parser.parse_args()

    # Basic sanity check to avoid creating a folder with characters that
    # would be awkward or invalid across common file systems.
    if any(c in args.case_id for c in r'/\:*?"<>|'):
        sys.exit("Case ID should not contain path separator or reserved filesystem characters.")

    base_path = create_case_structure(args.case_id, args.output_dir)

    print(f"Case folder created at: {base_path}")
    print("Structure:")
    print(f"  {base_path.name}/")
    print(f"  ├── evidence/")
    print(f"  ├── source_log.csv")
    print(f"  ├── working_notes/")
    print(f"  ├── report/")
    print(f"  └── pre_investigation_checklist.md")
    print(
        "\nNext step: complete the full osint-templates/operational-planning/ templates before "
        "beginning active collection."
    )


if __name__ == "__main__":
    main()
