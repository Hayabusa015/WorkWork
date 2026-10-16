#!/usr/bin/env python3
"""Draw a labelled molecular-structure figure from a SMILES string.

The structure comes from the SMILES, and the formula and molar mass printed under it
come from the same molecule, so the picture cannot disagree with its label. The name
is typed by you and is not checked. Verify the SMILES against the source before
use (verify-content); this script makes a wrong structure impossible to draw
by accident, not impossible to ask for.

Colours come from brand/tokens.json and type from the shipped Archivo files, the same
as build_diagram_nuclear_notation.py.

    python3 scripts/build_diagram_molecule.py --smiles "CC(=O)O" --name "acetic acid" \\
        --course chemistry --out /path/to/figure.png
"""
import argparse, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import science_tools as st

SCALE = 4               # drawn large, placed small - stays crisp on a projector
W, H = 900, 640         # logical px, before SCALE


def formula_runs(formula):
    """Split 'C2H4O2' into [('C', False), ('2', True), ...]; True marks a subscript digit."""
    return [(tok, tok.isdigit()) for tok in re.findall(r"\d+|[A-Z][a-z]?", formula)]


def draw_formula(draw, cx, y, formula, fonts, fill):
    """Centre a formula at cx, with digits as true subscripts."""
    big, small = fonts
    runs = formula_runs(formula)
    widths = [draw.textlength(t, font=small if sub else big) for t, sub in runs]
    x = cx - sum(widths) / 2
    for (t, sub), w in zip(runs, widths):
        if sub:
            draw.text((x, y + 14 * SCALE), t, font=small, fill=fill)
        else:
            draw.text((x, y), t, font=big, fill=fill)
        x += w


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--smiles", required=True)
    ap.add_argument("--name", required=True, help="label shown above the structure")
    ap.add_argument("--course", default="chemistry", choices=["chemistry", "physics", "geology"])
    ap.add_argument("--out", required=True, help="output .png path")
    ap.add_argument("--no-mass", action="store_true", help="omit the molar mass line")
    a = ap.parse_args()

    st.require("rdkit")
    from rdkit import Chem
    from rdkit.Chem import Descriptors, rdMolDescriptors
    from rdkit.Chem.Draw import rdMolDraw2D
    from PIL import Image, ImageDraw, ImageFont
    import io

    mol = Chem.MolFromSmiles(a.smiles)
    if mol is None:
        sys.exit(f"RDKit could not parse SMILES: {a.smiles!r}")

    pal = st.palette(a.course)
    formula = rdMolDescriptors.CalcMolFormula(mol)
    mass = Descriptors.MolWt(mol)

    # Structure panel: asphalt bonds and carbons, course accent on heteroatoms,
    # so the eye finds the functional group.
    sw, sh = W * SCALE, 400 * SCALE
    drawer = rdMolDraw2D.MolDraw2DCairo(sw, sh)
    o = drawer.drawOptions()
    o.setBackgroundColour(tuple(c / 255 for c in st.hex_to_rgb(pal["white"])))
    o.bondLineWidth = 2 * SCALE
    o.padding = 0.04
    o.setAtomPalette({0: tuple(c / 255 for c in st.hex_to_rgb(pal["asphalt"]))})
    for z in (7, 8, 9, 15, 16, 17, 35, 53):
        o.updateAtomPalette({z: tuple(c / 255 for c in st.hex_to_rgb(pal["accent"]))})
    o.updateAtomPalette({6: tuple(c / 255 for c in st.hex_to_rgb(pal["asphalt"]))})
    o.updateAtomPalette({1: tuple(c / 255 for c in st.hex_to_rgb(pal["asphalt"]))})
    o.fixedFontSize = 34 * SCALE
    fp = st.font_path("Archivo-SemiBold.ttf")
    if os.path.exists(fp):
        o.fontFile = fp
    drawer.DrawMolecule(mol)
    drawer.FinishDrawing()
    struct = Image.open(io.BytesIO(drawer.GetDrawingText())).convert("RGB")

    im = Image.new("RGB", (W * SCALE, H * SCALE), pal["white"])
    d = ImageDraw.Draw(im)
    f_name = ImageFont.truetype(st.font_path("Archivo-Bold.ttf"), 46 * SCALE)
    f_for = ImageFont.truetype(st.font_path("Archivo-Bold.ttf"), 52 * SCALE)
    f_sub = ImageFont.truetype(st.font_path("Archivo-Bold.ttf"), 34 * SCALE)
    f_lab = ImageFont.truetype(st.font_path("Archivo-SemiBold.ttf"), 22 * SCALE)

    cx = W * SCALE // 2
    d.text((cx, 34 * SCALE), a.name, font=f_name, fill=pal["asphalt"], anchor="ma")
    im.paste(struct, (0, 100 * SCALE))
    ry = 505 * SCALE
    d.line([(140 * SCALE, ry), ((W - 140) * SCALE, ry)], fill=pal["graphite"], width=1 * SCALE)
    draw_formula(d, cx, ry + 18 * SCALE, formula, (f_for, f_sub), pal["asphalt"])
    if not a.no_mass:
        d.text((cx, ry + 90 * SCALE), f"{mass:.2f} g/mol", font=f_lab,
               fill=pal["accent"], anchor="ma")

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    im.save(a.out)
    print(f"wrote {a.out}  {im.width}x{im.height}  {formula}  {mass:.3f} g/mol")
    return 0


if __name__ == "__main__":
    sys.exit(main())
