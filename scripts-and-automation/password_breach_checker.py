#!/usr/bin/env python3
"""
password_breach_checker.py

Check whether a password appears in the Have I Been Pwned Pwned Passwords
dataset, using the free, unauthenticated, privacy-preserving k-anonymity
API. The full password and full password hash never leave your machine;
only the first five characters of its SHA-1 hash are sent to the API.

Purpose in an OSINT/security context:
    Demonstrates a privacy-preserving API integration pattern and
    provides a genuinely useful defensive security check: warning against
    the use of previously breached passwords. See
    scripts-and-automation/api-integrations/README.md for a full
    explanation of the k-anonymity technique and its intended defensive
    use.

API documentation: https://haveibeenpwned.com/api/v3#PwnedPasswords

Requirements:
    Python 3.8+
    requests (pip install requests --break-system-packages)

Usage:
    python password_breach_checker.py
        (prompts securely for a password without echoing it to the terminal)
    python password_breach_checker.py --password "some-password-to-check"
        (convenient for scripting, but be aware this can leave the
        password visible in shell history or process listings — prefer
        the interactive prompt for checking a real, sensitive password)
"""

import argparse
import getpass
import hashlib
import sys

try:
    import requests
except ImportError:
    sys.exit(
        "This script requires the 'requests' package.\n"
        "Install it with: pip install requests --break-system-packages"
    )

PWNED_PASSWORDS_RANGE_URL = "https://api.pwnedpasswords.com/range/{prefix}"


def sha1_hash_uppercase(password: str) -> str:
    """Return the uppercase hex SHA-1 hash of the given password."""
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()


def query_range_api(prefix: str) -> str:
    """
    Query the k-anonymity range API for a given 5-character hash prefix
    and return the raw response text (a list of "SUFFIX:COUNT" lines).
    """
    headers = {"User-Agent": "osint-mastery-guide-password-breach-checker"}
    response = requests.get(
        PWNED_PASSWORDS_RANGE_URL.format(prefix=prefix), headers=headers, timeout=15
    )
    response.raise_for_status()
    return response.text


def parse_range_response(response_text: str) -> dict:
    """Parse the range API's response text into a {suffix: count} dict."""
    results = {}
    for line in response_text.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        suffix, count = line.split(":", 1)
        try:
            results[suffix.strip().upper()] = int(count.strip())
        except ValueError:
            continue
    return results


def check_password_breach(password: str) -> dict:
    """
    Check whether the given password appears in the Pwned Passwords
    dataset. Returns {"found": bool, "breach_count": int}.
    """
    full_hash = sha1_hash_uppercase(password)
    prefix, suffix = full_hash[:5], full_hash[5:]

    response_text = query_range_api(prefix)
    suffix_counts = parse_range_response(response_text)

    if suffix in suffix_counts:
        return {"found": True, "breach_count": suffix_counts[suffix]}
    return {"found": False, "breach_count": 0}


def main():
    parser = argparse.ArgumentParser(
        description="Check whether a password appears in the Have I Been Pwned Pwned Passwords dataset."
    )
    parser.add_argument(
        "--password",
        help="Password to check. If omitted, you will be prompted securely (input not echoed). "
             "Prefer the prompt over this argument for a real, sensitive password.",
    )
    args = parser.parse_args()

    password = args.password
    if not password:
        password = getpass.getpass("Enter the password to check (input will not be displayed): ")

    if not password:
        sys.exit("No password provided.")

    result = check_password_breach(password)

    if result["found"]:
        print(
            f"\nThis password was found in the Pwned Passwords dataset "
            f"{result['breach_count']:,} time(s)."
        )
        print("Recommendation: stop using this password anywhere, and change it immediately "
              "on any account where it is currently in use.")
    else:
        print("\nThis password was not found in the Pwned Passwords dataset.")
        print("Note: this does not guarantee the password is strong or has never been used "
              "elsewhere — only that it is not present in this specific known-breach corpus. "
              "Continue to follow general strong-password practices.")


if __name__ == "__main__":
    main()
