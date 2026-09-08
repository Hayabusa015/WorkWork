#!/usr/bin/env bash
# Stop hook: run every SHULL OS validator before the session ends.
#
# This is where drift actually gets caught. The governance rule that only the
# Secretary may edit brand/, standards/, governance/ and courses/ is enforced by
# the agents' tool grants (validate_agents.py checks those), NOT by a path hook -
# a shell hook cannot tell which agent is asking, so blocking by path would fire
# on legitimate Secretary work and become noise people learn to ignore.
set -uo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO" || exit 0
fail=0
for v in validate_layers validate_codes validate_tokens validate_agents validate_schemas validate_references; do
  if ! out=$(python3 "scripts/$v.py" 2>&1); then
    echo "── $v ──"; echo "$out"; fail=1
  fi
done
if ! out=$(python3 scripts/measure_tokens.py --check 2>&1); then
  echo "── measure_tokens ──"; echo "$out"; fail=1
fi
[ "$fail" -eq 0 ] && echo "[shull-os] validators clean"
exit 0   # report, never block the session
