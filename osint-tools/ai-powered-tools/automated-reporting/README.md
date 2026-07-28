# Automated Reporting

## Overview

This section covers tools and techniques for using AI assistance to speed up the drafting of report structure from structured findings data, while keeping analytical interpretation and verification firmly in human hands. See `generate_report_draft.py` in this folder for a ready-to-use script that populates a Markdown report skeleton from a structured findings file, using the repository's own report templates as the target structure.

---

## AI-Assisted Drafting Approaches

| Approach | Description | Best For | Cost |
|---|---|---|---|
| Large language model APIs with a scoped, template-constrained prompt | Providing a language model with structured findings and a fixed template to fill in, rather than open-ended drafting | Drafting report prose from verified findings, with a human reviewing every generated sentence against the source data | Paid, usage-based |
| Structured templating (this folder's script) | Populating a template directly from structured data (CSV/JSON) without any generative model involved | Fully deterministic, no-hallucination-risk report skeleton generation from data you have already verified | Free |
| Notebook-based reporting tools (e.g., Jupyter with nbconvert) | Combining code, data, and narrative in a notebook that can be exported to a shareable report format | Technical/data-heavy reports where the underlying analysis should be reproducible alongside the narrative | Free, open source |

---

## Using the Included Report Draft Generator

`generate_report_draft.py` reads a structured findings file (JSON or CSV) and populates a Markdown report skeleton modeled on this repository's [Executive Summary template](../../../osint-templates/specialized-formats/executive-summary.md), filling in the sections it can determine directly from the data (key findings list, confidence table, source list) and leaving clearly marked placeholders for sections that require human analytical judgment (bottom line, recommendations, limitations).

```bash
python generate_report_draft.py --input findings.json --output draft_report.md
python generate_report_draft.py --input findings.csv --output draft_report.md
```

See `sample_findings.json` in this folder for an example of the expected input structure.

---

## Critical Principle: Structure, Not Substance

This script and the general approach it demonstrates automate the *structural* work of reporting (formatting, organizing findings into consistent sections, building tables) — not the *analytical* work (drawing conclusions, assessing confidence, writing recommendations). Every generated draft:

- Leaves the Bottom Line Up Front, Recommendations, and Limitations sections as explicit placeholders requiring human input.
- Never invents a finding, confidence level, or source that was not present in the input data.
- Should be treated as a first draft requiring full analyst review before distribution, per the review stages in `osint-templates/operational-planning/investigation-workflow.md`.

If you use a generative language model to help draft narrative prose from your findings, provide it only with findings you have already verified, constrain it to the specific template structure, and review every sentence of its output against your source data before use — consistent with the human-verification requirements throughout `osint-templates/ai-assisted-templates/`.

---

## Usage Notes

- This script performs no analysis of its own; it organizes data you provide. Garbage in, garbage out: only feed it findings that have already been through your normal verification process.
- For narrative sections beyond simple templating (for example, a flowing prose summary rather than a bulleted list), consider using a language model with the structured findings as context, but always review the output line-by-line rather than distributing it directly.

---

## Legal and Ethical Notes

- Automated report generation does not change the underlying legal and ethical obligations that apply to the findings themselves; see `osint-templates/operational-planning/legal-compliance-checklist.md`.
- Do not use automated drafting to generate a report's conclusions or recommendations without human review; presenting AI-generated analytical conclusions as if they were independently verified human judgment is inconsistent with the standards in `osint-templates/ai-assisted-templates/`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
