#!/usr/bin/env python3
"""Draw the hand-built figures for CHEM U02 S2.3 Electron Configurations, and check them.

Hand-built, not generated. Everything here is science students read: orbital boxes,
spin arrows, electron counts, a filling-order chart. A generated one would have a
plausible and wrong electron count that nobody catches at a glance.

Two jobs, one file, so the drawing and the checking cannot drift apart:

  1. CHECKER. Every configuration and orbital diagram used on the slides is declared
     once below, re-added, and tested against Aufbau, Hund and Pauli. The deliberately
     WRONG ones are asserted to be wrong, and wrong in the way the slide says. The
     script also asserts that every configuration string it knows about appears
     verbatim in the deck spec, so the slide text is the text that was checked.
  2. DRAWING. The figures are drawn from the same data the checker validated. Spin
     arrows are shapes (line plus triangle), never text glyphs.

Convention (filling order, PROVISIONAL until confirmed): [Ar] 4s2 3d6. Written in the
deck spec with run markup, [Ar] 4s^{2} 3d^{6}, which build_deck.js turns into a true
superscript run (no Unicode superscript glyphs anywhere), so 2p4 cannot be misread as
"2p, four". Speaker notes are plain text and write the same thing as 4s^2 3d^6.
Required through Kr.

Colours come from brand/tokens.json. Type is the shipped Archivo, so the figure and the
slide around it are one typeface. Every text size is >= 46 px on a canvas drawn at
200 px per inch, which is 16.6 pt once placed in its slot.

    python3 scripts/build_diagram_u02_s02.3_configurations.py
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(REPO, "templates", "slide", "assets")
SPEC = os.path.join(REPO, "templates", "slide", "decks",
                    "chem_u02_s02.3_electron_configurations.json")
BUILDS = os.path.join(REPO, "templates", "slide", "decks",
                      "chem_u02_s02.3_electron_configurations.builds.json")
SCALE = 3                       # drawn large, placed small - stays crisp on a projector

# ---------------------------------------------------------------------------
# 1. THE CHECKER
# ---------------------------------------------------------------------------
FILL_ORDER = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s",
              "4f", "5d", "6p", "7s", "5f", "6d", "7p"]
CAP = {"s": 2, "p": 6, "d": 10, "f": 14}
NOBLE = [("He", 2), ("Ne", 10), ("Ar", 18), ("Kr", 36), ("Xe", 54), ("Rn", 86)]
NOBLE_Z = dict(NOBLE)
SYMBOL = {1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N", 8: "O", 9: "F",
          10: "Ne", 11: "Na", 12: "Mg", 13: "Al", 14: "Si", 15: "P", 16: "S", 17: "Cl",
          18: "Ar", 19: "K", 20: "Ca", 21: "Sc", 22: "Ti", 23: "V", 24: "Cr", 25: "Mn",
          26: "Fe", 27: "Co", 28: "Ni", 29: "Cu", 30: "Zn", 31: "Ga", 32: "Ge",
          33: "As", 34: "Se", 35: "Br", 36: "Kr"}
# The only two exceptions taught. value = {subshell: electrons} overrides for Z.
EXCEPTION = {24: {"4s": 1, "3d": 5}, 29: {"4s": 1, "3d": 10}}

UNI_SUP = "⁰¹²³⁴⁵⁶⁷⁸⁹"


def mark(cfg):
    """'1s2 2s2' -> '1s^{2} 2s^{2}'. Only digits that follow a subshell letter are raised."""
    out, i = [], 0
    while i < len(cfg):
        ch = cfg[i]
        out.append(ch)
        if ch in "spdf" and i > 0 and cfg[i - 1].isdigit():
            j = i + 1
            while j < len(cfg) and cfg[j].isdigit():
                j += 1
            out.append("^{" + cfg[i + 1:j] + "}")
            i = j
            continue
        i += 1
    return "".join(out)


def parse(cfg):
    """'[Ar] 4s2 3d6' -> (core_symbol_or_None, [(subshell, count), ...])."""
    core, parts = None, []
    for tok in cfg.split():
        if tok.startswith("["):
            core = tok.strip("[]")
        else:
            letter = next(c for c in tok if c in "spdf")
            k = tok.index(letter)
            parts.append((tok[:k + 1], int(tok[k + 1:])))
    return core, parts


def electrons(cfg):
    core, parts = parse(cfg)
    return (NOBLE_Z[core] if core else 0) + sum(n for _, n in parts)


def ground_state(Z):
    """The expected ground-state configuration as {subshell: electrons}."""
    left, out = Z, {}
    for sub in FILL_ORDER:
        if left <= 0:
            break
        take = min(CAP[sub[1]], left)
        out[sub] = take
        left -= take
    if Z in EXCEPTION:
        out.update(EXCEPTION[Z])
    return out


def full_string(Z):
    gs = ground_state(Z)
    return " ".join(f"{s}{gs[s]}" for s in FILL_ORDER if s in gs)


def shorthand_string(Z):
    core = max((nz for sym, nz in NOBLE if nz < Z), default=None)
    sym = next(s for s, nz in NOBLE if nz == core)
    gs = ground_state(Z)
    # Filling-order writing: drop every subshell the core already holds.
    held = {s for s in FILL_ORDER[:FILL_ORDER.index(
        {2: "2s", 10: "3s", 18: "4s", 36: "5s"}[core])]}
    rest = " ".join(f"{s}{gs[s]}" for s in FILL_ORDER if s in gs and s not in held)
    return f"[{sym}] {rest}"


def expand(cfg):
    """Any configuration string -> {subshell: electrons}, expanding the noble-gas core."""
    core, parts = parse(cfg)
    out = {}
    if core:
        cz = NOBLE_Z[core]
        out.update(ground_state(cz))
    for sub, n in parts:
        out[sub] = out.get(sub, 0) + n
    return out


def unpaired_in(Z):
    """Unpaired electrons in the ground state of Z, using Hund's rule per sublevel."""
    total = 0
    for sub, n in ground_state(Z).items():
        boxes = {"s": 1, "p": 3, "d": 5, "f": 7}[sub[1]]
        total += n if n <= boxes else 2 * boxes - n
    return total


def check_config(cfg, Z):
    """Return the list of rules a configuration string breaks for element Z."""
    broken = []
    if electrons(cfg) != Z:
        broken.append("count")
    ex = expand(cfg)
    if any(n > CAP[s[1]] for s, n in ex.items()):
        broken.append("caps")
    core, parts = parse(cfg)
    if core:
        # shorthand core must be the noble gas of the previous period
        want = max((nz for _, nz in NOBLE if nz < Z), default=None)
        if NOBLE_Z[core] != want:
            broken.append("core")
    order = [FILL_ORDER.index(s) for s, _ in parts]
    if order != sorted(order):
        broken.append("order")
    # Aufbau: a later subshell holds electrons while an earlier one is not full.
    # The taught exceptions (Cr, Cu) are the measured ground state, so they are exempt.
    if Z in EXCEPTION and ex == ground_state(Z):
        return broken
    seen_open = False
    for sub in FILL_ORDER:
        n = ex.get(sub, 0)
        if seen_open and n:
            broken.append("aufbau")
            break
        if n < CAP[sub[1]]:
            seen_open = True
    if not broken and ex != ground_state(Z):
        broken.append("observed")          # follows the rules, is not the real ground state
    return broken


def ion_string(Z, charge):
    """Cation of Z with `charge`, shorthand, filling order. Electrons leave the highest n first, then the
    highest l (4s before 3d), from the measured ground state."""
    ex = dict(ground_state(Z))
    for _ in range(charge):
        sub = max((k for k, v in ex.items() if v), key=lambda k: (int(k[0]), "spdf".index(k[1])))
        ex[sub] -= 1
    core = max(nz for _, nz in NOBLE if nz < Z)
    sym = next(sy for sy, nz in NOBLE if nz == core)
    held = set(FILL_ORDER[:FILL_ORDER.index({2: "2s", 10: "3s", 18: "4s", 36: "5s"}[core])])
    rest = " ".join(f"{k}{ex[k]}" for k in FILL_ORDER if ex.get(k) and k not in held)
    return f"[{sym}] {rest}"


def period_of(Z):
    return next(i for i, (_, nz) in enumerate(NOBLE + [("", 10 ** 6)], 1) if Z <= nz)


def group_of(Z):
    """Group (1-18) of an element in periods 3 and 4 (the rows the strip draws)."""
    p = period_of(Z)
    lo, hi = STRIP_PERIODS[p]
    return (Z - lo + 1) if (p == 4 or Z - lo + 1 <= 2) else Z - lo + 1 + 10


# Every config the slides print, declared once. (label, Z, ascii string, expected unpaired)
GOOD = [
    ("O",  8,  "1s2 2s2 2p4",                    2),
    ("N",  7,  "1s2 2s2 2p3",                    3),
    ("Cl", 17, "1s2 2s2 2p6 3s2 3p5",            1),
    ("Cl", 17, "[Ne] 3s2 3p5",                   1),
    ("Ca", 20, "1s2 2s2 2p6 3s2 3p6 4s2",        0),
    ("Fe", 26, "1s2 2s2 2p6 3s2 3p6 4s2 3d6",    4),
    ("Fe", 26, "[Ar] 4s2 3d6",                   4),
    ("Cr", 24, "[Ar] 4s1 3d5",                   6),
    ("Cu", 29, "[Ar] 4s1 3d10",                  1),
    ("Ca", 20, "[Ar] 4s2",                       0),
    ("K",  19, "[Ar] 4s1",                       1),     # slide 18 correction of (b)
    ("P",  15, "1s2 2s2 2p6 3s2 3p3",            3),     # slide 21 answers, in the notes
    ("S",  16, "[Ne] 3s2 3p4",                   2),
    ("Ge", 32, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2", 2),     # the noble-gas shorthand build
    ("Ge", 32, "[Ar] 4s2 3d10 4p2",              2),
    # the notation-only examples (Aluminum; Bromine and Nickel): no orbital diagram on those slides
    ("Al", 13, "1s2 2s2 2p6 3s2 3p1",            1),
    ("Al", 13, "[Ne] 3s2 3p1",                   1),
    ("Br", 35, "[Ar] 4s2 3d10 4p5",              1),
    ("Ni", 28, "[Ar] 4s2 3d8",                   2),
]
# Ions that the exception slides point forward to (S2.4). (label, Z, charge, ascii string). Computed by removing
# electrons valence-first (highest n, then highest l) from the MEASURED ground state, and compared.
ION = [
    ("Cu+",  29, 1, "[Ar] 3d10"),
    ("Cu2+", 29, 2, "[Ar] 3d9"),
]
# Beyond the required scope (Z > 36). Used ONLY in teacher notes, as counterexamples to the half/full heuristic.
# Electron totals are checked here; the configurations themselves are NOT verified against a source from this
# environment, so the notes must say PROVISIONAL wherever they appear.
BEYOND_SCOPE = [
    ("Nb", 41, "[Kr] 5s1 4d4"),        # not half-full, still moves an electron
    ("W",  74, "[Xe] 6s2 4f14 5d4"),   # regular, although Cr and Mo (same group) are exceptions
]
# The periodic-table strip on the shorthand slide: periods 3 and 4, with the three elements it marks.
STRIP_PERIODS = {3: (11, 18), 4: (19, 36)}
STRIP_MARK = {"before": 18, "element": 32, "wrong": 36}
# The deliberately wrong ones, and the check each one must trip.
BAD = [
    ("O",  8,  "1s2 2s2 2p6",         "count"),     # 10 electrons
    ("K",  19, "[Ar] 3d1",            "aufbau"),    # 3d before 4s
    ("Ca", 20, "[Ne] 4s2",            "count"),     # wrong core, only 12 electrons
    ("Cr", 24, "[Ar] 4s2 3d4",        "observed"),  # follows the rules, not the real atom
    ("Cu", 29, "[Ar] 4s2 3d9",        "observed"),
    ("Ge", 32, "[Kr] 4s2 3d10 4p2",   "core"),      # krypton comes AFTER germanium: the wrong core (never printed)
]
# Orbital diagrams. u = up, d = down, "" = empty box, uu = two same-spin (illegal).
DIAGRAMS = {
    "N_2p_correct":  ("N",  7, "2p", ["u", "u", "u"]),
    "N_2p_wrong":    ("N",  7, "2p", ["ud", "u", ""]),
    "pauli_ok":      ("-",  0, "-",  ["ud"]),
    "pauli_bad":     ("-",  0, "-",  ["uu"]),
    "N": ("N", 7,  None, [("1s", ["ud"]), ("2s", ["ud"]), ("2p", ["u", "u", "u"])]),
    "O": ("O", 8,  None, [("1s", ["ud"]), ("2s", ["ud"]), ("2p", ["ud", "u", "u"])]),
    "Fe": ("Fe", 26, None, [("4s", ["ud"]), ("3d", ["ud", "u", "u", "u", "u"])]),
    "Cr_pred": ("Cr", 24, None, [("4s", ["ud"]), ("3d", ["u", "u", "u", "u", ""])]),
    "Cr_act":  ("Cr", 24, None, [("4s", ["u"]), ("3d", ["u", "u", "u", "u", "u"])]),
    "Cu_pred": ("Cu", 29, None, [("4s", ["ud"]), ("3d", ["ud", "ud", "ud", "ud", "u"])]),
    "Cu_act":  ("Cu", 29, None, [("4s", ["u"]), ("3d", ["ud", "ud", "ud", "ud", "ud"])]),
    # slides 19-20: the Hund (spins) and Pauli error-spotting pair, and the Check Yourself S answer
    "N_2p_spins_wrong": ("N", 7, "2p", ["u", "d", "u"]),
    "pauli_Ne_2s_wrong": ("Ne", 10, "2s", ["uu"]),
    "pauli_Ne_2s_fixed": ("Ne", 10, "2s", ["ud"]),
    "S_3p":          ("S", 16, "3p", ["ud", "u", "u"]),
}


def box_violations(boxes):
    """Pauli and Hund violations inside one sublevel's row of boxes."""
    v = set()
    for b in boxes:
        if b == "uu" or b == "dd":
            v.add("pauli")
    if any(len(b) == 2 for b in boxes) and any(b == "" for b in boxes):
        v.add("hund")                       # paired while another box is empty
    singles = [b for b in boxes if len(b) == 1]
    if len(set(singles)) > 1:
        v.add("hund")                       # unpaired spins not parallel
    return v


def count_arrows(boxes):
    return sum(len(b) for b in boxes)


def run_checks():
    n_checked = 0
    for sym, Z, cfg, unp in GOOD:
        assert SYMBOL[Z] == sym, (sym, Z)
        assert electrons(cfg) == Z, f"{sym} {cfg}: {electrons(cfg)} != {Z}"
        assert check_config(cfg, Z) == [], f"{sym} {cfg}: {check_config(cfg, Z)}"
        # unpaired count for the *given* config (Cr, Cu use the observed state)
        got = sum(n if n <= {"s": 1, "p": 3, "d": 5, "f": 7}[s[1]]
                  else 2 * {"s": 1, "p": 3, "d": 5, "f": 7}[s[1]] - n
                  for s, n in expand(cfg).items())
        if sym == "Cr":
            assert got == 6, got                       # 4s1 + five singles
        else:
            assert got == unp, f"{sym} {cfg}: unpaired {got} != {unp}"
        n_checked += 1
    # the string builders agree with the hand-written ones
    for sym, Z, cfg, _ in GOOD:
        want = shorthand_string(Z) if cfg.startswith("[") else full_string(Z)
        assert want == cfg, f"{sym}: builder {want!r} != written {cfg!r}"
    for sym, Z, cfg, rule in BAD:
        got = check_config(cfg, Z)
        assert rule in got, f"{sym} {cfg}: expected {rule}, got {got}"
        n_checked += 1
    # the counts quoted in the content brief
    for Z, expect in [(15, "1s2 2s2 2p6 3s2 3p3"), (16, "[Ne] 3s2 3p4"), (25, "[Ar] 4s2 3d5"),
                      (35, "[Ar] 4s2 3d10 4p5"), (28, "[Ar] 4s2 3d8"), (32, "[Ar] 4s2 3d10 4p2")]:
        s = expect
        assert electrons(s) == Z and check_config(s, Z) == [], (Z, s)
    # diagrams: arrows = electrons, and the rules hold/break as labelled
    for key, (sym, Z, _, content) in DIAGRAMS.items():
        if key in ("N_2p_correct", "N_2p_wrong", "N_2p_spins_wrong"):
            assert count_arrows(content) == 3
        elif key.startswith("pauli"):
            assert count_arrows(content) == 2
        elif key == "S_3p":
            assert count_arrows(content) == 4          # S 3p4
        else:
            arrows = sum(count_arrows(b) for _, b in content)
            core = {"Fe": 18, "Cr_pred": 18, "Cr_act": 18, "Cu_pred": 18, "Cu_act": 18}.get(key, 0)
            assert arrows + core == Z, f"{key}: {arrows}+{core} != {Z}"
            for _, b in content:
                assert not box_violations(b), (key, b)
    assert box_violations(DIAGRAMS["N_2p_correct"][3]) == set()
    assert box_violations(DIAGRAMS["N_2p_wrong"][3]) == {"hund"}
    assert box_violations(DIAGRAMS["pauli_ok"][3]) == set()
    assert box_violations(DIAGRAMS["pauli_bad"][3]) == {"pauli"}
    # slides 19-20. (e): three singles, spins not all parallel -> Hund only. (f): up-up -> Pauli only.
    assert box_violations(DIAGRAMS["N_2p_spins_wrong"][3]) == {"hund"}
    assert box_violations(DIAGRAMS["pauli_Ne_2s_wrong"][3]) == {"pauli"}
    assert box_violations(DIAGRAMS["pauli_Ne_2s_fixed"][3]) == set()
    assert box_violations(DIAGRAMS["S_3p"][3]) == set()
    # the (e) fix is the already-validated N 2p diagram; the (f) fix is an up-down pair; both 2s holds 2
    assert DIAGRAMS["N_2p_correct"][3] == ["u", "u", "u"] and DIAGRAMS["pauli_Ne_2s_fixed"][3] == ["ud"]
    # Ne 2s is a filled 2s: Ne is 1s2 2s2 2p6 and its 2s holds 2
    assert ground_state(10)["2s"] == 2 and DIAGRAMS["pauli_Ne_2s_fixed"][1] == 10
    # S 3p: the 4 electrons are 1 pair + 2 singles (2 unpaired), matching the answer in the notes
    assert ground_state(16)["3p"] == 4 and unpaired_in(16) == 2 and unpaired_in(15) == 3
    # unpaired claims used in card text
    assert unpaired_in(7) == 3 and unpaired_in(8) == 2 and unpaired_in(17) == 1
    assert unpaired_in(20) == 0 and unpaired_in(26) == 4
    # Cr / Cu: predicted != actual, both 6 and 11 electrons past argon
    assert sum(n for _, n in parse("[Ar] 4s2 3d4")[1]) == 6 == sum(n for _, n in parse("[Ar] 4s1 3d5")[1])
    assert sum(n for _, n in parse("[Ar] 4s2 3d9")[1]) == 11 == sum(n for _, n in parse("[Ar] 4s1 3d10")[1])
    # --- S2.3 additions: Ge shorthand build, Cu and Cr exceptions, their ions, the strip, the counterexamples
    for lab, Z, ch, cfg in ION:
        assert ion_string(Z, ch) == cfg, f"{lab}: valence-first removal gives {ion_string(Z, ch)!r}, written {cfg!r}"
        assert electrons(cfg) == Z - ch, f"{lab}: {electrons(cfg)} electrons, expected {Z - ch}"
        n_checked += 1
    # the 4s1 electron leaves first: Cu+ has no 4s, and Cu2+ then loses one 3d
    assert ground_state(29)["4s"] == 1 and "4s" not in dict(parse("[Ar] 3d10")[1])
    for sym, Z, cfg in BEYOND_SCOPE:
        assert Z > 36 and electrons(cfg) == Z, f"{sym} {cfg}: {electrons(cfg)} != {Z}"
        n_checked += 1
    # a move changes no electron count, and moves exactly one electron out of 4s
    for Z in (24, 29):
        pred = {k: v for k, v in ground_state_aufbau(Z).items()}
        act = ground_state(Z)
        assert sum(pred.values()) == sum(act.values()) == Z
        assert pred["4s"] - act["4s"] == 1 and act["3d"] - pred["3d"] == 1, (Z, pred, act)
        assert {k for k in pred if pred[k] != act[k]} == {"4s", "3d"}
    # the strip: the noble gas BEFORE Ge is Ar (end of period 3); Kr ends Ge's own period, AFTER it
    ar, ge, kr = STRIP_MARK["before"], STRIP_MARK["element"], STRIP_MARK["wrong"]
    assert (SYMBOL[ar], SYMBOL[ge], SYMBOL[kr]) == ("Ar", "Ge", "Kr")
    assert max(nz for _, nz in NOBLE if nz < ge) == ar and ar < ge < kr
    assert period_of(ar) == 3 and period_of(ge) == 4 and period_of(kr) == 4
    assert group_of(ar) == 18 and group_of(kr) == 18 and group_of(ge) == 14
    assert NOBLE_Z["Ar"] == ar and NOBLE_Z["Kr"] == kr
    # Ge's first five segments are exactly argon's configuration (the highlight in the build)
    segs = parse("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2")[1]
    assert dict(segs[:5]) == ground_state(ar) and sum(n for _, n in segs[:5]) == 18
    # the two sums the Ge text build shows: the longhand sum (leaves at click 3) and the shorthand's own sum (click 4)
    assert sum(n for _, n in segs) == ge == 32
    assert "+".join(str(n) for _, n in segs) == "2+2+6+2+6+2+10+2"
    assert f"{ar} + " + " + ".join(str(n) for _, n in segs[5:]) + f" = {ge}" == "18 + 2 + 10 + 2 = 32"
    return n_checked


def ground_state_aufbau(Z):
    """What the filling rules alone give (the exception table ignored)."""
    left, out = Z, {}
    for sub in FILL_ORDER:
        if left <= 0:
            break
        out[sub] = min(CAP[sub[1]], left)
        left -= out[sub]
    return out


def check_against_spec():
    """The slide text is the text that was checked. Every config string must appear verbatim,
    nothing unchecked may appear, and no Unicode superscript glyph may survive anywhere."""
    import re
    if not os.path.exists(SPEC):
        print("  (spec not written yet - slide-text cross-check skipped)")
        return
    spec = json.load(open(SPEC, encoding="utf-8"))
    slides = spec["slides"]
    text = json.dumps(spec["slides"], ensure_ascii=False)
    # 1. markup only: no Unicode superscript digits in any slide field or note
    assert not any(ch in text for ch in UNI_SUP), "Unicode superscript glyph left in the spec"
    # 2. every slide has teacher notes, and every empty image slot's subject is in them
    for i, sl in enumerate(slides, 1):
        assert sl.get("notes", "").strip(), f"slide {i}: no notes"
        for subj in sl.get("imageSubjects", {}).values():
            assert subj in sl["notes"], f"slide {i}: image prompt missing from notes"
    assert "PROVISIONAL" in slides[0]["notes"] and "Mo, Ag" in slides[0]["notes"]
    # 3. slide text (fields only, not notes)
    ftext = json.dumps([sl["fields"] for sl in slides], ensure_ascii=False).replace("\\n", " ")
    # the click builds (builds.json) print text too: state lines, titles, and the text-line longhand/shorthand
    bspec = json.load(open(BUILDS, encoding="utf-8")) if os.path.exists(BUILDS) else {"builds": []}
    built = [mark(bb["longhand"]) + " " + mark(shorthand_string(bb["z"]))
             for bb in bspec["builds"] if bb.get("type") == "text_line"]
    ftext = ftext + " " + json.dumps(bspec, ensure_ascii=False) + " " + " ".join(built)
    off_slide = {"[Kr] 4s2 3d10 4p2"}       # Ge with the wrong core: never printed
    notes_only = {"1s2 2s2 2p6 3s2 3p3", "[Ne] 3s2 3p4"}   # P, S answers: speaker notes only
    missing = []
    for _, _, cfg, _ in GOOD:
        if cfg not in notes_only and mark(cfg) not in ftext:
            missing.append(("good", cfg, mark(cfg)))
    for _, _, cfg, _ in BAD:
        if cfg not in off_slide and mark(cfg) not in ftext:
            missing.append(("bad", cfg, mark(cfg)))
    # 4. strays: any config-looking token on a slide or in a note that no checked string contains
    checked = ({c for _, _, c, _ in GOOD} | {c for _, _, c, _ in BAD} | {c for *_, c in ION}
               | {c for _, _, c in BEYOND_SCOPE})
    pat_f = r"(?:\[[A-Z][a-z]\] ?)?(?:\d[spdf]\^\{\d+\} ?)+"
    pat_n = r"(?:\[[A-Z][a-z]\] ?)?(?:\d[spdf]\^\d+ ?)+"
    toks = [re.sub(r"\^\{?(\d+)\}?", r"\1", t).strip() for t in re.findall(pat_f, ftext)]
    toks += [re.sub(r"\^(\d+)", r"\1", t).strip()
             for t in re.findall(pat_n, " ".join(sl["notes"] for sl in slides))]
    strays = sorted({t for t in toks if t and not any(t in c for c in checked)})
    if missing:
        print("  MISSING from spec:", missing)
    if strays:
        print("  tokens in the spec or notes that no checked configuration contains:", strays)
    assert not missing, "slide text does not contain a checked configuration"
    assert not strays, "unchecked configuration on a slide or in the notes"
    # 5. the corrected configurations on the Spot-the-Mistake solutions slide are the checked ones
    def slide_by_headline(h):          # by headline, not position: slides get inserted
        return next(sl for sl in slides if sl["fields"].get("headline") == h)
    sol = " ".join(str(v) for v in slide_by_headline("Spot the Mistake, Worked")["fields"].values())
    for cfg in ["1s2 2s2 2p4", "[Ar] 4s1", "[Ar] 4s2", "[Ar] 4s1 3d5"]:
        assert mark(cfg) in sol, f"Spot the Mistake, Worked: missing corrected {cfg}"
    # each correction really is the ground state of its element
    for sym, Z, cfg in [("O", 8, "1s2 2s2 2p4"), ("K", 19, "[Ar] 4s1"), ("Ca", 20, "[Ar] 4s2"),
                        ("Cr", 24, "[Ar] 4s1 3d5")]:
        assert check_config(cfg, Z) == [], (sym, cfg)
        assert expand(cfg) == ground_state(Z), (sym, cfg)
    # 5b. S2.3 additions: ions the Cu slide points to, counterexamples kept off the student slides
    for lab, Z, ch, cfg in ION:
        assert mark(cfg) in ftext, f"{lab}: {cfg} is not on the Cu slide"
    note_text = {sl["fields"].get("headline"): sl["notes"] for sl in slides}
    for sym, Z, cfg in BEYOND_SCOPE:
        assert mark(cfg) not in ftext, f"{sym} {cfg} is beyond the required scope and must stay in the notes"
    why = slide_by_headline("Why Cr and Cu Break the Pattern")
    wtext = " ".join(str(v) for v in why["fields"].values())
    assert "simplification" in wtext and "look the rest up" in wtext, "Why slide must say it is a simplification"
    assert "always" not in wtext.lower(), "the Why slide must not claim half-full or full is always more stable"
    wn = why["notes"]
    for must in ("PROVISIONAL", "Nb", "[Kr] 5s^1 4d^4", "[Xe] 6s^2 4f^14 5d^4", "Mo, Ag and Au", "Cu^+ = [Ar] 3d^10",
                 "Cu^2+ = [Ar] 3d^9", "exchange stabilization"):
        assert must in wn, f"Why slide notes lack {must!r}"
    assert "click build" in note_text["Check Yourself"].lower(), "Check Yourself notes must point at the Cu build"
    heads = [sl["fields"].get("headline") for sl in slides]
    i_ng = heads.index("Noble-Gas Shorthand")
    assert heads[i_ng + 1] == "Shorthand: Germanium", "the Ge build slide must directly follow Noble-Gas Shorthand"
    assert "Two Exceptions: Cr and Cu" not in heads, "the old single exceptions slide should have been replaced"
    cu_i = heads.index("Exception: Copper")
    assert heads[cu_i:cu_i + 3] == ["Exception: Copper", "Exception: Chromium", "Why Cr and Cu Break the Pattern"]
    # builds.json agrees with the tables: Ge text line, Cu and Cr moves (predicted -> measured)
    for bb in bspec["builds"]:
        if bb.get("type") == "text_line":
            assert bb["longhand"] in [c for _, _, c, _ in GOOD] and electrons(bb["longhand"]) == bb["z"]
            assert bb["core"] == "Ar" and max(nz for _, nz in NOBLE if nz < bb["z"]) == NOBLE_Z[bb["core"]]
        if bb.get("predicted"):
            Z = bb["z"]
            pred = ground_state_aufbau(Z)
            assert {x["label"]: x["electrons"] for x in bb["sublevels"]} == {k: pred[k] for k in ("4s", "3d")}
            assert bb["start_text"] == mark("[Ar] " + " ".join(f"{k}{pred[k]}" for k in ("4s", "3d")))
            assert bb["steps"][-1]["text"] == "Actual: " + mark(shorthand_string(Z))
            assert bb["steps"][0].get("from") == "4s" and bb["steps"][-1].get("to") == "3d"
            key = {24: "Cr", 29: "Cu"}[Z]
            for (sub, boxes), sl_ in zip(DIAGRAMS[key + "_pred"][3], bb["sublevels"]):
                assert count_arrows(boxes) == sl_["electrons"], (key, sub)
    # 6. the Noble-Gas Shorthand slide carries the same-period-noble-gas note, and it is true: Ar is Cl's own period
    assert "not [Ar]" in slide_by_headline("Noble-Gas Shorthand")["fields"]["mustwrite"]
    # 7. sequence: orbital-notation block first, then the notation block, then the notation-only examples,
    #    then the exceptions. Notation-only examples carry no orbital diagram of any kind.
    for a_, b_ in [("Reading an Orbital Diagram", "Filling Oxygen's 2p Boxes"), ("Filling Oxygen's 2p Boxes", "Writing a Configuration"),
                  ("Writing a Configuration", "Example: Oxygen"), ("Example: Oxygen", "Oxygen, Worked"),
                  ("Oxygen, Worked", "Example: Iron"), ("Example: Iron", "Iron, Worked"),
                  ("Iron, Worked", "Longhand: N, Cl, and Ca"), ("Longhand: N, Cl, and Ca", "Noble-Gas Shorthand"),
                  ("Shorthand: Germanium", "Why [Ar] and Not [Kr]?"), ("Why [Ar] and Not [Kr]?", "Example: Aluminum"),
                  ("Example: Aluminum", "Aluminum, Worked"), ("Aluminum, Worked", "Example: Bromine and Nickel"),
                  ("Example: Bromine and Nickel", "Bromine and Nickel, Worked"),
                  ("Bromine and Nickel, Worked", "Exception: Copper")]:
        assert heads.index(a_) + 1 == heads.index(b_), f"order: {b_!r} must directly follow {a_!r}"
    notation_only = ["Example: Aluminum", "Aluminum, Worked", "Example: Bromine and Nickel", "Bromine and Nickel, Worked"]
    builds_by_head = {heads[bb["slide"] - 1] for bb in bspec["builds"]}
    EXPECT_BUILDS = {"Reading an Orbital Diagram", "Filling Oxygen's 2p Boxes", "Oxygen, Worked", "Iron, Worked",
                     "Shorthand: Germanium", "Exception: Copper", "Exception: Chromium"}
    assert builds_by_head == EXPECT_BUILDS, f"builds sit on the wrong slides: {sorted(builds_by_head ^ EXPECT_BUILDS)}"
    for bb in bspec["builds"]:                      # each build's asserted layout and title match its slide
        assert slides[bb["slide"] - 1]["master"] == bb["layout"], f"build on slide {bb['slide']}: layout differs"
    for h in notation_only:
        sl_ = slide_by_headline(h)
        assert h not in builds_by_head and "images" not in sl_, f"{h}: a picture or build is on a notation-only slide"
        words = (" ".join(str(v) for v in sl_["fields"].values()) + " " + sl_["notes"]).lower()
        for banned in ("orbital diagram", "boxes", "arrow", "hund", "pauli", "unpaired"):
            assert banned not in words.replace("no orbital diagram", "").replace("no diagram", ""), f"{h}: {banned!r} on a notation-only slide"
    # every configuration on the new slides is one of the tables above, and the elements are the right ones
    new_text = " ".join(str(v) for h in notation_only for v in slide_by_headline(h)["fields"].values()).replace("\n", " ")
    new_toks = {re.sub(r"\^\{?(\d+)\}?", r"\1", t).strip()
                for t in re.findall(r"(?:\[[A-Z][a-z]\] ?)?(?:\d[spdf]\^\{\d+\} ?)+", new_text)}
    table = {c for _, _, c, _ in GOOD}
    assert new_toks and new_toks <= table, f"configurations on the new slides not in GOOD: {sorted(new_toks - table)}"
    for cfg in ["1s2 2s2 2p6 3s2 3p1", "[Ne] 3s2 3p1", "[Ar] 4s2 3d10 4p5", "[Ar] 4s2 3d8"]:
        assert cfg in new_toks, f"new example missing {cfg}"
    for sym, Z, cfg in [("Al", 13, "1s2 2s2 2p6 3s2 3p1"), ("Al", 13, "[Ne] 3s2 3p1"), ("Br", 35, "[Ar] 4s2 3d10 4p5"),
                        ("Ni", 28, "[Ar] 4s2 3d8")]:
        assert check_config(cfg, Z) == [] and expand(cfg) == ground_state(Z), (sym, cfg)
    assert check_config("[Ar] 3s2 3p1", 13) != [] and check_config("[Kr] 4s2 3d10 4p5", 35) != []   # the traps in the notes
    assert "[Ne]" in slide_by_headline("Example: Aluminum")["fields"]["mustwrite"]
    assert "[Ar]" in slide_by_headline("Example: Bromine and Nickel")["fields"]["mustwrite"]
    assert check_config("[Ar] 3s2 3p5", 17) != []         # the error the note warns against
    print(f"  spec cross-check: {len(GOOD) + len(BAD)} configurations verbatim, no strays, "
          f"no Unicode superscripts, notes on all {len(slides)} slides")


# ---------------------------------------------------------------------------
# 2. THE DRAWING
# ---------------------------------------------------------------------------
def tokens():
    t = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
    return {"white": t["ground"]["white"]["hex"], "asphalt": t["ground"]["asphalt"]["hex"],
            "graphite": t["ground"]["graphite"]["hex"], "hair": t["ground"]["ruleHairline"]["hex"],
            "good": t["courses"]["chemistry"]["primaryDeep"]["hex"],
            "bad": t["semantic"]["danger"]["deep"],
            "lime": t["courses"]["chemistry"]["primary"]["hex"],
            "parch": t["ground"]["parchment"]["hex"]}


COL = tokens()


def font(name, px):
    return ImageFont.truetype(os.path.join(REPO, "brand", "fonts", name), int(px * SCALE))


class Canvas:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.im = Image.new("RGB", (w * SCALE, h * SCALE), COL["white"])
        self.d = ImageDraw.Draw(self.im)

    def P(self, v):
        return int(round(v * SCALE))

    def line(self, pts, color, width):
        self.d.line([(self.P(x), self.P(y)) for x, y in pts], fill=color, width=self.P(width),
                    joint="curve")

    def poly(self, pts, color):
        self.d.polygon([(self.P(x), self.P(y)) for x, y in pts], fill=color)

    def rect(self, x, y, w, h, outline, width, fill=None, dash=False):
        if dash:
            self.dashed_rect(x, y, w, h, outline, width)
            return
        self.d.rectangle([self.P(x), self.P(y), self.P(x + w), self.P(y + h)],
                         outline=outline, width=self.P(width), fill=fill)

    def dashed_rect(self, x, y, w, h, color, width, dash=14, gap=9):
        for (x0, y0, x1, y1) in [(x, y, x + w, y), (x + w, y, x + w, y + h),
                                 (x + w, y + h, x, y + h), (x, y + h, x, y)]:
            L = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
            ux, uy = (x1 - x0) / L, (y1 - y0) / L
            t = 0
            while t < L:
                e = min(t + dash, L)
                self.line([(x0 + ux * t, y0 + uy * t), (x0 + ux * e, y0 + uy * e)], color, width)
                t += dash + gap

    def text(self, x, y, s, f, color, anchor="mm"):
        self.d.text((self.P(x), self.P(y)), s, font=f, fill=color, anchor=anchor)

    def save(self, name):
        os.makedirs(ASSETS, exist_ok=True)
        path = os.path.join(ASSETS, name)
        self.im.save(path)
        print(f"wrote {os.path.relpath(path, REPO)}  {self.im.width}x{self.im.height}")


def spin_arrow(c, cx, top, bottom, up, color=None, shaft=9, head_w=30, head_h=26):
    """One spin arrow as a shape: a shaft and a filled triangle head."""
    color = color or COL["asphalt"]
    if up:
        c.line([(cx, bottom), (cx, top + head_h - 2)], color, shaft)
        c.poly([(cx - head_w / 2, top + head_h), (cx + head_w / 2, top + head_h), (cx, top)], color)
    else:
        c.line([(cx, top), (cx, bottom - head_h + 2)], color, shaft)
        c.poly([(cx - head_w / 2, bottom - head_h), (cx + head_w / 2, bottom - head_h), (cx, bottom)],
               color)


def orbital_box(c, x, y, size, content, border=None, width=5, dash=False, bad=False):
    """One orbital: a box, with 0, 1 or 2 spin arrows in it."""
    border = border or COL["asphalt"]
    c.rect(x, y, size, size, border, width, fill=COL["white"], dash=dash)
    k = size / 120.0
    top, bottom = y + 20 * k, y + size - 20 * k
    sh, hw, hh = max(6, 9 * k), 30 * k, 26 * k
    if len(content) == 1:
        spin_arrow(c, x + size / 2, top, bottom, content == "u", shaft=sh, head_w=hw, head_h=hh)
    elif len(content) == 2:
        spin_arrow(c, x + size * 0.32, top, bottom, content[0] == "u", shaft=sh, head_w=hw, head_h=hh)
        spin_arrow(c, x + size * 0.68, top, bottom, content[1] == "u", shaft=sh, head_w=hw, head_h=hh)


def tick(c, cx, cy, color, s=1.0):
    c.line([(cx - 30 * s, cy + 2 * s), (cx - 8 * s, cy + 26 * s), (cx + 34 * s, cy - 26 * s)], color, 11)


def cross(c, cx, cy, color, s=1.0):
    c.line([(cx - 26 * s, cy - 26 * s), (cx + 26 * s, cy + 26 * s)], color, 11)
    c.line([(cx - 26 * s, cy + 26 * s), (cx + 26 * s, cy - 26 * s)], color, 11)


F_BOLD = lambda px: font("Archivo-Bold.ttf", px)
F_SEMI = lambda px: font("Archivo-SemiBold.ttf", px)
F_REG = lambda px: font("Archivo-Regular.ttf", px)


# ---- figure 1: Aufbau filling-order chart ---------------------------------
def fig_aufbau():
    c = Canvas(1010, 600)
    cols = {"s": 125, "p": 365, "d": 605, "f": 845}
    rows = {1: "s", 2: "sp", 3: "spd", 4: "spdf", 5: "spdf", 6: "spd", 7: "sp"}
    cw, ch, y0, pitch = 150, 62, 62, 82
    pos = {}
    for n, letters in rows.items():
        for l in letters:
            pos[f"{n}{l}"] = (cols[l], y0 + (n - 1) * pitch)
    assert sorted(pos, key=FILL_ORDER.index) == FILL_ORDER          # exactly the 19
    bold = {"4s", "3d"}
    arrow = COL["graphite"]
    # arrows first, so boxes sit on top of any overlap at the ends
    def seg(A, B, head=True):
        (ax, ay), (bx, by) = A, B
        ex, ey = ax - 75, ay + 26            # leaves A's left edge
        nx, ny = bx + 75, by - 26            # enters B's right edge
        c.line([(ex, ey), (nx - 7, ny + 2.5)], arrow, 7)
        dx, dy = nx - ex, ny - ey
        L = (dx * dx + dy * dy) ** 0.5
        ux, uy = dx / L, dy / L
        px, py = -uy, ux
        hl, hw = 30, 15
        c.poly([(nx, ny), (nx - ux * hl + px * hw, ny - uy * hl + py * hw),
                (nx - ux * hl - px * hw, ny - uy * hl - py * hw)], arrow)
    diagonals = [["1s"], ["2s"], ["2p", "3s"], ["3p", "4s"], ["3d", "4p", "5s"],
                 ["4d", "5p", "6s"], ["4f", "5d", "6p", "7s"], ["5f", "6d", "7p"]]
    flat = [s for dg in diagonals for s in dg]
    assert flat == FILL_ORDER
    for dg in diagonals:
        # stub leading into the first cell of each diagonal
        bx, by = pos[dg[0]]
        nx, ny = bx + 75, by - 26
        sx, sy = nx + 66, ny - 23
        c.line([(sx, sy), (nx + 5, ny - 2)], arrow, 7)
        ux, uy = -66 / 70.0, 23 / 70.0
        px, py = -uy, ux
        c.poly([(nx, ny), (nx - ux * 30 + px * 15, ny - uy * 30 + py * 15),
                (nx - ux * 30 - px * 15, ny - uy * 30 - py * 15)], arrow)
        for a, b in zip(dg, dg[1:]):
            seg(pos[a], pos[b])
    for name, (cx, cy) in pos.items():
        heavy = name in bold
        c.rect(cx - cw / 2, cy - ch / 2, cw, ch, COL["asphalt"], 8 if heavy else 3, fill=COL["white"])
        c.text(cx, cy + 2, name, F_BOLD(48), COL["asphalt"])
    c.save("chem_u02_s2.3_aufbau_order.png")


# ---- figure 2: Pauli, allowed vs not allowed ------------------------------
def fig_pauli():
    c = Canvas(1010, 600)
    rows = [("pauli_ok", 40, True, "CORRECT", "opposite spins"),
            ("pauli_bad", 330, False, "WRONG", "same spin")]
    for key, y, ok, head, sub in rows:
        content = DIAGRAMS[key][3]
        bad = not ok
        orbital_box(c, 90, y + 20, 210, content[0], COL["bad"] if bad else COL["asphalt"], 8 if bad else 5)
        (cross if bad else tick)(c, 395, y + 125, COL["bad"] if bad else COL["good"], 1.3)
        c.text(470, y + 95, head, F_BOLD(56), COL["bad"] if bad else COL["good"], "lm")
        c.text(470, y + 160, sub, F_REG(50), COL["asphalt"], "lm")
    c.line([(60, 300), (950, 300)], COL["hair"], 3)
    c.save("chem_u02_s2.3_pauli.png")


# ---- figure 3: Hund, correct vs incorrect ---------------------------------
def fig_hund():
    c = Canvas(1010, 600)
    rows = [("N_2p_correct", 20, True, "CORRECT", "singles first"),
            ("N_2p_wrong", 315, False, "WRONG", "pairs too soon")]
    for key, y, ok, head, sub in rows:
        boxes = DIAGRAMS[key][3]
        size, pitch, x0 = 130, 142, 40
        for i, b in enumerate(boxes):
            flagged = (not ok) and (len(b) == 2 or b == "")
            orbital_box(c, x0 + i * pitch, y + 30, size, b,
                        COL["bad"] if flagged else COL["asphalt"], 8 if flagged else 5)
        c.text(x0 + pitch + size / 2, y + 30 + size + 40, "2p", F_BOLD(50), COL["asphalt"])
        cx = 520
        (cross if not ok else tick)(c, cx, y + 95, COL["bad"] if not ok else COL["good"], 1.1)
        c.text(cx + 55, y + 70, head, F_BOLD(52), COL["bad"] if not ok else COL["good"], "lm")
        c.text(cx + 55, y + 130, sub, F_REG(48), COL["asphalt"], "lm")
    c.line([(40, 300), (970, 300)], COL["hair"], 3)
    c.save("chem_u02_s2.3_hund.png")



def cfg_label(c, cx, y, sub, count, px=54):
    """'2p' with its electron count raised beside it. Drawn, not a glyph, so the count
    is as large as the letters: it is the number students are meant to read."""
    fb, fs = F_BOLD(px), F_BOLD(px * 0.78)
    wb = fb.getlength(sub) / SCALE
    ws = fs.getlength(str(count)) / SCALE
    x = cx - (wb + ws + 2) / 2
    c.text(x, y, sub, fb, COL["asphalt"], "lm")
    c.text(x + wb + 2, y - px * 0.30, str(count), fs, COL["asphalt"], "lm")

def draw_groups(c, groups, x_start, y, size, inner, outer, label_dy, cfg_text, f_label=54):
    """Draw labelled groups of boxes. Returns the x of each group's centre."""
    x = x_start
    for (sub, boxes), cfg in zip(groups, cfg_text):
        gw = len(boxes) * size + (len(boxes) - 1) * inner
        for i, b in enumerate(boxes):
            orbital_box(c, x + i * (size + inner), y, size, b)
        cfg_label(c, x + gw / 2, y + size + label_dy, sub, cfg, f_label)
        x += gw + outer
    return x


# ---- figure 4: anatomy, nitrogen ------------------------------------------
def fig_anatomy_n():
    c = Canvas(1010, 600)
    groups = DIAGRAMS["N"][3]
    sym = "N"
    c.text(505, 62, "NITROGEN   Z = 7", F_BOLD(54), COL["asphalt"])
    size, inner, outer = 140, 14, 62
    width = sum(len(b) * size + (len(b) - 1) * inner for _, b in groups) + outer * (len(groups) - 1)
    x0 = (1010 - width) / 2
    cfgs = [2, 2, 3]
    draw_groups(c, groups, x0, 150, size, inner, outer, 56, cfgs, 58)
    c.line([(80, 410), (930, 410)], COL["hair"], 3)
    c.text(505, 490, "2 + 2 + 3 = 7 arrows = 7 electrons", F_SEMI(52), COL["asphalt"])
    # count what was drawn
    assert sum(count_arrows(b) for _, b in groups) == 7
    c.save("chem_u02_s2.3_orbital_diagram_nitrogen.png")


# ---- figure 5: oxygen (solution slide, "data" slot, 846 x 496) -------------
def fig_oxygen():
    c = Canvas(846, 496)
    groups = DIAGRAMS["O"][3]
    c.text(423, 52, "OXYGEN   Z = 8", F_BOLD(50), COL["asphalt"])
    size, inner, outer = 112, 10, 44
    width = sum(len(b) * size + (len(b) - 1) * inner for _, b in groups) + outer * (len(groups) - 1)
    draw_groups(c, groups, (846 - width) / 2, 118, size, inner, outer, 52,
                [2, 2, 4], 52)
    c.line([(60, 350), (786, 350)], COL["hair"], 3)
    c.text(423, 420, "2 + 2 + 4 = 8", F_SEMI(52), COL["asphalt"])
    assert sum(count_arrows(b) for _, b in groups) == 8
    c.save("chem_u02_s2.3_orbital_diagram_oxygen.png")


# ---- figure 6: iron (solution slide) --------------------------------------
def fig_iron():
    c = Canvas(846, 496)
    groups = DIAGRAMS["Fe"][3]
    c.text(423, 52, "IRON   Z = 26", F_BOLD(50), COL["asphalt"])
    size, inner, outer = 100, 8, 48
    width = sum(len(b) * size + (len(b) - 1) * inner for _, b in groups) + outer * (len(groups) - 1)
    draw_groups(c, groups, (846 - width) / 2, 120, size, inner, outer, 52,
                [2, 6], 52)
    c.line([(60, 350), (786, 350)], COL["hair"], 3)
    c.text(423, 420, "[Ar] 18 + 2 + 6 = 26", F_SEMI(52), COL["asphalt"])
    assert 18 + sum(count_arrows(b) for _, b in groups) == 26
    c.save("chem_u02_s2.3_orbital_diagram_iron.png")


# ---- figure 7: Cr and Cu, predicted vs actual -------------------------------
def fig_cr_cu():
    c = Canvas(1010, 600)
    size, inner, gap = 80, 8, 30
    x0 = 150
    xs = [x0 + i * (size + inner) for i in range(1)]
    # column captions: 4s over the first box, 3d over the five
    x4s = x0
    x3d = x0 + size + gap
    c.text(x4s + size / 2, 36, "4s", F_BOLD(50), COL["asphalt"])
    c.text(x3d + (5 * size + 4 * inner) / 2, 36, "3d", F_BOLD(50), COL["asphalt"])
    spec = [("Cr", "Cr_pred", "Cr_act", 82), ("Cu", "Cu_pred", "Cu_act", 340)]
    for sym, kp, ka, y in spec:
        c.text(70, y + 100, sym, F_BOLD(72), COL["asphalt"])
        for key, yy, actual in [(kp, y, False), (ka, y + 100, True)]:
            groups = DIAGRAMS[key][3]
            for (sub, boxes), gx in zip(groups, [x4s, x3d]):
                for i, b in enumerate(boxes):
                    orbital_box(c, gx + i * (size + inner), yy, size, b,
                                COL["asphalt"] if actual else COL["graphite"],
                                6 if actual else 3, dash=not actual)
            tx = x3d + 5 * size + 4 * inner + 28
            c.text(tx, yy + size / 2, "actual" if actual else "predicted",
                   F_BOLD(50) if actual else F_REG(50),
                   COL["good"] if actual else COL["graphite"], "lm")
    c.line([(40, 300), (970, 300)], COL["hair"], 3)
    # electron counts past argon, re-added
    for key_p, key_a in [("Cr_pred", "Cr_act"), ("Cu_pred", "Cu_act")]:
        a = sum(count_arrows(b) for _, b in DIAGRAMS[key_p][3])
        b_ = sum(count_arrows(b) for _, b in DIAGRAMS[key_a][3])
        assert a == b_
    c.save("chem_u02_s2.3_cr_cu_exceptions.png")



# ---- figure 8: the periodic-table strip for germanium's noble gas --------------
def strip_cells(period):
    """Cells of one period: (column label, text). s-block and d-block are spans, p-block singles.
    Computed from the atomic numbers, so the strip cannot disagree with the checker."""
    lo, hi = STRIP_PERIODS[period]
    cells = []
    s_end = lo + 1
    cells.append(("1-2", f"{SYMBOL[lo]}\u2013{SYMBOL[s_end]}"))
    d_lo, d_hi = (21, 30) if period == 4 else (None, None)
    cells.append(("3-12", f"{SYMBOL[d_lo]}\u2013{SYMBOL[d_hi]}" if d_lo else "\u2014"))
    p_lo = (31 if period == 4 else 13)
    for Z in range(p_lo, hi + 1):
        assert group_of(Z) == 13 + (Z - p_lo)
        cells.append((str(group_of(Z)), SYMBOL[Z]))
    return cells


def fig_ge_strip():
    """Periods 3 and 4 as a strip: argon (end of period 3) marked as the noble gas BEFORE germanium,
    germanium in period 4, krypton (end of period 4, AFTER germanium) marked as the wrong choice.
    Marks are a tick, a cross and words as well as colour. 1010 x 600 = the slot, at 200 px per inch."""
    ar, ge, kr = STRIP_MARK["before"], STRIP_MARK["element"], STRIP_MARK["wrong"]
    c = Canvas(1010, 600)
    widths = [176, 176] + [88] * 6
    x_lab, x0 = 30, 84
    colx = [x0]
    for w in widths[:-1]:
        colx.append(colx[-1] + w)
    row_y = {3: 100, 4: 218}
    ch = 100
    # header: group numbers
    heads = [h for h, _ in strip_cells(4)]
    for cx_, w, h in zip(colx, widths, heads):
        c.text(cx_ + w / 2, 52, h, F_REG(46), COL["graphite"])
    for period, y in row_y.items():
        c.text(x_lab + 6, y + ch / 2, str(period), F_BOLD(56), COL["asphalt"], "lm")
        for cx_, w, (grp, txt) in zip(colx, widths, strip_cells(period)):
            sym = txt
            border, bw, fill, tcol, f = COL["hair"], 3, COL["white"], COL["asphalt"], F_REG(46 if "\u2013" in sym else 50)
            if sym == "Ar":
                border, bw, fill, f = COL["asphalt"], 8, COL["lime"], F_BOLD(48)
            elif sym == "Ge":
                border, bw, fill, f = COL["asphalt"], 8, COL["parch"], F_BOLD(48)
            elif sym == "Kr":
                border, bw, tcol, f = COL["bad"], 8, COL["bad"], F_BOLD(48)
            c.rect(cx_ + 2, y, w - 4, ch, border, bw, fill=fill)
            c.text(cx_ + w / 2, y + ch / 2, txt, f, tcol)
    # legend, drawn from the same three atomic numbers
    ly = 376
    tick(c, 62, ly + 38, COL["good"], 1.0)
    c.text(110, ly + 38, f"{SYMBOL[ar]}: ends period 3, BEFORE {SYMBOL[ge]}", F_BOLD(50), COL["good"], "lm")
    ly += 78
    cross(c, 62, ly + 38, COL["bad"], 1.0)
    c.text(110, ly + 38, f"{SYMBOL[kr]}: ends period 4, AFTER {SYMBOL[ge]}", F_BOLD(50), COL["bad"], "lm")
    ly += 78
    c.text(110, ly + 38, f"{SYMBOL[ge]}: period 4, group 14", F_BOLD(50), COL["asphalt"], "lm")
    c.save("chem_u02_s2.3_ge_noble_gas_strip.png")


def _row_label(c, x, y, s, f=None):
    c.text(x, y, s, f or F_BOLD(54), COL["asphalt"], "lm")


def fig_spot_problem():
    """Slide 19: the two wrong diagrams, neutral colour. Drawn from DIAGRAMS, not retyped."""
    c = Canvas(1010, 600)
    size, pitch = 130, 142
    e = DIAGRAMS["N_2p_spins_wrong"][3]
    f = DIAGRAMS["pauli_Ne_2s_wrong"][3]
    _row_label(c, 40, 105, "(e)  N")
    for i, b in enumerate(e):
        orbital_box(c, 400 + i * pitch, 40, size, b)
    c.text(400 + pitch + size / 2, 215, "2p", F_BOLD(50), COL["asphalt"])
    c.line([(40, 300), (970, 300)], COL["hair"], 3)
    _row_label(c, 40, 405, "(f)  Ne")
    orbital_box(c, 400 + pitch, 340, size, f[0])
    c.text(400 + pitch + size / 2, 515, "2s", F_BOLD(50), COL["asphalt"])
    assert count_arrows(e) == 3 and count_arrows(f) == 2
    c.save("chem_u02_s2.3_spot_diagrams.png")


def fig_spot_fixed():
    """Slide 20 (data slot, 846 x 496): the corrected diagrams, with the rule that fixed each."""
    c = Canvas(846, 496)
    size, pitch = 100, 112
    e = DIAGRAMS["N_2p_correct"][3]
    f = DIAGRAMS["pauli_Ne_2s_fixed"][3]
    _row_label(c, 30, 90, "(e)  N", F_BOLD(50))
    for i, b in enumerate(e):
        orbital_box(c, 190 + i * pitch, 40, size, b)
    c.text(190 + pitch + size / 2, 176, "2p", F_BOLD(50), COL["asphalt"])
    tick(c, 570, 92, COL["good"], 1.0)
    c.text(620, 92, "Hund", F_BOLD(50), COL["good"], "lm")
    c.line([(40, 232), (806, 232)], COL["hair"], 3)
    _row_label(c, 30, 322, "(f)  Ne", F_BOLD(50))
    orbital_box(c, 190 + pitch, 272, size, f[0])
    c.text(190 + pitch + size / 2, 408, "2s", F_BOLD(50), COL["asphalt"])
    tick(c, 570, 324, COL["good"], 1.0)
    c.text(620, 324, "Pauli", F_BOLD(50), COL["good"], "lm")
    assert count_arrows(e) == 3 and count_arrows(f) == 2
    c.save("chem_u02_s2.3_spot_diagrams_fixed.png")


def main():
    n = run_checks()
    print(f"checker: {n} configuration checks, all diagrams validated "
          f"(good configs pass, wrong configs fail the stated rule)")
    check_against_spec()
    fig_aufbau()
    fig_pauli()
    fig_hund()
    fig_anatomy_n()
    fig_oxygen()
    fig_iron()
    fig_cr_cu()
    fig_spot_problem()
    fig_spot_fixed()
    fig_ge_strip()
    return 0


if __name__ == "__main__":
    sys.exit(main())
