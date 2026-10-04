# Slide template — twelve layouts

**Authority:** `governance/proposals/SHULL-CHG-0013-slide-template.md`. Migrated from
`_Brand/Templates/build.js`, snapshotted byte-exact at `legacy/slide-template/`.

The twelve layouts, their geometry and their type scale are preserved from the template the user
approved. The palette, the fonts and the token mechanism are not — the change record has all eight
findings, including the two still open.

## Build

```bash
cd templates/slide
SHULL_COURSE=chemistry node build.js out.pptx      # or physics, or geology
```

One file, three courses, no fork. If a course needs a different colour, that is a token change in
`brand/tokens.json`, not a copy of this file.

`tokens.generated.js` is written by `scripts/build_slide_tokens.py` and **must never be hand-edited**
— it is the only path a hex takes out of `tokens.json`, and editing it puts a colour in two places.
`build_slide_tokens.py --check` fails if it has drifted.

`node_modules` is not committed. `scripts/setup-environment.sh` installs pptxgenjs.

## The twelve

| # | Layout | Ground | Use |
|---|---|---|---|
| 01 | Unit Title | dark | opens a unit |
| 02 | Section Title | accent panel | opens a section |
| 03 | Grouped Concept | light | two contrasting ideas + image |
| 04 | Divider | dark | visual reset, one concept image |
| 05 | Process / Timeline | light | four numbered steps |
| 06 | Concept + Image | dark | the one deliberate dark content slide |
| 07 | Comparison Cards | light | three parallel items |
| 08 | Diagram + Annotation | light | hand-built figure + labelled rules |
| 09 | Example Problem | light | problem, givens, **empty** work area |
| 10 | Worked Solution | light | data, formula, completed work |
| 11 | Givens / Equation / Answer | light | any course |
| 12 | Deck Index | dark | reference. Delete before class. |

**09 and 10 are a pair.** Every example problem ships with its solution slide, and 09's work area
is empty on purpose — it gets filled live on the board.

## The rules the layouts encode

- **One must-write bar per slide, never two.** Two write-this cues means students copy neither.
- **Dark grounds are structural** — 01, 02, 04, 12. Content slides are light. 06 is the single
  deliberate exception.
- **Reserve, don't layer.** A block reserves its height and text flows in what remains. Placing
  text first and overlaying the block is how slides 8 and 17 of the U8 preview shipped clipped.
- **16pt floor** for anything a student reads from a seat. 10–12pt is navigation only — eyebrows,
  card labels, footers.
- **Line caps** live in `tokens.json` `slideGeometry.lineCaps`. Over the cap, split the slide.
  Never shrink type to fit.
- **Course colour is never a small label on a card.** Measured, not taste — see the change record.

## Images

The masters carry **empty image regions**, not photographs. The legacy masters embedded seven
full-resolution PNGs, which is why the template was 20 MB and why every deck built from layout 01
arrived carrying a picture of an atom. Same geometry, no payload — 402 KB.

Images come from the loop in `SHULL_Slide_System_v2.md` §5: Claude supplies a prompt per slide, the
user generates and saves it, Claude places it. Anything a student *reads* as science — a diagram
with a number, a label, or a formula — is built, never generated.

## Spec markup and notes

Optional, backwards-compatible; documented at the top of `build_deck.js`.

- `^{...}` is a superscript run and `_{...}` a subscript run inside any field: `Mg^{2+}`, `10^{-19} J`, `3d^{5}`, `H_{2}O`. No nesting.
- The run is a baseline-shift attribute at the placeholder's own size, font and colour. No Unicode superscript glyphs.
- Line caps and the 110-char must-write check count the text with markup stripped.
- `"notes": "..."` on a slide object writes that slide's speaker notes. Absent means no notes part.
- `scripts/audit_slide_geometry.py` over-counts lines on marked-up text (it counts each run as a line). Visually check the raster.

## QA

```bash
python3 scripts/audit_slide_geometry.py deck.pptx
soffice --headless --convert-to pdf deck.pptx && pdffonts deck.pdf
```

The audit reads the built `.pptx`, so it checks what shipped rather than what the source intended.
It catches overlapping text, text off the slide, content below the type floor, and any text/ground
pair under the contrast target — resolving each run against the fill actually behind it.

`pdffonts` must show **Archivo, embedded, TrueType** and nothing else. Liberation or DejaVu in that
list means the font stack silently substituted, which is the defect behind SHULL-CHG-0006: every QA
render would be inspecting a different document than the one that ships.

**Neither check replaces looking at the raster.** Both open findings in the change record were found
mechanically; the two box collisions in finding 7 were found by eye first.

## Click builds

`build_deck.js` (pptxgenjs) cannot write animations. Orbital diagrams that must be built one click
at a time (boxes fly in, then one electron arrow per click in Hund and Pauli order, or one arrow
leaving or arriving per click for an ion) are added by a **post-processor**, never by the masters or
the deck builder:

```bash
cd templates/slide
SHULL_COURSE=chemistry node build_deck.js decks/<spec>.json /tmp/<deck>.pptx      # 1. static deck
python3 ../../scripts/add_click_builds.py /tmp/<deck>.pptx decks/<spec>.builds.json \
        ../../deliverables/<unit>/<final>.pptx                                  # 2. animated deliverable
```

Rules for the two files:

- The build slide must leave its slot **empty**: omit that slide's `images` entry in `<spec>.json`
  (the post-processor also deletes any picture inside the slot). The PNG figure script can keep
  drawing the static figure for print.
- `<spec>.builds.json` lists one object per build slide: 1-based `slide`, the `layout` name (asserted),
  the `region` (a slot name; coordinates come from `build.js` `SLOTS`, never typed), `title`,
  `sublevels` (`label`, `boxes`, `electrons`, Aufbau order), optional `z` and `core`, `start`
  (`empty` fills by clicks, `filled` flies the atom in whole), `captions` (`hund`, `pauli`), and for
  ions `steps` (`{"remove": n}` or `{"add": n}` with an optional `caption`). The script's docstring is
  the field reference.
- Arrow order, caps, Aufbau order, Pauli, Hund and electron totals (against Z, using the S2.3 checker's
  ground-state table) are computed and asserted by the script. A spec that cannot be filled legally fails
  the run. Ions remove valence-first (highest n, then highest l: 4s before 3d).
- The script appends `CLICK BUILD: N clicks: ...` to each changed slide's teacher notes, so the count in
  the notes is the count in the file.
- Verify: `python3 scripts/add_click_builds.py deck.pptx spec.builds.json out.pptx --preview K [--slide N]`
  writes a static copy showing the state after K clicks, for rasterising intermediate states.
  Then run the geometry audit and `pdffonts` as above. The animation was checked by script and by
  LibreOffice import; it has not been played in PowerPoint, Keynote or Google Slides.
- **Print / PDF / handout:** the animated deck shows every build state at once in any non-slideshow view.
  For those, run step 2 again with `--static` (`... builds.json out_Static.pptx --static`): no animation, each
  build slide shows only its final state (docstring: "Static final-state mode"). Name it with the descriptor
  `_Static` after the section code, e.g. `SHULL_CHEM_Slides_U02_S02.3_Static.pptx`.
- A rebuild from `build_deck.js` drops the animation. Always re-run step 2 after step 1.
