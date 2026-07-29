# API Integrations

## Overview

This section demonstrates integration patterns with free, publicly documented security and OSINT-relevant APIs, showing how to build defensive/protective tooling using well-established public services. See `password_breach_checker.py` for a ready-to-use script that checks whether a password appears in the Have I Been Pwned Pwned Passwords dataset, using its free, privacy-preserving k-anonymity API.

---

## Featured API: Have I Been Pwned Pwned Passwords

The [Pwned Passwords API](https://haveibeenpwned.com/api/v3) is a free, unauthenticated, no-API-key-required service that lets you check whether a password has appeared in a known data breach corpus, without ever transmitting the actual password (or even its full hash) to the service. It uses a privacy-preserving technique called k-anonymity:

1. Your password is hashed locally using SHA-1 (a one-way transformation; the original password cannot be recovered from the hash).
2. Only the **first five characters** of that hash are sent to the API.
3. The API returns every known breached hash suffix that shares those first five characters — typically several hundred.
4. Your script compares the remainder of your own hash against that list **locally**, so the full password (or even its full hash) never leaves your machine.

This is a widely adopted, security-industry-standard technique, used by many password managers and account registration systems to warn users against choosing a previously breached password.

---

## Using the Included Password Breach Checker

```bash
python password_breach_checker.py --password "correcthorsebatterystaple"
```

The script will prompt securely (without echoing to the terminal) if you omit `--password` from the command line, since passing a real password as a command-line argument can leave it visible in your shell history or process list.

---

## Other Free, Documented APIs Referenced Elsewhere in This Repository

| API | Used In | Authentication |
|---|---|---|
| SEC EDGAR company facts/submissions | `osint-tools/business-intelligence/financial-analysis/` | None required (User-Agent identification requested) |
| OFAC Sanctions List Service | `osint-tools/business-intelligence/regulatory-monitoring/` | None required (User-Agent identification requested) |
| OpenStreetMap Nominatim geocoding | `osint-tools/geospatial-intelligence/mapping-platforms/` | None required (rate limit and User-Agent policy apply) |

---

## Usage Notes

- Never send a real, currently-in-use password to any third-party service other than the k-anonymity range endpoint described above; the whole point of this technique is that the full password/hash never needs to leave your machine.
- A "found in breach corpus" result means the password has appeared in a known breach dataset somewhere, not necessarily tied to your specific account; treat it as a strong signal to stop using that password, not as confirmation of which account was compromised.

---

## Legal and Ethical Notes

- This API and technique are designed for and intended to be used defensively — checking your own or your organization's passwords against known-breached data to improve security, not for checking or attempting passwords belonging to accounts you do not own or have authorization to test.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
