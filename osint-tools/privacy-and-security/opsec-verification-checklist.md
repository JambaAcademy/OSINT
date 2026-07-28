# OPSEC Verification Checklist: VPN and Tor Setup

## Purpose Statement

This checklist verifies that a VPN or Tor setup is actually functioning as intended before it is relied upon for sensitive investigative work. A connection that appears active in its client application can still leak identifying information through DNS queries, WebRTC, or an improperly configured kill switch. Run this checklist at initial setup and periodically thereafter (network configurations, VPN client updates, and browser updates can all silently change leak behavior).

---

## 1. Setup Details

**Date:** [Date]
**Analyst:** [Name]
**Tool Being Verified:** [VPN provider name / Tor Browser / Tails / Whonix]
**Purpose of This Session:** [Brief description, e.g., "sensitive source verification research"]

---

## 2. Pre-Connection Baseline

Before connecting to the VPN or Tor, record your baseline (non-protected) network information for comparison.

- **Baseline public IP address:** [Record via a simple "what is my IP" lookup]
- **Baseline approximate geolocation (per IP lookup):** [City/region shown]
- **Baseline DNS resolver (per a DNS leak test site):** [Resolver shown]

---

## 3. Post-Connection Verification

### 3.1 IP Address Leak Check

- [ ] Connected to VPN/Tor
- [ ] Re-checked public IP address via a "what is my IP" lookup
- [ ] Confirmed the displayed IP address is different from the baseline and matches the expected VPN/Tor exit location
- [ ] Repeated the check after a few minutes to confirm the IP address remains stable (or, for Tor, changes only via deliberate circuit renewal)

**Result:** [Pass/Fail] **IP shown:** [Value]

### 3.2 DNS Leak Check

- [ ] Used a dedicated DNS leak test tool (not just the IP checker) to confirm DNS queries are routed through the VPN/Tor tunnel, not your ISP's default resolver
- [ ] Confirmed the DNS resolver shown is associated with the VPN/Tor provider, not your baseline ISP resolver

**Result:** [Pass/Fail] **Resolver shown:** [Value]

### 3.3 WebRTC Leak Check

- [ ] Used a WebRTC leak test tool to confirm the browser does not expose your real IP address via WebRTC, which can bypass VPN tunneling in some browser configurations
- [ ] If a leak was detected, disabled WebRTC in browser settings or switched to a browser/extension that blocks WebRTC leaks, and re-tested

**Result:** [Pass/Fail]

### 3.4 Kill Switch Verification

- [ ] Confirmed the VPN client's kill switch feature is enabled in settings
- [ ] Tested kill switch behavior by manually disconnecting the VPN connection (e.g., disabling the network adapter or force-quitting the VPN process) while monitoring whether internet access is blocked until the VPN reconnects
- [ ] Confirmed no traffic was observed to escape onto the unprotected connection during the simulated drop

**Result:** [Pass/Fail]

### 3.5 Time Zone and Locale Consistency

- [ ] Confirmed the system's displayed time zone and browser locale do not obviously contradict the VPN/Tor exit location in a way that could serve as a secondary fingerprinting signal
- [ ] For Tor Browser specifically, confirmed the browser window is not maximized/resized in a way that creates a unique screen-resolution fingerprint (Tor Browser's default window size is deliberately uniform across users)

---

## 4. Browser Fingerprint Check

- [ ] Ran a browser fingerprinting check tool (e.g., EFF's Cover Your Tracks) to assess overall uniqueness/traceability
- [ ] Reviewed and addressed any high-uniqueness factors flagged (unusual installed fonts, plugins, or canvas fingerprinting exposure)

**Result:** [Fingerprint uniqueness assessment, e.g., "unique among X browsers tested"]

---

## 5. Isolation Verification

- [ ] Confirmed this session uses a dedicated investigation browser profile, container, or virtual machine, not the analyst's personal browsing session
- [ ] Confirmed no personal accounts are logged in within this session/profile
- [ ] Confirmed browser history/cookies from this session will not be retained after the session ends (private/incognito mode, or a session designed to be wiped)

---

## 6. Overall Verification Outcome

**Overall Result:** [Cleared for sensitive work / Issues found — see below / Not yet verified]

**Issues Found and Remediation:**

| Issue | Remediation Taken | Re-Verified? |
|---|---|---|
| [Issue] | [Action taken] | [Yes/No] |

---

## 7. Re-Verification Schedule

- **Next scheduled re-verification:** [Date — recommend at least every 30 days, and immediately after any VPN client, browser, or OS update]
- **Trigger for immediate re-verification:** [e.g., after any software update to the VPN client, browser, or operating system]

---

## 8. Version Control

**Version:** [Version number]
**Last Updated:** [Date]

---

*This checklist verifies technical configuration only. It does not address the broader operational security practices (device compartmentalization, persona management) covered in `operational-security/README.md`, which should be used alongside this checklist.*
