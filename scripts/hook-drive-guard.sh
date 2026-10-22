#!/usr/bin/env bash
# PreToolUse hook: gate Drive trash operations behind logged, explicit approval.
#
# Permanent deletion is impossible through the connector - only trash exists - so
# trash IS the destructive operation here. Spec Part 24 and Part 47, and
# governance/GOVERNANCE.md's authority table (Librarian: Drive trash = "approval"),
# require explicit user approval for it, and an agent cannot grant itself that.
#
# Approval is recognized only via a manifest file under
# reports/drive-operations/approved-trash/*.txt listing the exact object ID, one
# per line (# comments and blank lines ignored). Per governance/CHANGE_CONTROL.md
# §7, Drive mutations are logged to reports/drive-operations/ before they happen -
# this manifest IS that pre-mutation log, plus the explicit sign-off. A missing or
# non-matching ID still blocks unconditionally: this hook never trusts conversation
# text, only a committed file the user's session wrote after real approval.
#
# Reads the tool call on stdin. Exit 2 blocks and returns the message to Claude.
set -uo pipefail
payload=$(cat)

if ! printf '%s' "$payload" | grep -q 'trash_file'; then
  exit 0
fi

approved_dir="${CLAUDE_PROJECT_DIR:-.}/reports/drive-operations/approved-trash"
file_id=$(printf '%s' "$payload" | grep -oE '"fileId"[[:space:]]*:[[:space:]]*"[^"]*"' | head -n1 | sed -E 's/.*"([^"]*)"$/\1/')

if [ -n "$file_id" ] && [ -d "$approved_dir" ]; then
  for manifest in "$approved_dir"/*.txt; do
    [ -e "$manifest" ] || continue
    if grep -vE '^[[:space:]]*(#|$)' "$manifest" | grep -qxF "$file_id"; then
      exit 0
    fi
  done
fi

cat >&2 <<MSG
BLOCKED — Drive trash requires explicit, logged approval.

Permanent deletion is not possible through this connector; trashing is the
destructive operation. Per governance/GOVERNANCE.md and standards/DRIVE_ARCHITECTURE.md:

  - Propose the deletion, naming the object ID and its current path.
  - Log it to reports/drive-operations/ first.
  - Get the user's explicit approval, then record it as a manifest under
    reports/drive-operations/approved-trash/<name>.txt listing this exact
    object ID (one per line) before retrying this call.

fileId seen by this hook: ${file_id:-<not found in payload>}
MSG
exit 2
