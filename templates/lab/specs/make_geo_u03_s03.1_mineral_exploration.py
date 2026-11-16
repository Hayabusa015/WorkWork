"""Geology U3 S3.1 Mineral Exploration Lab: student handout + teacher key, one source.

Matt's design (2026-11-11): an exploration, not an ID quiz. Students pick a mineral off a
tray (the name is on the tray), run the tests, and write that mineral under the property it
shows best - three minerals per property. A mineral may be used twice at most.

Geology has no lab notebook (DECISIONS: no formal lab report cycle), so unlike the
Chemistry/Physics labs this handout carries its own fill-in grid. QA_GATE scopes the
no-write-space rule to "where the course uses lab notebooks".
"""
import os, re

HERE = os.environ.get("OUT_DIR", os.path.dirname(os.path.abspath(__file__)))
TPL = "/home/user/WorkWork/templates/lab"

# property, how to test it (student), example key answers (mineral, what stands out)
PROPS = [
    ("Color", "Look at the outside of the sample. What color is it?",
     [("Pyrite", "Brassy gold, looks like gold"), ("Sulfur", "Bright yellow"),
      ("Olivine", "Olive green")]),
    ("Streak", "Rub the sample on the streak plate. What color is the powder?",
     [("Hematite", "Looks silver-black, streak is red-brown"),
      ("Pyrite", "Looks gold, streak is greenish-black"), ("Galena", "Gray streak")]),
    ("Luster", "How does light reflect? Metallic, or nonmetallic (glassy, pearly, dull)?",
     [("Galena", "Shiny, metallic"), ("Quartz", "Glassy"), ("Talc", "Pearly")]),
    ("Hardness", "Scratch test: fingernail ≈ 2.5 · copper ≈ 3.5 · glass ≈ 5.5 · steel ≈ 6.5",
     [("Talc", "Fingernail scratches it (1)"), ("Gypsum", "Fingernail scratches it (2)"),
      ("Quartz", "Scratches glass (7)")]),
    ("Cleavage", "Does it break along flat planes? Sheets, cubes, or blocks?",
     [("Biotite", "Peels into thin sheets"), ("Halite", "Breaks into cubes"),
      ("Calcite", "Breaks into slanted blocks (rhombs)")]),
    ("Fracture", "Does it break unevenly or in curved, shell-like surfaces?",
     [("Quartz", "Curved, shell-like break"), ("Olivine", "Curved, uneven break"),
      ("Garnet", "Uneven break, no flat planes")]),
    ("Special properties", "Magnet test. Fizz test (teacher's station only). Anything else unusual?",
     [("Magnetite", "Sticks to the magnet"), ("Calcite", "Fizzes in dilute acid"),
      ("Talc", "Feels soapy")]),
]

KEY_ALSO = {
    "Color": "Also fine: azurite (blue), malachite (green), fluorite (purple, green), rose quartz (pink).",
    "Streak": "Also fine: magnetite (black streak), graphite (black, marks paper). Streak only works below about 6.5; quartz leaves no streak.",
    "Luster": "Also fine: pyrite (metallic), muscovite (pearly), sulfur (glassy to greasy), kaolinite (dull).",
    "Hardness": "Also fine: calcite (copper scratches it, 3), fluorite (4), orthoclase (scratches glass, 6), corundum (9).",
    "Cleavage": "Also fine: muscovite (sheets), galena (cubes), orthoclase (two planes near 90°), fluorite (4 directions).",
    "Fracture": "Also fine: pyrite (uneven to shell-like). Accept any sample with no flat breaks.",
    "Special properties": "Also fine: calcite (double image through a clear piece), graphite (marks paper, greasy), halite (salty - never let students taste).",
}


def head(src_path, title):
    html = open(os.path.join(TPL, src_path), encoding="utf-8").read()
    h = html[:html.index("</head>")]
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", h, flags=re.S)
    h = re.sub(r"<!--.*?-->", "", h, flags=re.S)
    return h


EXTRA_CSS = """
<style>
  .grid { display: flex; flex-wrap: wrap; gap: 7pt 12pt; margin-top: 4pt; }
  .prop { flex: 1 1 46%; max-width: 49%; border-top: 1.2pt solid var(--accent);
          padding-top: 3pt; page-break-inside: avoid; }
  .prop .pt { font-family: var(--display); font-weight: 700; font-size: 10pt; }
  .prop .how { font-size: 8.2pt; color: var(--label); line-height: 1.25; margin: 1pt 0 3pt 0;
                }
  .prop table { width: 100%; border-collapse: collapse; }
  .prop th { font-family: var(--display); font-weight: 600; font-size: 6.4pt; letter-spacing: 0.14em;
             color: var(--label); text-align: left; padding: 0 3pt 2pt 3pt;
             border-bottom: 0.8pt solid var(--ink); }
  .prop td { border-bottom: 0.6pt solid var(--rule-hairline); height: 0.31in; padding: 0 3pt;
             font-size: 9pt; vertical-align: middle; }
  .prop td.n { width: 36%; border-right: 0.6pt solid var(--rule-hairline); }
  .key .prop td { font-weight: 700; color: var(--accent); }
  .also { font-size: 7.8pt; color: var(--label); line-height: 1.25; margin-top: 2pt; }
  .steps { margin: 3pt 0 4pt 17pt; }
  .steps li { margin-bottom: 3pt; }
  .eg { border-left: 2.5pt solid var(--accent); padding: 4pt 0 4pt 10pt; margin: 6pt 0; font-size: 9.6pt; }
  .eg b { font-family: var(--display); }
  .wl { border-bottom: 0.6pt solid var(--ink); height: 0.3in; }
  .tight p { margin-bottom: 3pt; }
  table.data td { font-size: 9.3pt; padding: 2.8pt 4pt; }
</style>
"""


def grid(key):
    out = ['<div class="grid">']
    for name, how, ex in PROPS:
        rows = "".join(
            f'<tr><td class="n">{m if key else ""}</td><td>{w if key else ""}</td></tr>'
            for m, w in ex)
        also = f'<div class="also">{KEY_ALSO[name]}</div>' if key else ""
        out.append(f'''<div class="prop"><div class="pt">{name}</div><div class="how">{how}</div>
<table><tr><th>MINERAL</th><th>WHAT STOOD OUT</th></tr>{rows}</table>{also}</div>''')
    out.append("</div>")
    return "\n".join(out)


GUIDE = """
<table class="data">
<tr><th>PROPERTY</th><th>TOOL</th><th>WHAT TO LOOK FOR</th></tr>
<tr><td><b>Color</b></td><td>Your eyes</td><td>The outside color. It can fool you, so test the powder too.</td></tr>
<tr><td><b>Streak</b></td><td>Streak plate</td><td>The color of the powder left on the plate.</td></tr>
<tr><td><b>Luster</b></td><td>Your eyes</td><td>How light reflects: metallic, or glassy, pearly or dull.</td></tr>
<tr><td><b>Hardness</b></td><td>Fingernail, copper, glass plate, steel nail</td><td>What scratches it, and what it scratches. Fingernail ≈ 2.5, copper ≈ 3.5, glass ≈ 5.5, steel ≈ 6.5.</td></tr>
<tr><td><b>Cleavage</b></td><td>Hand lens</td><td>Flat, shiny break surfaces: thin sheets, cubes or blocks.</td></tr>
<tr><td><b>Fracture</b></td><td>Hand lens</td><td>Uneven or curved, shell-like breaks with no flat planes.</td></tr>
<tr><td><b>Special properties</b></td><td>Magnet; teacher's acid station</td><td>Sticks to a magnet? Fizzes in dilute acid? Feels soapy?</td></tr>
</table>
"""


def student():
    h = head("SHULL_Lab_TEMPLATE_MASTER.html", "3.1 Lab - Mineral Exploration")
    body = f"""{EXTRA_CSS}
</head>
<body class="geo">
<div class="meta"><span class="m-course">GEOLOGY</span><span class="m-code">U03 / S03.1</span><span class="m-fright">MINERAL EXPLORATION LAB</span></div>
<div class="masthead">
  <div class="eyebrow">UNIT 3 — ROCKS &amp; MINERALS · SECTION 1</div>
  <div class="titlerow"><h1>Mineral Lab: <span class="accent">Explore</span> the Properties</h1><div class="chip">U03 / S03.1</div></div>
</div>
<div class="id-row"><div class="name"><div class="f">&nbsp;</div><div class="lbl">NAME</div></div>
<div class="date"><div class="f">&nbsp;</div><div class="lbl">DATE</div></div>
<div class="per"><div class="f">&nbsp;</div><div class="lbl">PERIOD</div></div></div>

<h2>GOAL</h2>
<p class="lead">Every mineral has a property that makes it stand out. Your job today is to explore the
mineral trays, test the samples, and find the property each mineral is best known for.</p>

<h2>HOW IT WORKS</h2>
<ol class="steps">
  <li>Pick up a mineral from a tray. Its name is on the tray label.</li>
  <li>Run the tests below. Look closely before you decide.</li>
  <li>Choose the property that stands out most for that mineral, the one you would remember it by.</li>
  <li>On page 2, write the mineral's name under that property and what stood out.</li>
  <li>Fill all three spots in every property. You may use a mineral in two properties, but no more than two.</li>
  <li>Put each sample back on its own tray before you take another.</li>
</ol>
<div class="eg"><b>Example.</b> Biotite peels apart into thin sheets, so it goes under <b>Cleavage</b>:
"peels into thin sheets." Pyrite looks like gold, so it could go under <b>Color</b>: "brassy gold."</div>

<h2>TESTING GUIDE</h2>
{GUIDE}

<h2 class="warn">SAFETY</h2>
<ul class="dot">
  <li>Keep the glass plate flat on the table when you scratch it, and scratch away from your hand. Report a chipped plate; do not use it.</li>
  <li>Only your teacher uses the acid. Bring the sample to the acid station.</li>
  <li>Never taste a mineral. Wash your hands when you finish.</li>
</ul>

<div class="pagebreak"></div>
<div class="runhead">U03 / S03.1 · MINERAL EXPLORATION LAB · DATA</div>
<h2>MINERAL PROPERTIES · THREE MINERALS FOR EACH</h2>
{grid(False)}

<h2>WRAP-UP</h2>
<ol class="q">
  <li>Which property could you spot without any tools? Name one mineral that shows it.<div class="wl"></div></li>
  <li>Pick a mineral you used twice. Which two properties made it stand out?<div class="wl"></div></li>
  <li>Why is color alone not enough to identify a mineral? Use one mineral from today as your example.<div class="wl"></div></li>
</ol>
</body></html>"""
    return h + body


def key():
    h = head("SHULL_Lab_TEMPLATE_TEACHER_KEY.html", "3.1 Lab Key - Mineral Exploration")
    body = f"""{EXTRA_CSS}
</head>
<body class="geo key">
<div class="meta"><span class="m-course">GEOLOGY</span><span class="m-code">U03 / S03.1</span></div>
<div class="masthead">
  <div class="eyebrow">TEACHER PREP + KEY · UNIT 3 — ROCKS &amp; MINERALS · SECTION 1</div>
  <div class="titlerow"><h1>Mineral Lab: Explore the Properties</h1><div class="chip">U03 / S03.1 · KEY</div></div>
</div>

<h2>WHAT THIS LAB IS</h2>
<p>An exploration, not an ID test. The mineral's name is on the tray, so students are deciding
which property each mineral is best known for, not working out what the mineral is. Many
answers are right. Accept any mineral the student can back up with what they saw.</p>

<h2>SETUP · PER STATION</h2>
<p>Mineral trays (labeled) · streak plate · glass plate · steel nail · copper coin or wire ·
magnet · hand lens · paper towel. One teacher-run acid station (dropper bottle of dilute acid,
goggles, waste cup).</p>
<p><b>Make sure the trays cover every property.</b> Each one needs at least three minerals that
show it well. The usual gap is <b>special properties</b>: magnetite is the only magnetic mineral in
most kits, so calcite (fizz) and talc (soapy feel) fill that row.</p>

<h2>TIMING · 50 MINUTES</h2>
<p>Intro and the example on page 1: 5 min · Exploring: 35 min · Wrap-up questions: 5 min ·
Cleanup and tray check: 5 min.</p>

<h2 class="warn">SAFETY · VERIFY BEFORE COPYING</h2>
<ul class="dot">
  <li><b>Acid station.</b> Check the acid's concentration and handling against the SDS and district
  policy, and record the check here: ____________ (date). If you are not running acid, delete the
  acid line from the student handout and the fizz test from Special properties.</li>
  <li><b>Glass plates.</b> Check the edges before class and pull any chipped plate.</li>
  <li><b>No tasting.</b> Galena contains lead. Hand washing at the end.</li>
</ul>

<h2>WATCH FOR</h2>
<ul class="dot">
  <li><b>Streak vs. hardness.</b> A powder line left on the glass is not a scratch. Students should rub it with a finger: a real scratch stays.</li>
  <li><b>Color vs. streak.</b> Pyrite (gold) and hematite (silver-black) are the best surprises. Steer students to try both tests on them.</li>
  <li><b>Hard minerals and streak.</b> Quartz and other minerals harder than the plate leave no streak; they scratch the plate instead.</li>
</ul>

<div class="pagebreak"></div>
<h2>EXAMPLE ANSWERS · ANY WELL-SUPPORTED MINERAL IS CORRECT</h2>
{grid(True)}

<h2>WRAP-UP · MODEL ANSWERS</h2>
<ol class="q">
  <li>Color or luster. Example: pyrite's gold color, or galena's metallic shine.</li>
  <li>Example: pyrite, for color (looks like gold) and streak (greenish-black, not gold).</li>
  <li>The outside color can change or mislead, so other tests are needed. Example: hematite looks
  silver-black but its streak is red-brown; pyrite looks like gold but is not.</li>
</ol>
</body></html>"""
    return h + body


for name, fn in (("3.1 Lab - Mineral Exploration.html", student),
                 ("3.1 Lab Key - Mineral Exploration.html", key)):
    with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
        f.write(fn())
print("ok")
