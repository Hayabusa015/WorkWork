#!/usr/bin/env python3
"""Build the printable handwriting-capture sheet and its layout manifest.

    python3 scripts/build_handwriting_sheet.py --out-dir /path/to/dir

Writes handwriting_sheet.pdf (three letter-size pages) and handwriting_sheet.json (where every
box sits, in inches, plus the character it is for). The second file is what lets a later step cut
a scan back into single characters without guessing.

The guide lines are a pale blue that a scan filter can drop out; the corner squares let a
skewed photo be straightened. Text colours come from brand/tokens.json; the guide colours are
named CSS colours because they are a scan aid, not a brand colour.
"""
import argparse, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import science_tools as st

COLS, ROWS = 6, 8
PER_PAGE = COLS * ROWS
BOX_W, BOX_H, LABEL_H = 1.25, 1.10, 0.20
GRID_X, GRID_Y = 0.50, 1.55
REG = 0.22                                   # corner square, inches
REG_AT = [(0.25, 0.25), (8.03, 0.25), (0.25, 10.53), (8.03, 10.53)]


def characters():
    out = []
    out += [(c, f"capital {c}") for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    out += [(c, f"small {c}") for c in "abcdefghijklmnopqrstuvwxyz"]
    out += [(c, f"digit {c}") for c in "0123456789"]
    out += [(c, f"digit {c} (again)") for c in "0123456789"]
    sym = [("+", "plus"), ("−", "minus"), ("=", "equals"), ("×", "times"), ("(", "open paren"),
           (")", "close paren"), ("[", "open bracket"), ("]", "close bracket"), (".", "period"),
           (",", "comma"), (":", "colon"), (";", "semicolon"), ("/", "slash"), ("%", "percent"),
           ("°", "degree"), ("?", "question"), ("!", "exclaim"), ("'", "apostrophe"),
           ('"', "quote"), ("<", "less than"), (">", "greater than"), ("·", "centered dot"),
           ("±", "plus-minus"), ("-", "hyphen")]
    out += sym
    greek = [("Δ", "delta"), ("μ", "mu"), ("Ω", "omega cap"), ("λ", "lambda"), ("π", "pi"),
             ("θ", "theta"), ("α", "alpha"), ("β", "beta"), ("ρ", "rho"), ("σ", "sigma"), ("τ", "tau")]
    out += greek
    out += [("→", "arrow right"), ("⇌", "equilibrium"), ("←", "arrow left"), ("↑", "arrow up"), ("↓", "arrow down")]
    out += [(c, f"small {c} (again)") for c in "abcdefghijklmnopqrstuvwxyz"]
    return out


def layout():
    chars = characters()
    pages = [chars[i:i + PER_PAGE] for i in range(0, len(chars), PER_PAGE)]
    manifest = {"page_in": [8.5, 11.0], "reg_squares_in": [[x, y, REG, REG] for x, y in REG_AT],
                "box": {"w": BOX_W, "h": BOX_H, "label_h": LABEL_H}, "pages": []}
    for pi, page in enumerate(pages, 1):
        boxes = []
        for i, (ch, name) in enumerate(page):
            r, c = divmod(i, COLS)
            x, y = GRID_X + c * BOX_W, GRID_Y + r * BOX_H
            wx, wy, wh = x, y + LABEL_H, BOX_H - LABEL_H            # writing area
            boxes.append({"char": ch, "name": name, "box": [x, y, BOX_W, BOX_H],
                          "write": [wx, wy, BOX_W, wh],
                          "baseline_y": wy + 0.62 * wh, "capline_y": wy + 0.14 * wh})
        manifest["pages"].append({"n": pi, "of": len(pages), "boxes": boxes})
    return manifest


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def html(manifest):
    pal = st.palette("chemistry")
    fonts = os.path.join(st.REPO, "brand", "fonts")
    css = f"""
@font-face {{ font-family: Archivo; src: url('file://{fonts}/Archivo-Regular.ttf'); font-weight: 400; }}
@font-face {{ font-family: Archivo; src: url('file://{fonts}/Archivo-Bold.ttf'); font-weight: 700; }}
@page {{ size: 8.5in 11in; margin: 0; }}
html, body {{ margin: 0; padding: 0; }}
.page {{ position: relative; width: 8.5in; height: 11in; page-break-after: always; overflow: hidden;
        font-family: Archivo, sans-serif; color: {pal['asphalt']}; }}
.reg {{ position: absolute; width: {REG}in; height: {REG}in; background: black; }}
.h1 {{ position: absolute; left: 0.5in; top: 0.5in; font-size: 17pt; font-weight: 700; }}
.how {{ position: absolute; left: 0.5in; top: 0.86in; width: 7.5in; font-size: 8.6pt; line-height: 1.32; }}
.box {{ position: absolute; box-sizing: border-box; border: 0.6pt solid lightsteelblue; }}
.lab {{ position: absolute; left: 0.05in; top: 0.02in; font-size: 7pt; color: gray; }}
.lab b {{ font-size: 9pt; color: dimgray; margin-right: 0.04in; }}
.base {{ position: absolute; left: 0; right: 0; border-top: 0.8pt solid lightsteelblue; }}
.cap {{ position: absolute; left: 0; right: 0; border-top: 0.5pt dashed lightsteelblue; }}
.pg {{ position: absolute; right: 0.5in; top: 0.54in; font-size: 9pt; color: gray; }}
"""
    out = [f"<html><head><meta charset='utf-8'><style>{css}</style></head><body>"]
    for pg in manifest["pages"]:
        out.append("<div class='page'>")
        for x, y, w, h in manifest["reg_squares_in"]:
            out.append(f"<div class='reg' style='left:{x}in;top:{y}in'></div>")
        out.append("<div class='h1'>Handwriting font sheet</div>")
        out.append(f"<div class='pg'>Page {pg['n']} of {pg['of']}</div>")
        out.append("<div class='how'>Write each character <b>once</b> in its box, sitting on the solid blue line, "
                   "in <b>dark pen or a dark soft pencil</b> (2B or softer), at the size you would write on an answer key. "
                   "Write naturally. Do not trace and do not touch the box edges. Letters with tails "
                   "(g j p q y) hang below the line. Where a box says &ldquo;again,&rdquo; write it a second time "
                   "the way it comes out naturally, not copied from the first. Keep the four black corner squares "
                   "clear. Scan flat at 300 dpi, or photograph straight down in even light with no shadows.</div>")
        for b in pg["boxes"]:
            x, y, w, h = b["box"]
            wx, wy, ww, wh = b["write"]
            bl = b["baseline_y"] - y
            cl = b["capline_y"] - y
            out.append(f"<div class='box' style='left:{x}in;top:{y}in;width:{w}in;height:{h}in'>"
                       f"<div class='lab'><b>{esc(b['char'])}</b>{esc(b['name'])}</div>"
                       f"<div class='cap' style='top:{cl}in'></div><div class='base' style='top:{bl}in'></div></div>")
        out.append("</div>")
    out.append("</body></html>")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True)
    a = ap.parse_args()
    from weasyprint import HTML
    os.makedirs(a.out_dir, exist_ok=True)
    m = layout()
    pdf = os.path.join(a.out_dir, "handwriting_sheet.pdf")
    HTML(string=html(m)).write_pdf(pdf)
    with open(os.path.join(a.out_dir, "handwriting_sheet.json"), "w") as fh:
        json.dump(m, fh, ensure_ascii=False, indent=1)
    n = sum(len(p["boxes"]) for p in m["pages"])
    print(f"wrote {pdf}  ({len(m['pages'])} pages, {n} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
