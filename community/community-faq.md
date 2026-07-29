# Community FAQ

## Purpose Statement

This document answers questions that come up repeatedly in this repository's discussions and issue tracker. Check here before opening a new discussion — your question may already be answered.

---

## General Questions

**Q: Is this repository affiliated with law enforcement or any government agency?**

No. This repository is an educational and professional resource companion to "A Complete Guide to Mastering Open-Source Intelligence (OSINT)." It is not affiliated with, endorsed by, or produced on behalf of any law enforcement or government agency.

**Q: Can I use these templates and tools commercially?**

Yes, subject to the terms of the repository's [LICENSE](../../LICENSE) (MIT License). See the license file for the exact terms.

**Q: I found a tool listed here that no longer works or has changed significantly. What should I do?**

Please open a bug report using `../contributions/bug_report_template.md`. Tool landscapes change constantly, and community reports are how this repository stays current.

**Q: Can I translate this repository into another language?**

Yes — translation contributions are welcome. See [CONTRIBUTING.md](../../CONTRIBUTING.md) for the general contribution process, and consider opening a feature request (`../contributions/feature_request_template.md`) first to coordinate with other potential translators and avoid duplicate effort.

---

## Scope and Ethics Questions

**Q: Why won't the maintainers add [specific tool that does X]?**

This repository excludes tools whose primary documented purpose is unauthorized access, account takeover, or circumventing platform security controls, per this repository's [Code of Conduct](../../CODE_OF_CONDUCT.md) and the scope note in `osint-tools/README.md`. If a tool has legitimate uses alongside a concerning primary purpose, it is generally still excluded, since the repository aims to avoid providing uplift for misuse even when a defensive framing is possible.

**Q: Can I get help investigating a specific person using this repository's discussion space?**

Only if you can articulate a specific, legitimate, proportionate purpose consistent with `osint-tools/people-investigation/README.md`, and even then, discussions should focus on methodology questions rather than requesting others to conduct the investigation for you. Requests that appear to be about a personal dispute, ex-partner, or private individual with no stated legitimate purpose will not be assisted, consistent with this repository's [Code of Conduct](../../CODE_OF_CONDUCT.md).

**Q: The legal guidance in this repository doesn't match what I understand about my jurisdiction. What should I do?**

This repository's legal content (including `documentation/legal-and-ethics/` and `osint-templates/operational-planning/legal-compliance-checklist.md`) is explicitly not legal advice and reflects general, non-exhaustive awareness points. If you believe something is materially incorrect, please open a bug report with a citation to an authoritative source, but also consult qualified legal counsel for your specific situation rather than relying solely on this repository.

**Q: Why do so many templates include a "legal and ethical considerations" section? Isn't that repetitive?**

Yes, deliberately. Given the sensitivity of OSINT investigative work, we consider this a feature, not a flaw. Repeating the reminder in context, at the point where it's relevant, is more effective than relying on a reader to remember a single centralized policy document.

---

## Technical Questions

**Q: A script in `osint-tools/` or `scripts-and-automation/` isn't working for me. Where do I get help?**

First, check the script's `--help` output and the accompanying README's usage notes. If the issue persists, open a bug report (`../contributions/bug_report_template.md`) with the exact error message, your Python version, and the command you ran.

**Q: Can I request a script be added for [specific task]?**

Yes — open a feature request (`../contributions/feature_request_template.md`). Scripts are generally added when they demonstrate a clear, legitimate, well-scoped OSINT use case and can be built using publicly accessible or properly authorized data sources.

**Q: Do I need to know how to code to use this repository?**

No. The majority of this repository — all of `osint-templates/` and most of `osint-tools/` — consists of documents, checklists, and curated tool directories that require no coding. Only `scripts-and-automation/` and the working scripts embedded in some `osint-tools/` subfolders require running Python or shell scripts.

---

## Contribution Questions

**Q: I'm new to OSINT. Can I still contribute?**

Yes. Documentation improvements, broken-link reports, and translation work are all valuable contributions that don't require deep OSINT expertise. See the "good first issue" guidance in [CONTRIBUTING.md](../../CONTRIBUTING.md).

**Q: How long does review take?**

Per [CONTRIBUTING.md](../../CONTRIBUTING.md), maintainer triage typically occurs within five to seven business days. Complex submissions (a full new template category, for example) may take longer for thorough review.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
