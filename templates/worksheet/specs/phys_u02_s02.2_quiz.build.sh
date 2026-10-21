#!/usr/bin/env bash
# Build + QA for the Physics U02 S2.2 vectors quiz, versions A and B, with a separate key for each.
#
#   bash templates/worksheet/specs/phys_u02_s02.2_quiz.build.sh [out_dir]
#
# Matt's choices for THIS document, applied in memory only (shared builders are NOT edited):
#   - a quiz layout (templates/quiz/build_quiz_docx.py): short questions share a row, the cards are the
#     work space, equations in plain notation with a drawn theta
#   - 16 points: three angle-restating questions at 2, two vector problems at 5
#   - keys: full-size hand, short rows merged, cards may break at a seam, and every boxed direction
#     is followed by a "same direction:" line (standards/ANSWER_KEYS.md section 10, SHULL-CHG-0046)
# Names follow standards/NAMING.md: "2.2 Quiz A", "2.2 Quiz A Key" (2.2 has no short title).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../../.." && pwd)"
OUT="${1:-$REPO/out/phys_u02_s02.2_quiz}"; mkdir -p "$OUT"; OUT="$(cd "$OUT" && pwd)"

python3 -I "$HERE/phys_u02_s02.2_quiz.verify.py"

for VER in A B; do
SPEC="$HERE/phys_u02_s02.2_quiz_${VER,,}.json"
STU="$OUT/2.2 Quiz $VER.docx"
KEY="$OUT/2.2 Quiz $VER Key.docx"
echo "===== Version $VER"
cd "$REPO/templates/worksheet"
python3 "$REPO/templates/quiz/build_quiz_docx.py" "$SPEC" "$STU"
python3 - "$SPEC" "$KEY" <<'PY2'
import sys
sys.path.insert(0, "."); sys.path.insert(0, "..")
import build_worksheet_key_docx as k
sys.path.insert(0, "../../scripts")
# Matt 2026-10-16: no tier tags on the key either.
_blk = k.answer_block
k.answer_block = lambda doc, n, q, pal: _blk(doc, n, {x: v for x, v in q.items() if x != "tier"}, pal)
# Matt 2026-10-16/19: shorter key at full hand size (17 was too small to read); consecutive short plain rows share a line.
# Every step, mistake and boxed answer is kept; only line breaks between short rows go.
import os, key_solution as ks
KEY_SIZE = float(os.environ.get("KEY_SIZE", "27"))
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
# Matt 2026-10-19: fewer pages at the same hand size. The shared builder keeps each question's
# card whole (no_split), which strands big gaps at page bottoms. Here a card may break across a
# page, but only at a natural seam: after a boxed answer, before the next part of the work.
# The number, the restated prompt and the first piece of work always stay together.
from docx.shared import Inches
def _pieces(steps):
    out, cur = [], []
    for i, st in enumerate(steps):
        # also a seam before a labelled part, e.g. after the conversion block
        if "label" in st and cur and not all("label" in x for x in cur):
            out.append(cur); cur = []
        cur.append(st)
        nxt = steps[i + 1].get("row", [""])[0] if i < len(steps) - 1 else ""
        if "answer" in st and i < len(steps) - 1 and not str(nxt).startswith("same direction"):
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out
def _answer_block(doc, n, q, pal):
    # One table row per piece of work; a page may break between rows, never inside one.
    # Outer border only, so the rows still read as one card.
    pieces = _pieces(q["steps"])
    t = doc.add_table(rows=len(pieces), cols=1)
    k.fix_widths(t, [k.TEXT_W_IN])
    last = len(pieces) - 1
    for j, piece in enumerate(pieces):
        row = t.rows[j]
        k.no_split(row)
        c = row.cells[0]
        edges = ("left", "right") + (("top",) if j == 0 else ()) + (("bottom",) if j == last else ())
        k.borders(c, pal.hair, sz=4, edges=edges)
        k.cell_margins(c, top=70 if j == 0 else 0, bottom=70 if j == last else 0, left=130, right=130)
        if j == 0:
            head = c.paragraphs[0]
            k.run(head, f"{n}.  ", 11, bold=True, color=pal.ink)
            p = k.para(c, q["prompt"].replace("**", ""), 9, color=pal.label); p.runs[0].italic = True
            for part in q.get("parts", []):
                p = k.para(c, "   " + str(part).replace("**", ""), 9, color=pal.label); p.runs[0].italic = True
            k.gap(c, 2)
            target = c.add_paragraph()
        else:
            target = c.paragraphs[0]
        png, _ = ks.solution_image(dict(q, steps=piece), os.path.join(k._TMP, f"q{n}_{j}.png"),
                                   width_in=k.HAND_W_IN)
        pf = target.paragraph_format
        pf.space_before = pf.space_after = 0
        target.add_run().add_picture(png, width=Inches(k.HAND_W_IN))
    return t
k.answer_block = _answer_block
sys.exit(k.main())
PY2

cd "$OUT"
soffice --headless --convert-to pdf "$STU" "$KEY" --outdir "$OUT"

cd "$REPO"
python3 scripts/audit_worksheet.py "$STU" "$SPEC"
python3 scripts/audit_fonts.py "$OUT/2.2 Quiz $VER.pdf"
python3 scripts/audit_fonts.py "$OUT/2.2 Quiz $VER Key.pdf"
python3 scripts/audit_print_ink.py "$OUT/2.2 Quiz $VER.pdf"
python3 scripts/audit_print_ink.py "$OUT/2.2 Quiz $VER Key.pdf"
done
echo "Builds and audits finished. Next: rasterize and inspect each page visually."
