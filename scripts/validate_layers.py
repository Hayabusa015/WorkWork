#!/usr/bin/env python3
"""Fail if a course fact appears in a Layer 1 file.

Layer 1 is standards, skills, agents, brand and workflows - how a document is
made, course-independent. Layer 2 is courses/*/DECISIONS.md - what is taught.
A fact lives in exactly one place.

This is the check that would have caught the Chemistry skill: governance ordered
seven specific sections cut on 2026-09-05 and all seven were still there days
later, because a to-do list in a document is not a mechanism.

    python3 scripts/validate_layers.py
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _shullos import REPO, read, report

LAYER1 = ["standards", "brand", "workflows", ".claude", "templates"]

# Course facts, drawn from the decisions files themselves so this stays true as
# the courses change. Unit titles are the strongest signal: a Layer 1 file has no
# reason to name "Thermochemistry" or "Plate Tectonics".
UNIT_TITLE = re.compile(r"^\*\*U(\d{1,2})[ ·.]+([^*]+?)\*\*", re.M)
UNIT_TITLE_ALT = re.compile(r"^###\s+U(\d{1,2})\s*·\s*(.+?)\s+—", re.M)

# Grading weights and calendar dates are course facts wherever they appear.
GRADING = re.compile(r"\b(Tests?|Quizzes|Homework|Binders|Labs? & Projects)\s+\d{1,2}\s*%?", re.I)
CALENDAR = re.compile(r"\b(Aug|Sept?|Oct|Nov|Dec|Jan|Feb|Mar|Apr|May|Jun)\w*\s+\d{1,2},?\s+20\d\d")

STOP = {"the", "and", "of", "in", "a", "review", "waves", "optics", "gases", "energy"}


def unit_titles():
    out = {}
    for course in ("chemistry", "physics", "geology"):
        p = os.path.join("courses", course, "DECISIONS.md")
        if not os.path.exists(os.path.join(REPO, p)):
            continue
        text = read(p)
        for m in list(UNIT_TITLE.finditer(text)) + list(UNIT_TITLE_ALT.finditer(text)):
            title = re.sub(r"\(\d+ sections?\)|—.*$", "", m.group(2)).strip(" ·—-")
            # Distinctive titles only. Multi-word, or a single long word like
            # "Thermochemistry". A short common noun - Waves, Gases, Caves - would
            # false-positive on ordinary prose and is deliberately not matched.
            distinctive = len(title.split()) >= 2 or len(title) >= 9
            if distinctive and title.lower() not in STOP:
                out.setdefault(title, course)
    return out


def layer1_files():
    for d in LAYER1:
        root = os.path.join(REPO, d)
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [x for x in dirnames if x not in {".git", "palette-archive", "superseded"}]
            for fn in filenames:
                if fn.lower().endswith((".md", ".json", ".html", ".css")):
                    yield os.path.relpath(os.path.join(dirpath, fn), REPO)


def main():
    titles = unit_titles()
    if not titles:
        print("validate_layers: no unit titles parsed — cannot validate")
        return 1

    errors, checked = [], 0
    for rel in layer1_files():
        checked += 1
        text = read(rel)
        norm = rel.replace(os.sep, "/")
        for title, course in titles.items():
            if title in text:
                line = next((i for i, l in enumerate(text.splitlines(), 1) if title in l), "?")
                errors.append(f"{norm}:{line} names the {course} unit \"{title}\" — "
                              f"course facts belong in courses/{course}/DECISIONS.md")
        for m in GRADING.finditer(text):
            line = text[: m.start()].count("\n") + 1
            errors.append(f"{norm}:{line} states a grading weight ({m.group(0).strip()}) — "
                          f"that is a course fact")
        for m in CALENDAR.finditer(text):
            line = text[: m.start()].count("\n") + 1
            errors.append(f"{norm}:{line} states a calendar date ({m.group(0)}) — "
                          f"that is a course fact")
    print(f"  {len(titles)} unit titles indexed from the decisions files")
    return report("validate_layers", errors, checked)


if __name__ == "__main__":
    sys.exit(main())
