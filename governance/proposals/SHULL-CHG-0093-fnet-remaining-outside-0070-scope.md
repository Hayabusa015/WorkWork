# SHULL-CHG-0093 — "Fnet" remains in Physics sources that SHULL-CHG-0070 F1 does not list

Repeat of: SHULL-CHG-0070 (partial: the F1 scope recorded there is incomplete)

> SHULL-CHG-0070 is APPROVED and F1 (switch the U3 deck to ∑F) is approved. This record only
> widens F1's listed scope. No conflict with a LOCKED rule is known.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0093 |
| **Date** | 2026-11-22 |
| **Source** | Researcher finding, weekly sweep 2026-11-22 (`reports/2026-W47/researcher.md` row 5) |
| **Current Rule** | `governance/proposals/SHULL-CHG-0070-physics-sum-of-forces-notation.md` F1: "U3 deck still prints `Fnet`. Matt approved switching it." Its location column names only "SHULL Physics Unit 03 - Forces and Motion.pptx". |
| **Proposed Rule** | Add to the F1 deck-switch scope: `scripts/build_diagram_phys_u03.py` (lines 140, 218, 404: regenerate the three images with ∑F), and the docstrings at `templates/slide/decks/phys_u03_specs.py` line 8 and `templates/worksheet/specs/phys_u03_slide_solutions.py` line 7. |
| **Supersedes** | Nothing in the rule layer. Corrects the F1 scope note on SHULL-CHG-0070. |
| **Reason** | The deck diagrams print "Fnet = 0", "Fnet = +30 N − 10 N = +20 N" and the axis label "net force Fnet (N)" (confirmed by grep). A text-only deck switch would leave Fnet in the images. Both docstrings justify Fnet with "Archivo has no Greek capital sigma"; `courses/physics/DECISIONS.md` now says U+2211 ∑ is available, so that reasoning is superseded. No U+03A3 Σ was found in non-legacy sources. Already covered elsewhere: the deck specs (F1) and `templates/practice/specs/physics.json` (F2, no-retrofit). |
| **Affected Agents** | Designer (deck and diagrams), Auditor (slide audits). |
| **Affected Skills** | build-presentation. |
| **Affected Courses** | Physics. |
| **Risk** | Low. |
| **Recommendation** | Adopt. Run F1 together with SHULL-CHG-0074 so the deck is rebuilt once. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |
