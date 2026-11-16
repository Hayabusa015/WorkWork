"""Geology U3 S3.1 Mineral ID Data Sheet (exploration) + teacher reference key.
Students choose 10-15 minerals from the trays and record every property for each.
Geology has no lab notebook, so the data table is on the sheet (QA_GATE scopes the
no-write rule to courses that use notebooks)."""
import os, re
HERE = os.environ.get("OUT_DIR", os.path.dirname(os.path.abspath(__file__)))
TPL = "/home/user/WorkWork/templates/lab"

def head(src, title):
    h = open(os.path.join(TPL, src), encoding="utf-8").read()
    h = h[:h.index("</head>")]
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", h, flags=re.S)
    return re.sub(r"<!--.*?-->", "", h, flags=re.S)

CSS = """
<style>
  @page { size: letter landscape; margin: 0.35in 0.4in 0.45in 0.4in; }
  .masthead h1 { font-size: 15pt; }
  table.id { width: 100%; border-collapse: collapse; margin-top: 5pt; table-layout: fixed; }
  table.id th { font-family: var(--display); font-weight: 600; font-size: 6.6pt; letter-spacing: 0.12em;
     text-align: left; vertical-align: bottom; padding: 0 4pt 3pt 4pt; border-bottom: 1.2pt solid var(--accent); }
  table.id th small { display: block; font-weight: 400; letter-spacing: 0.02em; font-size: 6.6pt;
     color: var(--label); text-transform: none; }
  table.id td { border: 0.6pt solid var(--rule-hairline); height: 0.6in; vertical-align: top; padding-top: 3pt; padding: 0 4pt; font-size: 8.6pt; }
  table.id td.n { width: 0.28in; text-align: center; font-family: var(--display); font-weight: 700;
     color: var(--accent); border-left: none; }
  table.id td.req { }
  .circ { color: var(--label); font-size: 7.6pt; letter-spacing: 0.04em; }
  .strip { display: flex; gap: 16pt; font-size: 8.4pt; margin: 4pt 0 0 0; color: var(--ink); }
  .strip b { font-family: var(--display); }
  .key table.id td { height: auto; vertical-align: middle; padding: 2.4pt 4pt; font-size: 8.2pt; }
  .opt { font-size: 7.4pt; color: var(--label); font-family: var(--display); letter-spacing: 0.12em; }
  .wl { border-bottom: 0.6pt solid var(--ink); height: 0.3in; }
</style>
"""

COLS = ('<tr><th style="width:0.28in">#</th>'
        '<th style="width:1.45in">MINERAL<small>from the tray label</small></th>'
        '<th style="width:1.05in">COLOR</th>'
        '<th style="width:0.95in">STREAK<small>color of the powder</small></th>'
        '<th style="width:0.95in">LUSTER<small>circle: M = metallic, NM = nonmetallic</small></th>'
        '<th style="width:1.35in">HARDNESS RANGE<small>e.g. 2.5–3.5, or &gt; 6.5</small></th>'
        '<th style="width:1.6in">CLEAVAGE OR FRACTURE<small>circle C or F, then describe</small></th>'
        '<th>SPECIAL PROPERTY<small>magnet, fizz, feel, other</small></th></tr>')

def rows(n0, n1):
    out = []
    for i in range(n0, n1 + 1):
        out.append(f'<tr><td class="n">{i}</td><td></td><td></td><td></td>'
                   '<td><span class="circ">M &nbsp;&nbsp; NM</span></td><td></td>'
                   '<td><span class="circ">C &nbsp;&nbsp; F</span></td><td></td></tr>')
    return "\n".join(out)

STRIP = ('<div class="strip"><span><b>Hardness tools:</b> fingernail ≈ 2.5 · copper ≈ 3.5 · '
         'glass ≈ 5.5 · steel nail ≈ 6.5</span><span><b>Streak:</b> rub on the back of the streak plate</span>'
         '<span><b>Cleavage</b> = flat planes · <b>Fracture</b> = uneven or curved</span></div>')

def student():
    h = head("SHULL_Lab_TEMPLATE_MASTER.html", "3.1 Lab - Mineral ID Data Sheet")
    return h + CSS + f"""</head><body class="geo">
<div class="meta"><span class="m-course">GEOLOGY</span><span class="m-code">U03 / S03.1</span><span class="m-fright">MINERAL ID DATA SHEET</span></div>
<div class="masthead"><div class="eyebrow">UNIT 3 — ROCKS &amp; MINERALS · SECTION 1 · MINERAL LAB</div>
<div class="titlerow"><h1>Mineral ID: <span class="accent">Test</span> Every Property</h1><div class="chip">U03 / S03.1</div></div></div>
<div class="id-row"><div class="name"><div class="f">&nbsp;</div><div class="lbl">NAME</div></div>
<div class="date"><div class="f">&nbsp;</div><div class="lbl">DATE</div></div>
<div class="per"><div class="f">&nbsp;</div><div class="lbl">PERIOD</div></div></div>
<p style="font-size:9.4pt; margin:2pt 0 0 0"><b>Your job:</b> choose at least <b>10</b> minerals from the trays (rows 11–15 are a bonus). For each one, run every test and fill in the whole row. Put each sample back on its own tray before you take another.</p>
{STRIP}
<table class="id">{COLS}{rows(1, 8)}</table>
<div class="pagebreak"></div>
<div class="runhead">U03 / S03.1 · MINERAL ID DATA SHEET</div>
<table class="id">{COLS}{rows(9, 15)}</table>
<h2>WRAP-UP</h2>
<ol class="q">
<li>Which two of your minerals were hardest to tell apart? Which test finally separated them?<div class="wl"></div></li>
<li>Find a mineral whose color and streak did not match. Name it and give both colors.<div class="wl"></div></li>
</ol>
</body></html>"""

# name, color, streak, luster, hardness, tool range, cleavage/fracture, special
REF = [
 ("Quartz", "Colorless, white, pink, purple", "None (scratches plate)", "Nonmetallic, glassy", "7", "> 6.5", "Fracture, curved (conchoidal)", "Scratches glass"),
 ("Orthoclase feldspar", "Pink, white", "White", "Nonmetallic, glassy", "6", "5.5–6.5", "Cleavage, 2 planes near 90°", "Blocky breaks"),
 ("Plagioclase feldspar", "White, gray", "White", "Nonmetallic, glassy", "6", "5.5–6.5", "Cleavage, 2 planes near 90°", "Fine parallel lines (striations)"),
 ("Muscovite mica", "Clear, silvery", "White", "Nonmetallic, pearly", "2–2.5", "2.5 or less", "Cleavage, 1 direction: thin sheets", "Sheets peel and bend"),
 ("Biotite mica", "Black, brown", "White to gray", "Nonmetallic, glassy to pearly", "2.5–3", "2.5–3.5", "Cleavage, 1 direction: thin sheets", "Sheets peel"),
 ("Hornblende", "Black, dark green", "Gray-green", "Nonmetallic, glassy", "5–6", "3.5–6.5", "Cleavage, 2 planes (not 90°)", "Long, shiny crystals"),
 ("Augite", "Dark green, black", "Gray-green", "Nonmetallic, dull to glassy", "5.5–6", "5.5–6.5", "Cleavage, 2 planes near 90°", "Stubby dark crystals"),
 ("Olivine", "Olive green", "White", "Nonmetallic, glassy", "6.5–7", "> 6.5", "Fracture, curved", "Sugary green grains"),
 ("Garnet", "Dark red, brown", "White", "Nonmetallic, glassy", "6.5–7.5", "> 6.5", "Fracture, uneven", "Rounded 12-sided crystals"),
 ("Calcite", "White, colorless", "White", "Nonmetallic, glassy", "3", "2.5–3.5", "Cleavage, 3 directions: slanted blocks", "Fizzes in dilute acid; double image"),
 ("Dolomite", "White, pink", "White", "Nonmetallic, glassy to pearly", "3.5–4", "3.5–5.5", "Cleavage, 3 directions: slanted blocks", "Fizzes only when powdered"),
 ("Gypsum", "White, colorless", "White", "Nonmetallic, glassy to silky", "2", "< 2.5", "Cleavage, 1 good direction", "Fingernail scratches it"),
 ("Halite", "Colorless, white", "White", "Nonmetallic, glassy", "2.5", "about 2.5", "Cleavage, 3 directions: cubes", "Salty (never taste)"),
 ("Fluorite", "Purple, green, yellow, clear", "White", "Nonmetallic, glassy", "4", "3.5–5.5", "Cleavage, 4 directions", "Some glow under UV light"),
 ("Talc", "White, pale green, gray", "White", "Nonmetallic, pearly to greasy", "1", "< 2.5", "Cleavage, 1 direction", "Feels soapy"),
 ("Pyrite", "Brassy gold", "Greenish-black", "Metallic", "6–6.5", "5.5–6.5", "Fracture, uneven", "Cube-shaped crystals; 'fool's gold'"),
 ("Galena", "Lead gray", "Gray", "Metallic", "2.5", "about 2.5", "Cleavage, 3 directions: cubes", "Very heavy for its size"),
 ("Hematite", "Silver-black or red-brown", "Red-brown", "Metallic or earthy", "5–6.5", "3.5–6.5", "Fracture, uneven", "Red-brown streak"),
 ("Magnetite", "Black", "Black", "Metallic", "5.5–6.5", "5.5–6.5", "Fracture, uneven", "Magnetic"),
 ("Graphite", "Black, gray", "Black-gray", "Metallic to dull", "1–2", "< 2.5", "Cleavage, 1 direction", "Greasy; marks paper"),
 ("Sulfur", "Bright yellow", "White to pale yellow", "Nonmetallic, resinous", "1.5–2.5", "< 2.5", "Fracture, uneven", "Bright yellow; brittle, crumbles"),
 ("Kaolinite", "White", "White", "Nonmetallic, dull (earthy)", "2–2.5", "< 2.5", "Fracture, earthy (crumbles)", "Smells earthy; chalky feel"),
]

def key():
    h = head("SHULL_Lab_TEMPLATE_TEACHER_KEY.html", "3.1 Lab Key - Mineral ID Data Sheet")
    body = "".join(f"<tr><td><b>{r[0]}</b></td>" + "".join(f"<td>{x}</td>" for x in r[1:]) + "</tr>" for r in REF)
    return h + CSS + f"""</head><body class="geo key">
<div class="meta"><span class="m-course">GEOLOGY</span><span class="m-code">U03 / S03.1</span></div>
<div class="masthead"><div class="eyebrow">TEACHER REFERENCE · UNIT 3 — ROCKS &amp; MINERALS · SECTION 1</div>
<div class="titlerow"><h1>Mineral ID Data Sheet: Reference Values</h1><div class="chip">U03 / S03.1 · KEY</div></div></div>
<p style="font-size:9pt; margin:4pt 0">Students choose their own minerals, so there is no single answer key. Check rows against these
typical values. Real samples vary, especially in color, so accept any answer that matches what the student's sample shows.
Hardness range is what the field tools can show (fingernail 2.5 · copper 3.5 · glass 5.5 · steel 6.5); the Mohs number is for reference.</p>
<table class="id"><tr><th style="width:1.25in">MINERAL</th><th style="width:1.35in">COLOR</th><th style="width:1.05in">STREAK</th><th style="width:1.2in">LUSTER</th><th style="width:0.55in">MOHS</th><th style="width:0.8in">TOOL RANGE</th><th style="width:1.55in">CLEAVAGE OR FRACTURE</th><th>SPECIAL PROPERTY</th></tr>{body}</table>
<p style="font-size:8.4pt; margin-top:5pt"><b>Wrap-up 1:</b> any pair with the test that split them (e.g. calcite vs. quartz: hardness or acid fizz).
<b>Wrap-up 2:</b> hematite (silver-black, streak red-brown) or pyrite (gold, streak greenish-black) are the likely answers.
<b>Acid:</b> if you run the fizz test, verify the acid against the SDS and district policy first; students bring samples to you.</p>
</body></html>"""

for name, fn in (("3.1 Lab - Mineral ID Data Sheet.html", student), ("3.1 Lab Key - Mineral ID Data Sheet.html", key)):
    open(os.path.join(HERE, name), "w", encoding="utf-8").write(fn())
print("ok")
