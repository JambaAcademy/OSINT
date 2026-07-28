# Case Study: Uncovering a Shell Company Network

## Disclaimer

This case study is entirely fictional. All names, companies, and identifying details are invented for illustrative purposes. Any resemblance to real persons or entities is coincidental.

---

## Background

A mid-sized insurance company, "Meridian Mutual" (fictional), received a large commercial property claim from a policyholder, "Harborview Logistics LLC" (fictional), following a warehouse fire. The claim amount was unusually high relative to the company's stated inventory value, and the Special Investigation Unit (SIU) was asked to review the claim before payment, following `osint-templates/specialized-formats/insurance-investigation.md`.

---

## Stage 1: Collection Planning

The SIU analyst completed `osint-templates/operational-planning/osint-collection-plan.md`, defining a specific priority intelligence requirement: **"Is Harborview Logistics LLC's corporate structure and claimed inventory value consistent with its public business footprint?"** — a narrow, proportionate question, not an open-ended investigation into the policyholder's entire life.

---

## Stage 2: Initial Registry Research

Using `osint-tools/search-and-discovery/government-databases/README.md`, the analyst found:

- Harborview Logistics LLC was registered eight months before the fire.
- Its registered agent was a corporate services company also serving as registered agent for over a dozen other LLCs registered in the same 30-day window.

**Analyst's note:** A shared registered agent alone is common and not inherently suspicious (see `osint-tools/data-visualization/link-analysis/README.md` usage notes) — many small businesses use the same corporate service provider. This is a lead, not a conclusion.

---

## Stage 3: Correlation — Applying Multi-Source Methodology

Following `../advanced-techniques/multi-source-correlation-methodology.md`, the analyst looked for additional, independent signals before drawing any conclusion:

| Signal | Source | Independent of the Registered Agent Signal? |
|---|---|---|
| Three of the co-registered LLCs list the same physical address as Harborview's claimed warehouse | Registry filings | Yes — this is a different underlying fact (shared address, not shared agent) |
| The warehouse address, per satellite imagery history in `osint-tools/geospatial-intelligence/satellite-imagery/README.md`, shows no inventory-scale structure consistent with the claimed goods until two months before the policy was taken out | Historical satellite imagery comparison | Yes — an independent, technical data source |
| The policy's stated inventory value was based on a self-reported inventory list with no corroborating purchase invoices provided | Claim file | Yes — independent of both registry and imagery findings |

The analyst used `osint-tools/data-visualization/link-analysis/link_analysis_graph_builder.py` to build a relationship diagram connecting Harborview, its co-registered sibling LLCs, and the shared registered agent, which made the pattern easy to communicate to non-technical claims management stakeholders.

---

## Stage 4: Alternative Explanation Testing

Before concluding anything, the analyst considered the leading alternative explanation: **"Harborview is a genuine business that simply used a common corporate formation service, and the imagery discrepancy reflects a recent facility expansion, not a fabricated inventory claim."**

This alternative was tested against the satellite imagery timeline (`osint-tools/geospatial-intelligence/satellite-imagery/README.md`): if a genuine facility expansion had occurred, imagery should show construction activity before the claimed inventory buildup. No such construction activity was visible in the available historical imagery, weakening the alternative explanation without fully eliminating it (satellite revisit frequency has gaps, a limitation the analyst noted explicitly per that folder's usage notes).

---

## Stage 5: Reporting

The analyst completed `osint-templates/specialized-formats/insurance-investigation.md`, presenting:

- The registry, imagery, and claim-file findings with their individual and combined significance
- The alternative explanation considered and why it was assessed as less likely, without claiming certainty
- A recommendation to refer the claim for further formal investigation and request corroborating purchase documentation directly from the policyholder — not an unsupported accusation of fraud, which requires a more formal legal process than OSINT alone can establish

---

## What This Case Study Demonstrates

- **Proportionate scope:** the investigation stayed focused on the specific claim-relevant question, not the policyholder's entire background.
- **Genuine multi-source correlation:** each signal came from an independent underlying process (legal registry, satellite imagery, claim documentation), consistent with `../advanced-techniques/multi-source-correlation-methodology.md`.
- **Honest alternative-explanation testing:** the analyst did not simply build a case for the suspected conclusion, but explicitly tested and reported on a competing explanation.
- **Appropriate recommendation:** the conclusion was a recommendation for further formal review, not a final determination of fraud, consistent with the limitations described in `osint-templates/specialized-formats/insurance-investigation.md`.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
