"""Generate the Geology U3 Rocks & Minerals guided-notes student and key specs (paged schema).

    python3 templates/notes/specs/make_geo_u03_figures.py       # the fill-in figures
    python3 templates/notes/specs/make_geo_u03_s03.1-s03.5_notes.py

One source, so the key is the student structure with answers filled and the two cannot
drift. Edit this file, not the JSON it writes.

**The notes follow the deck slide by slide** (Matt, 2026-11-09: "I do not want the
students wondering where we are and what to write down"). Every block is one content
slide, in deck order, and its cue label is that slide's number, the same number printed
in the slide's top corner. The notes heading is the slide's title. Blanks come only from
text visible on the slide, never from speaker notes.

Section order is the deck's, by Matt's direct instruction (2026-11-09): 3.1, then the
rock block as 3.5, then 3.2, 3.3, 3.4. No Concept Review page (Matt hands the unit review
out separately) and no difficulty ratings (Matt, same date).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "geo_u03_s03.1-s03.5_notes"
LINE = "______________"


def P(prompt, answer):
    """A line to complete, with ONE place to write (audit 2026-11-09).

    A short answer is written inline: each blank is sized to its share of the answer
    and the prompt gets no ruled line under it. A long answer (a clue list, a sentence)
    gets no inline blank: the label is printed and the student writes on the ruled
    line under it. The key prints the full answer under the prompt either way."""
    n = prompt.count(LINE)
    if not n:
        return {"prompt": prompt, "answer": answer, "lines": 1}
    frag = (len(answer) - len(prompt.replace(LINE, ""))) / n
    if frag <= 26:
        blank = "_" * max(8, int(frag * 1.3) + 4)
        return {"prompt": prompt.replace(LINE, blank), "answer": answer, "lines": 0}
    head = prompt.replace(LINE, "").rstrip()
    return {"prompt": head, "answer": answer, "lines": 2 if frag > 55 else 1}


def T(headers, rows, widths=None, row_h=0.27):
    """A fill-in table. rows: the first cell is printed in both copies; every later
    cell is the key's answer and is left blank on the student copy."""
    t = {"headers": headers, "rows": [[r[0]] + [""] * (len(r) - 1) for r in rows],
         "_key": rows}
    if widths:
        t["widths"] = widths
    if row_h:
        t["rowHeightIn"] = row_h
    return t


def FIG(name):
    return {"image": f"../assets/{name}.png", "keyImage": f"../assets/{name}_key.png"}


def S(n, title, cue, **kw):
    """One block = one slide. The cue label is the slide number."""
    row = {"title": f"Slide {n:02d}", "cueLabel": f"SLIDE {n:02d}",
           "notesLabel": title.upper(), "cues": [cue] if isinstance(cue, str) else cue,
           "extraNotes": False}
    row.update(kw)
    return row


def RECALL(prompt, answer, checks):
    return {"kind": "recall", "title": "Section summary",
            "cues": ["Close your notes before you write."],
            "prompt": prompt, "answer": answer, "lines": 3, "selfCheck": checks}


def LAB(n, title, steps):
    return S(n, title, "Record: the lab routine",
             notes=[P("Lab routine: ______ → ______ → ______ → ______",
                      "LOOK → TEST → RECORD → IDENTIFY"),
                    {"text": steps + " Record your observations on the lab handout."}])


# --------------------------------------------------------------------------- 3.1
s31 = {"code": "3.1", "title": "Minerals & Mineral ID",
       "learningTarget": "I can identify a mineral using its physical properties.",
       "pages": [
  {"rows": [
    S(3, "What Is a Mineral", "Record: the five characteristics",
      lead=["*A mineral must meet all five characteristics."],
      table=T(["On the slide", "Characteristic"], [
          ["Forms in nature.", "Naturally occurring"],
          ["Forms through nonliving processes.", "Inorganic"],
          ["Has a solid form.", "Solid"],
          ["A specific recipe. Quartz: SiO₂", "Definite composition"],
          ["Atoms follow a repeating pattern.", "Crystal structure"]], widths=[0.55, 0.45])),
    S(4, "Common Minerals", "Record: each formula and its key clue",
      lead=["*Use several properties together. Color alone is not enough. Most have a defining characteristic."],
      table=T(["Mineral", "Formula", "Key clue"], [
          ["Quartz", "SiO₂", "Hardness 7"],
          ["Halite", "NaCl", "Cubic cleavage"],
          ["Calcite", "CaCO₃", "Fizzes in dilute acid"],
          ["Pyrite", "FeS₂", "Greenish-black streak"],
          ["Galena", "PbS", "Gray streak"],
          ["Hematite", "Fe₂O₃", "Red-brown streak"]], widths=[0.22, 0.22, 0.56])),
  ]},
  {"rows": [
    S(5, "Color, Streak, and Luster", "Record: streak and the two kinds of luster",
      notes=[{"text": "The outside color can change. Test the powder too."},
             P(f"Hematite may look {LINE}. Its streak is {LINE}.",
               "Hematite may look silver-black. Its streak is red-brown."),
             P(f"Luster = how {LINE} reflects", "Luster = how light reflects"),
             P(f"Metallic: {LINE}", "Metallic: looks like metal."),
             P(f"Nonmetallic: {LINE}", "Nonmetallic: glassy, dull, or pearly."),
             "*Describe the shine before you guess the mineral."]),
    S(6, "Mohs Hardness", "Record: the definition and the field tools",
      lead=[P(f"Hardness measures resistance to {LINE}.",
               "Hardness measures resistance to scratching.")],
      figure=FIG("geo_u03_s06_mohs"),
      notes=[{"label": "Field tools"},
             P(f"Fingernail ≈ {LINE}    Copper ≈ {LINE}    Glass ≈ {LINE}    Steel ≈ {LINE}",
               "Fingernail ≈ 2.5    Copper ≈ 3.5    Glass ≈ 5.5    Steel ≈ 6.5")]),
    S(7, "Cleavage, Fracture, and Special Tests", "Record: how each sample breaks or reacts",
      lead=[P(f"Cleavage breaks along {LINE}. Fracture breaks {LINE}.",
               "Cleavage breaks along flat planes. Fracture breaks unevenly.")],
      table=T(["Sample or test", "What you see"], [
          ["Mica", "Cleavage: thin sheets"],
          ["Halite", "Cleavage: cubes"],
          ["Quartz", "Fracture: curved, shell-like"],
          ["Magnetism", "Magnetite attracts a magnet."],
          ["Acid reaction", "Calcite fizzes in dilute acid."]], widths=[0.32, 0.68])),
  ]},
  {"rows": [
    S(8, "Mineral A", "Record: the observations and test results",
      lead=[{"text": "Choose the best match. Use the test results as evidence."}],
      table=T(["Clue", "Result"], [
          ["Color", "Pink"], ["Streak", "White"], ["Luster", "Glassy"],
          ["Hardness test", "Scratches glass"], ["Cleavage", "Two cleavage planes near 90°"]],
          widths=[0.32, 0.68])),
    S(9, "Mineral A: Orthoclase Feldspar", "Record: the ID and the clues that support it",
      notes=[P(f"Mineral A = {LINE}", "Mineral A = orthoclase feldspar"),
             P(f"Strong clues: {LINE}", "Strong clues: hardness about 6; two cleavage planes near 90°"),
             P(f"Supporting clues: {LINE}", "Supporting clues: pink color, white streak, and glassy luster"),
             "*Color helps, but hardness and cleavage narrow the choices."]),
    LAB(10, "Mineral Lab", "At each station: observe color and luster, test streak and "
        "hardness, and look for cleavage or fracture."),
    RECALL("Explain how to identify a mineral. Use at least three properties.",
           "Observe color and luster, then test streak and hardness and look for cleavage "
           "or fracture. Color alone is not enough; streak, hardness and cleavage narrow it down.",
           ["I can list the five characteristics of a mineral.",
            "I can explain why streak is more useful than color.",
            "I can use hardness and cleavage to identify a mineral."]),
  ]},
]}

# --------------------------------------------------------------------------- 3.5
s35 = {"code": "3.5", "title": "The Rock Cycle",
       "learningTarget": "I can trace how any rock becomes any other rock.",
       "pages": [
  {"rows": [
    S(11, "Rocks", "Record: how each rock family forms",
      table=T(["Rock family", "How it forms"], [
          ["Igneous", "Melt cools and hardens."],
          ["Sedimentary", "Sediment builds up, or minerals form from water."],
          ["Metamorphic", "Heat and pressure change an existing rock."]], widths=[0.28, 0.72])),
    S(12, "What Is a Rock", "Record: the definition and the sandstone steps",
      lead=[P(f"A rock is a natural solid, usually made of one or more {LINE}.",
               "A rock is a natural solid, usually made of one or more minerals."),
             P(f"Minerals are the {LINE}. Some rocks also contain glass or organic material.",
               "Minerals are the ingredients. Some rocks also contain glass or organic material."),
             {"label": "One way to make a rock: sediment becomes sandstone"}],
      figure=FIG("geo_u03_s12_sandstone_chain")),
  ]},
  {"rows": [
    S(13, "The Rock Cycle", ["Record: the three rock types",
                             "Record: the process on each arrow"],
      figure=FIG("geo_u03_rock_cycle"),
      notes=["*No single starting point. Any exposed rock can become sediment."]),
    S(14, "One Rock's Journey", "Record: the rock at each step",
      lead=[{"text": "Quartz grains can survive weathering and become part of a new rock."}],
      figure=FIG("geo_u03_s14_journey"),
      notes=["*The quartz grains stay solid during the change to quartzite."]),
  ]},
  {"rows": [
    S(15, "Rock-Cycle Challenge", "Record: the starting and ending rock",
      notes=[P(f"Start: {LINE}      End: {LINE}", "Start: basalt      End: schist"),
             {"text": "Name the process. Decide whether the rock needs to melt. The next slide gives the route."}]),
    S(16, "Basalt → Schist", "Record: the route",
      lead=[P(f"Heat and pressure can change basalt while it stays {LINE}.",
               "Heat and pressure can change basalt while it stays solid.")],
      figure=FIG("geo_u03_s16_basalt_schist"),
      notes=["*Melting is not part of this route."]),
    RECALL("Describe one path a rock can take through the rock cycle. Name each process.",
           "Granite weathers and erodes into sediment; the sand deposits and cements into "
           "sandstone; heat and pressure change it to quartzite without melting.",
           ["I can name the three rock families and how each forms.",
            "I can label the rock cycle.",
            "I can explain why metamorphism does not need melting."]),
  ]},
]}

# --------------------------------------------------------------------------- 3.2
s32 = {"code": "3.2", "title": "Igneous Rocks",
       "learningTarget": "I can classify igneous rocks by texture and composition.",
       "pages": [
  {"rows": [
    S(18, "Intrusive and Extrusive", "Record: where each cools and its crystal size",
      figure=FIG("geo_u03_s18_intrusive_extrusive"),
      notes=["*Both form when melted rock cools and hardens."]),
    S(19, "Cooling and Texture", "Record: what each kind of cooling makes",
      lead=[{"text": "Texture describes crystal size and other visible features."}],
      table=T(["Cooling", "Result", "Why"], [
          ["Slow cooling", "Large crystals", "More time to grow"],
          ["Fast cooling", "Small crystals", "Less time to grow"],
          ["Very rapid cooling", "Glass", "Crystals may not have time to form"],
          ["Trapped gas", "Holes", "Bubbles leave spaces called vesicles"]],
          widths=[0.26, 0.24, 0.50])),
    S(20, "Cooling Changes Crystal Size", "Record: the rock each cooling rate makes",
      notes=[{"text": "Same general composition. Different time to grow crystals."},
             P(f"Slow cooling, large crystals: {LINE}", "Slow cooling, large crystals: granite"),
             P(f"Fast cooling, tiny crystals: {LINE}", "Fast cooling, tiny crystals: rhyolite")]),
  ]},
  {"rows": [
    S(21, "Igneous Rock Textures", "Record: what each texture looks like",
      lead=[{"text": "Texture describes the size and arrangement of crystals."}],
      table=T(["Texture", "What you see"], [
          ["Coarse", "Crystals easy to see"],
          ["Fine", "Crystals too small to see easily"],
          ["Glassy", "No visible crystals"],
          ["Vesicular", "Holes left by gas bubbles"],
          ["Porphyritic", "Large crystals in a finer background"]], widths=[0.28, 0.72])),
    S(22, "Igneous Rock Composition", "Record: the example, color and silica for each group",
      lead=["*The minerals in a rock affect its color."],
      table=T(["Group", "Example", "Color", "Silica"], [
          ["Felsic", "Granite", "Light pink or white", "More silica"],
          ["Intermediate", "Diorite", "Salt-and-pepper gray", "In between"],
          ["Mafic", "Gabbro", "Mostly dark minerals", "Less silica; more Fe + Mg"],
          ["Ultramafic", "Peridotite", "Often olive-green", "Least silica; rich in Fe + Mg"]],
          widths=[0.21, 0.19, 0.28, 0.32])),
  ]},
  {"rows": [
    S(23, "Bowen's Reaction Series", "Record: each mineral, in the order it forms",
      lead=["*As magma cools, different minerals can form."],
      figure=dict(FIG("geo_u03_bowens"), widthIn=5.3)),
  ]},
  {"rows": [
    S(24, "Igneous Rock ID Chart", "Record: the rock for each texture and composition",
      lead=[{"text": "Match crystal size with composition. Use the other textures too."}],
      notes=[P(f"Glassy: {LINE}", "Glassy: obsidian"),
             P(f"Holes, usually light: {LINE}", "Holes, usually light: pumice"),
             P(f"Holes, usually dark: {LINE}", "Holes, usually dark: scoria")],
      table=T(["Crystal size", "Felsic", "Intermediate", "Mafic"], [
          ["Coarse", "Granite", "Diorite", "Gabbro"],
          ["Fine", "Rhyolite", "Andesite", "Basalt"]], widths=[0.25, 0.25, 0.25, 0.25])),
    S(25, "Rock A", "Record: the texture and composition clues",
      lead=[{"text": "Describe the texture first. Then decide the composition."}],
      table=T(["Clue", "What you see"], [
          ["Texture", "Coarse grains. Crystals are easy to see."],
          ["Composition clues", "Mostly light-colored. Pink, clear, and black grains."]],
          widths=[0.3, 0.7])),
  ]},
  {"rows": [
    S(26, "Rock A: Granite", "Record: the ID and what each clue means",
      lead=["*Large crystals tell us the rock cooled slowly underground.",
            P(f"Rock A = {LINE}", "Rock A = granite")],
      table=T(["Clue", "What it tells us"], [
          ["Coarse", "Visible crystals"],
          ["Intrusive", "Slow cooling inside Earth"],
          ["Felsic", "Usually rich in quartz and feldspar"]], widths=[0.3, 0.7])),
    LAB(27, "Igneous Stations", "At each station: describe the texture, estimate the "
        "composition, and use the ID chart to name the rock."),
    RECALL("Explain how texture and composition together identify an igneous rock.",
           "Crystal size shows how fast it cooled (coarse = slow, inside Earth; fine = fast, at "
           "the surface). Color shows composition (light = felsic, dark = mafic). The chart "
           "matches the two.",
           ["I can tell intrusive from extrusive rocks by crystal size.",
            "I can name the felsic, intermediate and mafic rocks.",
            "I can put Bowen's minerals in order."]),
  ]},
]}

# --------------------------------------------------------------------------- 3.3
s33 = {"code": "3.3", "title": "Sedimentary Rocks",
       "learningTarget": "I can classify sedimentary rocks by grain size and origin.",
       "pages": [
  {"rows": [
    S(29, "How Sedimentary Rocks Form", "Record: the four steps and the two parts of lithification",
      lead=[{"text": "For clastic rocks, loose pieces become solid rock."}],
      figure=FIG("geo_u03_s29_sed_forms"),
      notes=[P(f"Compaction: {LINE}", "Compaction: burial squeezes the grains together."),
             P(f"Cementation: {LINE}", "Cementation: minerals glue the grains together.")]),
    S(30, "Sediment Becomes Rock", "Record: what happens at each stage",
      lead=[{"text": "Burial packs the grains. Mineral cement helps hold them together."}],
      figure=FIG("geo_u03_s30_sediment_rock")),
  ]},
  {"rows": [
    S(31, "Three Types of Sedimentary Rock", "Record: how each type forms, with an example",
      lead=["*The type depends on where the material came from."],
      table=T(["Type", "How it forms", "Example"], [
          ["Clastic", "Rock pieces stick together.", "Sandstone or shale"],
          ["Chemical", "Dissolved minerals form crystals.", "Rock salt"],
          ["Organic / biological", "Material comes from living things.",
           "Coal or shell-rich limestone"]], widths=[0.24, 0.42, 0.34])),
    S(32, "Sediment Grain Size", "Record: the size and the rock for each grain",
      lead=[{"text": "Look at the pieces that make up the rock."}],
      table=T(["Grain (what you see)", "Size", "Rock"], [
          ["Clay: too small to see", "Less than 1/256 mm", "Shale / claystone"],
          ["Silt: tiny, gritty particles", "1/256–1/16 mm", "Siltstone"],
          ["Sand: grains are visible", "1/16–2 mm", "Sandstone"],
          ["Gravel: pebbles or larger", "More than 2 mm", "Conglomerate / breccia"]],
          widths=[0.38, 0.30, 0.32])),
  ]},
  {"rows": [
    S(33, "Common Sedimentary Rocks", "Record: the clue for each rock",
      lead=[{"text": "Look at the grains, their shapes, and how they fit together."}],
      table=T(["Rock", "Clue"], [
          ["Shale", "Very fine / thin layers"], ["Sandstone", "Sand-sized grains"],
          ["Conglomerate", "Rounded pebbles"], ["Breccia", "Angular pieces"],
          ["Limestone", "Calcite / often fizzes"], ["Coal", "Plant remains"]],
          widths=[0.32, 0.68])),
    S(34, "Sedimentary Rock ID", "Record: the rock at the end of each path",
      lead=[{"text": "Start with visible grains. Confirm the ID with another clue."}],
      figure=FIG("geo_u03_sed_id_key"),
      notes=[P(f"Other clues: {LINE}, {LINE}, {LINE}, and {LINE}.",
               "Other clues: layers, fossils, ripple marks, and mud cracks.")]),
    S(35, "Rock B", "Record: what you see and how it holds together",
      lead=[{"text": "Use grain size and shape to support your answer."}],
      table=T(["Clue", "What you see"], [
          ["Grains", "Rounded pebbles. Smaller sand grains between them."],
          ["How it holds together", "The pieces are cemented into rock."]], widths=[0.32, 0.68])),
    S(36, "Rock B: Conglomerate", "Record: the ID and the key clues",
      lead=["*Rounded gravel-sized pieces are the key clue.",
            P(f"Rock B = {LINE}", "Rock B = conglomerate")],
      notes=["*Breccia has angular pieces."],
      table=T(["Clue", "What it tells us"], [
          ["Grain size", "Pebbles are larger than 2 mm."],
          ["Shape", "Rounded pieces help separate it from breccia."]], widths=[0.3, 0.7]),
      ),
  ]},
  {"rows": [
    LAB(37, "Sedimentary Stations", "At each station: look for grain size and shape, check for "
        "layers or fossils, and use only the approved acid test."),
    RECALL("Explain how grain size and grain shape help identify a sedimentary rock.",
           "Grain size sorts clay (shale), sand (sandstone) and gravel; for gravel, rounded "
           "pieces mean conglomerate and angular pieces mean breccia. No visible grains: check "
           "for fizzing (limestone) or plant material (coal).",
           ["I can put the steps of sedimentary rock formation in order.",
            "I can name the three types of sedimentary rock.",
            "I can tell conglomerate from breccia."]),
  ]},
]}

# --------------------------------------------------------------------------- 3.4
s34 = {"code": "3.4", "title": "Metamorphic Rocks",
       "learningTarget": "I can identify a metamorphic rock and its parent rock.",
       "pages": [
  {"rows": [
    S(39, "Heat and Pressure Change Rock", "Record: the two kinds of metamorphism",
      lead=[P(f"Metamorphism changes an existing rock without {LINE} it.",
               "Metamorphism changes an existing rock without melting it.")],
      figure=FIG("geo_u03_s39_contact_regional"),
      after=["*The rock stays solid. If it melts and then cools, the new rock is igneous."]),
    S(40, "How Foliation Forms", "Record: what pressure does to flat minerals",
      lead=[P(f"Pressure can help {LINE} minerals line up as the rock changes.",
              "Pressure can help flat minerals line up as the rock changes.")],
      figure=FIG("geo_u03_s40_foliation"),
      notes=[P(f"Before: {LINE}", "Before: minerals point in different directions."),
             P(f"After directed pressure: {LINE}",
               "After directed pressure: flat minerals align. The rock stays solid.")]),
  ]},
  {"rows": [
    S(41, "Foliated and Non-foliated", "Record: what each looks like",
      lead=["*Foliation is a pattern of aligned minerals or mineral bands."],
      table=T(["Texture", "What you see"], [
          ["Foliated", "Minerals line up or form bands."],
          ["Non-foliated", "No clear layers or mineral alignment."]], widths=[0.3, 0.7])),
    S(42, "Metamorphic Grade", "Record: each rock in the sequence",
      lead=[P(f"Grade describes the {LINE} of metamorphism.",
               "Grade describes the intensity of metamorphism.")],
      figure=FIG("geo_u03_s42_grade"),
      notes=["*Increasing grade → more change from heat and pressure."]),
    S(43, "Parent Rock → Metamorphic Rock", "Record: what each parent becomes",
      lead=[P(f"The parent rock is {LINE}.", "The parent rock is the rock you started with.")],
      table=T(["Parent rock", "Metamorphic rock"], [
          ["Limestone", "Marble"], ["Sandstone", "Quartzite"], ["Granite", "Gneiss"],
          ["Coal", "Anthracite"]], widths=[0.5, 0.5])),
  ]},
  {"rows": [
    S(44, "Metamorphic Rock ID", "Record: the rock at the end of each path",
      lead=[{"text": "Use texture first. Then test the mineral clues."}],
      figure=FIG("geo_u03_met_id_key")),
    S(45, "Rock C", "Record: the pattern and texture",
      lead=[{"text": "Describe the pattern before naming the rock."}],
      table=T(["Clue", "What you see"], [
          ["Pattern", "Alternating light and dark bands"],
          ["Texture", "Coarse grains. Minerals are easy to see."]], widths=[0.3, 0.7])),
  ]},
  {"rows": [
    S(46, "Rock C: Gneiss", "Record: the ID, family and parent rocks",
      lead=["*The mineral bands are the strongest clue.",
            P(f"Rock C = {LINE}", "Rock C = gneiss")],
      table=T(["Clue", "What it tells us"], [
          ["Rock family", "Metamorphic, foliated texture"],
          ["Possible parent rocks", "Granite or shale. The original composition matters."]],
          widths=[0.32, 0.68])),
    LAB(47, "Metamorphic Stations", "At each station: look for foliation, describe grains, "
        "sheen or bands, and match each rock to a possible parent."),
    RECALL("Explain how to identify a metamorphic rock and name a possible parent rock.",
           "Look for foliation first: slate, phyllite, schist and gneiss are foliated. "
           "Non-foliated: marble fizzes, quartzite scratches glass. Marble comes from "
           "limestone; quartzite from sandstone.",
           ["I can tell contact from regional metamorphism.",
            "I can put slate, phyllite, schist and gneiss in order of grade.",
            "I can match a metamorphic rock to its parent rock."]),
  ]},
]}

# Page layout, measured with block_height(). Every block stays in slide order; only
# where the sheet turns is chosen here. "R" is the section's RECALL block.
# Pages are packed to about 8.6 in of the 9.64 in body, and stretch stops short of the
# foot ("stretchHeadroomIn"): Word and Google Docs lay these pages out taller than
# LibreOffice does, and a page filled to the last point there spilled its final block
# onto a sheet of its own (Matt's screenshots, 2026-11-12). A short section ending
# shares its sheet with the next section's opening ("joinPrevious").
LAYOUT = {"3.1": [[3, 4], [5, 6, 7], [8, 9, 10], ["R"]],
          "3.5": [[11, 12], [13, 14, 15], [16, "R"]],
          "3.2": [[18], [19, 20, 21, 22], [23, 24], [25, 26, 27, "R"]],
          "3.3": [[29, 30, 31], [32, 33], [34, 35, 36], [37, "R"]],
          "3.4": [[39], [40, 41, 42], [43, 44, 45], [46, 47, "R"]]}
JOIN = {"3.5", "3.2", "3.4"}


def slide_of(row):
    return int(row["title"].split()[1]) if row["title"].startswith("Slide") else "R"


for sec in (s31, s35, s32, s33, s34):
    rows = []
    for pg in sec["pages"]:
        for r in pg["rows"]:
            if "after" in r:          # a must-write that belongs under a flowchart
                r.setdefault("notes", []).extend(r.pop("after"))
            rows.append(r)
    by = {slide_of(r): r for r in rows}
    assert len(by) == len(rows), sec["code"] + ": two blocks share a slide number"
    layout = LAYOUT[sec["code"]]
    assert [k for pg in layout for k in pg] == [slide_of(r) for r in rows], sec["code"]
    sec["pages"] = [{"rows": [by[k] for k in pg]} for pg in layout]
    if sec["code"] in JOIN:
        sec["pages"][0]["joinPrevious"] = True

spec = {
    "course": "geology",
    "unit": 3,
    "key": False,
    "stretchHeadroomIn": 0.85,
    "cover": {
        "unitTargets": [
            "S03.1  I can identify a mineral using its physical properties.",
            "S03.5  I can trace how any rock becomes any other rock.",
            "S03.2  I can classify igneous rocks by texture and composition.",
            "S03.3  I can classify sedimentary rocks by grain size and origin.",
            "S03.4  I can identify a metamorphic rock and its parent rock."],
        "keyTerms": [
            {"code": "3.1", "terms": ["Mineral", "streak", "luster", "hardness", "cleavage", "fracture"]},
            {"code": "3.5", "terms": ["Rock", "rock cycle", "weathering", "erosion", "deposition"]},
            {"code": "3.2", "terms": ["Intrusive", "extrusive", "texture", "vesicles", "felsic", "mafic"]},
            {"code": "3.3", "terms": ["Lithification", "compaction", "cementation", "clastic", "grain size"]},
            {"code": "3.4", "terms": ["Metamorphism", "foliated", "non-foliated", "grade", "parent rock"]}],
        "howItWorks": [
            "These notes follow the slides in order. Each block is one slide.",
            "The SLIDE number on the left matches the number in the top corner of the slide on the board.",
            "Write what the slide shows in the blanks, tables and flowcharts.",
            "A gray rule down the left of a line means must-write. Copy it exactly.",
            "Each section ends with a RECALL block. Close your notes before you write it."],
        "sectionList": [
            "S03.1   Minerals & Mineral ID  ·  slides 02–10",
            "S03.5   The Rock Cycle  ·  slides 11–16",
            "S03.2   Igneous Rocks  ·  slides 17–27",
            "S03.3   Sedimentary Rocks  ·  slides 28–37",
            "S03.4   Metamorphic Rocks  ·  slides 38–47"],
    },
    "sectionsContent": [s31, s35, s32, s33, s34],
}


def strip_answers(node):
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k == "_key" or (k == "answer" and "prompt" in node):
                continue
            out[k] = strip_answers(v)
        return out
    if isinstance(node, list):
        return [strip_answers(x) for x in node]
    return node


def fill_answers(node):
    if isinstance(node, dict):
        out = {k: fill_answers(v) for k, v in node.items() if k != "_key"}
        if "_key" in node:
            out["rows"] = node["_key"]
        return out
    if isinstance(node, list):
        return [fill_answers(x) for x in node]
    return node


student = strip_answers(spec)
key = fill_answers(spec)
key["key"] = True
for name, data in (("student", student), ("key", key)):
    with open(os.path.join(HERE, f"{STEM}_{name}.json"), "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
print("wrote", STEM + "_student.json and _key.json")
