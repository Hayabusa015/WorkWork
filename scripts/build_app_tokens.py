#!/usr/bin/env python3
"""Generate app/public/tokens.css from brand/tokens.json.

The app shipped thirteen hand-typed hex values, which is the defect
validate_tokens.py exists to catch, and one of them was worse than a duplicate:
#16B8A6 is Geology's LOCKED Terra Teal, and the app was using it as the accent on
every screen - including Chemistry and Physics. A course's identity colour is not
a UI accent.

So the accent here is a *slot*, not a value. `:root` carries the neutral product
accent; `[data-course]` on <body> swaps in that course's locked pair. Selecting
Chemistry turns the app Lab Lime because that is what Chemistry is, and nothing in
the stylesheet has to know a hex to make that happen.

Screen colour is picked against the dark ground: brand/tokens.json measures every
course display colour onAsphalt (Lab Lime 12.0:1, Quantum Gold 10.15:1, Terra Teal
7.27:1 - all AAA), so the display value is the one that carries type here, and the
`*Deep` text-on-light variants are deliberately unused.

    python3 scripts/build_app_tokens.py
"""
import json, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "app", "public", "tokens.css")

t = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
g, courses, sem, typ = t["ground"], t["courses"], t["semantic"], t["typography"]

COURSE_CLASS = {"chemistry": "chemistry", "physics": "physics", "geology": "geology"}


def course_block(name, key):
    c = courses[key]
    return f"""[data-course="{name}"] {{
  --accent:        {c['primary']['hex']};      /* {c['primary']['name']} */
  --accent-2:      {c['secondary']['hex']};      /* {c['secondary']['name']} */
  --accent-quiet:  color-mix(in oklab, {c['primary']['hex']} 14%, transparent);
  --accent-line:   color-mix(in oklab, {c['primary']['hex']} 38%, transparent);
}}"""


css = f"""/* GENERATED FROM brand/tokens.json BY scripts/build_app_tokens.py - DO NOT EDIT.
   Re-run the script after changing any token. Hand-editing a hex here is the
   defect validate_tokens.py exists to catch.

   Hallmark · genre: modern-minimal · macrostructure: Workbench
   design-system: app/design.md · designed-as-app
   Theme is not a Hallmark catalog pick: it is derived from the repository's own
   locked brand tokens, which outrank the catalog. */

:root {{
  color-scheme: dark;

  /* Ground - brand/tokens.json "ground" */
  --paper:      {g['asphalt']['hex']};
  --paper-2:    {g['graphite']['hex']};
  --paper-3:    color-mix(in oklab, {g['graphite']['hex']} 62%, {g['asphalt']['hex']});
  --ink:        {g['white']['hex']};
  --ink-2:      {g['mutedOnDark']['hex']};
  /* Measured, not eyeballed. At 62% this was 2.74:1 on a panel - below WCAG AA and
     well under the house 5.5 - and it carries every hint, date and caption in the
     app. At 85% it measures 6.57 on the ground, 5.38 in a field and 4.63 on a panel:
     clears AA everywhere and the house target on the two larger surfaces, while
     staying a visible step below --ink-2 (6.34 on panel). */
  --ink-3:      color-mix(in oklab, {g['mutedOnDark']['hex']} 85%, {g['asphalt']['hex']});
  --rule:       color-mix(in oklab, {g['mutedOnDark']['hex']} 22%, {g['asphalt']['hex']});
  /* Functional borders - field and button edges. WCAG 1.4.11 wants 3:1 for a UI
     boundary; 38% measured 1.51 on a panel. 70% measures 3.29 panel / 3.83 field.
     --rule stays faint: it only ever draws decorative separators. */
  --rule-strong:color-mix(in oklab, {g['mutedOnDark']['hex']} 70%, {g['asphalt']['hex']});
  --parchment:  {g['parchment']['hex']};

  /* Accent - neutral product default. A course overrides it below. */
  --accent:       {g['parchment']['hex']};
  --accent-2:     {g['mutedOnDark']['hex']};
  --accent-quiet: color-mix(in oklab, {g['parchment']['hex']} 12%, transparent);
  --accent-line:  color-mix(in oklab, {g['parchment']['hex']} 34%, transparent);
  --accent-ink:   {g['asphalt']['hex']};

  /* Every course at once - for lists and legends that show all three side by side,
     where a single active accent cannot say which course a row belongs to. The
     grayscaleSeparationMin rule still applies: these carry a dot AND a text label,
     never colour alone. */
  --course-chemistry: {courses['chemistry']['primary']['hex']};
  --course-physics:   {courses['physics']['primary']['hex']};
  --course-geology:   {courses['geology']['primary']['hex']};

  /* Semantic - meaning never yields to course identity (spec Part 9) */
  --danger:   {sem['danger']['hex']};
  --caution:  {sem['caution']['hex']};
  --success:  {sem['success']['hex']};

  /* Type - {typ['stack']} */
  --font-body: {typ['stack']};
  --font-display: {typ['stackCondensed']};

  /* 4pt scale */
  --space-3xs: .25rem; --space-2xs: .5rem;  --space-xs: .75rem;
  --space-sm:  1rem;   --space-md:  1.5rem; --space-lg: 2rem;
  --space-xl:  3rem;   --space-2xl: 4.5rem;

  --text-xs: .75rem;  --text-sm: .8125rem; --text-md: .9375rem;
  --text-lg: 1.0625rem; --text-xl: 1.375rem; --text-2xl: 1.875rem;
  --text-display: clamp(1.75rem, 1.2rem + 1.6vw, 2.5rem);

  --radius-card: 12px; --radius-input: 9px; --radius-pill: 999px;
  --rule-hair: 1px;

  --ease-out: cubic-bezier(.16, 1, .3, 1);
  --ease-in-out: cubic-bezier(.65, 0, .35, 1);
  --dur-short: 160ms;
  --dur-mid: 240ms;
}}

{chr(10).join(course_block(name, key) for name, key in COURSE_CLASS.items())}

/* "Class" routing is cross-course: it takes the neutral product accent, because
   no single course owns a general-class material. */
[data-course="class"] {{
  --accent:        {g['parchment']['hex']};
  --accent-2:      {g['mutedOnDark']['hex']};
  --accent-quiet:  color-mix(in oklab, {g['parchment']['hex']} 12%, transparent);
  --accent-line:   color-mix(in oklab, {g['parchment']['hex']} 34%, transparent);
}}
"""

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(css)
print(f"build_app_tokens: wrote {os.path.relpath(OUT, REPO)}")

# The tab mark. An SVG favicon cannot read a CSS custom property from another file,
# so its two colours are written here from the same tokens rather than hand-typed -
# the ground and the parchment product accent, no course identity borrowed.
ICON = os.path.join(REPO, "app", "public", "favicon.svg")
open(ICON, "w").write(
    f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="7" fill="{g['asphalt']['hex']}"/>
  <path d="M20.5 10.5a4.6 4.6 0 0 0-8 3c0 4.2 8 2.8 8 7a4.6 4.6 0 0 1-8 3"
        fill="none" stroke="{g['parchment']['hex']}" stroke-width="3"
        stroke-linecap="round"/>
</svg>''')
print(f"build_app_tokens: wrote {os.path.relpath(ICON, REPO)}")
