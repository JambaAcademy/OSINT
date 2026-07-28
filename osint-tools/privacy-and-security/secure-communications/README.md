# Secure Communications

## Overview

This section covers tools for confidential communication with sources, colleagues, and legal counsel during a sensitive investigation. See `verify_pgp_key.py` in this folder for a ready-to-use script that inspects a PGP/GPG public key file and extracts its fingerprint and identity details for out-of-band verification — an important step before trusting a key claimed to belong to a specific source.

---

## Encrypted Messaging

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Signal | Widely used end-to-end encrypted messaging application with a strong security track record and independent security audits | General-purpose secure messaging with sources and colleagues | Free |
| Wire | End-to-end encrypted messaging with a focus on business/team use | Team-based secure communication | Freemium/Paid |

## Encrypted Email

| Tool | Description | Best For | Cost |
|---|---|---|---|
| ProtonMail | End-to-end encrypted email provider based in Switzerland, with strong default privacy protections | General secure email, especially for source communication requiring email specifically | Freemium/Paid |
| Tutanota | End-to-end encrypted email provider with a strong privacy-focused design | Alternative to ProtonMail with similar privacy properties | Freemium/Paid |
| PGP/GPG (with a standard email provider) | Public-key encryption standard that can be layered onto standard email using tools like GnuPG | Communicating with sources or organizations who use their own PGP key rather than a specific encrypted email provider | Free, open source |

## Secure File Transfer

| Tool | Description | Best For | Cost |
|---|---|---|---|
| OnionShare | Open-source tool for securely and anonymously sharing files directly over the Tor network without a third-party server | Sharing sensitive files or documents directly with a source without relying on cloud storage | Free, open source |
| SecureDrop | Open-source whistleblower submission platform used by many news organizations | Receiving sensitive documents from anonymous sources in a journalism context | Free, open source (requires server setup by the receiving organization) |

---

## Using the Included PGP Key Verification Script

`verify_pgp_key.py` imports a PGP/GPG public key file into a temporary, isolated keyring (not your personal keyring, to avoid side effects) and extracts its fingerprint, key ID, creation date, expiration, and associated user ID(s), so you can verify these details against an out-of-band source (a phone call, a fingerprint posted on a verified website, or an in-person exchange) before trusting the key.

```bash
pip install python-gnupg --break-system-packages
python verify_pgp_key.py --key-file source_public_key.asc
```

---

## Why Out-of-Band Verification Matters

A PGP public key file, by itself, only proves that whoever generated it controls the corresponding private key — it does not prove the key belongs to the specific person or organization it claims to represent. Always verify a new key's fingerprint through a channel independent of the one where you received the key file itself (for example, if the key arrived by email, verify the fingerprint by phone or against a fingerprint the source has posted on a separately verified website) before relying on it for sensitive communication.

---

## Usage Notes

- This script only reads and reports on a public key; it does not import the key into your personal, everyday GPG keyring, avoiding clutter or accidental trust decisions from routine verification checks.
- A key's stated creation date and user ID are self-asserted by whoever generated the key and are not independently verified by GPG itself; the out-of-band verification step described above is what actually establishes trust, not the key file alone.

---

## Legal and Ethical Notes

- Secure communications tools in this section protect the confidentiality of lawful investigative and journalistic communication, including source protection where applicable.
- Encryption is legal in most jurisdictions for general use, though some countries restrict or regulate its use; confirm the legal status in your jurisdiction and your source's jurisdiction before relying on a specific tool for sensitive communication.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
