"""Shared access to the science libraries (RDKit, mendeleev, pint) and brand tokens.

Figure and problem builders import this instead of each reaching for the libraries
and for brand/tokens.json on their own. The libraries are optional installs (see
scripts/setup-environment.sh); `require()` fails with a message that says what to run.

Nothing here writes a rule or a course fact. mendeleev is a cross-check, never a source:
a value that has to reach a student page is verified (verify-content) and written into
the spec by a person.
"""
import json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(REPO, "brand", "fonts")


def require(*names):
    """Import and return the named libraries, or exit saying how to install them."""
    mods, missing = [], []
    for n in names:
        try:
            mods.append(__import__(n, fromlist=["_"]))
        except ImportError:
            missing.append(n)
    if missing:
        sys.exit(f"missing python package(s): {', '.join(missing)}\n"
                 "install with: python3 -m pip install rdkit mendeleev pint")
    return mods[0] if len(mods) == 1 else mods


def tokens():
    with open(os.path.join(REPO, "brand", "tokens.json")) as fh:
        return json.load(fh)


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def palette(course):
    """Ground and course colours for a figure, as hex strings, all read from tokens.json."""
    t = tokens()
    if course not in t["courses"]:
        sys.exit(f"unknown course '{course}'; expected one of {', '.join(t['courses'])}")
    return {
        "white": t["ground"]["white"]["hex"],
        "asphalt": t["ground"]["asphalt"]["hex"],
        "graphite": t["ground"]["graphite"]["hex"],
        "accent": t["courses"][course]["primaryDeep"]["hex"],
    }


def font_path(name):
    return os.path.join(FONT_DIR, name)


def molar_mass_check(formula_mass, element_symbols_counts, tol=0.02):
    """Cross-check a stated molar mass against standard atomic weights from mendeleev.

    element_symbols_counts: {"C": 2, "H": 4, "O": 2}. Returns (computed, ok).
    A reporting aid only: a False result means look again, not that either number is wrong.
    """
    element = require("mendeleev").element
    computed = sum(element(sym).atomic_weight * n for sym, n in element_symbols_counts.items())
    return computed, abs(computed - formula_mass) <= tol
