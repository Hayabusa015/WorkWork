#!/usr/bin/env python3
"""Fail if a U#/S#.# code is used that does not exist in that course's DECISIONS.md.

This is the check that would have caught the Geology numbering offset before a
packet printed with the wrong footer. Governance section 6, Check 2.

    python3 scripts/validate_codes.py
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _shullos import REPO, walk, read, report, section_codes, COURSE_BY_CODE

# A code is only checked when the surrounding text says which course it belongs to:
# either a SHULL_ filename or an explicit CHEM/PHYS/GEO nearby. A bare "U08_S08.2"
# in a generic example is not attributable and is not checked.
FILENAME = re.compile(r"SHULL_(CHEM|PHYS|GEO)_[A-Za-z_]+_U(\d{1,2})_S(\d{1,2}\.\d)")

# A deck spec states its code in structured fields, not in a SHULL_ filename, so the
# pattern above cannot see it. T-10 proved that: a spec declaring Chemistry section 1.9
# - which does not exist - sat in the repo and this validator passed it, while the
# builder cheerfully produced a deck footered U01 S01.9. That is the Geology numbering
# failure exactly, and it is what this standard exists to prevent.
SPEC_KEYS = ("course", "unit", "section")


def spec_codes(rel, text):
    """(course, unit, section) for every section a spec declares. Empty if it is not
    a spec."""
    if not rel.endswith(".json"):
        return []
    try:
        spec = json.loads(text)
    except ValueError:
        return []
    if not isinstance(spec, dict) or "course" not in spec or "unit" not in spec:
        return []
    if all(k in spec for k in SPEC_KEYS):                    # a deck spec: one section
        return [(str(spec["course"]).lower(), spec["unit"], str(spec["section"]))]
    if isinstance(spec.get("sections"), list):               # notes and worksheet specs
        # These carry a list. The builders check them too, but only when something is
        # built - a spec sitting in the repo with a bad code should not wait that long.
        return [(str(spec["course"]).lower(), spec["unit"], str(x))
                for x in spec["sections"]]
    return []

def main():
    valid = {c: section_codes(c) for c in ("chemistry", "physics", "geology")}
    missing = [c for c, v in valid.items() if v is None]
    if missing:
        print(f"validate_codes: no DECISIONS.md for {', '.join(missing)} — cannot validate")
        return 1

    errors, checked = [], 0
    for rel in walk():
        text = read(rel)
        checked += 1

        for course, unit, sect in spec_codes(rel, text):
            where = rel.replace(os.sep, "/")
            if course not in valid:
                errors.append(f"{where} — spec names course {course!r}, "
                              f"which is not one of {', '.join(sorted(valid))}")
                continue
            if sect not in valid[course]:
                errors.append(f"{where} — spec section {sect} is not in "
                              f"courses/{course}/DECISIONS.md")
                continue
            declared_unit = int(str(sect).split(".")[0])
            if int(unit) != declared_unit:
                errors.append(f"{where} — spec unit U{int(unit):02d} disagrees with "
                              f"section {sect}")

        for m in FILENAME.finditer(text):
            course_code, unit, sect = m.group(1), int(m.group(2)), m.group(3)
            course = COURSE_BY_CODE[course_code]
            # Normalise the padded section code back to the declared form.
            u, s = sect.split(".")
            bare = f"{int(u)}.{s}"
            if bare not in valid[course]:
                line = text[: m.start()].count("\n") + 1
                errors.append(
                    f"{rel.replace(os.sep,'/')}:{line} {m.group(0)} — "
                    f"section {bare} is not in courses/{course}/DECISIONS.md")
            elif int(u) != unit:
                line = text[: m.start()].count("\n") + 1
                errors.append(
                    f"{rel.replace(os.sep,'/')}:{line} {m.group(0)} — "
                    f"unit U{unit:02d} disagrees with section {bare}")
    for c in ("chemistry", "physics", "geology"):
        print(f"  {c:10} {len(valid[c]):>3} valid section codes")
    return report("validate_codes", errors, checked)

if __name__ == "__main__":
    sys.exit(main())
