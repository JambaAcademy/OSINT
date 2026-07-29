#!/usr/bin/env bash
#
# evidence_hash_logger.sh
#
# Walk a directory of collected evidence files, compute a SHA-256 hash for
# each, and append a timestamped record to a CSV chain-of-custody log.
# Re-running this script only adds new entries; files already logged with
# an unchanged hash are skipped. If a previously logged file's hash has
# changed, this script flags it prominently rather than silently updating
# the record, since an unexpected hash change on stored evidence requires
# immediate investigation per
# osint-templates/operational-planning/evidence-chain-custody.md, Section 7.
#
# Purpose in an OSINT context:
#     Directly automates the hash-verification and logging requirement
#     described in osint-templates/operational-planning/evidence-chain-custody.md.
#
# Requirements:
#     A POSIX-compatible shell and either `sha256sum` (standard on Linux)
#     or `shasum` (standard on macOS); the script detects which is
#     available automatically. No other dependencies.
#
# Usage:
#     chmod +x evidence_hash_logger.sh
#     ./evidence_hash_logger.sh /path/to/evidence/directory /path/to/evidence_hash_log.csv

set -euo pipefail

EVIDENCE_DIR="${1:-}"
LOG_FILE="${2:-}"

if [[ -z "$EVIDENCE_DIR" || -z "$LOG_FILE" ]]; then
    echo "Usage: $0 <evidence_directory> <log_csv_path>" >&2
    exit 1
fi

if [[ ! -d "$EVIDENCE_DIR" ]]; then
    echo "Error: evidence directory not found: $EVIDENCE_DIR" >&2
    exit 1
fi

# Detect which hashing utility is available.
if command -v sha256sum >/dev/null 2>&1; then
    HASH_CMD="sha256sum"
elif command -v shasum >/dev/null 2>&1; then
    HASH_CMD="shasum -a 256"
else
    echo "Error: neither sha256sum nor shasum was found on this system." >&2
    exit 1
fi

compute_hash() {
    # Prints just the hex digest for the given file path.
    $HASH_CMD "$1" | awk '{print $1}'
}

# Create the log file with a header if it does not already exist.
if [[ ! -f "$LOG_FILE" ]]; then
    echo "file_path,sha256_hash,file_size_bytes,logged_at,status" > "$LOG_FILE"
    echo "Created new evidence hash log: $LOG_FILE"
fi

NEW_COUNT=0
UNCHANGED_COUNT=0
CHANGED_COUNT=0
NOW="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

# Iterate over every regular file in the evidence directory, recursively.
while IFS= read -r -d '' FILE_PATH; do
    HASH="$(compute_hash "$FILE_PATH")"
    SIZE="$(wc -c < "$FILE_PATH" | tr -d ' ')"

    # Look for an existing entry for this exact file path in the log
    # (matching on the first CSV field).
    EXISTING_LINE="$(awk -F',' -v path="$FILE_PATH" '$1 == path {print; exit}' "$LOG_FILE" || true)"

    if [[ -z "$EXISTING_LINE" ]]; then
        echo "${FILE_PATH},${HASH},${SIZE},${NOW},logged" >> "$LOG_FILE"
        NEW_COUNT=$((NEW_COUNT + 1))
        echo "Logged: $FILE_PATH"
    else
        EXISTING_HASH="$(echo "$EXISTING_LINE" | awk -F',' '{print $2}')"
        if [[ "$EXISTING_HASH" == "$HASH" ]]; then
            UNCHANGED_COUNT=$((UNCHANGED_COUNT + 1))
        else
            echo "${FILE_PATH},${HASH},${SIZE},${NOW},HASH_CHANGED_SINCE_LAST_LOG" >> "$LOG_FILE"
            CHANGED_COUNT=$((CHANGED_COUNT + 1))
            echo "WARNING: Hash changed since last log for $FILE_PATH" >&2
            echo "  Previous hash: $EXISTING_HASH" >&2
            echo "  Current hash:  $HASH" >&2
            echo "  This requires immediate investigation per evidence-chain-custody.md, Section 7." >&2
        fi
    fi
done < <(find "$EVIDENCE_DIR" -type f -print0)

echo ""
echo "Summary: ${NEW_COUNT} new file(s) logged, ${UNCHANGED_COUNT} unchanged file(s) skipped, ${CHANGED_COUNT} file(s) with a changed hash flagged."
if [[ "$CHANGED_COUNT" -gt 0 ]]; then
    echo "ACTION REQUIRED: investigate the ${CHANGED_COUNT} flagged hash change(s) immediately." >&2
fi
