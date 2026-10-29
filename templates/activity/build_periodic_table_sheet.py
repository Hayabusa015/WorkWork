#!/usr/bin/env python3
"""Build the CHEM U03 coloring periodic table: a one-page landscape study sheet, plus its key.

    python3 templates/activity/build_periodic_table_sheet.py OUTDIR

Student sheet: a correct, full-size periodic table to color by family, a ten-family color
key along the bottom, two large trend arrows to label, and a trend chart in the empty space
above the transition metals (electronegativity, ionization energy, atomic radius, melting
point, boiling point). Uncolored and unfilled: the students do both.

Key: the family of every element, and the trend chart filled in.

The page is HTML rendered by WeasyPrint, so every cell lands where it is placed; a Word
table would reflow 118 cells. Element data lives in specs/periodic_table_elements.json and
nowhere else. Colour comes from brand/tokens.json; type is the shipped Archivo files.
"""
import html, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))
from _shull_name import document_name   # noqa: E402

T = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
G, ACC = T["ground"], T["courses"]["chemistry"]
INK, LABEL, HAIR, STRUCT = G["asphalt"]["hex"], G["label"]["hex"], G["ruleHairline"]["hex"], G["graphite"]["hex"]
ACCENT, FOOTER = ACC["primaryDeep"]["hex"], G["footer"]["hex"]
FONTS = os.path.join(REPO, "brand", "fonts")
DATA = json.load(open(os.path.join(HERE, "specs", "periodic_table_elements.json")))

CODE = "U03 / S3.1–S3.6"
FAMILIES = [("alkali", "Alkali metals"), ("alkaline-earth", "Alkaline earth metals"),
            ("transition", "Transition metals"), ("other-metal", "Other metals"),
            ("metalloid", "Metalloids"), ("nonmetal", "Nonmetals"), ("halogen", "Halogens"),
            ("noble-gas", "Noble gases"), ("lanthanide", "Lanthanides"), ("actinide", "Actinides")]
TRENDS = ["Electronegativity", "Ionization energy", "Atomic radius", "Melting point", "Boiling point"]
ANSWERS = {   # (across a period, down a group) - the key only
    "Electronegativity": ("Increases →", "Decreases ↓"),
    "Ionization energy": ("Increases →", "Decreases ↓"),
    "Atomic radius": ("Decreases →", "Increases ↓"),
    "Melting point": ("Peaks at group 14, then falls", "Varies by group"),
    "Boiling point": ("Peaks at group 14, then falls", "Varies by group"),
}

# ---- page geometry, inches. Landscape letter; every number below is placed, not flowed.
PW, PH = 11.0, 8.5
ML, MT = 0.35, 0.30
LEFT_BAND = 0.62                     # period numbers + the down arrow
CW = round((PW - 2 * ML - LEFT_BAND) / 18, 4)
CH = 0.665
TITLE_H, ARROW_H, GROUP_H, FGAP = 0.40, 0.40, 0.17, 0.14
X0 = ML + LEFT_BAND
Y0 = MT + TITLE_H + ARROW_H + GROUP_H


def face(name, file, weight=400, style="normal", stretch="normal"):
    return (f"@font-face {{ font-family: '{name}'; src: url('file://{os.path.join(FONTS, file)}'); "
            f"font-weight: {weight}; font-style: {style}; }}")


CSS = f"""
{face('Archivo', 'Archivo-Regular.ttf')}
{face('Archivo', 'Archivo-SemiBold.ttf', 600)}
{face('Archivo', 'Archivo-Bold.ttf', 700)}
{face('Archivo', 'Archivo-Italic[wdth,wght].ttf', 400, 'italic')}
{face('Archivo Narrow', 'ArchivoNarrow[wght].ttf')}
@page {{ size: {PW}in {PH}in; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'Archivo'; color: {INK}; }}
.abs {{ position: absolute; }}
.cell {{ position: absolute; width: {CW}in; height: {CH}in; border: 0.75pt solid {STRUCT};
         padding: 0.025in 0.03in 0 0.03in; overflow: hidden; }}
.top {{ display: flex; justify-content: space-between; font-family: 'Archivo Narrow'; font-size: 8pt;
        line-height: 1; }}
.z {{ font-family: 'Archivo'; font-weight: 600; }}
.sym {{ font-weight: 700; font-size: 15pt; line-height: 1; text-align: center; margin-top: 0.02in; }}
.name {{ font-family: 'Archivo Narrow'; font-size: 8pt; line-height: 1.0; text-align: center;
         margin-top: 0.015in; hyphens: manual; }}
.lab {{ font-size: 8pt; font-weight: 600; color: {LABEL}; letter-spacing: 0.04em; }}
.num {{ font-size: 8pt; font-weight: 600; color: {LABEL}; text-align: center; }}
.place {{ font-family: 'Archivo Narrow'; font-size: 8pt; text-align: center; color: {LABEL};
          padding-top: 0.2in; }}
table.trend {{ border-collapse: collapse; width: 100%; height: 100%; }}
table.trend th {{ font-size: 8pt; font-weight: 600; color: {LABEL}; letter-spacing: 0.04em; text-align: left;
                  padding: 0.03in 0.06in; border-bottom: 1pt solid {INK}; }}
table.trend td {{ font-size: 9pt; padding: 0.02in 0.06in; border-bottom: 0.5pt solid {HAIR};
                  height: {(3 * CH - 0.12 - 0.40) / 5:.3f}in; vertical-align: middle; }}
table.trend td.t {{ font-weight: 600; width: 1.45in; }}
td.ans {{ color: {ACCENT}; font-weight: 700; font-size: 8.5pt; }}
.line {{ border-bottom: 0.75pt solid {STRUCT}; }}
"""


def esc(s):
    return html.escape(str(s))


def name_html(name):
    # Long names wrap at a syllable break rather than at the cell edge.
    breaks = {"Rutherfordium": "Ruther&shy;fordium", "Praseodymium": "Praseo&shy;dymium",
              "Protactinium": "Protac&shy;tinium", "Mendelevium": "Mende&shy;levium",
              "Darmstadtium": "Darm&shy;stadtium", "Roentgenium": "Roent&shy;genium",
              "Copernicium": "Coper&shy;nicium", "Livermorium": "Liver&shy;morium",
              "Oganesson": "Oga&shy;nesson", "Molybdenum": "Molyb&shy;denum",
              "Technetium": "Tech&shy;netium", "Lawrencium": "Lawren&shy;cium",
              "Neodymium": "Neo&shy;dymium", "Gadolinium": "Gado&shy;linium",
              "Dysprosium": "Dyspro&shy;sium", "Promethium": "Prome&shy;thium",
              "Phosphorus": "Phos&shy;phorus", "Seaborgium": "Sea&shy;borgium",
              "Meitnerium": "Meit&shy;nerium", "Californium": "Califor&shy;nium",
              "Einsteinium": "Einstei&shy;nium", "Americium": "Ameri&shy;cium",
              "Berkelium": "Berke&shy;lium", "Ytterbium": "Ytter&shy;bium",
              "Tennessine": "Tennes&shy;sine", "Flerovium": "Flero&shy;vium",
              "Moscovium": "Mosco&shy;vium", "Manganese": "Manga&shy;nese",
              "Magnesium": "Magne&shy;sium", "Beryllium": "Beryl&shy;lium",
              "Strontium": "Stron&shy;tium", "Zirconium": "Zirco&shy;nium",
              "Ruthenium": "Ruthe&shy;nium", "Palladium": "Palla&shy;dium",
              "Germanium": "Germa&shy;nium", "Lanthanum": "Lantha&shy;num",
              "Plutonium": "Pluto&shy;nium", "Neptunium": "Neptu&shy;nium",
              "Nobelium": "Nobe&shy;lium", "Fermium": "Fer&shy;mium"}
    return breaks.get(name, esc(name))


def cell(x, y, e, family_label=None):
    return (f'<div class="cell" style="left:{x:.4f}in;top:{y:.4f}in">'
            f'<div class="top"><span class="z">{e["z"]}</span><span>{esc(e["mass"])}</span></div>'
            f'<div class="sym">{esc(e["symbol"])}</div><div class="name">{name_html(e["name"])}</div></div>')


def arrow_svg(w, h, horizontal):
    """An arrow drawn as SVG so it scales exactly; ink only, no fill bands."""
    if horizontal:
        return (f'<svg width="{w}in" height="{h}in" viewBox="0 0 {w*100:.0f} {h*100:.0f}">'
                f'<line x1="0" y1="{h*50:.0f}" x2="{w*100-14:.0f}" y2="{h*50:.0f}" stroke="{INK}" stroke-width="2.4"/>'
                f'<polygon points="{w*100:.0f},{h*50:.0f} {w*100-16:.0f},{h*50-7:.0f} {w*100-16:.0f},{h*50+7:.0f}" fill="{INK}"/></svg>')
    return (f'<svg width="{w}in" height="{h}in" viewBox="0 0 {w*100:.0f} {h*100:.0f}">'
            f'<line x1="{w*50:.0f}" y1="0" x2="{w*50:.0f}" y2="{h*100-14:.0f}" stroke="{INK}" stroke-width="2.4"/>'
            f'<polygon points="{w*50:.0f},{h*100:.0f} {w*50-7:.0f},{h*100-16:.0f} {w*50+7:.0f},{h*100-16:.0f}" fill="{INK}"/></svg>')


def student_page(key=False):
    out = []
    # ---- title strip: outlined, accent bar on the left, no solid slab (ink budget)
    out.append(f'<div class="abs" style="left:{ML}in;top:{MT}in;width:{PW-2*ML}in;height:{TITLE_H-0.06}in;'
               f'border-left:4pt solid {ACC["primary"]["hex"]};padding-left:0.1in;display:flex;'
               f'align-items:center;justify-content:space-between">'
               f'<div><span style="font-size:15pt;font-weight:700">The Periodic Table</span>'
               f'<span style="font-size:9pt;color:{LABEL};margin-left:0.15in">'
               f'{"KEY · " if key else ""}Color each family. Label the trends. Keep it in your binder.</span></div>'
               f'<div style="display:flex;gap:0.2in;align-items:flex-end">'
               f'<span class="lab">NAME</span><span class="line" style="width:2.1in;height:0.16in"></span>'
               f'<span class="lab">PERIOD</span><span class="line" style="width:0.55in;height:0.16in"></span>'
               f'<span style="font-size:10pt;font-weight:700;color:{ACCENT};margin-left:0.1in;white-space:nowrap">{CODE}</span>'
               f'</div></div>')
    # ---- the across arrow, with a line to write which trends increase that way
    ay = MT + TITLE_H
    out.append(f'<div class="abs" style="left:{X0}in;top:{ay}in;width:{18*CW}in;height:{ARROW_H}in">'
               f'<div style="display:flex;align-items:flex-end;gap:0.1in;height:0.2in">'
               f'<span class="lab">ACROSS A PERIOD — INCREASES THIS WAY:</span>'
               f'<span class="line" style="flex:1;height:0.17in;font-size:9pt;color:{ACCENT};font-weight:700">'
               f'{"Electronegativity, ionization energy" if key else ""}</span></div>'
               f'{arrow_svg(18*CW, 0.18, True)}</div>')
    # ---- the down arrow, label rotated to run along it
    tbl_h = 7 * CH
    out.append(f'<div class="abs" style="left:{ML}in;top:{Y0}in;width:0.18in;height:{tbl_h}in">'
               f'{arrow_svg(0.18, tbl_h, False)}</div>')
    # Label in the lower half, a write-on line in the upper half, both running along the arrow.
    half = tbl_h / 2
    lx = ML + 0.22
    out.append(f'<div class="abs" style="left:{lx}in;top:{Y0+half}in;width:0.2in;height:{half}in;'
               f'display:flex;align-items:center;justify-content:center">'
               f'<div class="lab" style="transform:rotate(-90deg);white-space:nowrap">'
               f'DOWN A GROUP — INCREASES THIS WAY:</div></div>')
    out.append(f'<div class="abs" style="left:{lx}in;top:{Y0+0.1}in;width:0.2in;height:{half-0.2}in;'
               f'border-left:0.75pt solid {STRUCT}"></div>')
    if key:
        out.append(f'<div class="abs" style="left:{lx}in;top:{Y0+0.1}in;width:0.2in;height:{half-0.2}in;'
                   f'display:flex;align-items:center;justify-content:center">'
                   f'<div style="transform:rotate(-90deg);white-space:nowrap;font-size:9pt;font-weight:700;'
                   f'color:{ACCENT}">Atomic radius</div></div>')
    # ---- group and period numbers
    for g in range(1, 19):
        out.append(f'<div class="abs num" style="left:{X0+(g-1)*CW}in;top:{Y0-GROUP_H}in;width:{CW}in">{g}</div>')
    for p in range(1, 8):
        out.append(f'<div class="abs num" style="left:{X0-0.18}in;top:{Y0+(p-1)*CH+CH/2-0.07}in;width:0.16in">{p}</div>')
    # ---- the elements
    fy = Y0 + 7 * CH + FGAP
    for e in DATA["elements"]:
        if e["frow"]:
            r = 0 if e["frow"] == "La" else 1
            out.append(cell(X0 + (2 + e["fcol"]) * CW, fy + r * CH, e))
        else:
            out.append(cell(X0 + (e["group"] - 1) * CW, Y0 + (e["period"] - 1) * CH, e))
    for p, txt in ((6, "57–71"), (7, "89–103")):
        out.append(f'<div class="cell place" style="left:{X0+2*CW}in;top:{Y0+(p-1)*CH}in">{txt}</div>')
    for r, txt in enumerate(("Lanthanides  57–71", "Actinides  89–103")):
        out.append(f'<div class="abs lab" style="left:{X0}in;top:{fy+r*CH+CH/2-0.07}in;width:{2*CW-0.06}in;'
                   f'text-align:right">{txt.split()[0].upper()}</div>')
    # ---- trend chart in the empty block above the transition metals (groups 3-12, periods 1-3)
    rows = "".join(
        f'<tr><td class="t">{t}</td>'
        + (f'<td class="ans">{ANSWERS[t][0]}</td><td class="ans">{ANSWERS[t][1]}</td>' if key else '<td></td><td></td>')
        + '</tr>' for t in TRENDS)
    out.append(f'<div class="abs" style="left:{X0+2*CW+0.06}in;top:{Y0+0.02}in;width:{10*CW-0.12}in;'
               f'height:{3*CH-0.08}in;border:0.75pt solid {STRUCT};padding:0.02in 0.04in">'
               f'<table class="trend"><tr><th>TREND</th><th>ACROSS A PERIOD →<br>'
               f'<span style="font-weight:400;letter-spacing:0">draw the arrow, write increases or decreases</span></th>'
               f'<th>DOWN A GROUP ↓<br><span style="font-weight:400;letter-spacing:0">draw the arrow, write increases '
               f'or decreases</span></th></tr>{rows}</table></div>')
    # ---- color key along the bottom
    ky = fy + 2 * CH + 0.12
    out.append(f'<div class="abs lab" style="left:{X0}in;top:{ky}in">COLOR KEY — COLOR EACH BOX, THEN EVERY '
               f'ELEMENT IN THAT FAMILY</div>')
    kw = (18 * CW) / 10
    for i, (cat, lab) in enumerate(FAMILIES):
        x = X0 + i * kw
        out.append(f'<div class="abs" style="left:{x}in;top:{ky+0.17}in;width:{kw-0.06}in;display:flex;gap:0.06in;'
                   f'align-items:center">'
                   f'<div style="width:0.3in;height:0.26in;border:0.75pt solid {STRUCT};flex:none"></div>'
                   f'<div style="font-family:\'Archivo Narrow\';font-size:8.5pt;line-height:1.05;font-weight:600;'
                   f'width:{kw-0.42:.3f}in">{lab}</div></div>')
    # ---- running footer
    out.append(f'<div class="abs" style="left:{ML}in;top:{PH-0.25}in;font-size:7pt;color:{FOOTER}">'
               f'SHULL SCIENCE   {CODE}   ORGANIZER{"   KEY" if key else ""}</div>')
    return "".join(out)


def key_page():
    """Page 2 of the key: the family of every element, in words, so nothing depends on color."""
    by = {c: [e["symbol"] for e in DATA["elements"] if e["category"] == c] for c, _ in FAMILIES}
    rows = "".join(f'<tr><td class="t">{lab}</td><td style="font-size:9.5pt">{", ".join(by[c])}</td></tr>'
                   for c, lab in FAMILIES)
    notes = [
        "Melting and boiling point have no single arrow. Across periods 2 and 3 they climb to carbon and "
        "silicon (group 14), whose atoms are locked in a network, then drop to the gases on the right. Down a "
        "group they fall steadily for the alkali metals and rise for the halogens and noble gases; the alkaline "
        "earth metals jump around (Mg 650 °C, Ca 842 °C). "
        "Accept any answer that says it depends on the group, or that it peaks in the middle.",
        "Hydrogen is colored as a nonmetal even though it sits in group 1.",
        "Tables differ on polonium (other metal or metalloid) and astatine (halogen or metalloid). This sheet "
        "uses other metal and halogen; accept either.",
        "Elements 113–118 are placed by prediction; almost nothing about them has been measured.",
        "Source: " + DATA["source"],
    ]
    return (f'<div style="position:absolute;left:{ML}in;top:{MT}in;width:{PW-2*ML}in">'
            f'<div style="border-left:4pt solid {ACC["primary"]["hex"]};padding-left:0.1in;margin-bottom:0.15in">'
            f'<span style="font-size:15pt;font-weight:700">The Periodic Table — Key</span>'
            f'<span style="font-size:9pt;color:{LABEL};margin-left:0.15in">Families in words, and notes</span></div>'
            f'<table class="trend" style="height:auto"><tr><th>FAMILY</th><th>ELEMENTS</th></tr>{rows}</table>'
            f'<div class="lab" style="margin-top:0.2in">NOTES</div>'
            + "".join(f'<p style="font-size:9.5pt;margin-top:0.06in;line-height:1.3">{esc(n)}</p>' for n in notes)
            + f'</div><div class="abs" style="left:{ML}in;top:{PH-0.25}in;font-size:7pt;color:{FOOTER}">'
            f'SHULL SCIENCE   {CODE}   ORGANIZER   KEY</div>')


def render(body_pages, out):
    from weasyprint import HTML
    pages = "".join(f'<div style="position:relative;width:{PW}in;height:{PH}in;page-break-after:always">{p}</div>'
                    for p in body_pages)
    HTML(string=f"<html><head><style>{CSS}</style></head><body>{pages}</body></html>",
         base_url=REPO).write_pdf(out)
    print("wrote", out)


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else HERE
    sections = ["3.1", "3.2", "3.3", "3.4", "3.6"]
    assert len(DATA["elements"]) == 118
    render([student_page()], os.path.join(outdir, document_name(
        "Organizer", sections, 3, descriptor="Periodic Table", ext="pdf")))
    render([student_page(key=True), key_page()], os.path.join(outdir, document_name(
        "Organizer", sections, 3, key=True, descriptor="Periodic Table", ext="pdf")))


if __name__ == "__main__":
    main()
