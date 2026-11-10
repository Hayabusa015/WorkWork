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

The span itself (`coversSections`) is SHULL-CHG-0066; `proseOnly` on a study guide is that
record's Q1, answer A.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "geo_u02_s02.1-s02.5_study_guide"

# ---------------------------------------------------------------------- the content
# Section A: one written line each. (prompt, answer)
BIG_IDEAS = [
    ("List the four units of geologic time, from largest to smallest.",
     "Eon, era, period, epoch."),
    ("In what kind of rock are most fossils found? Why there?",
     "Sedimentary rock: layers of sediment bury and preserve the remains."),
    ("What made oxygen build up in the air (the Great Oxidation Event)?",
     "Photosynthesis released oxygen faster than rocks and iron could absorb it "
     "(about 2.4 billion years ago)."),
    ("When volcanoes add CO₂ and other greenhouse gases to the air, what happens to "
     "temperatures?", "They go up: Earth warms."),
    ("When ice sheets grow, what happens to sea level?",
     "It falls. When the climate warms again, sea level recovers."),
    ("What kind of event ends both the Paleozoic Era and the Mesozoic Era?",
     "A mass extinction (end-Permian, about 252 million years ago; K–Pg, about 66 "
     "million years ago)."),
    ("Since the age of the dinosaurs, has Earth's climate warmed or cooled?",
     "Cooled, gradually, as the Mesozoic greenhouse faded, ending in repeated ice ages."),
]

# Section B, and each period: (label, answer). An empty label is a second line for the
# row above it. "BIG FOCUS" rows are the period's headline event.
FOCUS = "<b>BIG FOCUS</b>&nbsp; "

PRECAMBRIAN = [
    ("<b>Eons</b>&nbsp; Name the three, oldest to youngest:", "Hadean, Archean, Proterozoic."),
    ("<b>Time</b>&nbsp; About how much of Earth's history does it cover?",
     "About 88%."),
    ("<b>Hadean</b>&nbsp; What was happening to the young Earth?",
     "Earth forms (about 4.54 billion years ago); dense iron sinks to form the core."),
    ("<b>Archean</b>&nbsp; What formed on the surface? What lived there?",
     "Long-lasting crust and oceans; microbes (microbial ecosystems)."),
    ("<b>Proterozoic</b>&nbsp; How did the air change? Why did it matter for life?",
     "Oxygen rose (Great Oxidation Event). That made complex, oxygen-using life possible: "
     "eukaryotes, then multicellular life."),
    ("", None),
    (FOCUS + "What was Snowball Earth, and when did it happen?",
     "Ice spread over nearly all of Earth, even near the equator: the Sturtian and "
     "Marinoan glaciations, about 720–635 million years ago (Proterozoic)."),
    ("<b>The thaw</b>&nbsp; What ended Snowball Earth?",
     "Volcanoes kept releasing CO₂. It built up until Earth warmed enough to melt the ice."),
]

SNOW = next(i for i, (lab, _) in enumerate(PRECAMBRIAN) if "Snowball" in lab)

E, L, C = "<b>Earth</b>&nbsp; ", "<b>Life</b>&nbsp; ", "<b>Climate</b>&nbsp; "

# Era: (heading, [(period, [(label, answer), ...]), ...])
ERAS = [
    ("C  ·  The Paleozoic Era  (about 539 to 252 million years ago)", [
        ("CAMBRIAN PERIOD", [
            (E + "What covered the edges of the continents?",
             "Shallow seas; their sand, mud and lime became sandstone, shale and limestone."),
            (L + "Where did all life live?", "Only in the sea: life was entirely marine."),
            (C + "Warm or cold? Sea level high or low?",
             "Greenhouse (warm), high sea levels, less oxygen than today."),
            (FOCUS + "What was the Cambrian Explosion?",
             "Animal body plans diversified rapidly (trilobites, mollusks, sponges), starting "
             "about 539 million years ago, over tens of millions of years."),
        ]),
        ("ORDOVICIAN PERIOD", [
            (E + "What covered large areas of the continents?",
             "Shallow seas; plate collisions started new mountain building."),
            (L + "What thrived in the sea? What first reached land?",
             "Reefs and jawless fishes; early land plants."),
            (C + "How did it change by the end of the period?",
             "It cooled; ice grew and sea level fell. Major extinctions followed."),
        ]),
        ("SILURIAN PERIOD", [
            (E + "Which two landmasses collided?",
             "Laurentia and Baltica (Caledonian mountain building)."),
            (L + "What new fish appeared? What grew on land?",
             "Jawed fishes; small vascular plants and land arthropods built the first land "
             "communities."),
            (C + "What happened after the Ordovician ice age?",
             "It warmed, and sea levels recovered."),
        ]),
        ("DEVONIAN PERIOD", [
            (E + "Where did reefs thrive?",
             "In warm, shallow seas; continental collisions continued."),
            (L + "What spread across the land?",
             "Forests, insects and early tetrapods (four-limbed animals)."),
            (C + "What were the seas like? How did it end?",
             "Warm and shallow, until late-Devonian crises; extinctions hit hard."),
            (FOCUS + "Why is it called the \"Age of Fishes\"?",
             "Fish diversified hugely: armored placoderms, early sharks, lobe-finned fish."),
        ]),
        ("CARBONIFEROUS PERIOD", [
            (E + "Which supercontinent was forming?",
             "Pangaea, through major collisions (the Appalachians kept growing)."),
            (L + "What giant animals lived on land?",
             "Giant arthropods (<i>Meganeura</i>, <i>Arthropleura</i>) and amphibians; the "
             "amniotic egg let reptiles reproduce away from water."),
            (C + "What happened to oxygen and CO₂?",
             "Oxygen rose above modern levels as CO₂ fell; the tropics stayed warm while "
             "southern Gondwana glaciated."),
            (FOCUS + "What is the Carboniferous famous for?",
             "Coal: thick plant material buried in tropical swamps (wetlands) later became "
             "coal."),
        ]),
        ("PERMIAN PERIOD", [
            (E + "What did the continents form? What surrounded it?",
             "Pangaea, fully assembled; one ocean, Panthalassa; a dry interior."),
            (L + "Was <i>Dimetrodon</i> a dinosaur?",
             "No. It was a synapsid, on the mammal line."),
            (C + "What happened by the end of the period?",
             "Severe warming and widespread ocean oxygen loss."),
            (FOCUS + "What caused the end-Permian extinction?",
             "Siberian Traps volcanism released greenhouse gases: warming and ocean oxygen "
             "loss. Most marine species died, about 252 million years ago."),
        ]),
    ]),
    ("D  ·  The Mesozoic Era  (about 252 to 66 million years ago)", [
        ("TRIASSIC PERIOD", [
            (E + "What began to happen to Pangaea?",
             "Late-Triassic rifting began to break it apart."),
            (L + "What had to happen after the Permian die-off?",
             "Ecosystems rebuilt, over millions of years; reptiles diversified."),
            (C + "What were the inland areas like?", "Hot, dry and strongly seasonal."),
            (FOCUS + "What new animal group appeared?",
             "The first dinosaurs, about 230 million years ago (not yet dominant)."),
        ]),
        ("JURASSIC PERIOD", [
            (E + "What new ocean opened?",
             "The Atlantic (and the Gulf of Mexico), as Pangaea split apart."),
            (L + "Which dinosaurs ruled the land?",
             "Giant sauropods (<i>Diplodocus</i>, <i>Brachiosaurus</i>) and theropods "
             "(<i>Allosaurus</i>); marine reptiles in the sea, pterosaurs in the air."),
            (C + "Greenhouse or icehouse?", "Greenhouse; shallow seas covered large areas."),
            (FOCUS + "Why is <i>Archaeopteryx</i> important?",
             "A feathered dinosaur near the origin of birds, about 150 million years ago."),
        ]),
        ("CRETACEOUS PERIOD", [
            (E + "What flooded the continents?",
             "High seas; Antarctica even had forests."),
            (L + "What new kind of plant spread?",
             "Flowering plants; dinosaurs flourished, and small mammals were present."),
            (C + "What were conditions like for most of the period?",
             "Greenhouse, with high sea levels."),
            (FOCUS + "What ended the Cretaceous? What died?",
             "A 10 km asteroid hit near the Yucatán (Chicxulub), about 66 million years "
             "ago; about 75% of species died, including all non-bird dinosaurs."),
        ]),
    ]),
    ("E  ·  The Cenozoic Era  (about 66 million years ago to today)", [
        ("PALEOGENE PERIOD", [
            (E + "What landmass crashed into Asia?",
             "India, which began building the Himalaya."),
            (L + "Who took over the space the dinosaurs left?",
             "Mammals, which diversified rapidly."),
            (C + "Which way did temperatures go?",
             "Gradual cooling, as the Mesozoic greenhouse faded."),
        ]),
        ("NEOGENE PERIOD", [
            (E + "Which mountains kept growing?", "The Himalaya and the Andes."),
            (L + "What spread across the land? Who ate it?",
             "Grasslands; grazing mammals diversified with them."),
            (C + "Warmer or cooler? Wetter or drier?", "Cooler and drier."),
        ]),
        ("QUATERNARY PERIOD", [
            (E + "What advanced and retreated over the land?",
             "Continental ice sheets, several kilometers thick."),
            (L + "Which species evolved?", "Humans (modern mammals and birds diversified)."),
            (C + "What paces the ice-age cycles?",
             "Milankovitch cycles: changes in Earth's orbit and tilt."),
            (FOCUS + "What is the Holocene?",
             "The warm interglacial we live in now (the last 11,700 years)."),
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


def student_blocks():
    out = [{
        "kind": "reflection", "heading": "A  ·  Big Ideas of the Unit",
        "label": "ANSWER IN A SHORT SENTENCE", "linesEach": 1,
        "points": len(BIG_IDEAS), "prompts": [p for p, _ in BIG_IDEAS],
    }, {
        "kind": "plan", "heading": "B  ·  The Precambrian", "gapBefore": 8,
        "label": "THE FIRST 88%: HADEAN, ARCHEAN, PROTEROZOIC", "boldLabels": False,
        "points": answered(PRECAMBRIAN[:SNOW]), "rows": rows(PRECAMBRIAN[:SNOW]),
    }, {
        # Its own block, so the eons can finish page 1 without dragging Snowball Earth.
        "kind": "plan", "label": "SNOWBALL EARTH", "boldLabels": False, "gapBefore": 6,
        "points": answered(PRECAMBRIAN[SNOW:]), "rows": rows(PRECAMBRIAN[SNOW:]),
    }]
    for heading, periods in ERAS:
        for k, (period, items) in enumerate(periods):
            b = {"kind": "plan", "label": period, "boldLabels": False,
                 "points": answered(items), "rows": rows(items), "gapBefore": 6}
            if k == 0:
                b["heading"], b["gapBefore"] = heading, 10
            out.append(b)
    return out


def strip(s):
    return s.replace("&nbsp;", " ").replace(FOCUS.replace("&nbsp;", " "), "").strip()


def key_blocks():
    a = [f"{n}.  {p}  <b>{ans}</b>" for n, (p, ans) in enumerate(BIG_IDEAS, 1)]
    b = [f"{strip(lab)}  <b>{ans}</b>" for lab, ans in PRECAMBRIAN if ans is not None]
    table_rows = []
    for heading, periods in ERAS:
        table_rows.append({"group": heading.split("·", 1)[1].split("(")[0].strip().upper()})
        for period, items in periods:
            got = {}
            for lab, ans in items:
                tag = ("FOCUS" if lab.startswith(FOCUS) else
                       "EARTH" if lab.startswith(E) else
                       "LIFE" if lab.startswith(L) else "CLIMATE")
                got[tag] = ans
            table_rows.append([period.replace(" PERIOD", "").title(), got.get("EARTH", ""),
                               got.get("LIFE", ""), got.get("CLIMATE", ""),
                               got.get("FOCUS", "")])
    return [
        {"kind": "notes", "label": "A  ·  BIG IDEAS", "bullets": False, "items": a},
        {"kind": "notes", "label": "B  ·  THE PRECAMBRIAN", "bullets": False, "items": b,
         "gapBefore": 6},
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
            "pagesPerSection": 3,   # measured; Matt's ceiling is 4
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
