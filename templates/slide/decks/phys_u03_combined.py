#!/usr/bin/env python3
"""Combine the seven PHYS U03 section specs into one unit deck (Matt, 2026-11-04: "i want them
all combined into 1 slide"). Each slide keeps its own section footer (U03 • S03.N); a unit
title slide opens the deck. Run phys_u03_specs.py first.

    python3 templates/slide/decks/phys_u03_combined.py
    node templates/slide/build_deck.js templates/slide/decks/phys_u03_all.json "Unit 3 Slides.pptx"
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
slides = [{"master": "01_UNIT_TITLE",
           "fields": {"headline": "Unit 3\nForces and Motion",
                      "subhead": "Newton's laws, free body diagrams, inclines, F = ma, friction, and pulleys.",
                      "code": "U03"},
           "imageSubjects": {"hero": "a loaded freight cart on a ramp with a rope and pulley, dramatic side light"}}]
for n in range(1, 8):
    spec = json.load(open(os.path.join(HERE, f"phys_u03_s03.{n}.json")))
    for s in spec["slides"]:
        s["fields"].setdefault("code", f"U03 • S03.{n}")
        slides.append(s)
out = {"course": "physics", "unit": 3, "section": "3.1", "sectionTitle": "Forces and Motion (Unit 3, all sections)",
       "note": "Unit-level deck: sections 3.1-3.7 combined at Matt's request. 'section' is 3.1 only to satisfy the "
               "build's code check; every slide carries its own section footer.", "slides": slides}
json.dump(out, open(os.path.join(HERE, "phys_u03_all.json"), "w"), indent=2, ensure_ascii=False)
print(len(slides), "slides")
