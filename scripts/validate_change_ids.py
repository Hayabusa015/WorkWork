#!/usr/bin/env python3
"""Fail when two change records share a Change ID (SHULL-CHG-0078).

The allocation rule in governance/CHANGE_CONTROL.md ("Allocating a new Change
ID") says to take the next number from a freshly fetched origin/main. It did
not stop parallel branches each taking the same "next number" and landing
together, so eight IDs ended up naming 23 records. Matt chose to leave those
numbers as they are (option 1 of SHULL-CHG-0078): where an ID is shared, the
record's file path is its identifier.

This check makes the rule a mechanism. The duplicates that existed when the
decision was made are allow-listed below by exact filename, so:

  - a new record that reuses any existing number fails, including one of the
    eight already-shared numbers;
  - an allow-listed file that is renamed or removed fails too, so the list
    cannot quietly go stale.

The allow-list is closed. Adding to it is a governance change, not a fix.

    python3 scripts/validate_change_ids.py
"""
import os, re, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _shullos import REPO, report

PROPOSALS = os.path.join(REPO, "governance", "proposals")
NAME = re.compile(r"^(SHULL-CHG-\d{4})-.+\.md$")

# Records sharing a Change ID on 2026-11-23, kept as-is under SHULL-CHG-0078 option 1.
ALLOWED = {
    "SHULL-CHG-0023": {
        "SHULL-CHG-0023-assessment-template.md",
        "SHULL-CHG-0023-cognitive-load-visual-design.md",
        "SHULL-CHG-0023-notes-are-recall.md",
        "SHULL-CHG-0023-status-docs-stale-and-undocumented-app.md",
    },
    "SHULL-CHG-0024": {
        "SHULL-CHG-0024-app-identity-colour.md",
        "SHULL-CHG-0024-overseer-routes-classroom-builds.md",
        "SHULL-CHG-0024-physics-u1-vectors-section.md",
        "SHULL-CHG-0024-short-filenames.md",
        "SHULL-CHG-0024-validate-tokens-app-exclusion.md",
    },
    "SHULL-CHG-0046": {
        "SHULL-CHG-0046-equivalent-directions-on-keys.md",
        "SHULL-CHG-0046-phase-13-status-stale.md",
    },
    "SHULL-CHG-0054": {
        "SHULL-CHG-0054-chem-u3-short-unit.md",
        "SHULL-CHG-0054-chemistry-kinetic-orange.md",
        "SHULL-CHG-0054-notes-follow-slides.md",
    },
    "SHULL-CHG-0066": {
        "SHULL-CHG-0066-slide-template-four-fixes.md",
        "SHULL-CHG-0066-study-guide-unit-span.md",
    },
    "SHULL-CHG-0068": {
        "SHULL-CHG-0068-chemistry-reference-packet.md",
        "SHULL-CHG-0068-physics-u3-six-sections.md",
        "SHULL-CHG-0068-print-document-format-fixes.md",
    },
    "SHULL-CHG-0069": {
        "SHULL-CHG-0069-course-wide-reference-filename.md",
        "SHULL-CHG-0069-notes-no-inline-blanks.md",
    },
    "SHULL-CHG-0070": {
        "SHULL-CHG-0070-physics-sum-of-forces-notation.md",
        "SHULL-CHG-0070-reference-vsepr-grid-and-solubility-x.md",
    },
}


def main():
    files = sorted(f for f in os.listdir(PROPOSALS) if f.startswith("SHULL-CHG-"))
    errors, by_id = [], defaultdict(set)
    for f in files:
        m = NAME.match(f)
        if not m:
            errors.append(f"governance/proposals/{f}: name is not SHULL-CHG-NNNN-<slug>.md")
            continue
        by_id[m.group(1)].add(f)

    for cid, names in sorted(by_id.items()):
        allowed = ALLOWED.get(cid, set())
        extra = sorted(names - allowed) if len(names) > 1 else []
        for f in extra:
            errors.append(f"governance/proposals/{f}: {cid} is already used by "
                          f"{', '.join(sorted(names - {f}))}. Take the next free number from "
                          "origin/main (governance/CHANGE_CONTROL.md, Allocating a new Change ID)")

    for cid, names in sorted(ALLOWED.items()):
        for f in sorted(names - by_id.get(cid, set())):
            errors.append(f"scripts/validate_change_ids.py: allow-listed {f} no longer exists; "
                          "the allow-list is stale")

    return report("validate_change_ids", errors, len(files))


if __name__ == "__main__":
    sys.exit(main())
