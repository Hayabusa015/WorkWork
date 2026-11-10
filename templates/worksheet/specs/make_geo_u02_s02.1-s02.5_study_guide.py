"""Generate the Geology U2 study guide student and key specs (2.1-2.5, one spanned entry).

    python3 templates/worksheet/specs/make_geo_u02_s02.1-s02.5_study_guide.py

One source: every prompt is written next to its answer, so the student page and the key
cannot drift. Edit this file, not the JSON it writes. Build:

    python3 templates/worksheet/build_worksheet_docx.py     <STEM>_student.json
    python3 templates/worksheet/build_worksheet_key_docx.py <STEM>_key.json

Structure is Matt's (2026-11-10): Section A, the big ideas of the unit; Section B, the
Precambrian (its eons, what Earth and the air were like, a Snowball Earth question); then
the Paleozoic, Mesozoic and Cenozoic broken down by period, each period a short Earth /
Life / Climate prompt, plus a BIG FOCUS line where the period has one ("the carboniferous
... the swampy earth that turned into coal, or the Cambria explosion"). No fill-in-the-
blank: "just have them write it, small short prompt."

Content: every answer is the U2 guided-notes key (verified fact sheet, 2026-11-09), with
two exceptions, both taught on the September deck the notes follow. Snowball Earth's
reach to low latitudes and its volcanic-CO2 thaw are deck slides 15-16 (the notes key
gives only the names and dates). Devonian "Age of Fishes" is deck slide 24. Section A's
CO2 line is Matt's own example ("CO2 causes temps to go ___"), sourced to slide 16 and
S2.5's greenhouse-gas warming. O2 is not a greenhouse gas, so it has no temperature line.
Only 4 of 12 periods are described ending in extinctions, so A says eras, not periods.

Audit 2026-11-10 (auditor, blocking 1 + should-fix): no label or prompt prints another
prompt's answer (the eons are "oldest / middle / youngest", not named); the Ordovician
gets a BIG FOCUS row (major extinctions); two-part prompts get a second line; dating
(S2.1) joins Section A; the key bolds the minimum full-credit answer.

The span itself (`coversSections`) is SHULL-CHG-0066; `proseOnly` on a study guide is that
record's Q1, answer A.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "geo_u02_s02.1-s02.5_study_guide"

# ---------------------------------------------------------------------- the content
# Every row is (prompt, answer). The prompt is a bold lead and a short question, written on
# one line beside its write-on rule. In the answer, <b>bold</b> is the minimum full-credit
# answer and the rest is detail for the teacher. A row of ("", None) is a second line for
# the row above it. No prompt may print another prompt's answer (audit 2026-11-10).
FOCUS = "<b>BIG FOCUS</b>&nbsp; "


def lead(word):
    return f"<b>{word}</b>&nbsp; "


MORE = ("", None)

BIG_IDEAS = [
    (lead("Time scale") + "Its four units, largest to smallest:",
     "<b>Eon, era, period, epoch.</b>"),
    (lead("Fossils") + "What kind of rock holds most of them?",
     "<b>Sedimentary rock</b>: layers of sediment bury and preserve remains."),
    (lead("Dating") + "What method finds the age of very old rock?",
     "<b>Radiometric dating</b> (uranium-lead, potassium-argon). Carbon-14 dates organic "
     "material younger than about 50,000 years."),
    (lead("CO₂") + "When it builds up in the air, what happens to temperatures?",
     "<b>They go up</b>: Earth warms."),
    (lead("Ice") + "When ice sheets grow, what happens to sea level?",
     "<b>It falls</b>; it recovers when the climate warms again."),
    (lead("Era endings") + "What kind of event ends the Paleozoic and the Mesozoic?",
     "<b>A mass extinction</b> (end-Permian, about 252 million years ago; K–Pg, about 66 "
     "million years ago)."),
    (lead("Climate trend") + "How has Earth's climate changed since the dinosaurs?",
     "<b>It has cooled</b>, gradually, as the Mesozoic greenhouse faded, ending in repeated "
     "ice ages."),
]

PRECAMBRIAN = [
    (lead("Eons") + "Name the three, oldest to youngest:",
     "<b>Hadean, Archean, Proterozoic.</b>"),
    (lead("Time") + "About what share of Earth's history is the Precambrian?",
     "<b>About 88%.</b>"),
    (lead("Oldest eon") + "What sank to form Earth's core?",
     "<b>Dense iron</b>, as the young Earth formed (about 4.54 billion years ago) and "
     "separated into layers."),
    (lead("Middle eon") + "What formed on the surface? What lived there?",
     "<b>Crust and oceans; microbes.</b>"),
    (lead("Youngest eon") + "How did the air change? What caused it?",
     "<b>Oxygen rose</b> (the Great Oxidation Event, about 2.4 billion years ago), because "
     "<b>photosynthesis</b> released it faster than rocks and iron could absorb it."),
    MORE,
    (lead("Oxygen") + "Why did that change matter for life?",
     "It made <b>complex, oxygen-using life</b> possible: eukaryotes, then multicellular "
     "life."),
]

SNOWBALL = [
    (FOCUS + "What was Snowball Earth? About when was it?",
     "<b>Ice reached low latitudes, near the equator</b>: the Sturtian and Marinoan "
     "glaciations, <b>about 720–635 million years ago</b> (Proterozoic)."),
    MORE,
    (lead("The thaw") + "What ended Snowball Earth?",
     "<b>Volcanoes kept releasing CO₂</b>; it built up until Earth warmed enough to melt "
     "the ice."),
]

E, L, C = lead("Earth"), lead("Life"), lead("Climate")

# Era: (heading, [(period, [(prompt, answer), ...]), ...])
ERAS = [
    ("C  ·  The Paleozoic Era  (about 539 to 252 million years ago)", [
        ("CAMBRIAN PERIOD", [
            (E + "What covered the edges of the continents?",
             "<b>Shallow seas</b>; their sand, mud and lime became sandstone, shale and "
             "limestone."),
            (L + "Where did all life live?", "<b>Only in the sea.</b>"),
            (C + "What were temperatures and sea level like?",
             "<b>Warm (greenhouse), with high sea levels</b>; less oxygen than today."),
            (FOCUS + "What was the Cambrian Explosion?",
             "<b>Animal life diversified rapidly</b> into many body plans (trilobites, "
             "mollusks, sponges), starting about 539 million years ago."),
        ]),
        ("ORDOVICIAN PERIOD", [
            (E + "What did plate collisions begin to build?",
             "<b>Mountains</b>; shallow seas still covered large areas."),
            (L + "What thrived in the sea? What first reached land?",
             "<b>Reefs and jawless fishes; early land plants.</b>"),
            (C + "How did it change late in the period?",
             "<b>It cooled</b>; ice grew and sea level fell."),
            (FOCUS + "What happened to life at the end of the period?",
             "<b>Major extinctions</b>, after the late-Ordovician cooling."),
        ]),
        ("SILURIAN PERIOD", [
            (E + "Which two landmasses collided?",
             "<b>Laurentia and Baltica</b> (Caledonian mountain building)."),
            (L + "What new kind of fish appeared?",
             "<b>Jawed fishes</b>; small vascular plants and land arthropods built the first "
             "land communities."),
            (C + "How did temperature and sea level change?",
             "<b>It warmed, and sea levels recovered.</b>"),
        ]),
        ("DEVONIAN PERIOD", [
            (E + "What kept happening between the continents?",
             "<b>Collisions continued</b>; reefs thrived in warm, shallow seas."),
            (L + "What spread across the land?",
             "<b>Forests, insects and early tetrapods</b> (four-limbed animals)."),
            (C + "What were the seas like?",
             "<b>Warm and shallow</b>, until late-Devonian crises; extinctions hit hard."),
            (FOCUS + "Why is it called the \"Age of Fishes\"?",
             "<b>Fish diversified hugely</b>: placoderms, early cartilaginous fish (shark "
             "relatives), lobe-finned fish."),
        ]),
        ("CARBONIFEROUS PERIOD", [
            (E + "Which supercontinent was forming?",
             "<b>Pangaea</b>, through major collisions (the Appalachians kept growing)."),
            (L + "What giant animals lived on land?",
             "<b>Giant arthropods</b> (<i>Meganeura</i>, <i>Arthropleura</i>) "
             "<b>and amphibians.</b>"),
            (C + "What happened to oxygen and CO₂?",
             "<b>Oxygen rose above modern levels as CO₂ fell</b>; the tropics stayed warm "
             "while southern Gondwana glaciated."),
            (FOCUS + "What is the Carboniferous famous for?",
             "<b>Coal</b>: thick plant material buried in tropical swamps later became coal."),
        ]),
        ("PERMIAN PERIOD", [
            (E + "What supercontinent was complete? What ocean surrounded it?",
             "<b>Pangaea; Panthalassa.</b>"),
            (L + "What kind of animal was <i>Dimetrodon</i>?",
             "<b>A synapsid</b>, on the mammal line; not a dinosaur."),
            (C + "What happened to the oceans by the end?",
             "<b>They warmed and lost oxygen.</b>"),
            (FOCUS + "What ended the Permian?",
             "<b>Siberian Traps volcanism</b>: greenhouse gases drove warming and ocean oxygen "
             "loss; most marine species died, about 252 million years ago."),
        ]),
    ]),
    ("D  ·  The Mesozoic Era  (about 252 to 66 million years ago)", [
        ("TRIASSIC PERIOD", [
            (E + "What began to happen to Pangaea?",
             "<b>It began rifting apart</b> (late Triassic)."),
            (L + "What did ecosystems have to do early in the period?",
             "<b>Rebuild</b>, after the end-Permian crisis; reptiles diversified."),
            (C + "What were the inland areas like?", "<b>Hot, dry and strongly seasonal.</b>"),
            (FOCUS + "What new animal group appeared?",
             "<b>Dinosaurs</b>, about 230 million years ago (not yet dominant)."),
        ]),
        ("JURASSIC PERIOD", [
            (E + "What new ocean opened?",
             "<b>The Atlantic</b> (and the Gulf of Mexico), as Pangaea split apart."),
            (L + "Which dinosaurs ruled the land?",
             "<b>Giant sauropods</b> (<i>Diplodocus</i>, <i>Brachiosaurus</i>) <b>and "
             "theropods</b> (<i>Allosaurus</i>)."),
            (C + "What was the world's climate like?",
             "<b>Greenhouse (warm)</b>; shallow seas covered large areas."),
            (FOCUS + "Why is <i>Archaeopteryx</i> important?",
             "<b>A feathered dinosaur near the origin of birds</b>, about 150 million years "
             "ago."),
        ]),
        ("CRETACEOUS PERIOD", [
            (E + "What grew even in Antarctica?",
             "<b>Forests</b>; high seas flooded broad areas of the continents."),
            (L + "What new kind of plant spread?",
             "<b>Flowering plants</b>; dinosaurs flourished, and small mammals were present."),
            (C + "What were sea levels like?", "<b>High</b>, under greenhouse conditions."),
            (FOCUS + "What ended the Cretaceous?",
             "<b>An asteroid impact</b>: a roughly 10 km asteroid hit near the Yucatán "
             "(Chicxulub), about 66 million years ago; about 75% of species died, including "
             "all non-bird dinosaurs."),
        ]),
    ]),
    ("E  ·  The Cenozoic Era  (about 66 million years ago to today)", [
        ("PALEOGENE PERIOD", [
            (E + "What landmass crashed into Asia?",
             "<b>India</b>, beginning the Himalaya."),
            (L + "Which animal group diversified rapidly?",
             "<b>Mammals</b>, into the space left after the K–Pg extinction."),
            (C + "Which way did temperatures go?",
             "<b>Gradual cooling</b>, as the Mesozoic greenhouse faded."),
        ]),
        ("NEOGENE PERIOD", [
            (E + "Which mountains kept growing?", "<b>The Himalaya and the Andes.</b>"),
            (L + "What spread across the land?", "<b>Grasslands</b>, with grazing mammals."),
            (C + "What happened to rainfall in many regions?",
             "<b>It got drier</b> (and cooler)."),
        ]),
        ("QUATERNARY PERIOD", [
            (E + "What advanced and retreated over the land?",
             "<b>Ice sheets</b>, several kilometers thick."),
            (L + "What does the Quaternary have to do with us?",
             "<b>Humans evolved</b>, during its glacial cycles."),
            (C + "What paces its cycles of cold and warm?",
             "<b>Milankovitch cycles</b>: changes in Earth's orbit and tilt."),
            (FOCUS + "What is the Holocene?",
             "<b>The warm interglacial we live in now</b> (the last 11,700 years)."),
        ]),
    ]),
]

TITLE = "Unit 2 Study Guide"
DIRECTIONS = ("Answer each prompt in a few words or a short sentence. Use your guided "
              "notes if you get stuck.")


# ---------------------------------------------------------------------- the layout
def rows(items):
    return [[[lab, 1]] for lab, _ in items]


def answered(items):
    return sum(1 for _, a in items if a is not None)


def plan(label, items, **extra):
    return {"kind": "plan", "label": label, "boldLabels": False,
            "points": answered(items), "rows": rows(items), **extra}


def student_blocks():
    out = [
        plan("BIG IDEAS", BIG_IDEAS, heading="A  ·  Big Ideas of the Unit"),
        plan("EARTH'S EARLIEST HISTORY", PRECAMBRIAN, heading="B  ·  The Precambrian",
             gapBefore=10),
        plan("SNOWBALL EARTH", SNOWBALL, gapBefore=6),
    ]
    for heading, periods in ERAS:
        for k, (period, items) in enumerate(periods):
            out.append(plan(period, items, **({"heading": heading, "gapBefore": 10} if k == 0
                                              else {"gapBefore": 6})))
    return out


def plain(prompt):
    p = re.sub(r"^<b>(.*?)</b>&nbsp; ", r"\1: ", prompt.replace(FOCUS, "Big focus: "))
    return re.sub(r"</?b>", "", p).replace("&nbsp;", " ")


def qa(items, numbered=False):
    got = [(p, a) for p, a in items if a is not None]
    return [(f"{n}.  " if numbered else "") + f"{plain(p)}  →  {a}"
            for n, (p, a) in enumerate(got, 1)]


def key_blocks():
    table_rows = []
    for heading, periods in ERAS:
        table_rows.append({"group": heading.split("·", 1)[1].split("(")[0].strip().upper()})
        for period, items in periods:
            got = {}
            for lab, ans in items:
                tag = next(t for t, pre in (("FOCUS", FOCUS), ("EARTH", E), ("LIFE", L),
                                            ("CLIMATE", C)) if lab.startswith(pre))
                got[tag] = ans
            table_rows.append([period.replace(" PERIOD", "").title()]
                              + [got.get(t, "") for t in ("EARTH", "LIFE", "CLIMATE", "FOCUS")])
    return [
        {"kind": "notes", "label": "A  ·  BIG IDEAS", "bullets": False,
         "items": qa(BIG_IDEAS, numbered=True)},
        {"kind": "notes", "label": "B  ·  THE PRECAMBRIAN", "bullets": False,
         "items": qa(PRECAMBRIAN) + qa(SNOWBALL), "gapBefore": 6},
        {"kind": "notes", "bullets": False, "gapBefore": 4,
         "items": ["<b>Bold</b> is the minimum full-credit answer; the rest is detail."]},
        {"kind": "table", "label": "C–E  ·  PERIOD BY PERIOD", "size": 8.5, "gapBefore": 6,
         "headers": ["PERIOD", "EARTH", "LIFE", "CLIMATE", "BIG FOCUS"],
         "widths": [0.13, 0.21, 0.23, 0.20, 0.23], "rows": table_rows},
    ]


def spec(key):
    s = {
        "$comment": (f"GENERATED by {os.path.basename(__file__)}. Edit that file, not this one. "
                     "Geology U2 study guide, one entry spanning 2.1-2.5 (SHULL-CHG-0066). "
                     + ("Teacher key: build with build_worksheet_key_docx.py." if key else
                        "Student copy: build with build_worksheet_docx.py.")),
        "course": "geology",
        "unit": 2,
        "sections": ["2.1", "2.2", "2.3", "2.4", "2.5"],
        "docType": "Study_Guide",
        "source": ("U2 guided-notes keys (verified fact sheet, 2026-11-09); Snowball Earth "
                   "and Age of Fishes from the September deck, slides 15-16 and 24"),
        "sectionsContent": [{
            "code": "2.1",
            "coversSections": ["2.1", "2.2", "2.3", "2.4", "2.5"],
            "title": TITLE,
            "proseOnly": True,
            "pagesPerSection": 2 if key else 3,   # measured; Matt's ceiling is 4
            "directions": DIRECTIONS,
            "blocks": student_blocks(),
        }],
    }
    if key:
        s["key"] = {"blocks": key_blocks()}
    return s


if __name__ == "__main__":
    for name, key in (("student", False), ("key", True)):
        path = os.path.join(HERE, f"{STEM}_{name}.json")
        with open(path, "w") as f:
            json.dump(spec(key), f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("wrote", os.path.relpath(path))
