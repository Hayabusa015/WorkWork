#!/usr/bin/env python3
"""Fail if a guided-notes spec asks a question.

Guided notes are strictly recall: the page a student fills in while the slide
is up. The cue column names the thing to record; it does not ask for it. Both
renderers already refuse a spec that breaks the rule, but a spec can sit in the
repository unbuilt, and the specs are what the Designer copies when it writes a
new one — so a bad example teaches the defect forward.

The rule and its detection live in templates/notes/recall.py. This validator
only walks the specs and reports.

    python3 scripts/validate_notes.py
"""
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _shullos import REPO, report  # noqa: E402

sys.path.insert(0, os.path.join(REPO, "templates", "notes"))
import recall  # noqa: E402


def main():
    errors, checked = [], 0
    for path in sorted(glob.glob(os.path.join(REPO, "templates", "notes", "specs", "*.json"))):
        rel = os.path.relpath(path, REPO).replace(os.sep, "/")
        checked += 1
        with open(path, encoding="utf-8") as fh:
            spec = json.load(fh)
        for code, field, text in recall.offences(spec):
            where = "cue column" if field == "cues" else "notes line"
            errors.append(f"{rel} {code} {where}: {text[:78]} — guided notes are recall; "
                          f"name the thing to record, do not ask for it")
    return report("validate_notes", errors, checked)


if __name__ == "__main__":
    sys.exit(main())
