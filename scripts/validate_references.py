#!/usr/bin/env python3
"""Fail on a reference to a repository file that does not exist.

The legacy system carried ten of these - references to files that were specified
and never created, or created and never saved. SHULL_Color_Palette_Library.md was
the costly one: it was meant to be the single place the selected palette and the
archived alternates both lived, and because it never existed, an option that had
been explicitly passed over was later revived as a locked decision with nothing
to flag it.

This check is why that cannot happen twice.

    python3 scripts/validate_references.py
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _shullos import REPO, walk, read, report

DIRS = ("\\.claude/|scripts/|standards/|brand/|courses/|governance/|workflows/|"
        "schemas/|templates/|config/|docs/|change-log/|reports/|legacy/")
REF = re.compile(rf"`((?:{DIRS})[A-Za-z0-9_./-]+\.(?:md|py|json|css|html|sh|js|txt))`")

def main():
    errors, checked = [], 0
    for rel in walk():
        if not rel.endswith((".md", ".json", ".py", ".sh")):
            continue
        checked += 1
        text = read(rel)
        for m in REF.finditer(text):
            target = m.group(1)
            if os.path.exists(os.path.join(REPO, target)):
                continue
            # A path template rather than a real file.
            if any(t in target for t in ("<", "*", "NNNN", "YYYY")):
                continue
            line = text[: m.start()].count("\n") + 1
            errors.append(f"{rel.replace(os.sep,'/')}:{line} references {target} — which does not exist")
    return report("validate_references", errors, checked)

if __name__ == "__main__":
    sys.exit(main())
