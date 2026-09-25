#!/usr/bin/env python3
"""Grow a flowed notes packet's writing space into the room its page breaks free up.

    python3 templates/notes/fit_notes.py specs/<spec>.json [--write]

SHULL-CHG-0026. "Use the space available - if you move a section to the next page,
just increase the size of the boxes to use the new space. Just make it flow."
                                                    - Matthew Shull, 2026-09-25

A spec with "flow": true breaks before every section and never splits a row, so pages
end short. This renders the student copy, measures how much room is left at the foot
of each page, and hands it back as extra ruled lines to the writing slots ON that page:
every label line ("Earth:", "Define half-life:"), the section summary, and the close.
It rebuilds and re-measures until nothing is left to give, and backs a page off if a
row it grew got pushed to the next one. Nothing is added to a page that did not have
the room, so the page count never moves.

Measured in LibreOffice. Word sets the same Archivo a touch tighter, so a page that
fits here fits there; SAFETY_PT is the margin for the difference.

--write puts the fitted line counts back into the spec, so the build is reproducible
from what is committed. Without it the spec is only reported on.
"""
import copy, json, os, subprocess, sys, tempfile
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import recall  # noqa: E402

RULE_PT = 19.0      # one ruled line: a 10pt body line plus its 6pt space-after, measured
SAFETY_PT = 16.0    # left empty at the foot of every page, for Word's reflow
FOOTER_GAP_PT = 8.0
MAX_PASSES = 8


def is_label(n):
    text = n if isinstance(n, str) else n.get("text", "")
    return not text.startswith(("*", "✎")) and text.rstrip().endswith(":")


def normalise(spec):
    """Every label line becomes a dict at its natural line count.

    The fitter owns these counts: it starts from the natural ones every run, so a
    refit after a content edit is the same as a first fit, not a fit on top of a fit.
    """
    for sec in spec["sectionsContent"]:
        sec["summaryLines"] = 4
        for row in sec["rows"]:
            row.pop("breakBefore", None)
            out = []
            for n in row["notes"]:
                if is_label(n):
                    n = {"text": n} if isinstance(n, str) else dict(n)
                    n["lines"] = recall.ruled_lines(n["text"])
                out.append(n)
            row["notes"] = out
    spec["close"]["bigPictureLines"] = 3
    spec["close"]["fuzzyLines"] = 3


def render(spec, work):
    sp, dx = os.path.join(work, "fit.json"), os.path.join(work, "fit.docx")
    json.dump(spec, open(sp, "w"), ensure_ascii=False)
    subprocess.run([sys.executable, os.path.join(HERE, "build_notes_docx.py"), sp, dx],
                   check=True, capture_output=True)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", work, dx],
                   check=True, capture_output=True)
    return pymupdf.open(os.path.join(work, "fit.pdf"))


def measure(doc, spec):
    """Per page: remaining room in points, and which slots live there."""
    cue_order = [(si, ri, row["cueLabel"]) for si, sec in enumerate(spec["sectionsContent"])
                 for ri, row in enumerate(sec["rows"])]
    want, n_sum = 0, 0
    pages = []
    for pno, page in enumerate(doc):
        spans = [s for b in page.get_text("dict")["blocks"] for l in b.get("lines", [])
                 for s in l["spans"] if s["text"].strip()]
        foot = min((s["bbox"][1] for s in spans
                    if s["text"].startswith("SHULL SCIENCE") and s["size"] < 8
                    and s["bbox"][1] > page.rect.height * 0.85), default=page.rect.height - 40)
        ys = [s["bbox"][3] for s in spans if s["bbox"][3] < foot - 1]
        ys += [d["rect"].y1 for d in page.get_drawings() if d["rect"].y1 < foot - 1]
        info = {"room": (foot - FOOTER_GAP_PT) - max(ys, default=0), "rows": [],
                "summaries": [], "close": False}
        for s in sorted(spans, key=lambda s: (s["bbox"][1], s["bbox"][0])):
            t, flat = s["text"].strip(), s["text"].replace(" ", "")
            if want < len(cue_order) and t == cue_order[want][2]:
                info["rows"].append(cue_order[want][:2]); want += 1
            elif flat.startswith("SECTIONSUMMARY"):
                info["summaries"].append(n_sum); n_sum += 1
            elif flat.startswith("UNITBIGPICTURE"):
                info["close"] = True
        pages.append(info)
    return pages


def slots(spec, info):
    """Everything on one page that can take another ruled line, row by row."""
    out = []
    for si, ri in info["rows"]:
        for n in spec["sectionsContent"][si]["rows"][ri]["notes"]:
            if isinstance(n, dict) and "lines" in n:
                out.append(n)
    for si in info["summaries"]:
        out.append(("summary", si))
    if info["close"]:
        out += [("close", "bigPictureLines"), ("close", "fuzzyLines")]
    return out


def bump(spec, slot, by):
    if isinstance(slot, dict):
        slot["lines"] += by
    elif slot[0] == "summary":
        spec["sectionsContent"][slot[1]]["summaryLines"] += by
    else:
        spec["close"][slot[1]] += by


def placement(pages):
    return [tuple(p["rows"]) for p in pages], [tuple(p["summaries"]) for p in pages]


def main():
    args = [a for a in sys.argv[1:] if a != "--write"]
    path = args[0]
    spec = json.load(open(path))
    if not spec.get("flow"):
        print("fit_notes: spec has no \"flow\": true - nothing is page-broken, so there is "
              "no freed space to fit.", file=sys.stderr)
        return 1
    normalise(spec)
    with tempfile.TemporaryDirectory() as work:
        pages = measure(render(spec, work), spec)
        # A summary box alone on a page has been cut off from its notes. Send the
        # section's last row over with it - and if that row is already travelling,
        # the one before it - until every summary shares a page with a row.
        for _ in range(MAX_PASSES):
            orphans = [si for p in pages if not p["rows"] for si in p["summaries"]]
            if not orphans:
                break
            for si in orphans:
                rows = spec["sectionsContent"][si]["rows"]
                marked = [i for i, r in enumerate(rows) if r.get("breakBefore")]
                i = (min(marked) - 1) if marked else len(rows) - 1
                if i > 0:
                    rows[i]["breakBefore"] = True
            pages = measure(render(spec, work), spec)
        home = placement(pages)
        n_pages = len(pages)
        safety = SAFETY_PT
        for _ in range(MAX_PASSES):
            before = copy.deepcopy(spec)
            grew = False
            for info in pages:
                s = slots(spec, info)
                extra = int((info["room"] - safety) // RULE_PT)
                if not s or extra <= 0:
                    continue
                for i in range(extra):
                    bump(spec, s[i % len(s)], 1)
                grew = True
            if not grew:
                break
            new = measure(render(spec, work), spec)
            if len(new) != n_pages or placement(new) != home:
                # Something got pushed: back out this pass and ask for a line less.
                spec = before
                safety += RULE_PT
                continue
            pages = new
        final = measure(render(spec, work), spec)
    for i, p in enumerate(final, 1):
        print(f"   p{i}: {p['room']:5.0f}pt left")
    if "--write" in sys.argv[1:]:
        json.dump(spec, open(path, "w"), indent=2, ensure_ascii=False)
        print(f"fit_notes: wrote fitted line counts to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
