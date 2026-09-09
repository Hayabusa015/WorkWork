---
id: SHULL-CHG-0020
title: The Master_Physics card layout, and toner replaces marked as the ink budget
status: IMPLEMENTED
opened: 2026-09-09
decided: 2026-09-09
decided_by: Matthew Shull
---

# SHULL-CHG-0020 — The card layout

## What he asked for

He supplied `Master_Physics.pdf` as the design he wants:

> "look at the example i have given, you will need to modify a tiny bit but i love that example.
> the main thing is to get rid of the space where the problems are done because they do it in
> their lab notebooks, also make the header more ink saver."

and, on the same layout for the other two courses:

> "you can use that as the basis for chemistry and geology though"

## Adopted from his reference

- A card per question, bordered, with the number top left and the tier tag top right.
- Two short questions side by side on one row; longer ones full width.
- **REMEMBER** — a tinted panel with a heavy accent bar on its left, holding the concept recap.
- **BEFORE YOU START** — the prior-knowledge block, outlined rather than tinted so the two read
  as different things.
- Name / Date / Period as ruled fields on one line with the label sitting on the rule, rather than
  boxed. Score joins them, still summed from the questions and never typed.
- The unit eyebrow, the large section title, and the `U01 / S1.1` code on the right.

## The two changes he asked for

**No work space on a Physics sheet.** Already enforced by the course profile (SHULL-CHG-0019);
his reference has ruled "SHOW WORK HERE" areas under every question and they are gone.

**The header, measured.** His banner is a solid navy slab across the top of every page:
**28.46% marked, 8.70% toner, a 7.61 in solid band.** The band fails QA_GATE section 5 on its own —
the rule is "any solid fill larger than a small tag, chip or icon". The shape survives; the slab
does not. It is now an outlined header with a heavy accent bar on the left edge, which is the one
place a solid mark earns its ink.

## The ink budget was measuring the wrong thing

Fixing the header surfaced a defect in the gate itself. `audit_print_ink.py` used **marked** — the
count of pixels darker than white — as the ink budget. That counts a 7% grey tint exactly as hard
as solid black, and it produced a ranking that is simply false:

| | marked | toner | verdict |
|---|---|---|---|
| the new card layout, with two pale panels | 18.70% | **4.68%** | *failed* the old gate |
| his old PHYS U01 packet, navy banner every page | 12.47% | **8.15%** | *passed* the old gate |
| his `Master_Physics` mockup | 28.46% | 8.70% | — |
| his nebular cut-and-glue sheet | 6.72% | 3.09% | — |

The sheet the old gate failed lays down **43% less ink** than the sheet it passed. Toner coverage —
the mean darkness of the page — is the ink model, because a pixel at 93% white costs 7% of a black
one, which is what the cartridge spends.

So the audit now reports three numbers and fails on two:

- **toner** — ink volume, the budget. Ceiling **9.0%**, calibrated on his own files: his nebular
  sheet 3.09%, his old physics packet 8.15%, his mockup 8.70%. It passes everything he has written
  and shown, and fails a page meaningfully darker than any of it.
- **marked** — page density, reported. Ceiling raised to 40%, where it catches a genuinely covered
  page rather than one carrying a pale panel.
- **the widest solid band** — unchanged at 0.60 in, and it is what fails both of his own banners.

This change relaxes a gate that would otherwise have failed my own work, so: the threshold is set
from his files rather than from mine, both numbers are always printed, and the band check — the one
that catches the thing he actually asked me to fix — is untouched.

## A cost that is named rather than buried

His reference tags the tiers **green / amber / red**. Two departures:

`semantic.success` measures 2.28 on white and 5.02 at its deep variant, both under the 5.5 house
target, so it cannot be set as 7pt type. The easiest tier takes the muted label grey instead, which
suits a warm-up. The hardest takes full ink rather than a fourth hue.

The remaining cost: `semantic.danger` means *"danger, safety warning, error, stop"*. Spending it on
CHALLENGE dilutes that in a room where red also means hazard. The word CHALLENGE disambiguates it
and it is his design, so it ships — but it is a real cost. If he would rather keep red for hazards,
the ramp can run grey → course accent → ink with no loss to the layout.

## A defect the change exposed

`audit_worksheet.py` found the start of a section by matching the header's *wording*
(`SHULL SCIENCE · … · MR. SHULL`). Rewriting the header removed that string and the check silently
found nothing — it reported "not a worksheet built by this template" and passed the whole document
as one section. It now keys on the `U01 / S1.1` code, which is what identifies a section anyway,
and the running footer's different form (`U01 · S1.1-S1.4`) cannot be confused with it.

## Verification

- Physics **4 pages**, one section per page, down from 8 in his original packet.
- Chemistry 4 pages, Geology 2 — both on their declared budgets.
- Toner at worst: PHYS 5.30%, CHEM 3.42%, GEO 4.66%. **No solid band anywhere.**
- `audit_fonts.py` — Archivo only in all three.
- `validate_profiles.py` — 13 refusals fire, 3 real specs build.
- `hook-validate.sh` clean.
