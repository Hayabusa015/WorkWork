#!/usr/bin/env python3
"""Build a SHULL Day-1 multiple-choice item bank (.txt) from a JSON spec.

    python3 templates/assessment/build_day1_item_bank.py specs/<spec>.json [outdir]

The Chemistry two-day unit test, Day 1: conceptual multiple choice, delivered through
Pear Assessment (formerly Edulastic), not printed. This builder does not know Pear's
import format and does not claim to - it produces a clean, ordered reference per
version that gets typed or pasted into the platform item by item, plus a separate
teacher key. Building a real Pear import file (CSV/QTI) is future work once the exact
format Pear accepts is confirmed; inventing one now would be an unverified claim of
integration this system does not have.

Every item is checked before anything is written:

  - exactly four choices, exactly one correct index
  - no "all of the above" / "none of the above" (standards/... build-assessment rule)
  - a distractor rationale for every wrong choice - a real misconception, not a
    placeholder, because a distractor with no stated reason is a random wrong number
  - every version covers the same learning targets in the same order, so "Version B"
    is a genuine equivalent form and not a different, easier test with the same name

Colour, layout, and print do not apply here - there is nothing to print. This file is
plain text on purpose.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _shull_docx import COURSE_CODE, known_sections, section_span, unit_title  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BANNED = ("all of the above", "none of the above")


def refuse(msg, *more):
    print("build_day1_item_bank: " + msg, file=sys.stderr)
    for m in more:
        print("   " + m, file=sys.stderr)
    return 1


def validate_versions(versions):
    if not versions:
        return "spec has no versions."
    base_targets = [it["learningTarget"] for it in versions[0]["items"]]
    for v in versions:
        for i, it in enumerate(v["items"], 1):
            where = f"version {v['label']} item {i}"
            choices = it.get("choices", [])
            if len(choices) != 4:
                return f"{where}: has {len(choices)} choices, needs exactly 4."
            if not (0 <= it.get("correct", -1) < 4):
                return f"{where}: \"correct\" must be an index 0-3 into choices."
            for c in choices:
                if any(b in c.lower() for b in BANNED):
                    return (f"{where}: choice {c!r} is a banned catch-all "
                            "(\"all/none of the above\"). Write a real fourth option.")
            rat = it.get("distractorRationale", [])
            if len(rat) != 4:
                return f"{where}: distractorRationale must have 4 entries (one per choice)."
            for ci, r in enumerate(rat):
                if ci == it["correct"]:
                    continue
                if not r or not r.strip():
                    return (f"{where}: choice {chr(65+ci)} has no distractor rationale. "
                            "A wrong choice with no stated misconception is a random "
                            "wrong answer, not a real distractor.")
        targets = [it["learningTarget"] for it in v["items"]]
        if targets != base_targets:
            return (f"version {v['label']} covers a different set/order of learning "
                    f"targets than version {versions[0]['label']}. Parallel versions "
                    "carry identical blueprints (QA_GATE #9).")
    return None


def write_bank(version, path):
    lines = [f"ITEM BANK — VERSION {version['label']}",
             "(reference copy for manual entry into Pear Assessment — not an "
             "automated import file)", ""]
    for i, it in enumerate(version["items"], 1):
        lines.append(f"{i}. {it['stem']}")
        for ci, c in enumerate(it["choices"]):
            lines.append(f"   {chr(65 + ci)}. {c}")
        lines.append("")
    open(path, "w", encoding="utf-8").write("\n".join(lines))


def write_key(spec, versions, path):
    # The unit name is a course fact - read from DECISIONS.md, never typed into a
    # spec. validate_layers.py refuses a spec that carries its own copy.
    utitle = unit_title(spec["course"], spec["unit"])
    lines = [f"ANSWER KEY — Unit {int(spec['unit'])}: {utitle}", ""]
    for v in versions:
        lines.append(f"=== VERSION {v['label']} ===")
        for i, it in enumerate(v["items"], 1):
            correct_letter = chr(65 + it["correct"])
            lines.append(f"{i}. Correct: {correct_letter}  —  {it['learningTarget']}")
            for ci, c in enumerate(it["choices"]):
                if ci == it["correct"]:
                    continue
                lines.append(f"     {chr(65+ci)} wrong because: {it['distractorRationale'][ci]}")
            lines.append("")
        lines.append("")
    open(path, "w", encoding="utf-8").write("\n".join(lines))


def main():
    if len(sys.argv) < 2:
        return refuse("usage: build_day1_item_bank.py <spec.json> [outdir]")
    spec = json.load(open(sys.argv[1]))
    course = spec["course"]
    if course not in COURSE_CODE:
        return refuse(f"unknown course {course!r}.")
    outdir = sys.argv[2] if len(sys.argv) > 2 else HERE

    valid = known_sections(course)
    bad = [s for s in spec["sections"] if s not in valid]
    if bad:
        return refuse(f"section(s) {', '.join(bad)} are not in "
                      f"courses/{course}/DECISIONS.md.",
                      "Nothing is built against a code not in the decisions file.")

    day1 = spec.get("day1")
    if not day1:
        return refuse("spec has no \"day1\" block.")
    err = validate_versions(day1["versions"])
    if err:
        return refuse(err)

    code = COURSE_CODE[course]
    unit = f"U{int(spec['unit']):02d}"
    span = section_span(spec["sections"])

    for version in day1["versions"]:
        base = f"SHULL_{code}_Test_{unit}_{span}_Day1_{version['label']}"
        out = os.path.join(outdir, base + ".txt")
        write_bank(version, out)
        print(f"wrote {out}  —  Version {version['label']}, "
              f"{len(version['items'])} items")

    key_out = os.path.join(outdir, f"SHULL_{code}_Test_{unit}_{span}_Day1_Key.txt")
    write_key(spec, day1["versions"], key_out)
    print(f"wrote {key_out}  —  {len(day1['versions'])} version(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
