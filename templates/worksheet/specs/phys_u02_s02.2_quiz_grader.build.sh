#!/usr/bin/env bash
# Build the one-page quick grader for the Physics U02 S2.2 vectors quiz (versions A and B together).
#
#   bash templates/worksheet/specs/phys_u02_s02.2_quiz_grader.build.sh [out_dir]
#
# Every answer, acceptable direction form and point split is read from the two quiz specs
# (phys_u02_s02.2_quiz_a.json and _b.json), so rebuild this after any change to a quiz.
# Name per standards/NAMING.md: "2.2 Quiz Key - Quick Grader".
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../../.." && pwd)"
OUT="${1:-$REPO/out/phys_u02_s02.2_quiz}"; mkdir -p "$OUT"; OUT="$(cd "$OUT" && pwd)"
NAME="2.2 Quiz Key - Quick Grader"
python3 -I "$HERE/phys_u02_s02.2_quiz.verify.py" > /dev/null
python3 "$REPO/templates/quiz/build_grader_docx.py" "$HERE/phys_u02_s02.2_quiz_a.json" "$HERE/phys_u02_s02.2_quiz_b.json" "$OUT/$NAME.docx"
cd "$OUT" && soffice --headless --convert-to pdf "$OUT/$NAME.docx" --outdir "$OUT"
cd "$REPO"
python3 scripts/audit_fonts.py "$OUT/$NAME.pdf"
python3 scripts/audit_print_ink.py "$OUT/$NAME.pdf"
