# SHULL-CHG-0055 — Worksheet tier tags set in the muted label grey

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0055 |
| **Date** | 2026-10-28 |
| **Source** | User, 2026-10-28, answering the SHULL-CHG-0054 follow-up about the collision between the tier colour and the course deep. Verbatim: *"You could change the difficulty label, but I almost don't even like the difficulty label in there."* |
| **Current Rule** | See section 1, verbatim, with file and line. |
| **Proposed Rule** | See section 2. |
| **Supersedes** | The tier-colour part of SHULL-CHG-0020 (`governance/proposals/SHULL-CHG-0020-master-physics-layout.md`, "A cost that is named rather than buried"), as built in `templates/worksheet/build_worksheet_docx.py` `tier_colour()` lines 96-114 and stated in `templates/worksheet/README.md` line 58. The rest of SHULL-CHG-0020 is unchanged: the card layout, the tag position and column, the header, and the ink budget. |
| **Reason** | (1) It resolves the collision SHULL-CHG-0054 confirmed on the page. The amber PRACTICE tag (`semantic.caution` deep) and the Chemistry headings in Energy Orange Deep look like nearly the same orange-brown, and the same grey in greyscale. (2) It retires the cost SHULL-CHG-0020 named itself: `semantic.danger` was spent on CHALLENGE "in a room where red also means hazard". Afterwards, semantic amber and red mean only caution and danger again. |
| **Affected Agents** | Secretary (records). Designer and any agent that builds worksheets get the change through the builder. |
| **Affected Skills** | None restate the tier colours. `.claude/skills/build-document/SKILL.md` lines 78-83 cover the tag's position and the absence of a box only, and are unchanged. |
| **Affected Courses** | All three: Chemistry, Physics, Geology. See section 3 for why this is wider than the SHULL-CHG-0054 follow-up. |
| **Risk** | Low. Students lose colour as a difficulty cue. The tags stay as words in a fixed order. |
| **Recommendation** | Approve. Optional follow-up, the user's choice only: remove the tier tags altogether. The user said they "almost don't even like" the label, but did not ask for it to go. Removing it would be its own record. |
| **Decision** | **Approved by the user, 2026-10-28**, in the main session. Verbatim: *"You could change the difficulty label, but I almost don't even like the difficulty label in there."* Recorded under SHULL-CHG-0034. |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | 10c8a7f |
| **Verified** | Yes. The main session reported running these and the results below; I did not re-run them. It rebuilt the worksheets `chem_u01_s01.5_massnumbers`, `phys_u01_s01.1-s01.4` and `geo_u04_s04.1`. `audit_worksheet.py` passes on all three (page budget and ink). `validate_profiles.py` passes (15 refusals fire, 2 allowances hold, 4 real specs build). `npm test` reports 37 pass, 0 fail. The sheets were rendered through LibreOffice and checked by eye: on the Chemistry and Physics sheets every tier tag (WARM-UP, PRACTICE, CHALLENGE, MULTI-TOPIC) is in the label grey. **The Geology sheet has no tier tags, so Geology was checked by the shared builder only, not on a page.** The Grep sweep found no remaining statement of the old grey, amber, red, ink ramp outside the excluded directories. The Secretary checked by Read/Grep: `tier_colour()` (lines 96-104) returns `pal.label` and its docstring cites 0055, 0020 and 0054. `templates/worksheet/README.md` line 58 states the new rule and cites SHULL-CHG-0055. The key builder line 74 is unchanged, as section 2 requires. |

---

## 1. Current Rule (verbatim)

`templates/worksheet/build_worksheet_docx.py` lines 96-114:

```python
def tier_colour(tier, pal):
    """The tier ramp: quiet grey, amber, red, then full ink.

    Taken from his Master_Physics layout, which tags the tiers green / amber / red.
    Two changes. `semantic.success` measures 2.28 on white and its deep variant 5.02,
    both under the 5.5 house target, so the easiest tier is set in the muted label grey
    instead - which suits a warm-up anyway. And the hardest tier is full ink rather than
    a fourth hue: after red there is nowhere to go in colour, and black is
    unambiguously the heaviest thing on a page.

    SHULL-CHG-0020 records the cost: `semantic.danger` means "danger, safety warning,
    error, stop". Spending it on CHALLENGE dilutes that in a room where red also means
    hazard. The word CHALLENGE disambiguates it and it is his design, so it ships - but
    it is named rather than buried.
    """
    return {"warm-up": pal.label,
            "practice": T["semantic"]["caution"]["deep"],
            "challenge": T["semantic"]["danger"]["deep"],
            "multi-topic": pal.ink}[tier]
```

It is called once, at line 380, and colours both the bullet and the tag word (lines 382-383).

`templates/worksheet/README.md` lines 58-60:

> **Tier colours** run quiet grey → amber → red → full ink. `semantic.success` measures 5.02 on white
> even at its deep variant, under the 5.5 house target, so the easiest tier takes the muted label
> grey instead; the hardest takes ink, because after red there is nowhere to go in colour.

SHULL-CHG-0020, "A cost that is named rather than buried", already offered a fallback: "If he would
rather keep red for hazards, the ramp can run grey → course accent → ink with no loss to the
layout." That fallback is **not** proposed here. On Chemistry the course accent is Energy Orange
Deep itself, so the collision would come straight back.

## 2. Proposed Rule

> Every tier tag (WARM-UP, PRACTICE, CHALLENGE, MULTI-TOPIC) and its bullet is set in the muted
> label grey (`pal.label`). The word carries the tier, and the order of the questions carries the
> difficulty. No tier is coloured.

- `tier_colour()` returns `pal.label` for every tier, or is removed and its call site uses
  `pal.label` directly. The docstring is rewritten to cite SHULL-CHG-0055.
- `templates/worksheet/README.md` line 58 paragraph becomes one sentence giving the new rule and
  citing SHULL-CHG-0055.
- The tags stay: same position, column, 7pt bold and letter-spacing. Only the colour changes.
- **Not changed:** teacher keys. `build_worksheet_key_docx.py` line 74 sets the tier in
  `pal.accent`. Keys are teacher-only and carry no semantic notes, so they are out of scope.
- `pal.label` is `ground.label`, which measures 6.62:1 on white (`brand/tokens.json`, body text,
  meets the SHULL target), so 7pt bold tags stay readable. No tier distinction is carried by
  colour any more, so the grayscale-separation rule (`rules.grayscaleSeparationMin`) no longer
  applies to the tags. The word is the label.

The change is in `templates/` and touches no brand token. It is recorded as a build-rule change
because it governs every course's worksheets.

## 3. Wider than the SHULL-CHG-0054 follow-up: tell the user plainly

SHULL-CHG-0054 follow-up 2 suggested "a different tier colour **on Chemistry**". This record applies
to **all three courses**, for two reasons:

1. **One builder, one rule.** `tier_colour()` serves every course. A Chemistry-only branch would
   make the tier rule course-dependent inside a shared build mechanic, which is the duplication
   CLAUDE.md section 1 warns against. By the test in CLAUDE.md section 2, a change that affects all
   three courses belongs in the shared build rule.
2. **The user's remark was about the label in general** ("I almost don't even like the difficulty
   label in there"), not about Chemistry.

As a result, Physics and Geology sheets also lose their amber and red tier tags. If the user wants
Chemistry only, this record should be rejected or revised, not implemented as written.

## 4. Verification plan (for `Verified:`)

1. Rebuild one worksheet per course (Chemistry, Physics, Geology), render to PDF, and check by eye
   that every tier tag and bullet is grey and no amber or red remains on the page.
2. On the Chemistry sheet, confirm the PRACTICE tag no longer looks like the Energy Orange Deep
   headings, in colour and in greyscale.
3. `python3 scripts/validate_profiles.py`, `python3 scripts/audit_worksheet.py` on each rebuilt sheet,
   and `npm test`: all pass.
4. Grep `templates/` and `.claude/skills/` for "amber", "caution" and "danger" next to "tier", and for
   `tier_colour`. Expect no statement of the old ramp to remain.
