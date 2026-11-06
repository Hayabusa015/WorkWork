#!/usr/bin/env python3
"""Build the Chemistry reference packet (SHULL-CHG-0058) as HTML, one file per sheet.

    python3 templates/reference/build_reference.py <out_dir>
    node templates/reference/render.cjs <out_dir>          # HTML -> PDF, then the Full Packet

Filenames come from the REF rows of courses/chemistry/DECISIONS.md through the naming builder,
never typed here. Print rules: brand/SHULL_DESIGN_SYSTEM.md section 8 (outlined, not filled;
fractions stacked; survives greyscale). Archivo only: characters Archivo lacks (star, lambda, nu)
are drawn as SVG so no fallback font enters the PDF.
"""
import html, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
from _shull_name import document_name, reference_titles
import chem_data as D
from vsepr_geometry import svg as vsepr_svg

FONTS = os.path.join(os.path.dirname(HERE), "..", "brand", "fonts")
FONTS = os.path.normpath(os.path.join(HERE, "..", "..", "brand", "fonts"))
ORANGE, DEEP, INK, ASPHALT, RULE = "#FF6B1A", "#B84100", "#2E3338", "#14161B", "#C8CDC2"

# ---------- markup helpers ----------
def F(s):
    """Formula markup: 'Cr2O7^2-' -> Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>."""
    body, _, charge = s.partition("^")
    body = re.sub(r"(?<=[A-Za-z)])(\d+)", r"<sub>\1</sub>", body)
    if charge:
        charge = charge.replace("-", "−")
        body += f"<sup>{charge}</sup>"
    return body

def frac(n, d):
    return f'<span class="fr"><span class="n">{n}</span><span class="d">{d}</span></span>'

STAR = ('<svg class="star" viewBox="0 0 20 20" width="9" height="9"><polygon points="10,1 12.6,7.2 19.3,7.6 '
        '14.1,11.9 15.8,18.5 10,14.8 4.2,18.5 5.9,11.9 0.7,7.6 7.4,7.2" fill="' + INK + '"/></svg>')
LAMBDA = ('<svg class="gl" viewBox="0 0 10 12"><path d="M1.6 1.2 Q4 0.6 4.9 3.6 L8.6 11.2 M5.3 4.9 L1.4 11.2" '
          'fill="none" stroke="currentColor" stroke-width="1.15" stroke-linecap="round"/></svg>')
NU = ('<svg class="gl" viewBox="0 0 10 12"><path d="M1.4 4.2 L1.9 4 L4.3 11 Q7.6 7.6 8.4 4.2" fill="none" '
      'stroke="currentColor" stroke-width="1.15" stroke-linecap="round" stroke-linejoin="round"/></svg>')

CSS = f"""
@font-face{{font-family:Archivo;src:url(file://{FONTS}/Archivo-Regular.ttf);font-weight:400}}
@font-face{{font-family:Archivo;src:url(file://{FONTS}/Archivo-Medium.ttf);font-weight:500}}
@font-face{{font-family:Archivo;src:url(file://{FONTS}/Archivo-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:Archivo;src:url(file://{FONTS}/Archivo-Bold.ttf);font-weight:700}}
@font-face{{font-family:'Archivo Var';src:url(file://{FONTS}/Archivo[wdth,wght].ttf);font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:'Archivo Narrow';src:url(file://{FONTS}/ArchivoNarrow[wght].ttf);font-weight:100 900}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Trade Gothic Next',Archivo,sans-serif;color:{ASPHALT};background:#fff;font-size:10pt;line-height:1.3}}
header{{display:flex;align-items:baseline;justify-content:space-between;border-bottom:1.5px solid {ORANGE};padding-bottom:4px;margin-bottom:10px}}
h1{{font-family:'Trade Gothic Next Condensed','Archivo Narrow',sans-serif;font-weight:700;font-size:24pt;margin:0;line-height:1}}
.chip{{border:1.2px solid {ORANGE};color:{DEEP};font-weight:700;font-size:8pt;padding:2px 8px;border-radius:3px;letter-spacing:.6px;white-space:nowrap}}
h2{{font-family:'Archivo Narrow',sans-serif;font-weight:700;font-size:12.5pt;margin:0 0 4px;color:{ASPHALT};
   border-bottom:0.75px solid {RULE};padding-bottom:2px}}
h2 .tag{{color:{DEEP};font-weight:700}}
table{{border-collapse:collapse}}
td,th{{border:0.75px solid {RULE};padding:2px 6px;vertical-align:middle}}
th{{font-weight:700;font-size:9pt;color:{INK};text-align:left}}
sub,sup{{font-size:70%;line-height:0}}
.fr{{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;margin:0 2px;line-height:1.15}}
.fr .n{{padding:0 3px 1px}} .fr .d{{border-top:1px solid {ASPHALT};padding:1px 3px 0}}
.gl{{width:0.62em;height:0.78em;vertical-align:-0.05em;margin:0 0.03em}}
.star{{vertical-align:0}}
.note{{font-size:8.5pt;color:{INK}}}
.eq{{font-size:11pt;white-space:nowrap}}
"""

def page(title, body, landscape=False, extra_css=""):
    size = "letter landscape" if landscape else "letter"
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>{html.escape(title)}</title><style>"
            f"@page{{size:{size};margin:0.35in 0.4in 0.4in}}{CSS}{extra_css}</style></head><body>"
            f"<header><h1>{title}</h1><span class='chip'>CHEMISTRY REFERENCE</span></header>{body}</body></html>")

# ---------- 1 Equations & Constants ----------
def sheet_equations():
    def block(name, rows):
        r = "".join(f"<tr><td class='lab'>{a}</td><td class='eq'>{b}</td></tr>" for a, b in rows)
        return f"<section><h2>{name}</h2><table class='eqt'>{r}</table></section>"
    sub = lambda a, b: f"{a}<sub>{b}</sub>"
    P1, P2, V1, V2, T1, T2, n1, n2 = (sub("P",1), sub("P",2), sub("V",1), sub("V",2), sub("T",1), sub("T",2), sub("n",1), sub("n",2))
    left = block("Measurement", [
        ("Density", f"D = {frac('m','V')}"),
        ("Percent error", f"% error = {frac('| experimental − accepted |','accepted')} × 100"),
        ("Percent composition", f"% element = {frac('mass of element','mass of compound')} × 100"),
        ("Average atomic mass", "(mass<sub>1</sub> × abundance<sub>1</sub>) + (mass<sub>2</sub> × abundance<sub>2</sub>) + …<br><span class='note'>abundance as a decimal</span>"),
    ]) + block("The Mole", [
        ("Moles from mass", f"n = {frac('m','M')}<span class='note'>&nbsp; n moles · m mass (g) · M molar mass (g/mol)</span>"),
        ("Particles", "particles = n × N<sub>A</sub>"),
        ("Gas at STP", "1 mol = 22.4 L"),
    ]) + block("Gas Laws <span class='note'>T in kelvin</span>", [
        ("Boyle's law", f"{P1}{V1} = {P2}{V2}"),
        ("Charles's law", f"{frac(V1,T1)} = {frac(V2,T2)}"),
        ("Gay-Lussac's law", f"{frac(P1,T1)} = {frac(P2,T2)}"),
        ("Combined gas law", f"{frac(P1+V1,T1)} = {frac(P2+V2,T2)}"),
        ("Avogadro's law", f"{frac(V1,n1)} = {frac(V2,n2)}"),
        ("Ideal gas law", "PV = nRT"),
        ("Dalton's law", "P<sub>total</sub> = P<sub>1</sub> + P<sub>2</sub> + P<sub>3</sub> + …"),
    ])
    right = block("Solutions", [
        ("Molarity", f"M = {frac('moles of solute','liters of solution')}"),
        ("Dilution", "M<sub>1</sub>V<sub>1</sub> = M<sub>2</sub>V<sub>2</sub>"),
    ]) + block("Thermochemistry", [
        ("Heat", "q = mcΔT"),
        ("Temperature change", "ΔT = T<sub>final</sub> − T<sub>initial</sub>"),
    ]) + block("Acids &amp; Bases", [
        ("pH", "pH = −log[H<sup>+</sup>]&nbsp;&nbsp;&nbsp; [H<sup>+</sup>] = 10<sup>−pH</sup>"),
        ("pOH", "pOH = −log[OH<sup>−</sup>]&nbsp;&nbsp;&nbsp; [OH<sup>−</sup>] = 10<sup>−pOH</sup>"),
        ("pH and pOH", "pH + pOH = 14"),
        ("Titration (1 : 1)", "M<sub>a</sub>V<sub>a</sub> = M<sub>b</sub>V<sub>b</sub>"),
    ]) + block("Light", [
        ("Wave speed", f"c = {LAMBDA}{NU}"),
        ("Photon energy", f"E = h{NU}"),
    ]) + block("Nuclear", [
        ("Half-life", f"amount left = initial amount × ({frac('1','2')})<sup>n</sup>"),
        ("", f"n = {frac('time elapsed','half-life')}"),
    ])
    # page 2
    consts = [("Avogadro's number","N<sub>A</sub> = 6.022 × 10<sup>23</sup> particles/mol"),
              ("Gas constant","R = 0.0821 L·atm/(mol·K)"),("","R = 8.314 L·kPa/(mol·K)"),("","R = 62.4 L·mmHg/(mol·K)"),
              ("Speed of light","c = 3.00 × 10<sup>8</sup> m/s"),("Planck's constant","h = 6.626 × 10<sup>−34</sup> J·s"),
              ("Specific heat of water","c = 4.184 J/(g·°C)"),
              ("STP","0 °C (273 K) and 1 atm"),("Molar volume at STP","22.4 L/mol")]
    ct = "".join(f"<tr><td class='lab'>{a}</td><td>{b}</td></tr>" for a, b in consts)
    prefixes = [("giga","G","10<sup>9</sup>"),("mega","M","10<sup>6</sup>"),("kilo","k","10<sup>3</sup>"),
                ("— base unit —","","1"),("deci","d","10<sup>−1</sup>"),("centi","c","10<sup>−2</sup>"),
                ("milli","m","10<sup>−3</sup>"),("micro","µ","10<sup>−6</sup>"),("nano","n","10<sup>−9</sup>")]
    pt = "".join(f"<tr><td>{a}</td><td class='c'>{b}</td><td>{c}</td></tr>" for a, b, c in prefixes)
    conv = [("Pressure","1 atm = 760 mmHg = 760 torr = 101.3 kPa"),("Temperature","K = °C + 273"),
            ("Volume","1 mL = 1 cm<sup>3</sup>&nbsp;&nbsp; 1 L = 1000 mL"),("Length","1 in = 2.54 cm"),
            ("Mass","1 lb = 453.6 g&nbsp;&nbsp; 1 kg = 1000 g"),("Energy","1 cal = 4.184 J&nbsp;&nbsp; 1 kJ = 1000 J")]
    cv = "".join(f"<tr><td class='lab'>{a}</td><td>{b}</td></tr>" for a, b in conv)
    box = lambda t, w="1.25in": f"<span class='dbox' style='width:{w}'>{t}</span>"
    da = (f"<div class='da'>{box('given<br>number + unit')} × {frac(box('new unit','1.1in'), box('unit to cancel','1.1in'))}"
          f" × {frac(box('new unit','1.1in'), box('unit to cancel','1.1in'))} = {box('answer<br>number + unit')}</div>"
          "<ol class='steps'><li>Write what you are given, with its unit.</li>"
          "<li>Multiply by a conversion factor written so the unit you have is on the bottom.</li>"
          "<li>Cancel units. Repeat until only the unit you want is left.</li>"
          "<li>Multiply across the top, divide by everything on the bottom.</li></ol>"
          f"<p class='ex'><b>Example</b>&nbsp; 2.50 mol H<sub>2</sub>O × {frac('18.02 g H<sub>2</sub>O','1 mol H<sub>2</sub>O')} = 45.1 g H<sub>2</sub>O</p>")
    p2 = (f"<section><h2>Constants</h2><table class='kv'>{ct}</table></section>"
          f"<div class='two'><section><h2>Metric Prefixes</h2><table class='pre'><tr><th>Prefix</th><th>Symbol</th><th>Factor</th></tr>{pt}</table></section>"
          f"<section><h2>Conversions</h2><table class='kv'>{cv}</table></section></div>"
          f"<section><h2>Dimensional Analysis</h2>{da}</section>")
    css = """.cols{display:grid;grid-template-columns:1fr 1fr;gap:6px 22px} section{margin-bottom:9px;break-inside:avoid}
    .eqt{width:100%} .eqt td{border:none;border-bottom:0.75px solid #C8CDC2;padding:4px 4px}
    .lab{font-size:9pt;color:#2E3338;width:34%;font-weight:600}
    .kv{width:100%} .kv td{border:none;border-bottom:0.75px solid #C8CDC2;padding:4px 4px;font-size:10.5pt}
    .two{display:grid;grid-template-columns:0.8fr 1.2fr;gap:22px}
    .pre td{padding:2px 10px;font-size:10pt} .pre .c{text-align:center;font-weight:700}
    .da{display:flex;align-items:center;gap:6px;font-size:12pt;margin:6px 0 8px}
    .dbox{display:inline-block;border:1px solid #2E3338;border-radius:3px;text-align:center;font-size:8.5pt;
          padding:6px 4px;color:#2E3338;line-height:1.2}
    .steps{margin:2px 0 6px 18px;padding:0;font-size:9.5pt} .ex{font-size:10.5pt;margin:4px 0}
    .pg{break-after:page}"""
    body = (f"<div class='pg cols'><div>{left}</div><div>{right}</div></div>"
            f"<header><h1>Constants &amp; Conversions</h1><span class='chip'>CHEMISTRY REFERENCE</span></header>{p2}")
    return page("Equations", body, extra_css=css)

# ---------- 2 Significant figures ----------
def sheet_sigfigs():
    rows = [("Nonzero digits are always significant.","4.72","3"),
            ("Zeros between nonzero digits are significant.","2005","4"),
            ("Leading zeros are never significant. They only place the decimal point.","0.0032","2"),
            ("Trailing zeros are significant when the number has a decimal point.","3.200 &nbsp;·&nbsp; 150.","4 · 3"),
            ("Trailing zeros with no decimal point are not significant.","1500","2"),
            ("In scientific notation, every digit in the coefficient is significant.","4.50 × 10<sup>3</sup>","3"),
            ("Exact numbers (counted items, defined conversions) have unlimited significant figures.","12 eggs · 1 m = 100 cm","∞")]
    t = "".join(f"<tr><td>{a}</td><td class='x'>{b}</td><td class='c'>{c}</td></tr>" for a, b, c in rows)
    calc = (f"<div class='calc'><div class='cbox'><h3>Multiplying and dividing</h3><p>The answer has the same number of "
            f"<b>significant figures</b> as the measurement with the fewest.</p><p class='x'>2.5 cm × 3.42 cm = 8.55 → <b>8.6 cm<sup>2</sup></b></p>"
            f"<p class='note'>2.5 has 2 significant figures, so the answer has 2.</p></div>"
            f"<div class='cbox'><h3>Adding and subtracting</h3><p>The answer has the same number of <b>decimal places</b> as the "
            f"measurement with the fewest.</p><p class='x'>12.11 g + 3.2 g = 15.31 → <b>15.3 g</b></p>"
            f"<p class='note'>3.2 has 1 decimal place, so the answer has 1.</p></div></div>"
            "<div class='cbox wide'><h3>Rounding</h3><p>Look at the first digit you are dropping. 5 or more: round up. "
            "Less than 5: leave the last kept digit alone.&nbsp;&nbsp; <span class='x'>3.476 to 3 sig figs → 3.48</span>"
            "&nbsp;&nbsp;·&nbsp;&nbsp;<span class='x'>3.474 → 3.47</span></p><p class='note'>In a multi-step problem, "
            "keep extra digits until the final answer, then round once.</p></div>")
    body = (f"<h2>Which digits count</h2><table class='sf'><tr><th>Rule</th><th>Example</th><th>Sig figs</th></tr>{t}</table>"
            f"<h2 style='margin-top:16px'>Calculations</h2>{calc}")
    css = """.sf{width:100%;margin-bottom:6px} .sf td{padding:6px 8px;font-size:10.5pt} .sf .x{font-size:12pt;white-space:nowrap;width:24%}
    .sf .c{text-align:center;font-weight:700;font-size:12pt;width:11%} .calc{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:8px 0 14px}
    .cbox{border:1px solid #2E3338;border-radius:4px;padding:8px 12px} .cbox h3{margin:0 0 4px;font-size:11.5pt;color:#B84100}
    .cbox p{margin:4px 0} .x{font-size:12pt}"""
    return page("Significant Figure Rules", body, extra_css=css)

# ---------- 3 VSEPR ----------
def sheet_vsepr():
    EG = {2:"Linear",3:"Trigonal Planar",4:"Tetrahedral",5:"Trigonal Bipyramidal",6:"Octahedral"}
    MG = {(2,0):("Linear","180°"),(3,0):("Trigonal Planar","120°"),(3,1):("Bent","&lt;120°"),
          (4,0):("Tetrahedral","109.5°"),(4,1):("Trigonal Pyramidal","≈107°"),(4,2):("Bent","≈104.5°"),
          (5,0):("Trigonal Bipyramidal","90°, 120°"),(5,1):("Seesaw","&lt;90°, &lt;120°"),(5,2):("T-Shaped","&lt;90°"),
          (5,3):("Linear","180°"),(6,0):("Octahedral","90°"),(6,1):("Square Pyramidal","&lt;90°"),(6,2):("Square Planar","90°")}
    rows = ""
    for d in range(2, 7):
        cells = (f'<th class="rh"><div class="dn">{d}</div><div class="dl">electron domains</div>'
                 f'<div class="egl">electron geometry</div><div class="eg">{EG[d]}</div></th>')
        for e in range(4):
            if (d, e) in MG:
                n, a = MG[(d, e)]
                b = d - e
                axe = f"AX<sub>{b}</sub>" + (f"E<sub>{e}</sub>" if e else "")
                cells += (f'<td><div class="img">{vsepr_svg((d, e))}</div><div class="mg">{n}</div>'
                          f'<div class="meta">{b} bonding · {e} lone&nbsp;&nbsp;|&nbsp;&nbsp;{a}&nbsp;&nbsp;|&nbsp;&nbsp;<span class="axe">{axe}</span></div></td>')
            else:
                cells += '<td class="na"></td>'
        rows += f"<tr>{cells}</tr>"
    key = (f'<div class="key"><span><svg width="16" height="16"><circle cx="8" cy="8" r="6.5" fill="{ORANGE}" stroke="{INK}" stroke-width="1.3"/></svg> central atom (A)</span>'
           f'<span><svg width="16" height="16"><circle cx="8" cy="8" r="6" fill="#fff" stroke="{INK}" stroke-width="1.3"/></svg> bonded atom (X)</span>'
           f'<span><svg width="28" height="16"><ellipse cx="14" cy="8" rx="12" ry="6.5" fill="#E9F8FC" stroke="{INK}" stroke-dasharray="3 2.2"/>'
           f'<circle cx="14" cy="5.3" r="1.6" fill="{INK}"/><circle cx="14" cy="10.7" r="1.6" fill="{INK}"/></svg> lone pair (E)</span>'
           '<span>grey bond = pointing behind the page</span>'
           '<span>Electron domains = bonded atoms + lone pairs on the central atom. A double or triple bond counts as one domain.</span></div>')
    body = (f'<table class="vs"><thead><tr><th></th><th>0 lone pairs</th><th>1 lone pair</th><th>2 lone pairs</th>'
            f'<th>3 lone pairs</th></tr></thead><tbody>{rows}</tbody></table>{key}')
    css = """.vs{width:100%;table-layout:fixed} .vs td,.vs th{text-align:center;padding:1px 3px 3px}
    .vs thead th{text-align:center;font-size:9.5pt;padding:3px} .vs thead th:first-child{width:15%}
    .rh{text-align:left!important;padding-left:9px!important} .dn{font-family:'Archivo Narrow';font-weight:700;font-size:22pt;line-height:1}
    .dl,.egl{font-size:8pt;color:#2E3338;text-transform:uppercase;letter-spacing:.4px} .egl{margin-top:5px}
    .eg{font-weight:700;font-size:10.5pt;color:#B84100}
    .img svg{width:1.14in;height:auto;display:block;margin:0 auto} .mg{font-weight:700;font-size:10.5pt;margin-top:-3px}
    .meta{font-size:8pt;color:#2E3338} .axe{font-family:'Archivo Narrow'}
    td.na{background:repeating-linear-gradient(135deg,#fff 0 6px,#E4E7E0 6px 7px)}
    .key{display:flex;flex-wrap:wrap;gap:4px 18px;align-items:center;font-size:8.5pt;margin-top:5px;color:#2E3338}
    .key svg{vertical-align:middle}"""
    return page("VSEPR Shapes", body, landscape=True, extra_css=css)

# ---------- 4/5 periodic tables ----------
def _grid(cell):
    main, frow = {}, {}
    for z, sym, name, mass in D.ELEMENTS:
        p = D.position(z)
        if p[0] == "f": frow[(p[1], p[2])] = (z, sym, name, mass)
        else: main[p] = (z, sym, name, mass)
    head = "<tr><th class='corner'></th>" + "".join(f"<th>{g}</th>" for g in range(1, 19)) + "</tr>"
    rows = ""
    for period in range(1, 8):
        r = f"<tr><th class='per'>{period}</th>"
        gap = (2, 17) if period == 1 else (3, 12) if period in (2, 3) else None
        for g in range(1, 19):
            el = main.get((g, period))
            if el: r += cell(*el, mark=("*" if el[1] == "La" else "**" if el[1] == "Ac" else ""))
            elif gap and g == gap[0]: r += f"<td class='blank' colspan='{gap[1] - gap[0] + 1}'></td>"
            elif gap and gap[0] < g <= gap[1]: pass
            else: r += "<td class='blank'></td>"
        rows += r + "</tr>"
    rows += "<tr class='gap'><td colspan='19'></td></tr>"
    for period, lab in ((6, "* Lanthanides"), (7, "** Actinides")):
        r = f"<tr><th class='per'></th><td class='flab' colspan='3'>{lab}</td>"
        for i in range(14): r += cell(*frow[(period, i)], mark="")
        rows += r + "<td class='blank'></td></tr>"
    return f"<table class='pt'>{head}{rows}</table>"

PT_CSS = """.pt{width:100%;table-layout:fixed} .pt th{text-align:center;font-size:8pt;padding:1px;border:none;color:#2E3338}
 .pt th.per{width:2.2%} .pt td{padding:1px 2px;text-align:center;vertical-align:top}
 .pt td.blank{border:none} .gap td{border:none;height:8px} .flab{border:none!important;text-align:right!important;
 font-size:8.5pt;font-weight:700;color:#B84100;vertical-align:middle!important;padding-right:6px!important}
 .z{font-size:8pt;text-align:left;line-height:1.1} .sym{font-weight:700;font-size:13pt;line-height:1.05}
 .nm{font-family:'Archivo Var';font-stretch:68%;font-size:8pt;line-height:1.1;white-space:nowrap;overflow:hidden}
 .ms{font-size:8pt;line-height:1.15} .mk{color:#B84100;font-weight:700}"""

def sheet_periodic():
    def cell(z, sym, name, mass, mark=""):
        mk = f"<span class='mk'>{mark}</span>" if mark else ""
        return (f"<td><div class='z'>{z}{mk}</div><div class='sym'>{sym}</div>"
                f"<div class='nm'>{name}</div><div class='ms'>{mass}</div></td>")
    legend = ("<div class='leg'><table class='lg'><tr><td><div class='z'>atomic number</div><div class='sym'>Symbol</div>"
              "<div class='nm'>Name</div><div class='ms'>average atomic mass</div></td></tr></table>"
              "<span class='note'>A mass in brackets [ ] is the mass number of the element's longest-lived isotope. "
              "These elements have no standard atomic mass.</span></div>")
    css = PT_CSS + """.leg{display:flex;align-items:center;gap:14px;margin-top:6px} .lg td{padding:2px 10px;text-align:center}
    .lg .z,.lg .nm,.lg .ms{text-align:center}"""
    return page("Periodic Table of the Elements", _grid(cell) + legend, landscape=True, extra_css=css)

def sheet_electronegativity():
    def cell(z, sym, name, mass, mark=""):
        v = D.EN.get(sym)
        val = f"{v:.2f}" if (v is not None and sym not in D.NOBLE) else "&nbsp;"
        mk = f"<span class='mk'>{mark}</span>" if mark else ""
        return (f"<td><div class='z'>{z}{mk}</div><div class='sym'>{sym}</div>"
                f"<div class='en'>{val}</div></td>")
    legend = ("<div class='leg'><table class='lg'><tr><td><div class='z'>atomic number</div><div class='sym'>Symbol</div>"
              "<div class='en'>electronegativity</div></td></tr></table>"
              "<span class='note'>Pauling scale. Noble gases are left blank. Blank cells elsewhere have no measured value.</span></div>")
    css = PT_CSS + """.en{font-size:10.5pt;font-weight:600;line-height:1.2;padding-bottom:1px} .pt td{padding:2px 2px 3px}
    .leg{display:flex;align-items:center;gap:14px;margin-top:6px} .lg td{padding:2px 10px;text-align:center} .lg .z{text-align:center}
    .lg .en{font-size:8.5pt;font-weight:400}"""
    return page("Electronegativity", _grid(cell) + legend, landscape=True, extra_css=css)

# ---------- 6 Polyatomic ions ----------
def sheet_polyatomic():
    def group(charge, ions):
        r = "".join(f"<tr class='{'m' if m else ''}'><td class='s'>{STAR if m else ''}</td><td>{n}</td><td class='f'>{F(f)}</td></tr>"
                    for n, f, m in ions)
        return f"<section><h2><span class='tag'>{charge}</span> ions</h2><table class='pa'>{r}</table></section>"
    g = {c: ions for c, ions in D.POLYATOMIC}
    left = group("1+", g["1+"]) + group("2+", g["2+"]) + group("1−", g["1−"])
    right = group("2−", g["2−"]) + group("3−", g["3−"])
    key = (f"<p class='note k'>{STAR} <b>Memorize these 15.</b> The rest are here to look up. "
           "Each group lists the ions to memorize first.</p>")
    body = f"{key}<div class='cols'><div>{left}</div><div>{right}</div></div>"
    css = """.cols{display:grid;grid-template-columns:1fr 1fr;gap:0 26px} section{margin-bottom:10px}
    .pa{width:100%} .pa td{border:none;border-bottom:0.75px solid #C8CDC2;padding:3px 4px;font-size:10pt}
    .pa .s{width:16px;padding:0} .pa .f{text-align:right;font-size:11pt;white-space:nowrap}
    .pa tr.m td{font-weight:700} .k{margin:0 0 8px;font-size:9.5pt}"""
    return page("Polyatomic Ions", body, extra_css=css)

# ---------- 7 Naming toolkit ----------
def sheet_naming():
    roman = [("I",1),("II",2),("III",3),("IV",4),("V",5),("VI",6),("VII",7),("VIII",8)]
    rt = "".join(f"<tr><td class='big'>{a}</td><td class='c'>{b}</td></tr>" for a, b in roman)
    pre = [("mono-",1),("di-",2),("tri-",3),("tetra-",4),("penta-",5),("hexa-",6),("hepta-",7),("octa-",8),("nona-",9),("deca-",10)]
    pt = "".join(f"<tr><td class='big'>{a}</td><td class='c'>{b}</td></tr>" for a, b in pre)
    di = ["H2","N2","O2","F2","Cl2","Br2","I2"]
    dt = "".join(f"<span class='dm'>{F(x)}</span>" for x in di)
    body = (f"<div class='cols3'><section><h2>Roman Numerals</h2><p class='note'>The charge on a metal ion in a name: "
            f"iron(III) is Fe<sup>3+</sup>.</p><table class='nt'><tr><th>Numeral</th><th>Value</th></tr>{rt}</table></section>"
            f"<section><h2>Covalent Prefixes</h2><p class='note'>The number of each atom in a molecular compound.</p>"
            f"<table class='nt'><tr><th>Prefix</th><th>Number</th></tr>{pt}</table></section></div>"
            f"<section class='dia'><h2>Diatomic Elements</h2><p class='note'>These seven exist as two-atom molecules when the "
            f"element is on its own.</p><div class='dms'>{dt}</div></section>")
    css = """.cols3{display:grid;grid-template-columns:1fr 1fr;gap:30px} .nt{width:100%} .nt td{padding:4px 12px;font-size:12pt}
    .nt .big{font-weight:700;font-size:13pt} .nt .c{text-align:center} .nt th{padding:4px 12px}
    .dia{margin-top:22px} .dms{display:flex;gap:12px;margin-top:8px}
    .dm{border:1.2px solid #2E3338;border-radius:4px;padding:8px 0;width:72px;text-align:center;font-size:17pt;font-weight:700}"""
    return page("Naming Toolkit", body, extra_css=css)

# ---------- 8 Multi-charge metals ----------
def sheet_multicharge():
    r = "".join("<tr><td class='mt'>{}</td>{}</tr>".format(m, "".join(
        f"<td class='f'>{F(f)}</td><td>{n}</td>" for f, n in ions)) for m, ions in D.MULTI_CHARGE)
    fx = "".join(f"<tr><td class='mt'>{m}</td><td class='f'>{F(f)}</td><td class='note'>always this charge — no Roman numeral</td></tr>"
                 for m, f in D.FIXED_CHARGE)
    body = (f"<p class='note'>These metals form more than one ion. The Roman numeral in the name gives the charge.</p>"
            f"<table class='mc'><tr><th>Metal</th><th colspan='2'>Ion</th><th colspan='2'>Ion</th></tr>{r}</table>"
            f"<h2 style='margin-top:18px'>Transition metals with one charge</h2><table class='mc'>{fx}</table>")
    css = """.mc{width:100%} .mc td{padding:5px 10px;font-size:11pt} .mc .mt{font-weight:700;width:22%}
    .mc .f{font-size:13pt;font-weight:700;width:12%;text-align:center} .mc th{padding:4px 10px}"""
    return page("Metals with Multiple Charges", body, extra_css=css)

# ---------- 9 Solubility ----------
def sheet_solubility():
    head = "<tr><th class='corner'><span class='an'>anions →</span><span class='ca'>cations ↓</span></th>" + "".join(
        f"<th class='ah'><div class='f'>{F(a)}</div><div class='nm'>{n}</div></th>" for a, n in zip(D.ANIONS, D.ANION_NAMES)) + "</tr>"
    rows = ""
    for f, name, s in D.SOLUBILITY:
        vals = s.split()
        assert len(vals) == len(D.ANIONS), (f, vals)
        rows += f"<tr><th class='rh'><span class='f'>{F(f)}</span> <span class='nm'>{name}</span></th>" + "".join(
            f"<td class='v {v.lower()}'>{v}</td>" for v in vals) + "</tr>"
    rules = "".join(f"<li>{r}</li>" for r in D.SOLUBILITY_RULES)
    key = ("<div class='key'><span><b>S</b> soluble (more than 1 g per 100 mL)</span><span><b>SS</b> slightly soluble (0.1–1 g)</span>"
           "<span class='ikey'><b>I</b> insoluble (less than 0.1 g) — a precipitate</span><span><b>X</b> reacts with water or does not form</span>"
           "<span class='note'>Water at about 25 °C.</span></div>")
    body = (f"<div class='wrap'><table class='sol'>{head}{rows}</table><div class='side'>{key}<h2>Rules</h2><ol class='rules'>{rules}</ol></div></div>")
    css = """.wrap{display:grid;grid-template-columns:1fr 2.35in;gap:16px} .sol{width:100%;table-layout:fixed}
    .sol td,.sol th{padding:2px 2px;text-align:center} .sol .corner{width:1.45in;font-size:8pt;text-align:left;position:relative}
    .an{display:block;text-align:right} .ca{display:block}
    .ah .f{font-size:10pt;font-weight:700} .ah .nm,.rh .nm{font-family:'Archivo Narrow';font-size:8pt;font-weight:400;color:#2E3338}
    .rh{text-align:left!important;padding-left:5px!important;white-space:nowrap} .rh .f{font-size:10pt;font-weight:700}
    .v{font-size:10pt;height:0.33in} .v.i{font-weight:700;border:1.4px solid #2E3338} .v.ss{font-style:italic} .v.x{color:#7A8086}
    .key{display:flex;flex-direction:column;gap:3px;font-size:9pt;margin-bottom:10px} .rules{margin:0;padding-left:16px;font-size:9pt}
    .rules li{margin-bottom:5px}"""
    return page("Solubility", body, landscape=True, extra_css=css)

# ---------- 10 Activity series ----------
def sheet_activity():
    rows = ""
    for label, metals in D.ACTIVITY_METALS:
        span = len(metals)
        for i, x in enumerate(metals):
            lab = (f"<td class='al' rowspan='{span}'>{label or ''}</td>") if i == 0 else ""
            gap = " class='g'" if (i == 0 and rows) else ""
            rows += f"<tr{gap}><td class='m{' h' if x.startswith('H<') else ''}'>{x}</td>{lab}</tr>"
    hal = "".join(f"<tr><td class='m'>{x}</td></tr>" for x in D.ACTIVITY_HALOGENS)
    arrow = ("<td class='arr' rowspan='{n}'><div class='top'>most<br>active</div><div class='line'></div>"
             "<div class='bot'>least<br>active</div></td>")
    n_m = sum(len(m) for _, m in D.ACTIVITY_METALS)
    mt = rows.replace("<tr>", "<tr>" + arrow.format(n=n_m), 1)
    ht = hal.replace("<tr>", "<tr>" + arrow.format(n=len(D.ACTIVITY_HALOGENS)), 1)
    body = (f"<p class='note'>In a single-replacement reaction, an element replaces any element <b>below</b> it in its "
            f"own list. It does not replace an element above it.</p><div class='cols'>"
            f"<section><h2>Metals</h2><table class='lad'>{mt}</table></section>"
            f"<section><h2>Halogens</h2><table class='lad'>{ht}</table></section></div>")
    css = """.cols{display:grid;grid-template-columns:1.3fr 1fr;gap:40px;margin-top:6px}
    .lad{border-collapse:separate;border-spacing:0 3px} .lad td{border:none;padding:1px 6px} .lad tr.g td{border-top:10px solid transparent}
    .lad tr.g td.arr{border-top:none} .lad .m{border:1px solid #2E3338;border-radius:4px;width:58px;text-align:center;
    font-weight:700;font-size:12pt;padding:2px 0} .lad .m.h{border-style:dashed}
    .lad tr td.m{border-left:1px solid #2E3338} .al{font-size:9pt;color:#2E3338;vertical-align:middle;width:2.2in;padding-left:14px!important;
    background:linear-gradient(#B84100,#B84100) 6px 3px/1.5px calc(100% - 6px) no-repeat}
    .arr{width:46px;vertical-align:top;padding:0 8px 0 0!important;position:relative}
    .arr .top,.arr .bot{font-size:8pt;font-weight:700;color:#B84100;text-align:center;line-height:1.1}
    .arr .bot{position:absolute;bottom:0;left:0;right:8px}
    .arr .line{position:absolute;top:24px;bottom:24px;left:calc(50% - 4px);border-left:1.5px solid #B84100}
    .arr .line:after{content:'';position:absolute;bottom:-2px;left:-5.5px;border:4.5px solid transparent;border-top:8px solid #B84100}"""
    return page("Activity Series", body, extra_css=css)

# ---------- 11 Strong acids & bases ----------
def sheet_acids():
    a = "".join(f"<tr><td class='f'>{F(f)}</td><td>{n}</td></tr>" for f, n in D.STRONG_ACIDS)
    b = "".join(f"<tr><td class='f'>{F(f)}</td><td>{n}</td></tr>" for f, n in D.STRONG_BASES)
    body = (f"<p class='note'>Strong acids and bases ionize completely in water. Treat any acid or base not on this "
            "sheet as weak.</p><div class='cols'>"
            f"<section><h2>Strong Acids</h2><table class='ab'>{a}</table></section>"
            f"<section><h2>Strong Bases</h2><table class='ab'>{b}</table><p class='note'>Group 1 hydroxides, and the "
            "hydroxides of Ca, Sr and Ba.</p></section></div>")
    css = """.cols{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-top:8px} .ab{width:100%}
    .ab td{border:none;border-bottom:0.75px solid #C8CDC2;padding:6px 6px;font-size:11pt} .ab .f{font-weight:700;font-size:13pt;width:38%}"""
    return page("Strong Acids &amp; Bases", body, extra_css=css)

# ---------- 12 Specific heats ----------
def sheet_specific_heats():
    r = "".join(f"<tr><td>{n}</td><td class='v'>{v}</td></tr>" for n, v in D.SPECIFIC_HEATS)
    body = (f"<p class='note'>Specific heat (c) is the energy needed to raise 1 g of a substance by 1 °C. "
            f"Use it in q = mcΔT (Equations sheet).</p><table class='sh'><tr><th>Substance</th><th>c, J/(g·°C)</th></tr>{r}</table>")
    css = """.sh{width:62%;margin-top:8px} .sh td{padding:5px 12px;font-size:11pt} .sh .v{text-align:right;font-weight:700;
    font-variant-numeric:tabular-nums;width:40%} .sh th{padding:5px 12px} .sh th:last-child{text-align:right}"""
    return page("Specific Heats", body, extra_css=css)

SHEETS = [("Equations", sheet_equations), ("Sig Figs", sheet_sigfigs), ("VSEPR Shapes", sheet_vsepr),
          ("Periodic Table", sheet_periodic), ("Electronegativity", sheet_electronegativity),
          ("Polyatomic Ions", sheet_polyatomic), ("Naming Toolkit", sheet_naming),
          ("Multi-Charge Metals", sheet_multicharge), ("Solubility", sheet_solubility),
          ("Activity Series", sheet_activity), ("Strong Acids & Bases", sheet_acids),
          ("Specific Heats", sheet_specific_heats)]

def main(out):
    os.makedirs(out, exist_ok=True)
    titles = reference_titles("chemistry")
    order = []
    for short, fn in SHEETS:
        if short not in titles:
            sys.exit(f"'{short}' has no REF row in courses/chemistry/DECISIONS.md - refusing to invent a filename")
        pdf = document_name("Reference", [], None, topic=short, scope="course")
        path = os.path.join(out, pdf[:-4] + ".html")
        open(path, "w").write(fn())
        order.append(pdf)
    if "Full Packet" not in titles: sys.exit("no REF row for Full Packet")
    open(os.path.join(out, "order.txt"), "w").write("\n".join(order + [document_name("Reference", [], None, topic="Full Packet", scope="course")]))
    print("\n".join(order))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "output", "chemistry", "reference"))
