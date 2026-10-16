#!/usr/bin/env bash
# Build + QA for Physics U02 S2.2 Practice Set and its key, exactly as filed in Drive 2026-10-16.
#
#   bash templates/worksheet/specs/phys_u02_s02.2.build.sh [out_dir]
#
# Matt's one-off choices for THIS document, applied in memory only. The shared builders
# (build_worksheet_docx.py, build_worksheet_key_docx.py, scripts/key_solution.py) are NOT edited:
#   - 8 problems, ramp 3/3/1/1 (Physics default is 2/2/1/1)
#   - no tier tags (WARM-UP / PRACTICE / ...) on the student sheet or the key
#   - condensed key: hand size 17 (KEY_SIZE) and short consecutive rows merged onto one line
# None of these is a standing rule yet; making any of them permanent is a Secretary change.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../../.." && pwd)"
SPEC="$HERE/phys_u02_s02.2.json"
OUT="${1:-$REPO/out/phys_u02_s02.2}"; mkdir -p "$OUT"; OUT="$(cd "$OUT" && pwd)"
STU="$OUT/2.2 Practice Set.docx"
KEY="$OUT/2.2 Practice Set Key.docx"

python3 -I "$HERE/phys_u02_s02.2.verify.py"

cd "$REPO/templates/worksheet"
python3 - "$SPEC" "$STU" <<'PY'
import sys
sys.path.insert(0, "."); sys.path.insert(0, "..")
import build_worksheet_docx as b
b.RAMP["physics"] = {"warm-up": 3, "practice": 3, "challenge": 1, "multi-topic": 1}
# Matt 2026-10-16: no tier tags on this student sheet. Tiers stay in the spec for the ramp check.
_card = b.question_card
b.question_card = lambda cell, q, *a, **k: _card(cell, {x: v for x, v in q.items() if x != "tier"}, *a, **k)
sys.exit(b.main())
PY
python3 - "$SPEC" "$KEY" <<'PY2'
import sys
sys.path.insert(0, "."); sys.path.insert(0, "..")
import build_worksheet_key_docx as k
sys.path.insert(0, "../../scripts")
# Matt 2026-10-16: no tier tags on the key either.
_blk = k.answer_block
k.answer_block = lambda doc, n, q, pal: _blk(doc, n, {x: v for x, v in q.items() if x != "tier"}, pal)
# Matt 2026-10-16: condense the key. Smaller hand, and consecutive short plain rows share a line.
# Every step, mistake and boxed answer is kept; only line breaks between short rows go.
import os, key_solution as ks
KEY_SIZE = float(os.environ.get("KEY_SIZE", "17"))
MAX_CHARS = int(os.environ.get("KEY_MERGE", "88"))
def _plain(st):
    return ("row" in st and "note" not in st and all(isinstance(x, str) for x in st["row"]))
def _merge(steps):
    out = []
    for st in steps:
        if out and _plain(st) and _plain(out[-1]):
            a, b = " ".join(out[-1]["row"]), " ".join(st["row"])
            if len(a) + len(b) + 6 <= MAX_CHARS:
                out[-1] = {"row": [a + "      " + b]}
                continue
        out.append(dict(st))
    return out
_img = ks.solution_image
def _small(q, out_png, width_in=7.2, size=27):
    q = dict(q); q["steps"] = _merge(q["steps"])
    return _img(q, out_png, width_in=width_in, size=KEY_SIZE)
ks.solution_image = _small
sys.exit(k.main())
PY2

cd "$OUT"
soffice --headless --convert-to pdf "$STU" "$KEY" --outdir "$OUT"

cd "$REPO"
python3 scripts/audit_worksheet.py "$STU" "$SPEC"
python3 scripts/audit_fonts.py "$OUT/2.2 Practice Set.pdf"
python3 scripts/audit_fonts.py "$OUT/2.2 Practice Set Key.pdf"
python3 scripts/audit_print_ink.py "$OUT/2.2 Practice Set.pdf"
python3 scripts/audit_print_ink.py "$OUT/2.2 Practice Set Key.pdf"
echo "Builds and audits finished. Next: rasterize and inspect each page visually, then run audit-deliverable."
