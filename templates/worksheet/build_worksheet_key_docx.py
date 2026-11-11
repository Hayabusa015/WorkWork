#!/usr/bin/env python3
"""Build the separate teacher answer key for a SHULL worksheet / practice set.

    python3 templates/worksheet/build_worksheet_key_docx.py specs/<spec>.json out.docx

Matt's rule, stated plainly: produce the answer key whenever a Physics problem set like this
is created (2026-09-14, courses/physics/DECISIONS.md). The student handout uses inline
self-check brackets on every calculation but the last (SHULL-CHG-0021) - deliberately withheld
so the last question is finished without a net. The key is a separate file precisely so that
withheld answer, and full worked steps for every question, live somewhere: never on the
student page.

This is a companion to build_worksheet_docx.py, not a course-profile-enforcing builder in its
own right - the key is teacher-only, so the no-work-area / no-answer-blank rules that govern
the student handout do not apply to it. It shares the same masthead, palette, fonts, and
footer grammar as the student handout so the two read as one document set, not two different
templates that happened to be filed in the same folder.

Each question in the spec must carry a "solution" field: the full worked steps and final
answer, independent of any "selfCheck" bracket. A question with no "solution" is refused -
a key that silently skips a question is worse than no key.

A question may carry "keyImage" (SHULL-CHG-0071): a drawn scene, such as a free-body diagram,
placed in its answer box, with any "steps" drawn below it. The schema lives once, in the
scripts/key_solution.py docstring. If the scene cannot model the item, the typed "solution"
prints instead and the build says so; a force arrow labelled as motion refuses the build.
"""
import json, os, sys, tempfile
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _shull_docx import (          # noqa: E402
    COURSE_CODE, Palette, known_sections, unit_title, borders, para, run,
    fix_widths, no_split, page_setup, running_footer, cell_margins, gap, trim_tail,
)

from _shull_name import document_name, short_title   # noqa: E402
# A project key is reference tables and grading notes, not worked questions. It draws them
# with the handout's own blocks, so the key and the handout share one look.
from build_worksheet_docx import table_block, notes_block   # noqa: E402
# The opt-in grid layout ("layout": "grid") is the student sheet's; the key draws the same
# grid so a teacher grades square against square.
from build_worksheet_docx import (   # noqa: E402
    grid_opts, grid_check, grid_rows, grid_table, grid_head, square, GRID_PROMPT_GAP_TW,
)

HERE = os.path.dirname(os.path.abspath(__file__))
TEXT_W_IN = 7.50
HAND_W_IN = 7.20            # handwritten solution image width; fits the 7.50 in card less its margins
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "scripts"))
_TMP = tempfile.mkdtemp(prefix="shull_key_")


def refuse(msg, *more):
    print("build_worksheet_key_docx: " + msg, file=sys.stderr)
    for m in more:
        print("   " + m, file=sys.stderr)
    return 1


def page_break(doc):
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    p = doc.add_paragraph()
    r = p.add_run()
    br = OxmlElement("w:br")
    br.set(qn("w:type"), "page")
    r._element.append(br)


def answer_block(doc, n, q, pal):
    """One question's key entry: number + tier, the prompt restated small, the full
    worked solution, and the final answer set apart so it can be read at a glance
    while grading - never just the bracket the student sheet withholds."""
    t = doc.add_table(rows=1, cols=1)
    fix_widths(t, [TEXT_W_IN])
    no_split(t.rows[0])          # a question's key entry stays whole across a page break,
    c = t.rows[0].cells[0]       # same rule the student handout's cards follow.
    borders(c, pal.hair, sz=4)
    cell_margins(c, top=70, bottom=70, left=130, right=130)

    head = c.paragraphs[0]
    r = run(head, f"{n}.  ", 11, bold=True, color=pal.ink)
    if q.get("tier"):
        run(head, q["tier"].upper(), 7, bold=True, color=pal.accent)

    p = para(c, q["prompt"].replace("**", ""), 9, color=pal.label)   # the key restates; bold is the handout's job
    p.runs[0].italic = True
    for part in q.get("parts", []):
        p = para(c, "   " + str(part).replace("**", ""), 9, color=pal.label)
        p.runs[0].italic = True

    gap(c, 2)
    if q.get("steps") or q.get("keyImage"):
        # Handwritten worked solution in the key-handwriting face (standards/ANSWER_KEYS.md):
        # the key image, the steps, any scene sketch and the boxed answer are drawn, so no
        # typed copy follows. A key image the scene cannot model falls back to the typed
        # solution below (SHULL-CHG-0071) - the drawing is the answer, so it is never just
        # omitted.
        from key_solution import solution_image, SceneUnsupported
        try:
            png, _ = solution_image(q, os.path.join(_TMP, f"q{n}.png"), width_in=HAND_W_IN)
        except SceneUnsupported as e:
            if not q.get("keyImage"):
                raise
            print(f"build_worksheet_key_docx: Q{n} key image not drawn ({e}); "
                  "printing the typed solution instead.", file=sys.stderr)
        else:
            c.add_paragraph().add_run().add_picture(png, width=Inches(HAND_W_IN))
            return c
    for line in str(q["solution"]).split("\n"):
        if line.strip():
            para(c, line.strip(), 10, color=pal.ink)

    if q.get("finalAnswer"):
        para(c, "ANSWER:  " + str(q["finalAnswer"]), 10, bold=True, color=pal.accent)
    return c


# ---------------------------------------------------------------- grid layout key

KEY_DRAW_W_IN = 3.4         # FBD panels are drawn this wide, cropped to their ink, then fitted
KEY_PX_PER_IN = 300         # key_solution saves at 300 dpi
KEY_NOTE_SCALE = 0.75       # the note's handwriting is set at this fraction of full key size


def _crop_to_ink(png, pad=10):
    """Crop a key PNG to its ink plus `pad` px; return its size in inches at 300 dpi."""
    from PIL import Image, ImageChops
    im = Image.open(png).convert("RGB")
    bg = Image.new("RGB", im.size, im.getpixel((0, 0)))
    box = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 24 else 0).getbbox()
    if box:
        box = (max(0, box[0] - pad), max(0, box[1] - pad),
               min(im.width, box[2] + pad), min(im.height, box[3] + pad))
        im = im.crop(box)
    im.save(png)
    return im.width / KEY_PX_PER_IN, im.height / KEY_PX_PER_IN


def grid_panels(n, q):
    """Each object of an item's FBD drawn on its own, at one magnitude scale across the
    item, so a two-object item's arrows still compare (one panel per square). Returns
    [(png, w_in, h_in)], or None if the scene cannot model the item."""
    from key_solution import solution_image, SceneUnsupported, fbd_forces
    sc = q.get("keyImage")
    if not sc or sc.get("scene") != "fbd":
        return None
    try:
        panels = fbd_forces(sc)
    except SceneUnsupported as e:
        print(f"build_worksheet_key_docx: Q{n} key image not drawn ({e}); "
              "printing the typed solution instead.", file=sys.stderr)
        return None
    big = max(f["mag"] for p in panels for f in p["forces"])
    full = float(sc.get("arrowPx", 118))
    out = []
    for k, p in enumerate(panels):
        one = {key: v for key, v in p.items() if key != "caption"}
        one["scene"] = "fbd"
        one["arrowPx"] = full * max(f["mag"] for f in p["forces"]) / big
        png = os.path.join(_TMP, f"g{n}_{k}.png")
        solution_image({"prompt": q["prompt"] + (f" [{k}]" if k else ""), "keyImage": one},
                       png, width_in=KEY_DRAW_W_IN)
        out.append((png,) + _crop_to_ink(png))
    return out


def grid_note(n, q, width_in):
    """The item's steps as a short handwritten note under its square(s), or None."""
    if not q.get("steps"):
        return None
    from key_solution import draw_steps, Page, LOGICAL_PER_IN
    png = os.path.join(_TMP, f"g{n}_note.png")
    W = int(width_in / KEY_NOTE_SCALE * LOGICAL_PER_IN)
    # The steps wrap to the note's width, on a canvas a little wider: the handwriting face
    # can run a few px past its measured width, and a canvas cut at the wrap width clips
    # the last letter of a full line. The spare width is cropped off as white.
    pad = 40
    P = Page(W + pad, 1600, seed=hash(q.get("prompt", "")) % 1000)
    y = draw_steps(P, 14, 8, q["steps"], W - 28, 27)
    P.crop(y + 10)
    P.save(png=png)
    _crop_to_ink(png, pad=12)
    return png


def _pin_row(t, ri, height_in=None):
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    trPr = t.rows[ri]._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:cantSplit"))
    if height_in:
        e = OxmlElement("w:trHeight")
        e.set(qn("w:val"), str(int(height_in * 1440))); e.set(qn("w:hRule"), "exact")
        trPr.append(e)


def render_key_grid(doc, questions, pal, g):
    """The student grid, answered: each square carries its drawn FBD, one magnitude scale
    per item, and the item's note is written under its square(s). Every drawing on the
    key is set at one size, the largest that lets the biggest diagram fit its square."""
    from docx.shared import Pt
    from docx.enum.table import WD_ALIGN_VERTICAL
    S = g["square"]
    avail_w = S - 0.20
    avail_h = S - 0.30                     # the tier / caption line sits inside the top
    drawn = {n: grid_panels(n, q) for n, q in enumerate(questions, 1)}
    fits = [min(avail_w / w, avail_h / h) for ps in drawn.values() if ps for _, w, h in ps]
    scale = min([1.0] + fits)
    for gi, row in enumerate(grid_rows(questions, g["columns"])):
        if gi:
            gap(doc, g["rowGapPt"])
        outer, t = grid_table(doc, g, 3)
        _pin_row(t, 0); _pin_row(t, 1, S); _pin_row(t, 2)
        for n, q, col, span in row:
            last = col + span == g["columns"]
            end = (col + span - 1) * 2 + (0 if last else 1)
            right = 0 if last else GRID_PROMPT_GAP_TW
            head = t.rows[0].cells[col * 2]
            note = t.rows[2].cells[col * 2]
            if end > col * 2:
                head = head.merge(t.rows[0].cells[end])
                note = note.merge(t.rows[2].cells[end])
            head.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            # The prompt restated small and grey, as on the card key.
            grid_head(head, n, q, pal, prompt_pt=8.5, prompt_color=pal.label,
                      italic=True, right=right)
            caps = [p.get("caption") for p in (q.get("keyImage") or {}).get("panels", [])] \
                or (q.get("draw") or {}).get("captions") or []
            ps = drawn.get(n)
            for k in range(span):
                sq = t.rows[1].cells[(col + k) * 2]
                square(sq, pal, S, caps[k] if span > 1 and k < len(caps) else None,
                       q.get("tier") if k == 0 else None)
                if ps and k < len(ps):
                    png, w, h = ps[k]
                    pp = sq.add_paragraph()
                    pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    pp.paragraph_format.space_after = Pt(0)
                    pp.paragraph_format.space_before = Pt(max(0, (avail_h - h * scale) / 2 * 72))
                    pp.add_run().add_picture(png, width=Inches(w * scale))
            cell_margins(note, top=30, bottom=0, left=0, right=right)
            width = S * span + g["gutter"] * (span - 1) + (0 if last else g["gutter"]) \
                - right / 1440
            if not ps:
                # The drawing is the answer; with no drawing the typed solution goes here.
                para(note, str(q["solution"]), 9, color=pal.ink, first=True)
                continue
            png = grid_note(n, q, width)
            if png:
                from PIL import Image
                with Image.open(png) as im:      # cropped to ink, so set by scale, not width
                    w_in = im.width / KEY_PX_PER_IN * KEY_NOTE_SCALE
                note.paragraphs[0].add_run().add_picture(png, width=Inches(min(w_in, width)))
        from _shull_docx import unpad_cell
        unpad_cell(outer)
    return scale


def main():
    if len(sys.argv) < 2:
        return refuse("usage: build_worksheet_key_docx.py <spec.json> [out.docx]")
    spec = json.load(open(sys.argv[1]))
    course = spec["course"]
    if course not in COURSE_CODE:
        return refuse(f"unknown course {course!r}.")
    pal = Palette(course)
    sections = spec["sectionsContent"]

    valid = known_sections(course)
    bad = [s for s in spec["sections"] if s not in valid]
    if bad:
        return refuse(f"section(s) {', '.join(bad)} are not in courses/{course}/DECISIONS.md.")

    missing = []
    for sec in sections:
        for i, q in enumerate(sec.get("questions", []), start=1):
            if not q.get("solution"):
                missing.append(f"{sec['code']} Q{i}")
    if missing:
        return refuse("no \"solution\" field for: " + ", ".join(missing),
                       "A key that silently skips a question is worse than no key.")

    typed_div = [f"{sec['code']} Q{i}" for sec in sections
                 for i, q in enumerate(sec.get("questions", []), start=1)
                 if not q.get("steps") and "÷" in str(q.get("solution", ""))]
    if typed_div:
        print("build_worksheet_key_docx: WARNING typed solution uses ÷ (keys show division as a stacked "
              "fraction; add \"steps\"): " + ", ".join(typed_div), file=sys.stderr)

    code = COURSE_CODE[course]
    unit = f"U{int(spec['unit']):02d}"
    utitle = unit_title(course, spec["unit"])
    span = (f"S{spec['sections'][0]}-S{spec['sections'][-1]}"
            if len(spec["sections"]) > 1 else f"S{spec['sections'][0]}")
    kind = spec.get("docType", "Practice_Set")
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, document_name(
        kind, spec["sections"], spec["unit"], key=True,
        unit_title=short_title(course, f"U{spec['unit']}"),
        topic=short_title(course, spec["sections"][0])))

    doc = Document()
    s = page_setup(doc)

    for si, sec in enumerate(sections):
        if si:
            page_break(doc)

        t = doc.add_table(rows=1, cols=2)
        fix_widths(t, [5.55, 1.95])
        h, hr = t.rows[0].cells
        for cc in (h, hr):
            borders(cc, pal.hair, sz=4, edges=("top", "bottom"))
        borders(h, pal.display, sz=30, edges=("left",))
        cell_margins(h, top=80, bottom=80, left=160, right=80)
        cell_margins(hr, top=80, bottom=80, left=80, right=60)
        para(h, f"UNIT {int(spec['unit'])} — {utitle.upper()} · TEACHER KEY", 7.5,
             bold=True, color=pal.accent, caps_track=True, first=True)
        para(h, spec.get("key", {}).get("title", sec["title"]), 15, bold=True, color=pal.ink)
        pp = para(hr, f"{unit} / S{sec['code']}", 11, bold=True, color=pal.accent,
                  caps_track=True, first=True)
        pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        pp = para(hr, kind.replace("_", " ").upper() + "  ·  ANSWER KEY",
                  6.5, color=pal.label, caps_track=True)
        pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT

        gap(doc, 6)
        from key_solution import MotionArrowError
        g = grid_opts(spec, sec)
        if g:
            err = grid_check(sec.get("questions", []), g)
            if err:
                return refuse(f"section {sec['code']}: {err}")
            try:
                scale = render_key_grid(doc, sec.get("questions", []), pal, g)
            except MotionArrowError as e:
                return refuse(f"{sec['code']}: {e}")
            print(f"build_worksheet_key_docx: grid key drawings at {scale:.2f} of full size",
                  file=sys.stderr)
        for i, q in enumerate([] if g else sec.get("questions", []), start=1):
            try:
                answer_block(doc, i, q, pal)
            except MotionArrowError as e:
                return refuse(f"{sec['code']} Q{i}: {e}")
            gap(doc, 4)

        for block in spec.get("key", {}).get("blocks", []) if si == 0 else []:
            if block.get("gapBefore"):
                gap(doc, float(block["gapBefore"]))
            if block["kind"] == "table":
                table_block(doc, block, pal)
            elif block["kind"] == "notes":
                notes_block(doc, block, pal)
            else:
                return refuse(f"unknown key block kind {block['kind']!r}.")

    running_footer(s, f"SHULL SCIENCE          {unit} · {span} · KEY", pal,
                   with_page_numbers=True)
    trim_tail(doc)
    doc.save(out)
    nq = sum(len(x.get("questions", [])) for x in sections)
    print(f"wrote {out}  —  {code} {unit} {span} KEY, "
          f"{len(sections)} section(s), {nq} answer(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
