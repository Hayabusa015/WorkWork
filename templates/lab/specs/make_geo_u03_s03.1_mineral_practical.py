"""Geology U3 S3.1 Mineral ID Practical (17 specimens): answer sheet, ID chart, teacher key.

    OUT_DIR=<folder> python3 templates/lab/specs/make_geo_u03_s03.1_mineral_practical.py
    python3 templates/lab/build_lab.py "<folder>/3.1 Lab - Mineral ID Practical.html"

Matt's container, specimens 1-17 (2026-11-25): talc, magnetite, hematite, galena, sulfur,
apatite, quartz, olivine, feldspar, pyrite, halite, sodalite, fluorite, muscovite, kyanite,
calcite, biotite. Students test each specimen, record its properties, and name it from the
ID chart. The chart holds 30 minerals: all 17 plus look-alikes, so a name has to come from the
tests, not from elimination. Graded on accuracy.
"""
import os, re

HERE = os.environ.get("OUT_DIR", os.path.dirname(os.path.abspath(__file__)))
TPL = "/home/user/WorkWork/templates/lab"

SPECIMENS = ["Talc", "Magnetite", "Hematite", "Galena", "Sulfur", "Apatite", "Quartz", "Olivine",
             "Feldspar", "Pyrite", "Halite", "Sodalite", "Fluorite", "Muscovite", "Kyanite",
             "Calcite", "Biotite"]

# Chart rows: (mohs, streak, color, cleavage/fracture, other clues, name)
CHART = [
 ("METALLIC LUSTER · shines like metal", [
  ("1–2", "Black-gray", "Black to steel gray", "Cleavage, 1 direction", "Greasy feel; marks paper", "Graphite"),
  ("2.5", "Gray", "Lead gray", "Cleavage, 3 directions (cubes)", "Very heavy for its size", "Galena"),
  ("3.5–4", "Greenish-black", "Brassy yellow; may tarnish", "Fracture, uneven", "Softer than pyrite; a nail scratches it", "Chalcopyrite"),
  ("5–6.5", "Red-brown", "Silver-gray to black, or red-brown", "Fracture, uneven", "Red-brown streak; not magnetic", "Hematite"),
  ("5.5–6.5", "Black", "Black", "Fracture, uneven", "Strongly magnetic", "Magnetite"),
  ("6–6.5", "Greenish-black", "Brassy gold", "Fracture, uneven", "Cube-shaped crystals; 'fool's gold'", "Pyrite"),
 ]),
 ("NONMETALLIC · SOFT · your fingernail scratches it (under 2.5)", [
  ("1", "White", "White, pale green, gray", "Cleavage, 1 direction", "Feels soapy", "Talc"),
  ("1.5–2.5", "White to pale yellow", "Bright yellow", "Fracture, uneven", "Brittle; crumbles", "Sulfur"),
  ("2", "White", "Clear, white", "Cleavage, 1 good direction", "Fingernail scratches it easily", "Gypsum"),
  ("2–2.5", "White", "White", "Fracture, earthy (crumbles)", "Chalky; smells earthy", "Kaolinite"),
  ("2–2.5", "White", "Clear, silvery, light brown", "Cleavage, 1 direction (thin sheets)", "Clear sheets peel and bend", "Muscovite mica"),
 ]),
 ("NONMETALLIC · MEDIUM · fingernail cannot scratch it; it cannot scratch glass (2.5–5.5)", [
  ("2.5", "White", "Clear, white, pink", "Cleavage, 3 directions (cubes)", "Salty taste (never taste)", "Halite"),
  ("2.5–3", "White to gray", "Black, dark brown", "Cleavage, 1 direction (thin sheets)", "Dark sheets peel", "Biotite mica"),
  ("3", "White", "Clear, white", "Cleavage, 3 directions (slanted blocks)", "Fizzes in dilute acid; clear pieces show a double image", "Calcite"),
  ("3.5–4", "White", "White, pink", "Cleavage, 3 directions (slanted blocks)", "Fizzes only when powdered", "Dolomite"),
  ("3.5–4", "Light blue", "Deep blue", "Fracture, uneven", "Fizzes in dilute acid", "Azurite"),
  ("3.5–4", "Light green", "Green, often banded", "Fracture, uneven", "Fizzes in dilute acid", "Malachite"),
  ("4", "White", "Purple, green, yellow, clear", "Cleavage, 4 directions", "Cubes or 8-sided crystals; some glow under UV", "Fluorite"),
  ("4–5.5", "Yellow-brown", "Yellow-brown to brown", "Fracture, earthy", "Rusty look", "Limonite"),
  ("4.5–7 *", "White", "Blue to blue-gray", "Cleavage, 1 direction", "Long blade-shaped crystals; *softer along the blade than across it", "Kyanite"),
  ("5", "White", "Green, blue, brown, yellow", "Fracture, uneven to curved", "Six-sided crystals; just softer than glass", "Apatite"),
 ]),
 ("NONMETALLIC · HARD · it scratches glass (over 5.5)", [
  ("5–6", "Gray-green", "Black, dark green", "Cleavage, 2 directions (not 90°)", "Long, shiny dark crystals", "Hornblende"),
  ("5.5–6", "Gray-green", "Dark green, black", "Cleavage, 2 directions (near 90°)", "Short, stubby dark crystals", "Augite"),
  ("5.5–6", "White to light blue", "Royal blue, often with white veins", "Fracture, uneven", "Blue with white streaks through it", "Sodalite"),
  ("6", "White", "Pink, salmon, white", "Cleavage, 2 directions (near 90°)", "Blocky breaks", "Feldspar (orthoclase)"),
  ("6", "White", "White, gray", "Cleavage, 2 directions (near 90°)", "Fine parallel lines on flat faces", "Feldspar (plagioclase)"),
  ("6.5–7", "White", "Olive green", "Fracture, curved", "Sugary green grains", "Olivine"),
  ("6.5–7.5", "White", "Dark red, brown", "Fracture, uneven", "Rounded 12-sided crystals", "Garnet"),
  ("7", "White (or none)", "Clear, white, pink, purple", "Fracture, curved (shell-like)", "Six-sided crystals; scratches glass easily", "Quartz"),
  ("8", "White (or none)", "Clear, yellow, blue", "Cleavage, 1 direction", "Harder than quartz", "Topaz"),
  ("9", "White (or none)", "Gray, brown, red, blue", "Fracture, uneven", "Six-sided barrel crystals; extremely hard", "Corundum"),
 ]),
]

# Key: what each specimen should show. (color, streak, luster, tool range, C/F, special)
KEY = {
 "Talc": ("White to pale green", "White", "NM", "< 2.5", "C, 1 direction", "Soapy feel"),
 "Magnetite": ("Black", "Black", "M", "5.5–6.5", "F, uneven", "Magnetic"),
 "Hematite": ("Silver-black or red-brown", "Red-brown", "M (or earthy)", "3.5–6.5", "F, uneven", "Red-brown streak"),
 "Galena": ("Lead gray", "Gray", "M", "about 2.5", "C, cubes", "Very heavy"),
 "Sulfur": ("Bright yellow", "Pale yellow to white", "NM", "< 2.5", "F, uneven", "Brittle"),
 "Apatite": ("Green, blue or brown", "White", "NM", "3.5–5.5", "F", "Six-sided crystals"),
 "Quartz": ("Clear, white or pink", "White / none", "NM", "> 6.5", "F, curved", "Scratches glass"),
 "Olivine": ("Olive green", "White", "NM", "> 6.5", "F, curved", "Sugary grains"),
 "Feldspar": ("Pink or white", "White", "NM", "5.5–6.5", "C, 2 near 90°", "Blocky breaks"),
 "Pyrite": ("Brassy gold", "Greenish-black", "M", "5.5–6.5", "F, uneven", "Cubes; fool's gold"),
 "Halite": ("Clear to white", "White", "NM", "about 2.5", "C, cubes", "Salty (not tasted)"),
 "Sodalite": ("Royal blue, white veins", "White to light blue", "NM", "5.5–6.5", "F, uneven", "Blue with white veins"),
 "Fluorite": ("Purple, green or clear", "White", "NM", "3.5–5.5", "C, 4 directions", "8-sided or cube crystals"),
 "Muscovite": ("Clear, silvery", "White", "NM", "2.5 or less", "C, sheets", "Clear sheets peel"),
 "Kyanite": ("Blue", "White", "NM", "varies by direction", "C, 1 direction", "Blade-shaped"),
 "Calcite": ("Clear to white", "White", "NM", "2.5–3.5", "C, slanted blocks", "Fizzes; double image"),
 "Biotite": ("Black to dark brown", "White to gray", "NM", "2.5–3.5", "C, sheets", "Dark sheets peel"),
}
NOTES = {
 "Hematite": "Accept silver-black or red-brown color; the streak decides it.",
 "Feldspar": "Accept feldspar, orthoclase or plagioclase.",
 "Muscovite": "Accept muscovite or mica.",
 "Biotite": "Accept biotite or mica; muscovite is wrong (biotite is dark).",
 "Kyanite": "Hardness changes with direction; accept any range they measured.",
 "Calcite": "Without acid, hardness 3 plus slanted-block cleavage identifies it.",
 "Sodalite": "Look-alikes on the chart: azurite (fizzes, softer) and kyanite (blades).",
 "Pyrite": "Look-alike: chalcopyrite. A steel nail scratches chalcopyrite, not pyrite.",
 "Magnetite": "Look-alikes: hematite (red-brown streak), graphite (soft, marks paper).",
}


def head(src, title):
    h = open(os.path.join(TPL, src), encoding="utf-8").read()
    h = h[:h.index("</head>")]
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", h, flags=re.S)
    return re.sub(r"<!--.*?-->", "", h, flags=re.S)


CSS = """
<style>
  @page { size: letter landscape; margin: 0.35in 0.4in 0.45in 0.4in; }
  .masthead h1 { font-size: 15pt; }
  table.id { width: 100%; border-collapse: collapse; margin-top: 4pt; table-layout: fixed; }
  table.id th { font-family: var(--display); font-weight: 600; font-size: 6.6pt; letter-spacing: 0.12em;
     text-align: left; vertical-align: bottom; padding: 0 4pt 3pt 4pt; border-bottom: 1.2pt solid var(--accent); }
  table.id th small { display: block; font-weight: 400; letter-spacing: 0.02em; font-size: 6.6pt; color: var(--label); }
  table.id td { border: 0.6pt solid var(--rule-hairline); height: 0.56in; padding: 3pt 4pt 0 4pt;
     font-size: 8.6pt; vertical-align: top; }
  table.id td.n { text-align: center; vertical-align: middle; font-family: var(--display); font-weight: 700;
     font-size: 11pt; color: var(--accent); border-left: none; }
  table.id td.name { border: 1.2pt solid var(--ink); }
  .circ { color: var(--label); font-size: 7.6pt; letter-spacing: 0.04em; }
  .strip { display: flex; gap: 16pt; font-size: 8.4pt; margin: 3pt 0 0 0; }
  .strip b { font-family: var(--display); }
  table.chart { width: 100%; border-collapse: collapse; table-layout: fixed; }
  table.chart th { font-family: var(--display); font-weight: 600; font-size: 6.6pt; letter-spacing: 0.12em;
     text-align: left; padding: 0 4pt 2pt 4pt; border-bottom: 1.2pt solid var(--accent); }
  table.chart td { border-bottom: 0.6pt solid var(--rule-hairline); padding: 2.2pt 4pt; font-size: 8.3pt;
     line-height: 1.22; vertical-align: top; }
  table.chart tr.grp td { font-family: var(--display); font-weight: 700; font-size: 7.6pt; letter-spacing: 0.1em;
     color: var(--accent); border-bottom: 1pt solid var(--accent); padding-top: 7pt; }
  table.chart td.mn { font-weight: 700; }
  .key table.id td { height: auto; padding: 2.6pt 4pt; font-size: 8.2pt; vertical-align: middle; }
  .score { float: right; font-family: var(--display); font-weight: 600; font-size: 9pt; }
  .fine { font-size: 8.2pt; color: var(--label); }
</style>
"""

def meta(code_right):
    return (f'<div class="meta"><span class="m-course">GEOLOGY</span><span class="m-code">U03 / S03.1</span>'
            f'<span class="m-fright">{code_right}</span></div>')

IDROW = ('<div class="id-row"><div class="name"><div class="f">&nbsp;</div><div class="lbl">NAME</div></div>'
         '<div class="date"><div class="f">&nbsp;</div><div class="lbl">DATE</div></div>'
         '<div class="per"><div class="f">&nbsp;</div><div class="lbl">PERIOD</div></div></div>')

COLS = ('<tr><th style="width:0.4in">#</th><th style="width:1.15in">COLOR</th>'
        '<th style="width:1.0in">STREAK</th><th style="width:0.75in">LUSTER<small>M or NM</small></th>'
        '<th style="width:1.15in">HARDNESS RANGE<small>from your scratch tests</small></th>'
        '<th style="width:1.45in">CLEAVAGE OR FRACTURE<small>circle, then describe</small></th>'
        '<th>SPECIAL PROPERTY<small>magnet, feel, crystal shape...</small></th>'
        '<th style="width:1.65in">MINERAL NAME<small>from the ID chart</small></th></tr>')

def rows(a, b):
    return "".join(f'<tr><td class="n">{i}</td><td></td><td></td><td><span class="circ">M &nbsp; NM</span></td>'
                   f'<td></td><td><span class="circ">C &nbsp; F</span></td><td></td><td class="name"></td></tr>'
                   for i in range(a, b + 1))

STRIP = ('<div class="strip"><span><b>Hardness tools:</b> fingernail ≈ 2.5 · copper ≈ 3.5 · glass ≈ 5.5 · '
         'steel nail ≈ 6.5</span><span><b>Streak:</b> back of the streak plate</span>'
         '<span><b>Magnet</b> on every dark metallic sample</span></div>')


def practical():
    return head("SHULL_Lab_TEMPLATE_MASTER.html", "3.1 Lab - Mineral ID Practical") + CSS + f"""</head><body class="geo">
{meta("MINERAL ID PRACTICAL")}
<div class="masthead"><div class="eyebrow">UNIT 3 — ROCKS &amp; MINERALS · SECTION 1 · MINERAL PRACTICAL</div>
<div class="titlerow"><h1>Mineral ID Practical: <span class="accent">Name</span> All 17</h1><div class="chip">U03 / S03.1</div></div></div>
{IDROW}
<p style="font-size:9.4pt; margin:2pt 0 0 0"><span class="score">SCORE ______ / 17</span><b>Directions:</b> work through specimens
1–17 in order. Run every test and record what you see. Then use the <b>Mineral ID Chart</b> to name the mineral. You are graded on
the mineral names, so let the tests decide. Return each specimen to its numbered spot.</p>
{STRIP}
<table class="id">{COLS}{rows(1, 9)}</table>
<div class="pagebreak"></div>
<div class="runhead">U03 / S03.1 · MINERAL ID PRACTICAL</div>
<table class="id">{COLS}{rows(10, 17)}</table>
</body></html>"""


def chart():
    hdr = ('<table class="chart"><tr><th style="width:0.7in">HARDNESS</th><th style="width:1.35in">STREAK</th>'
           '<th style="width:1.9in">COLOR</th><th style="width:2.0in">CLEAVAGE OR FRACTURE</th><th>OTHER CLUES</th>'
           '<th style="width:1.45in">MINERAL</th></tr>')
    body = hdr
    for gi, (grp, items) in enumerate(CHART):
        if gi == 3:   # the HARD group opens page 2 with its own header row
            body += ('</table><div class="pagebreak"></div>'
                     '<div class="runhead">U03 / S03.1 · MINERAL ID CHART</div>' + hdr)
        body += f'<tr class="grp"><td colspan="6">{grp}</td></tr>'
        for m, s, c, cf, o, n in items:
            body += f"<tr><td>{m}</td><td>{s}</td><td>{c}</td><td>{cf}</td><td>{o}</td><td class='mn'>{n}</td></tr>"
    body += "</table>"
    return head("SHULL_Lab_TEMPLATE_MASTER.html", "3.1 Mineral ID Chart") + CSS + f"""</head><body class="geo">
{meta("MINERAL ID CHART")}
<div class="masthead"><div class="eyebrow">UNIT 3 — ROCKS &amp; MINERALS · SECTION 1 · REFERENCE</div>
<div class="titlerow"><h1>Mineral <span class="accent">ID</span> Chart</h1><div class="chip">U03 / S03.1</div></div></div>
<p style="font-size:8.8pt; margin:4pt 0 3pt 0"><b>How to use it:</b> start with <b>luster</b>. If it is nonmetallic, use your
<b>hardness</b> test to pick the group. Then match <b>streak</b>, <b>cleavage or fracture</b> and the other clues. Color helps, but it
is the least reliable clue. Do not write on this chart.</p>
{body}
<p class="fine" style="margin-top:4pt">Hardness tools: fingernail ≈ 2.5 · copper ≈ 3.5 · glass ≈ 5.5 · steel nail ≈ 6.5.
Minerals near a boundary (hornblende, apatite) can test either way.</p>
</body></html>"""


def key():
    rowsk = ""
    for i, m in enumerate(SPECIMENS, 1):
        k = KEY[m]
        rowsk += (f"<tr><td class='n' style='font-size:9pt'>{i}</td><td><b>{m}</b></td>"
                  + "".join(f"<td>{x}</td>" for x in k) + f"<td>{NOTES.get(m, '')}</td></tr>")
    return head("SHULL_Lab_TEMPLATE_TEACHER_KEY.html", "3.1 Lab Key - Mineral ID Practical") + CSS + f"""</head><body class="geo key">
<div class="meta"><span class="m-course">GEOLOGY</span><span class="m-code">U03 / S03.1</span></div>
<div class="masthead"><div class="eyebrow">TEACHER KEY · UNIT 3 — ROCKS &amp; MINERALS · SECTION 1</div>
<div class="titlerow"><h1>Mineral ID Practical: Answer Key</h1><div class="chip">U03 / S03.1 · KEY</div></div></div>
<p style="font-size:8.8pt; margin:4pt 0">Grade the <b>mineral name</b>, 1 point each (17). The property columns show what each specimen
should test as; use them to see where a wrong answer went wrong. Real samples vary, especially in color.</p>
<table class="id"><tr><th style="width:0.3in">#</th><th style="width:0.9in">MINERAL</th><th style="width:1.1in">COLOR</th>
<th style="width:0.95in">STREAK</th><th style="width:0.55in">LUSTER</th><th style="width:0.85in">HARDNESS</th>
<th style="width:0.95in">CLEAVAGE / FRACTURE</th><th style="width:1.05in">SPECIAL</th><th>GRADING NOTES</th></tr>{rowsk}</table>
<h2>SETUP</h2>
<p style="font-size:8.6pt">Per station: streak plate, glass plate, steel nail, copper coin, magnet, hand lens. Specimens stay in
numbered order. If you run an acid station for calcite, check the acid against the SDS and district policy first; the
practical can be done without it.</p>
</body></html>"""


for name, fn in (("3.1 Lab - Mineral ID Practical.html", practical),
                 ("3.1 Mineral ID Chart.html", chart),
                 ("3.1 Lab Key - Mineral ID Practical.html", key)):
    open(os.path.join(HERE, name), "w", encoding="utf-8").write(fn())
print("ok")
