#!/usr/bin/env python3
"""Prove the worksheet course profiles actually refuse what they say they refuse.

    python3 scripts/validate_profiles.py

The profiles in templates/worksheet/build_worksheet_docx.py are the mechanism that
keeps a Physics sheet from growing a work box and a Geology sheet from growing an
equation bar. A refusal that never fires is not a refusal, so each one is exercised
here against a spec built to trip it.

Each case states what it does and what the builder must say. If a case builds instead
of refusing, the profile has a hole.
"""
import copy, json, os, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(REPO, "templates", "worksheet", "build_worksheet_docx.py")
SPECS = os.path.join(REPO, "templates", "worksheet", "specs")


def load(name):
    return json.load(open(os.path.join(SPECS, name)))


def build(spec):
    d = tempfile.mkdtemp()
    p = os.path.join(d, "spec.json")
    json.dump(spec, open(p, "w"))
    r = subprocess.run([sys.executable, BUILD, p, os.path.join(d, "out.docx")],
                       capture_output=True, text=True)
    return r.returncode, (r.stderr + r.stdout)


def phys():
    return copy.deepcopy(load("phys_u01_s01.1-s01.4.json"))


def geo():
    return copy.deepcopy(load("geo_u01_s01.4.json"))


def chem():
    return copy.deepcopy(load("chem_u07_s07.4.json"))


def _work_box(s):
    s["sectionsContent"][0]["questions"][0]["math"] = True
    return s


def _ruled(s):
    s["sectionsContent"][0]["questions"][0]["answerLines"] = 3
    return s


def _no_pk(s):
    del s["sectionsContent"][0]["priorKnowledge"]
    return s


def _no_eq(s):
    del s["sectionsContent"][0]["equations"]
    return s


def _extra_q(s):
    q = copy.deepcopy(s["sectionsContent"][0]["questions"][2])
    s["sectionsContent"][0]["questions"].insert(3, q)
    return s


def _out_of_order(s):
    qs = s["sectionsContent"][0]["questions"]
    qs[0], qs[4] = qs[4], qs[0]
    return s


def _geo_eq(s):
    s["sectionsContent"][0]["equations"] = [{"plain": "v = d/t"}]
    return s


def _geo_math(s):
    s["sectionsContent"][0]["questions"] = [
        {"tier": "warm-up", "prompt": "Find the mass.", "math": True}]
    return s


def _geo_no_visual(s):
    s["sectionsContent"][0]["blocks"] = [
        {"kind": "reflection", "prompts": ["Why?"]}]
    return s


def _chem_no_eq(s):
    del s["equations"]
    return s


def _bad_code(s):
    s["sections"] = ["9.9"]
    s["sectionsContent"][0]["code"] = "9.9"
    return s


def _mismatch(s):
    s["sectionsContent"] = s["sectionsContent"][:1]
    return s


def _unknown_block(s):
    s["sectionsContent"][0]["blocks"] = [{"kind": "collage"}]
    return s


def _calc_no_answer(s):
    for q in s["sectionsContent"][0]["questions"]:
        if q.get("selfCheck"):
            del q["selfCheck"]
            return s
    s["sectionsContent"][0]["questions"][0]["calculation"] = True
    return s


def _geo_match_only(s):
    """A Geology sheet whose only visual element is a matching grid. This must BUILD -
    the point of SHULL-CHG-0022 is that a light format satisfies the rule."""
    s["sectionsContent"][0]["blocks"] = [
        {"kind": "match", "terms": ["Crust", "Mantle"],
         "descriptions": ["The outer skin.", "The thick middle."]}]
    return s


def _geo_prose_escape(s):
    """And a genuine reading response, declared as such, must build too."""
    s["sectionsContent"][0]["blocks"] = [
        {"kind": "reflection", "prompts": ["What changed your mind?"]}]
    s["sectionsContent"][0]["proseOnly"] = True
    return s


def _answer_on_last(s):
    s["sectionsContent"][0]["questions"][-1]["selfCheck"] = "[ 42 ]"
    return s


CASES = [
    ("physics refuses a work box",        phys, _work_box,     "no work areas at all"),
    ("physics refuses ruled answers",     phys, _ruled,        "no work areas at all"),
    ("physics needs prior knowledge",     phys, _no_pk,        "prior-knowledge recall"),
    ("physics needs its equations",       phys, _no_eq,        "no equations"),
    ("physics holds the 2/2/1/1 ramp",    phys, _extra_q,      "the ramp is"),
    ("questions must ramp upward",        chem, _out_of_order, "do not ramp"),
    ("geology refuses an equation bar",   geo,  _geo_eq,       "no math"),
    ("geology refuses a math question",   geo,  _geo_math,     "no math"),
    ("geology needs something visual",    geo,  _geo_no_visual, "the whole sheet is prose"),
    ("chemistry math needs equations",    chem, _chem_no_eq,   "no equation bar"),
    ("an unknown section code is refused", phys, _bad_code,    "not in"),
    ("sections and content must agree",   phys, _mismatch,     "same fact"),
    ("an unknown block kind is refused",  chem, _unknown_block, "unknown block kind"),
    ("a calculation needs its answer",    phys, _calc_no_answer, "no self-check answer"),
    ("the last question gets no answer",  phys, _answer_on_last, "without a net"),
]


# Cases that must BUILD, not refuse. A profile that refuses everything proves nothing,
# so the permissive side is tested too.
ALLOW = [
    ("a matching grid satisfies Geology", geo, _geo_match_only),
    ("a declared prose sheet is allowed",  geo, _geo_prose_escape),
]


def main():
    fails = []
    for name, base, mutate, expect in CASES:
        rc, out = build(mutate(base()))
        if rc == 0:
            fails.append((name, "BUILT — the refusal never fired"))
        elif expect not in out:
            fails.append((name, f"refused, but not for this reason: {out.strip()[:90]}"))
        else:
            print(f"  ok   {name}")

    for name, base, mutate in ALLOW:
        rc, out = build(mutate(base()))
        if rc:
            fails.append((name, f"refused a spec it should accept: {out.strip()[:110]}"))
        else:
            print(f"  ok   {name}")

    # And the three real specs must still build, or the profiles are refusing
    # everything and the cases above prove nothing.
    for f in ("phys_u01_s01.1-s01.4.json", "geo_u01_s01.4.json", "geo_u04_s04.1.json",
              "chem_u07_s07.4.json"):
        rc, out = build(load(f))
        if rc:
            fails.append((f, f"a good spec was refused: {out.strip()[:120]}"))
        else:
            print(f"  ok   {f} still builds")

    if fails:
        print("\nFAIL")
        for n, why in fails:
            print(f"  {n}: {why}")
        return 1
    print(f"\nOK - {len(CASES)} refusals fire, {len(ALLOW)} allowances hold, "
          f"4 real specs build")
    return 0


if __name__ == "__main__":
    sys.exit(main())
