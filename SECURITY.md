# 🛡️ Security Policy

This document describes how to report security vulnerabilities in the code contained in this repository, how we handle reports of content that could enable harm, and the supported-version policy for scripts and tools maintained here.

---

## 📌 Scope of This Policy

This repository primarily contains **documentation, templates, and reference material**, along with a smaller set of **automation scripts** (Python/Bash) in `scripts-and-automation/`. This policy covers:

1. **Code vulnerabilities** — bugs in scripts that could cause unintended data exposure, unsafe file handling, credential leakage, or unsafe network behavior.
2. **Content safety concerns** — templates, tool listings, or documentation that inadvertently provide meaningful uplift toward stalking, harassment, unauthorized access, or other harmful activity, and that should not have passed review.
3. **Dependency vulnerabilities** — known CVEs in third-party packages referenced in `requirements.txt` files or setup instructions.

It does **not** cover vulnerabilities in third-party tools or platforms merely *referenced* or *linked* in our tool directories — those should be reported directly to the maintainers of those tools.

---

## ✅ Supported Versions

| Version | Supported |
|---|---|
| 2.x.x   | ✅ Yes |
| 1.3.x   | ✅ Critical fixes only |
| 1.2.x and earlier | ❌ No |

We recommend always using the latest tagged release or the `main` branch, since scripts that interact with external APIs and services can break or become insecure as those services change their authentication or rate-limiting requirements.

---

## 🚨 Reporting a Vulnerability

**Please do not open a public GitHub issue for security vulnerabilities.** Public disclosure before a fix is available can put users of the affected script or tool at risk.

Instead, report privately through one of these channels:

1. **GitHub Security Advisories** (preferred): Use the "Report a vulnerability" option under this repository's Security tab. This creates a private discussion thread with maintainers.
2. **Email:** <security@jambaacademy.com> — please use the subject line `[SECURITY] <short description>`.

### What to include in your report

- A clear description of the vulnerability and its potential impact
- Steps to reproduce (proof-of-concept code, if applicable)
- The affected file(s), script(s), or template(s), with version/commit hash
- Your assessment of severity (we use CVSS 3.1 as a reference scale, but a plain-language estimate is fine)
- Whether you are aware of the issue being publicly known or actively exploited

### What to expect

| Stage | Timeline |
|---|---|
| Acknowledgment of report | Within 3 business days |
| Initial assessment and severity triage | Within 7 business days |
| Fix developed and validated | Typically within 30 days, depending on severity and complexity |
| Coordinated disclosure / public advisory | After a fix is released, or by mutual agreement with the reporter |
| Credit to reporter (if desired) | Included in the security advisory and release notes |

We follow a **coordinated disclosure** model: we ask reporters to give us reasonable time to investigate and patch before any public disclosure, and in return we commit to timely communication and public credit unless you prefer to remain anonymous.

---

## ⚠️ Reporting Harmful or Unsafe Content

Because this repository deals with open-source intelligence methodology, some content review failures are about **safety and ethics**, not traditional software bugs. If you find a template, tool description, or script that you believe:

- Provides specific, actionable instructions for unauthorized access to systems or accounts,
- Is designed primarily to enable stalking, harassment, or doxxing of a real individual, or
- Includes real, identifiable personal data in example content,

please report it using the same private channels above with the subject line `[CONTENT SAFETY] <short description>`. These reports are handled with the same urgency as code vulnerabilities and may result in immediate removal of the content pending review, per our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 🔐 Secure Use of Scripts and Tools in This Repository

If you use the automation scripts provided in `scripts-and-automation/`, please follow these operational security practices:

- **Never commit API keys, tokens, or credentials.** Use environment variables or a local, git-ignored configuration file (see the provided `config.example.yaml` templates).
- **Run scripts in an isolated environment** (virtual environment, container, or dedicated investigation machine) rather than your primary system, consistent with the operational security guidance in `osint-templates/operational-planning/`.
- **Respect target platform rate limits and Terms of Service.** Scripts are provided for lawful, authorized, ToS-compliant use only.
- **Keep dependencies up to date.** Run `pip list --outdated` (Python) periodically and review the repository's dependency update notices in [CHANGELOG.md](CHANGELOG.md).
- **Validate before trusting output.** OSINT automation can produce false positives or stale data; always corroborate findings from automated tools against the [Source Verification Framework](osint-templates/operational-planning/source-verification-framework.md) before including them in a report.

---

## 📚 Related Policies

- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — community behavior standards, including OSINT-specific ethical expectations
- [CONTRIBUTING.md](CONTRIBUTING.md) — includes legal and ethical requirements for all submitted content
- `osint-templates/operational-planning/legal-compliance-checklist.md` — for guidance on lawful investigation practices
- `osint-templates/operational-planning/evidence-chain-custody.md` — for secure handling of collected evidence

---

## 🙏 Acknowledgments

We thank the security researchers and community members who respectfully and privately report issues, helping keep this resource safe and trustworthy for the entire OSINT and cybersecurity community.

---

**Document version:** 1.0
**Last reviewed:** 2026-07-25
**Maintained by:** Jamba Academy OSINT Team
