"""Slide 12's "Drawing Lewis Structures" flowchart, rebuilt for the U4-U5 guided notes.

    python3 templates/notes/specs/make_chem_u04-u05_flowchart.py

Writes two PNGs into templates/notes/assets/chem_u04-u05_key/:
  s12_flow_student.png  step names printed, the slide's text left as ruled lines to fill in
  s12_flow_key.png      the slide's text, word for word

Same layout as the slide (Matt, 2026-11-05: "create the flow chart on the slide"):
Count -> Connect -> Fill -> Check; No loops to "Fix, then check again", Yes goes to Done.
Ink only, Archivo from brand/fonts, hairline boxes, so it prints like the rest of the page.
"""
import json, os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
OUT = os.path.join(REPO, "templates", "notes", "assets", "chem_u04-u05_key")
TOK = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
G = TOK["ground"]
INK, LABEL, HAIR = G["asphalt"]["hex"], G["label"]["hex"], G["ruleHairline"]["hex"]
ACCENT = TOK["courses"]["chemistry"]["primaryDeep"]["hex"]

DPI, W_IN, H_IN = 300, 6.0, 2.95
px = lambda inch: int(round(inch * DPI))
font = lambda w, pt: ImageFont.truetype(os.path.join(REPO, "brand", "fonts", f"Archivo-{w}.ttf"),
                                        int(round(pt / 72 * DPI)))
TITLE, BODY, SMALL = font("Bold", 10), font("Regular", 8.5), font("Bold", 8.5)

# Each step: title, then the slide's lines (key) / that many ruled lines (student).
STEPS = [
    ("1  Count", ["Add valence electrons.", "− charge: add electrons", "+ charge: subtract electrons"]),
    ("2  Connect", ["Center: usually lowest EN.", "Never put H in the center.", "Add single bonds."]),
    ("3  Fill", ["Fill outer atoms first.", "H: 2; usually 8 for others.", "Put leftovers on the center."]),
]
FIX = ("Fix, then check again", ["Recount electrons. Check octet exceptions.",
                                 "If needed, turn lone pairs into double or triple bonds."])
CHECK = ("4  Check", "Total and shells correct?")


def draw(key):
    im = Image.new("RGB", (px(W_IN), px(H_IN)), "white")
    d = ImageDraw.Draw(im)
    lw = max(2, px(0.008))

    def arrow(x0, y0, x1, y1):
        d.line([(px(x0), px(y0)), (px(x1), px(y1))], fill=LABEL, width=lw)
        dx, dy = x1 - x0, y1 - y0
        L = (dx * dx + dy * dy) ** 0.5
        ux, uy = dx / L, dy / L
        a, b = 0.07, 0.04
        d.polygon([(px(x1), px(y1)), (px(x1 - ux * a - uy * b), px(y1 - uy * a + ux * b)),
                   (px(x1 - ux * a + uy * b), px(y1 - uy * a - ux * b))], fill=LABEL)

    def card(x, y, w, h, title, lines):
        d.rectangle([px(x), px(y), px(x + w), px(y + h)], outline=LABEL, width=lw)
        d.text((px(x + 0.08), px(y + 0.06)), title, font=TITLE, fill=ACCENT)
        ly = y + 0.34
        for ln in lines:
            if key:
                d.text((px(x + 0.08), px(ly - 0.02)), ln, font=BODY, fill=INK)
                ly += 0.17
            else:
                ly += 0.2
                d.line([(px(x + 0.08), px(ly)), (px(x + w - 0.08), px(ly))], fill=HAIR, width=lw)

    bw, gap, top, bh = 1.78, 0.33, 0.05, 1.12
    for i, (t, ls) in enumerate(STEPS):
        x = i * (bw + gap)
        card(x, top, bw, bh, t, ls)
        if i < 2:
            arrow(x + bw + 0.04, top + bh / 2, x + bw + gap - 0.04, top + bh / 2)
    # Check diamond under Fill
    cx, cy, rw, rh = 2 * (bw + gap) + bw / 2, 1.78, 0.86, 0.42
    d.polygon([(px(cx), px(cy - rh)), (px(cx + rw), px(cy)), (px(cx), px(cy + rh)), (px(cx - rw), px(cy))],
              outline=LABEL, width=lw)
    arrow(cx, top + bh + 0.03, cx, cy - rh - 0.03)
    t, q = CHECK
    tw = d.textlength(t, font=TITLE)
    d.text((px(cx) - tw / 2, px(cy - 0.27)), t, font=TITLE, fill=ACCENT)
    if key:
        qw = d.textlength(q, font=BODY)
        d.text((px(cx) - qw / 2, px(cy - 0.02)), q, font=BODY, fill=INK)
    else:
        cw = d.textlength("correct?", font=BODY)
        d.line([(px(cx - 0.62), px(cy + 0.1)), (px(cx + 0.05), px(cy + 0.1))], fill=HAIR, width=lw)
        d.text((px(cx + 0.1), px(cy - 0.04)), "correct?", font=BODY, fill=INK)
    # No -> Fix (left)
    fx, fw, fy, fh = 0.0, 3.45, 1.42, 0.78
    card(fx, fy, fw, fh, *FIX)
    arrow(cx - rw - 0.03, cy, fx + fw + 0.04, cy)
    d.text((px((cx - rw + fx + fw) / 2 - 0.08), px(cy - 0.22)), "No", font=SMALL, fill=INK)
    # Fix loops back up to Check (the slide's "check again")
    # Yes -> Done (below)
    dy0 = cy + rh + 0.03
    arrow(cx, dy0, cx, H_IN - 0.33)
    d.text((px(cx + 0.08), px(dy0 + 0.02)), "Yes", font=SMALL, fill=INK)
    d.rectangle([px(cx - 0.45), px(H_IN - 0.31), px(cx + 0.45), px(H_IN - 0.03)], outline=LABEL, width=lw)
    dw = d.textlength("Done", font=TITLE)
    d.text((px(cx) - dw / 2, px(H_IN - 0.27)), "Done", font=TITLE, fill=ACCENT)
    return im


os.makedirs(OUT, exist_ok=True)
for key, name in ((False, "s12_flow_student.png"), (True, "s12_flow_key.png")):
    draw(key).save(os.path.join(OUT, name), dpi=(DPI, DPI))
print("wrote s12_flow_student.png and s12_flow_key.png")
