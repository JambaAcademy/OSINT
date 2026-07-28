# Your First Investigation: A Complete Walkthrough

## Purpose Statement

This walkthrough demonstrates a complete, beginner-friendly OSINT investigation from intake through final report, using this repository's own templates and tools at each step. It uses a fictional practice scenario. Follow along with your own practice subject (see `../training-materials/` for suggested low-stakes practice scenarios), never with a real private individual, until you have completed the legal and ethical review steps described in Stage 2 below.

---

## The Scenario (Fictional, for Illustration)

A small business owner has asked your organization to conduct basic due diligence on "Example Widgets Co.," a prospective supplier they have not worked with before. This is a legitimate, common business intelligence use case with a clear, proportionate purpose.

---

## Stage 1: Intake and Objective Definition

Following `osint-templates/operational-planning/investigation-workflow.md`, Stage 1:

- **Requesting party:** Business owner (internal client)
- **Objective:** Confirm Example Widgets Co. is a legitimate, operating business with no major red flags, before entering a supply contract
- **Investigation type:** Business intelligence
- **Deadline:** One week

This objective is specific and answerable — a good sign you're ready to proceed, rather than an open-ended "find out everything about this company."

---

## Stage 2: Legal and Ethical Review

Open `osint-templates/operational-planning/legal-compliance-checklist.md` and work through it:

- **Legal basis:** Legitimate business due diligence before a contractual relationship — a well-established, low-risk basis.
- **Jurisdiction:** Confirm where the company is registered and where your organization operates.
- **Sensitive data risk:** Low — this investigation concerns a business entity, not a private individual's sensitive personal data.

This is a low-risk investigation, but complete the checklist anyway — the habit matters more than the specific result for any single case.

---

## Stage 3: Collection Planning

Complete `osint-templates/operational-planning/osint-collection-plan.md`. The key section is breaking your objective into specific priority intelligence requirements (PIRs):

| PIR | Sub-Question |
|---|---|
| PIR-1 | Is this a genuine, currently active registered business? |
| PIR-2 | Who owns/controls it, and are there any red flags associated with those individuals? |
| PIR-3 | Is there any history of complaints, litigation, or regulatory action? |
| PIR-4 | Does its online presence match what it claims to be? |

Notice that each PIR is specific and independently answerable — this is what makes the collection efficient rather than an unfocused search.

---

## Stage 4: Active Collection

Work through each PIR using the appropriate tools:

- **PIR-1:** Use `osint-tools/search-and-discovery/government-databases/README.md` to check the relevant state/national business registry. Log the registration status, date, and registered address.
- **PIR-2:** Use the same registry for officer/director information, then check `osint-tools/business-intelligence/company-research/README.md` for additional profile data. If a named individual needs further investigation, consult the elevated standard in `osint-tools/people-investigation/README.md` first.
- **PIR-3:** Use `osint-tools/search-and-discovery/government-databases/README.md` (court records) and `osint-tools/business-intelligence/regulatory-monitoring/README.md` for any enforcement history.
- **PIR-4:** Review the company's website and cross-check against `osint-tools/technical-reconnaissance/domain-analysis/README.md` (how old is the domain? does the registration date make sense relative to the claimed company history?).

**Log every source as you go** — don't wait until the report-writing stage. Note the URL, access date, and your name for each finding.

---

## Stage 5: Source Verification

Apply `osint-templates/operational-planning/source-verification-framework.md` to each finding. For example:

- The company's registration status from the official state registry: **A1** (completely reliable source, confirmed fact).
- A claim about the company's founding year from its own marketing website: **B2** (usually reliable source for its own claims, probably true, but self-reported).

---

## Stage 6: Analysis

Organize findings against your four PIRs. In this fictional scenario, suppose you find:

- The company is actively registered and in good standing (PIR-1: resolved, high confidence).
- Its sole listed officer has no other concerning associations (PIR-2: resolved, high confidence).
- No litigation or regulatory action found (PIR-3: resolved, medium confidence — absence of evidence is not the same as evidence of absence).
- Its domain was registered only three months ago, despite the website claiming "10 years in business" (PIR-4: a genuine discrepancy worth flagging).

---

## Stage 7: Gap Assessment

The domain-age discrepancy from PIR-4 is worth a closer look before finalizing the report — perhaps the company rebranded or migrated domains. A quick additional search (checking web archive snapshots via the tools in `osint-tools/search-and-discovery/specialized-databases/README.md`) resolves this: an older domain under a previous company name redirects to the new one, consistent with a legitimate rebrand. Document this resolution rather than leaving the discrepancy unexplained.

---

## Stage 8: Draft Report

Choose `osint-templates/investigation-reports/business-intelligence-report.md` as your primary template, since this is a standard business intelligence investigation, not one requiring a specialized format. Populate each section using your logged findings and source ratings.

---

## Stage 9: Quality Review

Have a colleague review the draft against your working notes: does every claim trace back to a logged, rated source? Is the domain-age discrepancy explained clearly rather than glossed over?

---

## Stage 10: Delivery

Deliver the completed report to the business owner who requested it, per your organization's classification handling policy.

---

## Stage 11: Closure

Close the case, retain your working notes and evidence log per your retention policy, and note any process lessons (in this case: domain-age checks are a fast, high-value verification step worth including as standard practice for any business intelligence investigation).

---

## What Made This a Good Investigation

- The objective was specific from the start, which made every later stage more efficient.
- Sources were logged and rated continuously, not reconstructed at the end.
- A discrepancy was investigated and resolved, not silently dropped or over-stated.
- The final report is fully traceable to its underlying evidence.

---

## Next Steps

- Practice this same workflow with one of the scenarios in `../training-materials/`.
- Review `../advanced-techniques/` once you're comfortable with this basic workflow, to learn more sophisticated correlation methods for more complex investigations.
- Keep `../reference-guides/` open in a second window during your next real investigation.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
