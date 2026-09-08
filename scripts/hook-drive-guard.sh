#!/usr/bin/env bash
# PreToolUse hook: refuse Drive trash operations.
#
# Permanent deletion is impossible through the connector - only trash exists - so
# trash IS the destructive operation here. Spec Part 24 and Part 47 both require
# explicit user approval for it, and an agent cannot grant itself that.
#
# Reads the tool call on stdin. Exit 2 blocks and returns the message to Claude.
set -uo pipefail
payload=$(cat)
if printf '%s' "$payload" | grep -q 'trash_file'; then
  cat >&2 <<'MSG'
BLOCKED — Drive trash requires explicit user approval.

Permanent deletion is not possible through this connector; trashing is the
destructive operation. Per governance/GOVERNANCE.md and standards/DRIVE_ARCHITECTURE.md:

  - Propose the deletion, naming the object ID and its current path.
  - Log it to reports/drive-operations/ first.
  - The user trashes it, or explicitly approves you doing so in this turn.

If the user has already approved this specific object in this conversation, say so
and ask them to run it, or to allow the tool for this call.
MSG
  exit 2
fi
exit 0
