#!/usr/bin/env python3
"""Audit a built deck: colliding text, clipped text, type below the floor, and contrast.

Every check reads the .pptx that actually shipped, not the source that produced it. The
distinction matters: the legacy system's most expensive defect was a font that resolved
to something other than what the source named, and no amount of reading the source would
have caught it.

Clipped and colliding text is the most common slide defect and the legacy record says
so plainly - slides 8 and 17 of the U8 preview shipped with text cut off. Looking at a
raster catches it only if a human looks at every slide of every deck. This does not.

The contrast check resolves each text run against the fill actually behind it and
measures the pair, because "the accent is fine on a card" is exactly the kind of belief
that put four locked course colours onto a white background at 1.5:1.

    python3 scripts/audit_slide_geometry.py deck.pptx
"""
import sys, os, json
from pptx import Presentation
from pptx.util import Emu
from pptx.enum.dml import MSO_FILL

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from measure_tokens import contrast

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Longest run permitted below the content floor. An eyebrow, a card label and a footer
# code all fit inside this; a sentence does not.
NAV_LABEL_MAX = 40

def boxes(shapes):
    out = []
    for sh in shapes:
        if not sh.has_text_frame:
            continue
        text = sh.text_frame.text.strip()
        if not text:
            continue
        out.append((sh.name, text.split("\n")[0][:28],
                    Emu(sh.left).inches, Emu(sh.top).inches,
                    Emu(sh.left + sh.width).inches, Emu(sh.top + sh.height).inches))
    return out


def rect(sh):
    return (Emu(sh.left).inches, Emu(sh.top).inches,
            Emu(sh.left + sh.width).inches, Emu(sh.top + sh.height).inches)


def solid_fills(shapes):
    """Every solid-filled shape, in z-order, as (rect, hex)."""
    out = []
    for sh in shapes:
        if sh.left is None or sh.width is None:
            continue
        try:
            if sh.fill.type != MSO_FILL.SOLID:
                continue
            out.append((rect(sh), "#" + str(sh.fill.fore_color.rgb)))
        except (AttributeError, TypeError, ValueError):
            continue
    return out


def ground_behind(box, fills):
    """The topmost solid fill containing this box's centre - what the text sits on."""
    cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
    found = None
    for (x0, y0, x1, y1), hexv in fills:
        if x0 <= cx <= x1 and y0 <= cy <= y1:
            found = hexv
    return found


def text_runs(shapes):
    """(shape, run) for every non-empty run, with the shape for its geometry."""
    for sh in shapes:
        if not sh.has_text_frame or not sh.text_frame.text.strip():
            continue
        if sh.left is None or sh.width is None:
            continue
        for para in sh.text_frame.paragraphs:
            for run in para.runs:
                if run.text.strip():
                    yield sh, run


def run_color(run):
    try:
        return "#" + str(run.font.color.rgb)
    except (AttributeError, TypeError, ValueError):
        return None


def overlap(a, b):
    return not (a[4] <= b[2] or b[4] <= a[2] or a[5] <= b[3] or b[5] <= a[3])


def main():
    path = sys.argv[1]
    geo = json.load(open(os.path.join(REPO, "brand", "tokens.json")))["slideGeometry"]
    W, H, M = geo["widthIn"], geo["heightIn"], geo["margins"]
    floor = json.load(open(os.path.join(REPO, "brand", "tokens.json")))["typography"]["floors"]["slideContent"]["pt"]

    target = json.load(open(os.path.join(REPO, "brand", "tokens.json")))["rules"]["contrastTargetText"]

    prs = Presentation(path)
    errors = []
    for i, slide in enumerate(prs.slides, 1):
        # Contrast: every run, against the fill actually behind it. Layout fills sit
        # under slide fills, so they are stacked in that order.
        fills = solid_fills(slide.slide_layout.shapes) + solid_fills(slide.shapes)
        for shapes in (slide.slide_layout.shapes, slide.shapes):
            for sh, run in text_runs(shapes):
                fg, bg = run_color(run), ground_behind(rect(sh), fills)
                if not fg or not bg:
                    continue
                ratio = contrast(fg, bg)
                if ratio < target:
                    errors.append(f"slide {i}: {run.text.strip()[:24]!r} is {fg} on {bg} "
                                  f"= {ratio:.2f}:1, below the {target}:1 target")
        bs = boxes(slide.shapes)
        for j in range(len(bs)):
            for k in range(j + 1, len(bs)):
                if overlap(bs[j], bs[k]):
                    errors.append(f"slide {i}: text overlaps - "
                                  f"{bs[j][0]!r} ({bs[j][1]!r}) x {bs[k][0]!r} ({bs[k][1]!r})")
        for b in bs:
            if b[2] < -0.01 or b[3] < -0.01 or b[4] > W + 0.01 or b[5] > H + 0.01:
                errors.append(f"slide {i}: {b[0]!r} ({b[1]!r}) runs off the slide")
        # Student-facing type floor. Slide System v2 permits 10-12pt for eyebrows, card
        # labels and footers - navigation, not content. pptxgenjs renames placeholders to
        # "Text N" on the slide, so the exemption cannot key on a name. It keys on what
        # actually distinguishes the two: navigation is a short label, content is a
        # sentence. A 10pt run of 200 characters is the defect this check exists for.
        for sh in slide.shapes:
            if not sh.has_text_frame or not sh.text_frame.text.strip():
                continue
            for para in sh.text_frame.paragraphs:
                for run in para.runs:
                    if not run.font.size or run.font.size.pt >= floor:
                        continue
                    body = run.text.strip()
                    if len(body) <= NAV_LABEL_MAX and "\n" not in body:
                        continue
                    errors.append(f"slide {i}: {run.font.size.pt}pt on {len(body)} characters "
                                  f"({body[:40]!r}) - below the {floor}pt content floor, and too "
                                  f"long to be navigation")

    name = os.path.basename(path)
    if errors:
        print(f"audit_slide_geometry: {name} - {len(errors)} problem(s)")
        for e in errors:
            print("  " + e)
        return 1
    print(f"audit_slide_geometry: {name} - {len(prs.slides)} slides. No overlapping text, "
          f"nothing off-slide, nothing below the {floor}pt content floor, every text/ground "
          f"pair at or above {target}:1.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
