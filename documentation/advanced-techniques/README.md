# Advanced Techniques

## Overview

This section covers methodology for experienced analysts working on more complex investigations: combining weak individual signals into stronger conclusions, pivoting efficiently across data types, and managing large, multi-source investigations without losing analytical rigor. See `multi-source-correlation-methodology.md` for a detailed treatment of the core advanced technique underlying most sophisticated OSINT work: correlation across independently weak signals.

---

## When You're Ready for This Section

The techniques here assume comfort with the fundamentals in `../getting-started/` and fluency with the templates in `osint-templates/operational-planning/`. If you find yourself unsure how to rate a source's reliability or what "proportionate scope" means in practice, revisit the fundamentals before continuing here.

---

## Topics Covered

| Guide | Covers |
|---|---|
| [`multi-source-correlation-methodology.md`](multi-source-correlation-methodology.md) | Combining independently weak signals into a higher-confidence conclusion, and avoiding the common analytical traps in doing so |

---

## General Principles for Advanced Work

- **Weak signals can combine into strong conclusions, but only if they are genuinely independent.** Ten mentions of the same fact that all trace back to one original source are not ten independent confirmations.
- **Pivoting has diminishing returns.** Each additional hop away from your original, well-corroborated findings introduces more uncertainty; know when to stop pivoting and consolidate what you have.
- **Document your reasoning, not just your findings.** In a complex investigation, the analytical path — why you considered and rejected an alternative explanation — is often as valuable to a reviewer as the conclusion itself.
- **Revisit your collection plan as the investigation evolves.** Complex investigations often reveal that the original priority intelligence requirements need updating; treat the collection plan as a living document within a single investigation's lifecycle, re-approving significant scope changes per `osint-templates/operational-planning/osint-collection-plan.md`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
