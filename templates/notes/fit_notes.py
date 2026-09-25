#!/usr/bin/env python3
"""Give a flowed notes packet's leftover page room back as writing space - modestly.

    python3 templates/notes/fit_notes.py specs/<spec>.json [--write]

SHULL-CHG-0026. Matthew, 2026-09-25, in order:
    "use the space available ... just increase the size of the boxes"
    "well shit theres way too much spacing now"
    "keep each section together, if a section ends just head to a new page!"

With "flow": true each section starts a page and runs down it continuously - a row may
break between prompts, never through one - so the only room left is at the end of each
section's last page, and on the close's page. This renders the student copy, measures
that room, and hands it back: one more line for every prompt in the section if there is
room for all of them (never some and not others), then the rest to the section summary,
up to a cap. Anything past the cap stays white. It re-renders and backs off if anything
moved to another page, so the page count never changes.

Every box starts at least as tall as its answer - the key writes the answer on the same
lines, and a student needs at least that much room.

--write puts the fitted counts back into the spec, so the build is reproducible from
what is committed. The fitter owns lines / summaryLines / bigPictureLines / fuzzyLines
and resets them every run: refit after any content edit.
"""
import copy, json, os, subprocess, sys, tempfile
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import recall  # noqa: E402
sys.path.insert(0, os.path.dirname(HERE))
from _shull_docx import wrap_to  # noqa: E402
from build_notes_docx import NOTES_INNER_IN  # noqa: E402

RULE_PT = 20.0      # one ruled line: 14pt exact + 5pt after + the 1pt spacer (rule_lines)
SAFETY_PT = 16.0    # left empty at the foot of every page, for Word's reflow of labels
FOOTER_GAP_PT = 8.0
MAX_PASSES = 8
# Growth over natural. "Way too much spacing" came from boxes grown 4-6 lines each.
CAP = {"label": 1, "summary": 6, "close": 4}
NATURAL = {"summary": 4, "close": 3}


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
        sec.pop("breakBefore", None)
        for row in sec["rows"]:
            row.pop("breakBefore", None)
            out = []
            for n in row["notes"]:
                if is_label(n):
                    n = {"text": n} if isinstance(n, str) else dict(n)
                    # A box is never smaller than its answer: the key writes the answer
                    # on these same lines, and a student needs at least that many.
                    need = len(wrap_to(n.get("key", ""), NOTES_INNER_IN - 0.05, 9.5, True))
                    n["lines"] = n["natural"] = max(recall.ruled_lines(n["text"]), need)
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
    titles = [sec["title"] for sec in spec["sectionsContent"]]
    want, n_sum, n_title = 0, 0, 0
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
                "summaries": [], "titles": [], "close": False}
        for s in sorted(spans, key=lambda s: (s["bbox"][1], s["bbox"][0])):
            t, flat = s["text"].strip(), s["text"].replace(" ", "")
            if n_title < len(titles) and t == titles[n_title] and s["size"] > 11:
                info["titles"].append(n_title); n_title += 1
            elif want < len(cue_order) and t == cue_order[want][2]:
                info["rows"].append(cue_order[want][:2]); want += 1
            elif flat.startswith("SECTIONSUMMARY"):
                info["summaries"].append(n_sum); n_sum += 1
            elif flat.startswith("UNITBIGPICTURE"):
                info["close"] = True
        pages.append(info)
    return pages


def section_ends(pages):
    """Section index -> the page its summary box sits on: where the section ends."""
    return {si: pno for pno, p in enumerate(pages) for si in p["summaries"]}


def grow(spec, pages, safety):
    """One pass of handing room back. Returns True if anything grew."""
    grew = False
    ends = section_ends(pages)
    for si, sec in enumerate(spec["sectionsContent"]):
        if si not in ends:
            continue
        extra = int((pages[ends[si]]["room"] - safety) // RULE_PT)
        labels = [n for row in sec["rows"] for n in row["notes"]
                  if isinstance(n, dict) and "lines" in n
                  and n["lines"] < n["natural"] + CAP["label"]]
        # Every prompt in the section gets its line, or none does - uneven boxes read
        # as a mistake.
        if labels and extra >= len(labels):
            for n in labels:
                n["lines"] += 1
            extra -= len(labels); grew = True
        add = max(0, min(extra, NATURAL["summary"] + CAP["summary"] - sec["summaryLines"]))
        if add:
            sec["summaryLines"] += add; grew = True
    for p in pages:
        if p["close"]:
            extra = int((p["room"] - safety) // RULE_PT)
            for k in ("bigPictureLines", "fuzzyLines") * max(0, extra):
                if extra <= 0:
                    break
                if spec["close"][k] < NATURAL["close"] + CAP["close"]:
                    spec["close"][k] += 1; extra -= 1; grew = True
    return grew


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
        home, n_pages = section_ends(pages), len(pages)
        safety = SAFETY_PT
        for _ in range(MAX_PASSES):
            before = copy.deepcopy(spec)
            if not grow(spec, pages, safety):
                break
            new = measure(render(spec, work), spec)
            if len(new) != n_pages or section_ends(new) != home:
                # Something moved to another page: back out, ask for a line less.
                spec = before
                safety += RULE_PT
                continue
            pages = new
        final = measure(render(spec, work), spec)
    lonely = [si for p in final if not p["rows"] for si in p["summaries"]]
    for i, p in enumerate(final, 1):
        print(f"   p{i}: {p['room']:5.0f}pt left")
    if lonely:
        print(f"fit_notes: summary box alone on a page for section(s) {lonely} - "
              f"look at it.", file=sys.stderr)
    if "--write" in sys.argv[1:]:
        for sec in spec["sectionsContent"]:
            for row in sec["rows"]:
                for n in row["notes"]:
                    if isinstance(n, dict):
                        n.pop("natural", None)
        json.dump(spec, open(path, "w"), indent=2, ensure_ascii=False)
        print(f"fit_notes: wrote fitted line counts to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
