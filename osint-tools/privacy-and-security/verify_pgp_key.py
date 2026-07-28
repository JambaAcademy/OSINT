#!/usr/bin/env python3
"""
verify_pgp_key.py

Inspect a PGP/GPG public key file and extract its fingerprint, key ID,
creation date, expiration, and associated user ID(s), to support
out-of-band verification before trusting a key claimed to belong to a
specific source or contact.

Purpose in an OSINT/journalism context:
    A public key file alone only proves that whoever generated it
    controls the corresponding private key — it does not prove the key
    belongs to the specific person or organization it claims to
    represent. This script extracts the details you need to verify
    through a separate, independent channel (phone call, a fingerprint
    posted on a verified website, or an in-person exchange) before
    relying on the key. See
    osint-tools/privacy-and-security/secure-communications/README.md for
    the full explanation of why this step matters.

Isolation:
    This script imports the key into a temporary, isolated GPG keyring
    (created fresh in a temp directory and deleted afterward) rather than
    your personal, everyday keyring, so routine verification checks don't
    clutter your real keyring or make an implicit trust decision.

Requirements:
    Python 3.8+
    python-gnupg (pip install python-gnupg --break-system-packages)
    The GnuPG binary (gpg) must also be installed separately:
        Debian/Ubuntu: sudo apt-get install gnupg
        macOS (Homebrew): brew install gnupg

Usage:
    python verify_pgp_key.py --key-file source_public_key.asc
"""

import argparse
import datetime
import shutil
import sys
import tempfile

try:
    import gnupg
except ImportError:
    sys.exit(
        "This script requires python-gnupg.\n"
        "Install it with: pip install python-gnupg --break-system-packages\n"
        "You must also have the gpg binary installed on your system."
    )

# Common OpenPGP public-key algorithm IDs (RFC 4880 section 9.1) mapped to
# human-readable names, for friendlier display than the raw numeric code.
ALGORITHM_NAMES = {
    "1": "RSA", "2": "RSA (encrypt only)", "3": "RSA (sign only)",
    "16": "Elgamal", "17": "DSA", "18": "ECDH", "19": "ECDSA", "22": "EdDSA",
}


def format_unix_timestamp(value) -> str:
    """Convert a GPG-reported Unix timestamp string to a readable date, if possible."""
    if not value:
        return "No expiration set"
    try:
        return datetime.datetime.fromtimestamp(int(value), tz=datetime.timezone.utc).strftime(
            "%Y-%m-%d %H:%M UTC"
        )
    except (ValueError, TypeError):
        return str(value)  # fall back to raw value if it wasn't a plain timestamp


def inspect_key(key_file_path: str) -> list:
    """
    Import the given public key file into a fresh temporary keyring and
    return a list of dicts describing each key found in the file.
    """
    with open(key_file_path, "r", encoding="utf-8", errors="replace") as f:
        key_data = f.read()

    temp_dir = tempfile.mkdtemp(prefix="pgp_verify_")
    try:
        gpg = gnupg.GPG(gnupghome=temp_dir)
        import_result = gpg.import_keys(key_data)

        if not import_result.fingerprints:
            sys.exit(
                "No valid PGP public key could be parsed from this file. "
                "Confirm it is an ASCII-armored public key (typically beginning with "
                "'-----BEGIN PGP PUBLIC KEY BLOCK-----')."
            )

        keys = gpg.list_keys()
        results = []
        for key in keys:
            algo_code = key.get("algo")
            results.append({
                "fingerprint": key.get("fingerprint"),
                "key_id": key.get("keyid"),
                "algorithm": ALGORITHM_NAMES.get(algo_code, f"Unknown (code {algo_code})"),
                "length": key.get("length"),
                "creation_date": format_unix_timestamp(key.get("date")),
                "expiration_date": format_unix_timestamp(key.get("expires")),
                "user_ids": key.get("uids", []),
                "trust_level_in_this_temp_keyring": key.get("trust"),
            })
        return results
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


def print_results(results: list) -> None:
    for i, key in enumerate(results, start=1):
        print(f"\n--- Key {i} ---")
        print(f"Fingerprint:      {key['fingerprint']}")
        print(f"Key ID (short):   {key['key_id']}")
        print(f"Algorithm/Length: {key['algorithm']} / {key['length']} bits")
        print(f"Creation date:    {key['creation_date']}")
        print(f"Expiration:       {key['expiration_date']}")
        print(f"User ID(s) claimed by this key:")
        for uid in key["user_ids"]:
            print(f"  - {uid}")

    print(
        "\nIMPORTANT: The user ID(s) and creation date above are self-asserted by "
        "whoever generated this key and are NOT independently verified by this script "
        "or by GPG itself. Before trusting this key for sensitive communication, verify "
        "the fingerprint above through a channel independent of however you received "
        "this key file (e.g., a phone call, an in-person exchange, or a fingerprint the "
        "source has posted on a separately verified website)."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Inspect a PGP public key file and extract its fingerprint and identity details."
    )
    parser.add_argument("--key-file", required=True, help="Path to an ASCII-armored PGP public key file")
    args = parser.parse_args()

    try:
        results = inspect_key(args.key_file)
    except FileNotFoundError:
        sys.exit(f"File not found: {args.key_file}")

    print_results(results)


if __name__ == "__main__":
    main()
