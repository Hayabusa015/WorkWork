#!/usr/bin/env python3
"""Fail if a U#/S#.# code is used that does not exist in that course's DECISIONS.md.

This is the check that would have caught the Geology numbering offset before a
packet printed with the wrong footer. Governance section 6, Check 2.

    python3 scripts/validate_codes.py
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _shullos import REPO, walk, read, report, section_codes, COURSE_BY_CODE

# A code is only checked when the surrounding text says which course it belongs to:
# either a SHULL_ filename or an explicit CHEM/PHYS/GEO nearby. A bare "U08_S08.2"
# in a generic example is not attributable and is not checked.
FILENAME = re.compile(r"SHULL_(CHEM|PHYS|GEO)_[A-Za-z_]+_U(\d{1,2})_S(\d{1,2}\.\d)")

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
