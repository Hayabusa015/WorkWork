"""Generate the Geology U2 study guide student and key specs (2.1-2.5, one spanned entry).

    python3 templates/worksheet/specs/make_geo_u02_s02.1-s02.5_study_guide.py

One source, so the key is the student page with the blanks filled and the two cannot drift.
Edit this file, not the JSON it writes. Build:

    python3 templates/worksheet/build_worksheet_docx.py     <STEM>_student.json
    python3 templates/worksheet/build_worksheet_key_docx.py <STEM>_key.json

Content: Matt asked for big ideas first ("CO2 causes temps to go ___ and O2 causes temps
to ___", "periods end and begin with ___ (mass extinctions)"), then a compact Earth / Life /
Climate / big-event summary per period (2026-11-09). The main session set the twelve Big
Ideas' final wording from the verified U2 fact sheet (2026-11-09), which traces each fact
to the U2 guided-notes spec. Three of Matt's examples were reworded for accuracy: CO2 (#5,
sourced to the deck's Snowball Earth thaw slide, "Accumulated CO2 raises temperatures..."),
O2 (#6, what the Carboniferous key says happened, since O2 is not a greenhouse gas) and
mass extinctions (#10, which end eras; only 4 of 12 periods are described ending in one).
Time Walk cells are the fact sheet's, with these edits only: word counts dropped, "Mya" and
"~" written out, an unsupported cell printed empty, "Tropics warm" restored to the
Carboniferous climate cell (fact-sheet finding 7), "falls" -> "declines" there (the spec's
word, so it does not answer Big Idea #7). Genus names are italic.

Blanks are chosen so no answer is printed anywhere else on the student page (audit
2026-11-09, finding 2).

The span itself (`coversSections`) is SHULL-CHG-0066; `proseOnly` on a study guide is that
record's Q1, answer A.
"""
import copy, json, math, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "geo_u02_s02.1-s02.5_study_guide"

# ---------------------------------------------------------------------- the content
# Each Big Idea is written once with "___" where the blank goes, and its answer.
BIG_IDEAS = [
    ("The time scale, largest to smallest: eon → era → period → ___.", "epoch"),
    ("Most fossils are found in ___ rock.", "sedimentary"),
    ("Oxygen built up in the air (the Great Oxidation Event, about 2.4 billion years ago) "
     "because ___ released it faster than rocks and iron could absorb it.", "photosynthesis"),
    ("Rising oxygen made ___, oxygen-using life possible.", "complex"),
    ("When volcanoes build up CO₂ in the air, temperatures go ___.", "up"),
    ("In the Carboniferous, as CO₂ declined and O₂ rose above modern levels, southern "
     "Gondwana ___.", "glaciated"),
    ("When ice sheets grow, sea level ___.", "falls"),
    ("In the Cambrian, all life lived in the ___; plants, then animals, later moved onto land.", "sea"),
    ("Pangaea was fully assembled by the Permian, then began breaking apart in the Late "
     "Triassic, opening the ___ Ocean.", "Atlantic"),
    ("The ends of the Paleozoic and Mesozoic Eras are each marked by a ___.",
     "mass extinction"),
    ("After each of those die-offs, rebuilding ecosystems took ___ of years.",
     "millions"),
    ("Since the Mesozoic greenhouse faded, Earth's climate has gradually ___.", "cooled"),
]

# Period, Earth, Life, Climate, Big Event, and the one word blanked on the student copy.
# An empty string is a cell the source has nothing for; it prints empty.
TIME_WALK = [
    ("Hadean", "Earth accretes; iron sinks to form the core", "", "",
     "Earth forms, about 4.54 billion years ago", "core"),
    ("Archean", "Long-lived crust and oceans develop", "Microbial ecosystems develop", "", "",
     "Microbial"),
    ("Proterozoic", "Supercontinent Rodinia assembles, about 1.1–0.9 billion years ago",
     "Oxygen rises; eukaryotes, then multicellular life, diversify",
     "Snowball Earth: Sturtian, Marinoan glaciations (about 720–635 million years ago)",
     "Great Oxidation Event, about 2.4 billion years ago", "Rodinia"),
    ("Cambrian", "Shallow seas spread; sandstone, shale, limestone form",
     "Body plans diversify rapidly (trilobites); life entirely marine",
     "Greenhouse, high sea levels, less oxygen than today",
     "Cambrian Explosion, about 539 million years ago", "Explosion"),
    ("Ordovician", "Shallow seas widespread; plate collisions start mountain building",
     "Reefs, jawless fishes flourish; early land plants appear",
     "Warm, then cooling, ice growth, sea level falls",
     "Major extinctions follow late-Ordovician cooling", "falls"),
    ("Silurian", "Laurentia, Baltica converge in Caledonian mountain building",
     "Jawed fishes diversify; vascular plants, arthropods build land communities",
     "Warming after glaciation; sea levels recover", "", "Jawed"),
    ("Devonian", "Continental collisions continue; reefs thrive in warm seas",
     "Fishes diversify; forests, insects, early tetrapods spread on land",
     "Warm shallow seas, then late-Devonian crises",
     "Late-Devonian extinctions hit hard", "tetrapods"),
    ("Carboniferous", "Pangaea assembles; tropical wetland deposits later become coal",
     "Giant arthropods and amphibians dominate wet land habitats",
     "Tropics warm; O₂ above modern, CO₂ declines; southern Gondwana glaciates",
     "Amniotic egg: reproduction away from standing water", "glaciates"),
    ("Permian", "Pangaea fully assembled; one ocean, Panthalassa; dry interior",
     "Synapsids like <i>Dimetrodon</i> (mammal line), not dinosaurs",
     "Varies; ends with severe warming, ocean oxygen loss",
     "End-Permian extinction, about 252 million years ago: Siberian Traps volcanism", "Panthalassa"),
    ("Triassic", "Pangaea largely intact; late-Triassic rifting starts breakup",
     "Ecosystems rebuild after end-Permian; reptiles diversify",
     "Hot, dry, strongly seasonal interiors",
     "First dinosaurs appear, about 230 million years ago", "rifting"),
    ("Jurassic", "Pangaea splits; Atlantic and Gulf of Mexico open",
     "Giant sauropods, theropods rule land; marine reptiles, pterosaurs",
     "Greenhouse; shallow seas cover large areas",
     "<i>Archaeopteryx</i>, feathered dinosaur near bird origins, about 150 million years ago",
     "Atlantic"),
    ("Cretaceous", "High sea levels flood continents; forests even in Antarctica",
     "Flowering plants spread; dinosaurs flourish; small mammals present",
     "Greenhouse conditions, high sea levels",
     "K–Pg extinction, about 66 million years ago: asteroid impact", "asteroid"),
    ("Paleogene", "India collides with Asia; Alpine–Himalayan, Circum-Pacific belts begin",
     "Mammals diversify rapidly into space left by K–Pg",
     "Gradual cooling as Mesozoic greenhouse fades", "", "India"),
    ("Neogene", "Plate motion keeps building Himalaya and Andes",
     "Grasslands spread; grazing mammals diversify",
     "Cools further; drier in many regions", "", "Grasslands"),
    ("Quaternary", "Ice sheets kilometers thick advance and retreat repeatedly",
     "Modern mammals, birds diversify; humans evolve",
     "Glacial cycles paced by Milankovitch orbital cycles",
     "We now live in the Holocene interglacial", "Holocene"),
]

DIRECTIONS = "Fill in each blank. Check your guided notes if you get stuck."
TITLE = "Unit 2 Study Guide"

# ---------------------------------------------------------------------- the layout
NOTES_PT = 11            # tokens printScale.notesBody; Geology errs larger (DECISIONS.md)
TABLE_PT = 10.5          # tokens printScale.body; room to write in the cell (Geology errs larger)
HEADERS = ["PERIOD", "EARTH", "LIFE", "CLIMATE", "BIG EVENT"]
WIDTHS = [0.145, 0.215, 0.23, 0.205, 0.205]
TEXT_W_IN = 7.50         # the builder's text width
CELL_PAD_IN = 2 * 60 / 1440  # table_block's left + right cell margins

# A blank is sized to its answer: room for that many handwritten letters, measured in
# Archivo underscores (0.485 em each, from brand/fonts/Archivo-Regular.ttf).
UNDERSCORE_EM = 0.485
HAND_IN_PER_CHAR = 0.12
HAND_PAD_IN = 0.20
HAND_MIN_IN = 0.60


def blank(answer, size_pt, max_in=None):
    want = max(HAND_MIN_IN, len(answer) * HAND_IN_PER_CHAR + HAND_PAD_IN)
    if max_in:
        want = min(want, max_in)
    return "_" * math.ceil(want / (UNDERSCORE_EM * size_pt / 72))


def fill(answer):
    return f"<b>{answer}</b>"


def big_ideas(key):
    items = []
    for n, (text, ans) in enumerate(BIG_IDEAS, 1):
        assert text.count("___") == 1, text
        items.append(f"{n}.  " + text.replace("___", fill(ans) if key else blank(ans, NOTES_PT)))
    return {"kind": "notes", "label": "PART 1: BIG IDEAS", "bullets": False,
            "size": NOTES_PT, "points": len(BIG_IDEAS), "items": items}


def time_walk(key):
    rows = []
    for row in TIME_WALK:
        cells, word = list(row[:5]), row[5]
        pat = re.compile(rf"\b{re.escape(word)}\b")
        hits = [i for i, c in enumerate(cells) if pat.search(c)]
        assert len(hits) == 1 and len(pat.findall(cells[hits[0]])) == 1, (row[0], word)
        i = hits[0]
        col_in = TEXT_W_IN * WIDTHS[i] - CELL_PAD_IN
        sub = fill(word) if key else blank(word, TABLE_PT, max_in=col_in * 0.85)  # room for the punctuation after it
        cells[i] = pat.sub(lambda _m: sub, cells[i])
        rows.append(cells)
    return {"kind": "table", "label": "PART 2: TIME WALK", "size": TABLE_PT,
            "headers": HEADERS, "widths": WIDTHS, "points": len(TIME_WALK),
            "gapBefore": 8, "rows": rows}


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
        "source": "Verified U2 fact sheet, 2026-11-09, traced to the U2 guided-notes spec",
        "sectionsContent": [{
            "code": "2.1",
            "coversSections": ["2.1", "2.2", "2.3", "2.4", "2.5"],
            "title": TITLE,
            "proseOnly": True,
            "pagesPerSection": 2,   # measured: two full pages; Matt's ceiling is 4
            "directions": DIRECTIONS,
            "blocks": [big_ideas(False), time_walk(False)],
        }],
    }
    if key:
        s["key"] = {"blocks": [big_ideas(True), time_walk(True)]}
    return s


if __name__ == "__main__":
    for name, key in (("student", False), ("key", True)):
        path = os.path.join(HERE, f"{STEM}_{name}.json")
        with open(path, "w") as f:
            json.dump(spec(key), f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("wrote", os.path.relpath(path))
