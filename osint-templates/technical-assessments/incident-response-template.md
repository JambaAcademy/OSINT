# Incident Response Documentation Template

## Executive Summary

**Incident ID:** [Unique incident identifier]
**Incident Name/Codename:** [Internal reference name]
**Organization:** [Organization name]
**Incident Category:** [Malware/Ransomware / Unauthorized Access / Data Exfiltration / Denial of Service / Insider Threat / Phishing Compromise / Other]
**Severity:** [Critical / High / Medium / Low]
**Status:** [Detected / Contained / Eradicated / Recovered / Closed]
**Report Date:** [Report completion date]
**Classification:** [Confidential / Restricted, per organizational policy]

### Incident Snapshot

- **Detection Date/Time:** [Date and time, with timezone]
- **Estimated Onset Date/Time:** [Date and time, if determinable]
- **Systems Affected:** [Count and general category]
- **Data Impact:** [Confirmed/Suspected/None identified]
- **Current Operational Impact:** [Description]

---

## 1. Incident Declaration

### 1.1 Detection Details

- **How Detected:** [Automated alert / User report / Third-party notification / Threat intelligence match / Other]
- **Detecting System/Person:** [Name of tool or reporting individual/role]
- **Initial Alert/Report Reference:** [Ticket number]
- **Time to Detection (Estimated Onset to Detection):** [Duration]

### 1.2 Incident Response Team Activation

| Role | Name | Contact | Activation Time |
|---|---|---|---|
| Incident Commander | [Name] | [Contact] | [Time] |
| Technical Lead | [Name] | [Contact] | [Time] |
| Communications Lead | [Name] | [Contact] | [Time] |
| Legal Counsel | [Name] | [Contact] | [Time] |
| Executive Sponsor | [Name] | [Contact] | [Time] |

### 1.3 Initial Severity Classification

| Factor | Assessment |
|---|---|
| Scope of systems affected | [Assessment] |
| Data sensitivity involved | [Assessment] |
| Business function disruption | [Assessment] |
| Regulatory notification triggers | [Assessment] |
| **Overall Initial Severity** | [Critical/High/Medium/Low] |

---

## 2. Timeline of Events

| Date/Time (Timezone) | Event | Source/Evidence | Logged By |
|---|---|---|---|
| [DateTime] | [Suspected initial compromise] | [Log source/evidence reference] | [Name] |
| [DateTime] | [Detection] | [Alert reference] | [Name] |
| [DateTime] | [Response team activated] | [Notification record] | [Name] |
| [DateTime] | [Containment action taken] | [Change record] | [Name] |
| [DateTime] | [Eradication action taken] | [Change record] | [Name] |
| [DateTime] | [Systems restored] | [Verification record] | [Name] |
| [DateTime] | [Incident closed] | [Closure record] | [Name] |

---

## 3. Technical Investigation Findings

### 3.1 Initial Access Vector

- **Vector Identified:** [Phishing / Exploited vulnerability / Compromised credentials / Third-party compromise / Insider / Unknown]
- **Supporting Evidence:** [Log excerpts, email headers, authentication records — reference location of evidence, do not embed raw sensitive logs in this document]
- **Vulnerability Exploited (if applicable):** [CVE identifier, cross-reference to vulnerability-intelligence-report.md if one was produced]

### 3.2 Scope of Compromise

| System/Asset | Compromise Status | Evidence | Data at Risk |
|---|---|---|---|
| [Hostname/System] | [Confirmed/Suspected/Cleared] | [Evidence reference] | [Data category] |

### 3.3 Threat Actor Activity Observed

- **Lateral Movement Observed:** [Yes/No, with summary]
- **Privilege Escalation Observed:** [Yes/No, with summary]
- **Persistence Mechanisms Identified:** [Summary, with reference to detailed forensic evidence log]
- **Data Staging/Exfiltration Evidence:** [Summary]
- **Tools/Malware Identified:** [Reference to associated malware-analysis-report.md if produced]

### 3.4 Indicators of Compromise Identified

| Indicator | Type | Source | Action Taken |
|---|---|---|---|
| [IOC value — reference evidence log rather than embedding raw sensitive data here] | [Type] | [Detection source] | [Blocked/Monitored/Investigated] |

---

## 4. Containment Actions

### 4.1 Immediate Containment

- [ ] Isolated affected systems from the network
- [ ] Disabled compromised credentials
- [ ] Blocked identified malicious indicators at network perimeter
- [ ] Preserved forensic evidence prior to remediation (see Section 7)
- [ ] Notified relevant internal stakeholders

### 4.2 Short-Term Containment Decisions

| Decision | Rationale | Approved By | Time |
|---|---|---|---|
| [Decision, e.g., take system offline vs. monitor] | [Rationale] | [Name/Role] | [Time] |

---

## 5. Eradication and Recovery

### 5.1 Eradication Actions

- [ ] Removed identified malware/unauthorized tools
- [ ] Closed exploited vulnerability or misconfiguration
- [ ] Reset all potentially compromised credentials
- [ ] Rebuilt affected systems from known-good sources where warranted
- [ ] Verified absence of persistence mechanisms

### 5.2 Recovery Actions

- [ ] Restored systems to production from verified clean state
- [ ] Enhanced monitoring implemented for affected systems
- [ ] Phased return to normal operations completed
- [ ] Post-recovery validation testing completed

### 5.3 Recovery Validation

| System | Validation Method | Result | Validated By |
|---|---|---|---|
| [System] | [Method] | [Pass/Fail] | [Name] |

---

## 6. Impact Assessment

### 6.1 Data Impact

- **Data Types Involved:** [Categories]
- **Estimated Records/Individuals Affected:** [Number, if applicable]
- **Confirmed vs. Suspected Exposure:** [Distinction]

### 6.2 Operational Impact

- **Systems/Services Unavailable:** [List and duration]
- **Estimated Downtime Cost:** [If calculated]
- **Customer/Partner Impact:** [Description]

### 6.3 Regulatory and Legal Considerations

- **Notification Obligations Triggered:** [Regulation names, e.g., state breach notification laws, GDPR, sector-specific requirements]
- **Notification Deadlines:** [Dates]
- **Notifications Made:** [Regulator/individual notifications completed, with dates]
- **Law Enforcement Engagement:** [Yes/No, agency and case reference if applicable]

---

## 7. Evidence Handling and Chain of Custody

> Cross-reference the organization's evidence-chain-custody.md template for full chain-of-custody documentation. Summarize key points here.

| Evidence Item | Collected By | Collection Date/Time | Storage Location | Hash (if file-based) |
|---|---|---|---|---|
| [Description] | [Name] | [DateTime] | [Secure storage reference] | [Hash value] |

---

## 8. Communications Log

| Date/Time | Audience | Message Summary | Channel | Approved By |
|---|---|---|---|---|
| [DateTime] | [Internal staff/Customers/Regulators/Media] | [Summary] | [Email/Press release/Portal notice] | [Name] |

---

## 9. Root Cause Analysis

### 9.1 Root Cause Statement

[Concise statement of the underlying cause that allowed the incident to occur]

### 9.2 Contributing Factors

- [Factor 1]
- [Factor 2]
- [Factor 3]

### 9.3 Five Whys Analysis (Optional)

1. Why did the incident occur? [Answer]
2. Why did that happen? [Answer]
3. Why did that happen? [Answer]
4. Why did that happen? [Answer]
5. Why did that happen? [Root cause]

---

## 10. Lessons Learned and Corrective Actions

### 10.1 What Went Well

- [Observation]

### 10.2 What Could Be Improved

- [Observation]

### 10.3 Corrective Action Plan

| Action Item | Owner | Due Date | Status |
|---|---|---|---|
| [Action] | [Owner] | [Date] | [Not Started/In Progress/Complete] |

---

## 11. Post-Incident Review

- **Review Meeting Date:** [Date]
- **Attendees:** [List]
- **Key Decisions:** [Summary]
- **Follow-Up Review Scheduled:** [Date, if applicable]

---

## 12. Distribution and Classification

**Classification:** [Confidential/Restricted]
**Distribution List:** [Names/roles authorized to view this document]
**Retention Period:** [Per organizational policy and any legal hold requirements]

**Version Control:**

- **Version:** [Version number]
- **Last Updated:** [Date]
- **Prepared By:** [Name]
- **Reviewed By:** [Name]

---

*This document contains sensitive incident details and should be handled according to the organization's information classification policy. Portions of this document may be subject to legal privilege; consult legal counsel before external distribution.*
