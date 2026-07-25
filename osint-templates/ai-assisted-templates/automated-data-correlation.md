# Automated Data Correlation Report

## Purpose Statement

This template documents the process and findings of using automated tools to correlate data points across multiple sources within an OSINT investigation — for example, linking an email address, username, phone number, or image across different platforms and records. It emphasizes disclosing the correlation method and confidence basis clearly, since automated correlation carries a meaningful risk of false-positive matches, particularly for common identifiers.

---

## Executive Summary

**Case/Project ID:** [Unique identifier]
**Correlation Objective:** [What entities or identifiers this correlation exercise was intended to link]
**Analyst(s):** [Name(s)]
**Tool(s) Used:** [Name(s) and version(s)]
**Report Date:** [Date]
**Classification:** [Public / Internal / Confidential]

### Key Findings Summary

- **Total Correlations Identified:** [Count]
- **Correlations Confirmed with High Confidence:** [Count]
- **Correlations Requiring Further Verification:** [Count]

---

## 1. Correlation Objective and Scope

- **Seed Identifier(s):** [The starting identifier(s), e.g., an email address, username, phone number, or image hash]
- **Target Identifier Types Sought:** [What other types of identifiers or accounts the correlation aimed to find]
- **Scope Boundaries:** [Any explicit limits on which platforms/sources were included]
- **Legal/Ethical Basis:** [Reference to the [OSINT Collection Plan](../operational-planning/osint-collection-plan.md) and [Legal Compliance Checklist](../operational-planning/legal-compliance-checklist.md) governing this investigation]

---

## 2. Correlation Methodology

### 2.1 Tool(s) and Technique(s) Used

| Tool/Technique | Purpose | Data Sources Queried |
|---|---|---|
| [Tool name] | [e.g., username correlation across platforms] | [List of platforms/databases] |
| [Technique, e.g., reverse image hashing] | [Purpose] | [Sources] |

### 2.2 Matching Logic

- **Exact Match Fields Used:** [e.g., identical email address]
- **Fuzzy Match Fields Used:** [e.g., similar username with minor variation, phonetic name matching]
- **Match Threshold Applied:** [Any similarity score threshold used by the tool, and what that threshold means in practice]

---

## 3. Correlation Findings

### 3.1 Correlation Results Table

| Identifier A | Identifier B | Platform/Source of B | Match Type | Match Confidence (Tool) | Analyst Confidence |
|---|---|---|---|---|---|
| [Seed identifier] | [Correlated identifier] | [Platform] | [Exact/Fuzzy] | [Score/Rating] | [High/Medium/Low] |

### 3.2 Supporting Evidence Per Correlation

**Correlation 1: [Identifier A] to [Identifier B]**

- **Matching Basis:** [What specifically matched, e.g., identical profile photo, identical unique username string, shared phone number]
- **Corroborating Evidence Beyond the Automated Match:** [Any additional independent evidence supporting this specific correlation, per the corroboration standard in [Source Verification Framework](../operational-planning/source-verification-framework.md)]
- **Screenshot/Archive Reference:** [Evidence ID, cross-referenced to the evidence log]

---

## 4. False Positive Risk Assessment

Automated correlation tools can produce false positives, especially for common usernames, stock profile photos, or widely shared contact details. Assess this risk explicitly for each correlation.

| Correlation | False Positive Risk Factors Present | Risk Level |
|---|---|---|
| [Correlation] | [e.g., username is a common word; photo is a stock/default image] | [High/Medium/Low] |
| [Correlation] | [e.g., identifier is a rare, distinctive alphanumeric string] | [Low] |

### 4.1 Mitigation Steps Taken

- [ ] Manually reviewed each high-risk correlation before including it in findings
- [ ] Searched for the matched identifier independently to assess how commonly it appears (a widely reused username lowers confidence)
- [ ] Sought at least one additional, independent corroborating data point for any correlation rated as higher false-positive risk

---

## 5. Network/Relationship Visualization (If Applicable)

[Reference to an accompanying link-analysis diagram, if produced, showing the correlated identifiers and their relationships. Describe the visualization's structure here; store the actual diagram file per the data-visualization templates.]

**Diagram Reference:** [File name/location]

---

## 6. Confidence Summary

| Correlation | Overall Confidence | Basis for Rating |
|---|---|---|
| [Correlation 1] | [High/Medium/Low] | [Basis] |
| [Correlation 2] | [High/Medium/Low] | [Basis] |

---

## 7. Alternative Explanations

| Correlation | Alternative Explanation | Assessment |
|---|---|---|
| [Correlation] | [e.g., coincidental reuse of a common username by different individuals] | [Assessment] |

---

## 8. Limitations

- **Tool Coverage Limitations:** [Note any platforms the correlation tool does not cover]
- **Data Currency:** [Note that correlated accounts/profiles may have changed or been deleted since the tool's data was last indexed]
- **Automated Confidence Score Caveats:** [Clarify that a tool's internal confidence score is not equivalent to a verified fact and should not be presented as such without independent corroboration]

---

## 9. Recommendations

- [ ] [Recommendation, e.g., treat high-confidence correlations as established fact for reporting purposes]
- [ ] [Recommendation, e.g., seek additional corroboration before relying on medium/low-confidence correlations]
- [ ] [Recommendation regarding any further investigation steps]

---

## 10. Source Documentation

- [Source 1]: [Citation] — [Access date]
- [Source 2]: [Citation] — [Access date]

---

## 11. Distribution and Classification

**Classification:** [Public / Internal Use / Confidential]
**Version:** [Version number]
**Last Updated:** [Date]

---

*Automated correlation results in this report have been reviewed for false-positive risk and, where required by the applicable confidence rating, independently corroborated before being presented as findings. Correlations rated as lower confidence should not be treated as established fact without further verification.*
