# SHULL-CHG-0108 — Chemistry: Ice Blue Deep token and a blue print pairing

> **ID note.** The main session supplied 0108 and confirmed it is free on `origin/main` (highest
> record there: SHULL-CHG-0107, PENDING). The Secretary that drafted this record has no shell and
> could not run `git fetch origin main` itself (`governance/CHANGE_CONTROL.md` §2, "Allocating a new
> Change ID"). Locally the highest record is also SHULL-CHG-0107. Under that rule the ID is not
> allocated until this file is pushed to `origin/main`.

> **CONFLICT with a design rule, marked and not resolved.** `brand/SHULL_DESIGN_SYSTEM.md` §3, "The
> rule that governs coloured type", says coloured type on a light ground uses the course's
> `primaryDeep`. Using Ice Blue Deep as accent text breaks that sentence as written. This record
> proposes amended wording (§2b). The Secretary does not apply it on its own judgment. Approving
> this record approves that amendment; rejecting the amendment means the token can be added but not
> used as type. See §4.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0108 |
| **Date** | 2026-11-23 (drafted) |
| **Source** | User, in the main session, 2026-11-23, as the main session relayed it. Matt asked *"What if we used the blue instead of energy"* (Ice Blue in place of Energy Orange as the Chemistry accent). The main session explained that Ice Blue measures 1.73:1 on white (`NOT TYPE`) and offered (A) Ice Blue for rules and borders with orange text, or (B) an all-blue look: Ice Blue for rules and borders plus a new dark blue for accent text, added to the brand file once a shade tests readable on white. Matt replied, verbatim as relayed: *"B, go with the dark blue"*. The Secretary did not hear him directly. **This record is not the approval.** The main session records his decision under `governance/CHANGE_CONTROL.md` §4. The shade `#066679` was picked by the main session, not by Matt (see §5). |
| **Current Rule** | See §1, verbatim, with file and section. |
| **Proposed Rule** | (a) New token `brand/tokens.json` `courses.chemistry.secondaryDeep`, Ice Blue Deep `#066679`, PROVISIONAL, `use: text-on-light`. (b) `brand/SHULL_DESIGN_SYSTEM.md` §3 coloured-type rule generalised so a course's text-safe deep token may be `primaryDeep` or, where the course has one, `secondaryDeep`. The course decides which. (c) `courses/chemistry/DECISIONS.md` "Course brand exceptions": Chemistry has a blue print pairing (Ice Blue for rules, borders and outline boxes; Ice Blue Deep for accent text), used in place of the orange pairing on the document types it lists. The first listed type is Unit Roadmaps. Exact text in §2. |
| **Supersedes** | `brand/SHULL_DESIGN_SYSTEM.md` §3, "The rule that governs coloured type", first line of the boxed rule (*"On a light ground, coloured type uses the course's `primaryDeep`."*). `courses/chemistry/DECISIONS.md` "Course brand exceptions", the live text *"**None.** Chemistry's identity colours are..."* (replaced; the decision-log history is not edited). Restatements of the primaryDeep-only rule in `.claude/` and `templates/lab/README.md` become consistent with the new wording (§2e). **Not superseded:** `courses.chemistry.primary` (Energy Orange, LOCKED), `courses.chemistry.secondary` (Ice Blue, LOCKED) and `courses.chemistry.primaryDeep` (Energy Orange Deep, PROVISIONAL). All three keep their hex, status and use. |
| **Reason** | Matt prefers the blue look for Chemistry (Source). Ice Blue cannot be type on white (1.73:1), so an all-blue look needs a text-safe dark blue, which does not exist in `tokens.json` today. Adding a token is a brand change (Path B). Which documents use the blue look is a one-course decision, so it belongs in the Chemistry decisions file (CLAUDE.md §2 test). |
| **Affected Agents** | Secretary (implements the brand and course edits). Designer and Auditor: their colour-as-type lines restate "use `primaryDeep`". The Auditor would otherwise flag Ice Blue Deep text as a defect (`.claude/agents/auditor.md` line 34; `.claude/agents/designer.md` line 21). Overseer routes the roadmap rebuilds (first use). |
| **Affected Skills** | `.claude/skills/apply-shull-design/SKILL.md` lines 20-22 (verbatim restatement of the design-system rule). `.claude/skills/build-presentation/SKILL.md` line 67 is slides-only and not affected, because this pairing is print-only. `.claude/skills/build-lab/SKILL.md` line 18 is unchanged; the course class still sets the default. |
| **Affected Courses** | **Chemistry only.** Physics and Geology have no `secondaryDeep` and are unchanged. The design-system wording becomes general, but it changes nothing for a course without the token. |
| **Risk** | **Medium.** The token itself is low risk. The design-rule amendment, the grey-level near-misses and the restatements that need to change make it medium. See §3. |
| **Recommendation** | Approve, after Matt answers the one question in §5 (confirm the shade). The approval covers the token, the §2b wording, the §2c course text and the §2d generator line. The roadmap builder switch and the rebuild of the 16 roadmaps are a separate classroom job routed through the Overseer (§6). They are **not bundled**. |
| **Decision** | Approved by the user, 2026-11-23: "B, go with the dark blue" (answering option B: Ice Blue for rules and borders plus a new dark blue for accent text, shade picked by the main session and stated in chat as #066679) |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

---

## 1. Current Rule (verbatim)

### 1a. `brand/tokens.json` `courses.chemistry` (lines 121-169)

There is no `secondaryDeep`. The keys are `primary` (Energy Orange `#FF6B1A`, LOCKED, `display`),
`secondary` (Ice Blue `#3DD6F4`, LOCKED, `display`), `primaryDeep` (Energy Orange Deep `#B84100`,
PROVISIONAL, `text-on-light`) and `icons`. The measured block format, from `primaryDeep`:

```json
        "measured": {
          "grayscale": 93,
          "onWhite": 5.53,
          "onWhiteVerdict": "body text, meets SHULL target",
          "onParchment": 4.8,
          "onAsphalt": 3.27,
          "onAsphaltVerdict": "large text only (24px+, or 19px bold)"
        }
```

The file's `$comment` says: *"Every 'measured' block is computed by scripts/measure_tokens.py -
never hand-edit one."*

### 1b. `brand/SHULL_DESIGN_SYSTEM.md` §3, "The rule that governs coloured type" (lines 108-110)

> **On a light ground, coloured type uses the course's `primaryDeep`.
> On a dark ground, coloured type uses `primary` or `secondary`.
> Neither is ever used as type on the other.**

### 1c. `courses/chemistry/DECISIONS.md` "Course brand exceptions" (lines 365-366)

> **None.** Chemistry's identity colours are `courses.chemistry` in `brand/tokens.json`, inside the
> shared system (SHULL-CHG-0054). This file does not restate them.

### 1d. Generator: `scripts/build_lab_css.py` lines 48-49 and 65

`--accent` is always `primaryDeep` and `--accent-display` is always `primary`. There is no way to
select the blue pairing today. The Unit Roadmap and Course Outline builders take all their colour
through `templates/lab/shull-lab-tokens.css` (`templates/unit-roadmap/README.md` line 9). The header
double rule uses `--accent-display`, and the kicker, accent word, labels and chips use `--accent`
(`templates/_shull_header.css` lines 22, 25, 30; `templates/unit-roadmap/unit_roadmap.css` lines
30, 32, 52).

## 2. Proposed Rule and exact edits

### 2a. Edit 1 (brand layer): `brand/tokens.json`

Insert after `courses.chemistry.primaryDeep` and before `"icons"`:

```json
      "secondaryDeep": {
        "hex": "#066679",
        "name": "Ice Blue Deep",
        "status": "PROVISIONAL",
        "use": "text-on-light",
        "source": "SHULL-CHG-0108; derived from Ice Blue hue, darkened, not user-supplied",
        "measured": {}
      },
```

Then run `python3 scripts/measure_tokens.py`. That script fills `measured`, because the file forbids
hand-written measurements. Then run `python3 scripts/measure_tokens.py --check`. Bump `"updated"` to
the implementation date and `"version"` to `1.2.0` (an additive token).

**Measurements computed while drafting (not authoritative).** I computed these by hand from the
same formulas as `scripts/measure_tokens.py` (WCAG relative luminance, and greyscale =
round(0.299R + 0.587G + 0.114B)), against the grounds in this file. **Three of them differ from the
values in the brief:**

| Field | Brief | Drafting value | Why it differs |
|---|---|---|---|
| grayscale | 76 | **75** | 0.299·6 + 0.587·102 + 0.114·121 = 75.46, which rounds to 75 |
| onWhite | 6.59 | **6.59** | Matches. Verdict: `body text, meets SHULL target` (5.5 ≤ x < 7) |
| onParchment | 5.76 vs `#F4EFE6` | **≈5.71** vs `#EDF0E5` | The file's parchment is `ground.parchment` `#EDF0E5`, not `#F4EFE6` |
| onAsphalt | not given | **≈2.74** | Verdict: `NOT TYPE - fill, rule, border or block only`. Ice Blue Deep is light-ground type only |

The expected block, for checking the script's output:

```json
        "measured": {
          "grayscale": 75,
          "onWhite": 6.59,
          "onWhiteVerdict": "body text, meets SHULL target",
          "onParchment": 5.71,
          "onAsphalt": 2.74,
          "onAsphaltVerdict": "NOT TYPE - fill, rule, border or block only"
        }
```

If the script's numbers differ from these, the script's numbers are correct and are recorded in
`Verified`.

### 2b. Edit 1, continued (brand layer): `brand/SHULL_DESIGN_SYSTEM.md` §3

This edit resolves the CONFLICT and needs Matt's approval. Replace the boxed rule (lines 108-110)
with:

> **On a light ground, coloured type uses the course's text-safe deep token: `primaryDeep`, or
> `secondaryDeep` where the course has one and its `DECISIONS.md` says which documents use it.
> On a dark ground, coloured type uses `primary` or `secondary`.
> Neither is ever used as type on the other.**

Then add one paragraph after the existing "The display colours are unchanged..." paragraph:

> A course with a `secondaryDeep` has a second print pairing: `secondary` for rules, borders and
> outline boxes, and `secondaryDeep` for coloured type. A document uses one pairing throughout and
> never mixes the two. Which documents use the second pairing is a course decision, recorded under
> "Course brand exceptions" in that course's `DECISIONS.md`.

This names no course and no hex, so the design system still states only the mechanism. The
Chemistry fact lives in one place, the course file (§2c).

### 2c. Edit 2 (course layer): `courses/chemistry/DECISIONS.md`

Replace the live text under `## Course brand exceptions` (lines 365-366) with:

```markdown
**One: a blue print pairing.** Chemistry's identity colours are `courses.chemistry` in
`brand/tokens.json`, inside the shared system (SHULL-CHG-0054). This file does not restate them.
Chemistry has two print pairings (`brand/SHULL_DESIGN_SYSTEM.md` §3):

- **Orange (default):** `primary` for rules, borders and outline boxes; `primaryDeep` for accent
  text.
- **Blue:** `secondary` (Ice Blue) for rules, borders and outline boxes; `secondaryDeep` (Ice Blue
  Deep) for accent text: the headline accent word, kicker, labels and chips.

A document uses one pairing throughout. Every document type not listed below uses orange.

| Document type | Pairing | Since |
|---|---|---|
| Unit Roadmap (U0–U15) | Blue | SHULL-CHG-0108 |

Adding a document type to this table is a course decision (a dated log entry). It needs no brand
change. Energy Orange is not retired.
```

The `*Superseded 2026-09-07...*` line under it stays.

Decision-log entry, at the **top** of the log (above whatever entry is on top at implementation;
SHULL-CHG-0107, if implemented first, puts its own entry there):

```markdown
### YYYY-MM-DD — Blue print pairing for Unit Roadmaps
Chemistry gains a second print pairing: Ice Blue for rules, borders and outline boxes, and Ice Blue
Deep (a new PROVISIONAL token, `courses.chemistry.secondaryDeep`) for accent text. It is used in
place of the orange pairing on the document types listed under "Course brand exceptions". The first
is the Unit Roadmaps, U0–U15. Energy Orange is unchanged and stays the default. Decided by Matt
2026-11-23 ("B, go with the dark blue").
Supersedes: "Course brand exceptions" (None), SHULL-CHG-0054.
Status: CONFIRMED · SHULL-CHG-0108
```

"Last updated" is set to the implementation date.

### 2d. Generator: `scripts/build_lab_css.py`

After the `body.chem` line (line 65), add:

```python
body.chem.pair-blue {{ --accent: {c['chemistry']['secondaryDeep']['hex']}; --accent-display: {c['chemistry']['secondary']['hex']}; }}
```

Extend the closing comment (lines 70-73) with: *"body.chem.pair-blue switches Chemistry to its blue
pairing (secondaryDeep as type, secondary as rule). See courses/chemistry/DECISIONS.md, Course brand
exceptions."* Then run `python3 scripts/build_lab_css.py`. **Yes, `templates/lab/shull-lab-tokens.css`
must be regenerated, by `scripts/build_lab_css.py`.** The same run also rewrites
`templates/notes/shull-notes-tokens.css`. The new class is unused there, which is harmless.

`scripts/build_slide_tokens.py` and `scripts/build_app_css.py` emit `primary`, `secondary` and
`primaryDeep` only. They do not need to change, and their `--check` runs must still pass. This
pairing is print-only. Slides keep the dark/light rule unchanged.

### 2e. Restatements made consistent (same commit, labelled)

| File | Now | Proposed |
|---|---|---|
| `.claude/skills/apply-shull-design/SKILL.md` lines 20-22 | Quotes the old §3 rule | Quote the new §2b wording verbatim |
| `.claude/agents/designer.md` line 21 | "on a light ground use the course `primaryDeep`" | "on a light ground use the course's text-safe deep token (`primaryDeep`, or `secondaryDeep` on a document type the course's `DECISIONS.md` lists for its second pairing)" |
| `.claude/agents/auditor.md` line 34 | "using a display colour instead of `primaryDeep`" | "using a display colour instead of the course's text-safe deep token (`primaryDeep` or `secondaryDeep`), or mixing a course's two pairings on one document" |
| `templates/lab/README.md` lines 39 and 96 | "switches `--accent` to that course's `primaryDeep`"; "uses the course `primaryDeep`" | Add: "`chem pair-blue` switches to Chemistry's blue pairing (SHULL-CHG-0108)". Line 96 becomes "uses the course's text-safe deep token" |

`.claude/` and `templates/` are outside the Secretary's governed directories. They are listed here
because the record must name every affected file. On implementation the main session (or the owning
agent) makes them in the same commit, as was done for SHULL-CHG-0054 §2b.

## 3. Risks

1. **Grey-level near-miss with Energy Orange Deep.** Ice Blue Deep is ≈75 and `primaryDeep` is 93,
   18 grey levels apart, below `rules.grayscaleSeparationMin` (20). The two are never meant to carry
   a distinction, so this is not a breach. It is the reason for the "one pairing per document, never
   mixed" sentence in §2b and §2c.
2. **Same grey as `semantic.danger.deep`.** Both measure ≈75. In colour they are very different (red
   vs. teal-blue), so a Chemistry hazard note reads more clearly as a warning beside blue text than
   it does beside orange text. SHULL-CHG-0054 risks 2 and 5 are eased in colour. On a photocopy they
   are the same grey. The existing rule already covers this: warnings differ by border and label as
   well as colour (`brand/SHULL_DESIGN_SYSTEM.md` §3, "Grayscale survival"). Roadmaps carry no
   hazard notes.
3. **Near-twin of `keyInk.arrow`** (`#16609A`, grey 80, a dark blue). If a Chemistry answer key ever
   used the blue pairing, annotation arrows and accent text would be nearly the same colour. Keys
   separate arrow from box by shape, but not from accent text. Roadmaps have no key. **Before any
   key-bearing document type is added to the §2c table, this needs its own check.**
4. **Close to Geology's identity.** Ice Blue Deep (hue ≈190°, grey ≈75) sits near Terra Teal Deep
   (`#0E766A`, hue ≈173°, grey 86), and Ice Blue sits near Terra Teal. Blue Chemistry roadmaps and
   teal Geology documents may look alike side by side. This is the same kind of cross-course risk as
   SHULL-CHG-0054 risk 1. `measure_tokens.py` `pair_warnings` checks only primary against secondary
   within a course, so it will not report it.
5. **Derived, not supplied.** Like Energy Orange Deep, the shade was derived, so it starts
   PROVISIONAL. Matt has not seen it on paper.
6. **Nothing propagates on its own.** Roadmaps already in `output/chemistry/` and on Drive stay
   orange until rebuilt. The Course Outline (SHULL-CHG-0106) uses the same stylesheet, is not in the
   first-use table, and stays orange unless Matt adds it.

## 4. Conflict check against LOCKED rules

| Rule | Status | Effect of this change | Result |
|---|---|---|---|
| `courses.chemistry.primary` Energy Orange, `use: display` | LOCKED | Not touched. It stays the default pairing's rule colour | No conflict |
| `courses.chemistry.secondary` Ice Blue, `use: display` | LOCKED | Not touched. The blue pairing uses it only for rules, borders and outline boxes, which is display use. Its `NOT TYPE` verdict is respected | No conflict |
| `courses.chemistry.primaryDeep` | PROVISIONAL | Not touched. This record does not lock it or retire it | No conflict |
| `brand/SHULL_DESIGN_SYSTEM.md` §3, "coloured type uses the course's `primaryDeep`" | Design rule (SHULL-CHG-0008) | Blue accent text breaks it as written | **CONFLICT. Not resolved here.** §2b proposes the amendment; Matt's approval decides it |
| "Each course has one accent" | none found | Grep of `brand/`, `standards/`, `.claude/`, `README.md` and template READMEs finds no such rule. §1 of the design system says each course "differs only in its identity colours", which are plural. Ice Blue is already one of them | No conflict |
| §3 "One accent word" (one accent-coloured word per headline) | Design rule | Unchanged. The roadmap header still has one accent word, now in Ice Blue Deep | No conflict |
| §8 print discipline (colour is a thin accent; outlined, not filled) | Hard rule | The blue pairing uses rules, borders and outline boxes only | No conflict |
| §11 document header: kicker "in the course's text-safe colour", double rule "in the course display colour" | LOCKED (`print.header`, SHULL-CHG-0101) | The wording is generic. Under `pair-blue` the header draws `--accent` and `--accent-display`, which become Ice Blue Deep and Ice Blue. No header geometry changes | No conflict |
| `rules.contrastTargetText` 5.5 | rule | ≈6.59 on white clears it | No conflict |
| `rules.grayscaleSeparationMin` 20 | rule | 18 from `primaryDeep`; addressed by "never mixed" (risk 1) | No conflict as written |

## 5. The question for Matt (one, before approval)

**Is `#066679` the dark blue you want?** "Go with the dark blue" approved the approach (option B).
The shade was then picked by the main session. It is a deep teal-blue: roughly 6.6:1 on white, and
the same hue as Ice Blue, darkened. It starts **PROVISIONAL** either way, like Energy Orange Deep,
until it has been seen on a printed roadmap. If Matt wants a different shade, or wants it LOCKED,
the approval should say so. Otherwise the Secretary implements `#066679` as PROVISIONAL.

## 6. Out of scope (follow-up jobs, not bundled)

- **Roadmap builder switch.** `templates/unit-roadmap/build_unit_roadmap.py` line 140 must emit
  `class="chem pair-blue"` for Chemistry roadmaps. The pairing choice lives in the §2c table. The
  builder should carry a single constant that points at it (for example
  `PAIRING = {"chemistry": "pair-blue"}  # courses/chemistry/DECISIONS.md, Course brand exceptions; SHULL-CHG-0108`),
  rather than a field repeated in 16 specs.
- **Rebuild the 16 Chemistry roadmaps (U0–U15).** This is a classroom deliverable and goes through
  the Overseer, followed by the usual QA (`scripts/audit_print_ink.py`, `scripts/audit_fonts.py`,
  `scripts/validate_tokens.py`) and a printed proof. That printed proof is what would move the
  token from PROVISIONAL.

## 7. Rollback

One commit carrying `SHULL-CHG-0108` (Edit 1 brand, Edit 2 course, generator and restatements,
labelled). `git revert <sha>` removes the token, restores the §3 wording and the "None." exception,
and removes the CSS class. Re-run `scripts/build_lab_css.py` after a revert. No Drive mutation is
part of this change.

## 8. Verification plan (only after APPROVED and implemented)

1. `python3 scripts/measure_tokens.py`, then `--check`. Record the authoritative block. Expected
   values are in §2a; if they differ, the script wins.
2. `python3 scripts/build_lab_css.py`. `templates/lab/shull-lab-tokens.css` contains
   `body.chem.pair-blue` with the Ice Blue Deep and Ice Blue hexes. `build_app_css.py --check` and
   `build_slide_tokens.py` show no diff.
3. All `scripts/validate_*.py` pass, `validate_tokens.py` in particular: no raw hex outside
   `tokens.json` and the generated files.
4. Grep: `secondaryDeep` appears in `tokens.json`, the design system §3, the Chemistry decisions
   file and the edited restatements. No file outside `tokens.json` and the generated files states
   `#066679`. Energy Orange's three Chemistry keys are byte-identical to before.
5. The diff of `courses/chemistry/DECISIONS.md` is limited to the "Course brand exceptions" live
   text, the new log entry and "Last updated".
6. Fill in `Implemented By` and `Verified` here, and move the CHANGELOG row's status.
