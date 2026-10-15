#!/usr/bin/env python3
"""Generate the SHULL OS app's colour tokens from brand/tokens.json.

The app is a screen, not a page, so it needs a dark ground and lighter
surfaces that no printed template needs. Those are *derived* here from the
ground tokens with color-mix rather than picked by eye, so the app cannot
quietly acquire a fourth teal that nothing else in the system knows about.

    python3 scripts/build_app_css.py
    python3 scripts/build_app_css.py --check    # fail if the file has drifted

Writes app/public/tokens.generated.css. Never hand-edit it — that is the
defect validate_tokens.py exists to catch.
"""
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "app", "public", "tokens.generated.css")
ICON = os.path.join(REPO, "app", "public", "icon.svg")

tokens = json.load(open(os.path.join(REPO, "brand", "tokens.json"), encoding="utf-8"))
g = tokens["ground"]
c = tokens["courses"]
sem = tokens["semantic"]
typ = tokens["typography"]

# Geology's Terra Teal is the app's own accent: the workspace is not a course,
# and this is the identity the shipped app already carried. Course surfaces
# still use their own colour — see --course-* below.
APP = c["geology"]

css = f"""/* GENERATED FROM brand/tokens.json BY scripts/build_app_css.py — DO NOT EDIT.
   Re-run the script after changing any token. app/public/style.css must not
   contain a colour literal; every colour it uses is named here.

   Screen tokens, not print tokens. The grounds below are mixed from
   ground.asphalt so the app's dark surfaces stay on the same neutral axis as
   the dark slide layouts instead of drifting to a different grey. */

:root {{
  color-scheme: dark;

  /* ---- Raw brand values. The only place the app names one. ---- */
  --t-asphalt:       {g['asphalt']['hex']};
  --t-graphite:      {g['graphite']['hex']};
  --t-white:         {g['white']['hex']};
  --t-parchment:     {g['parchment']['hex']};
  --t-muted-on-dark: {g['mutedOnDark']['hex']};
  --t-rule:          {g['ruleHairline']['hex']};

  --t-chem:          {c['chemistry']['primary']['hex']};
  --t-chem-2:        {c['chemistry']['secondary']['hex']};
  --t-phys:          {c['physics']['primary']['hex']};
  --t-phys-2:        {c['physics']['secondary']['hex']};
  --t-geo:           {c['geology']['primary']['hex']};
  --t-geo-2:         {c['geology']['secondary']['hex']};

  --t-danger:        {sem['danger']['hex']};
  --t-caution:       {sem['caution']['hex']};
  --t-success:       {sem['success']['hex']};

  /* ---- Screen grounds, derived. Each step is a stated mix of asphalt and
     white, so the ladder is even and reproducible. ---- */
  --ground-0: color-mix(in oklab, var(--t-asphalt) 92%, black);   /* page */
  --ground-1: color-mix(in oklab, var(--t-asphalt) 97%, white);   /* rail */
  --ground-2: color-mix(in oklab, var(--t-asphalt) 92%, white);   /* panel */
  --ground-3: color-mix(in oklab, var(--t-asphalt) 87%, white);   /* raised */
  --ground-4: color-mix(in oklab, var(--t-asphalt) 82%, white);   /* input */

  --edge:       color-mix(in oklab, var(--t-graphite) 78%, white 6%);
  --edge-soft:  color-mix(in oklab, var(--t-graphite) 90%, black);
  --edge-bright:color-mix(in oklab, var(--t-graphite) 55%, white);

  /* ---- Type on dark. mutedOnDark is the token for secondary text on a dark
     ground; it measures 8.99:1 on asphalt. ---- */
  --text:        color-mix(in oklab, var(--t-white) 96%, var(--t-parchment));
  --text-muted:  var(--t-muted-on-dark);
  --text-dim:    color-mix(in oklab, var(--t-muted-on-dark) 72%, var(--t-asphalt));

  /* ---- Accent: the workspace's own identity. ---- */
  --accent:       var(--t-geo);
  --accent-bright:color-mix(in oklab, var(--t-geo) 72%, white);
  --accent-deep:  color-mix(in oklab, var(--t-geo) 55%, var(--t-asphalt));
  --accent-ink:   color-mix(in oklab, var(--t-asphalt) 82%, var(--t-geo));

  /* ---- Course identity. Used for the course a document belongs to, never
     as decoration. ---- */
  --course-chemistry:   var(--t-chem);
  --course-chemistry-2: var(--t-chem-2);
  --course-physics:     var(--t-phys);
  --course-physics-2:   var(--t-phys-2);
  --course-geology:     var(--t-geo);
  --course-geology-2:   var(--t-geo-2);
  --course: var(--accent);

  /* ---- Semantic. Meaning, never branding. A course colour never stands in
     for a warning colour. ---- */
  --danger:  var(--t-danger);
  --caution: var(--t-caution);
  --success: var(--t-success);

  /* ---- Paper. The document previews and the draft preview show a printed
     page; a printed page is white. ---- */
  --paper:     var(--t-white);
  --paper-ink: var(--t-asphalt);
  --paper-rule:var(--t-rule);

  /* ---- Type stacks, from the locked font stack. ---- */
  --font:           {typ['stack']};
  --font-condensed: {typ['stackCondensed']};
}}

/* Course scoping. Set data-course on any subtree and everything inside it that
   reads var(--course) follows, so a Chemistry card cannot end up wearing the
   Geology accent. */
[data-course="chemistry"] {{ --course: var(--course-chemistry); --course-2: var(--course-chemistry-2); }}
[data-course="physics"]   {{ --course: var(--course-physics);   --course-2: var(--course-physics-2); }}
[data-course="geology"]   {{ --course: var(--course-geology);   --course-2: var(--course-geology-2); }}
[data-course="class"],
[data-course="system"],
[data-course="all"]       {{ --course: var(--accent);           --course-2: var(--accent-bright); }}
"""


# The browser tab icon. Same source, same accent — a second file rather than a
# second palette.
icon = f"""<!-- GENERATED FROM brand/tokens.json BY scripts/build_app_css.py - DO NOT EDIT. -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="7" fill="{g['asphalt']['hex']}"/>
  <path d="M8 21.5c1.8 1.6 4 2.4 6.4 2.4 3.2 0 5.2-1.5 5.2-3.7 0-2.1-1.5-3.1-4.6-3.9l-1.8-.5c-3.6-.9-5.6-2.6-5.6-5.5C7.6 7 10.3 5 14.6 5c2.2 0 4.2.6 5.8 1.7"
        fill="none" stroke="{c['geology']['primary']['hex']}" stroke-width="3"
        stroke-linecap="round"/>
  <rect x="7" y="25" width="18" height="2" rx="1" fill="{c['chemistry']['primary']['hex']}"/>
</svg>
"""


def main(argv):
    outputs = [(OUT, css), (ICON, icon)]
    if "--check" in argv:
        for path, wanted in outputs:
            rel = os.path.relpath(path, REPO)
            if not os.path.exists(path):
                print(f"build_app_css: {rel} missing — run scripts/build_app_css.py")
                return 1
            if open(path, encoding="utf-8").read() != wanted:
                print(f"build_app_css: {rel} has drifted from brand/tokens.json — "
                      "re-run scripts/build_app_css.py")
                return 1
        print("build_app_css: OK — generated files match brand/tokens.json")
        return 0
    for path, content in outputs:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"wrote {os.path.relpath(path, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
