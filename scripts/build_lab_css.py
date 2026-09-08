#!/usr/bin/env python3
"""Generate templates/lab/shull-lab-tokens.css from brand/tokens.json.

The lab templates must not contain hand-typed hex values - that is the rule
validate_tokens.py enforces and the reason six palettes drifted apart. This
emits CSS custom properties, and the body course class (chem | phys | geo)
switches the course accent.

    python3 scripts/build_lab_css.py
"""
import json, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tokens = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
out = os.path.join(REPO, "templates", "lab", "shull-lab-tokens.css")

g = tokens["ground"]
c = tokens["courses"]
sem = tokens["semantic"]
typ = tokens["typography"]

css = f"""/* GENERATED FROM brand/tokens.json BY scripts/build_lab_css.py - DO NOT EDIT.
   Re-run the script after changing any token. Hand-editing a hex here is the
   defect validate_tokens.py exists to catch. */

:root {{
  /* Grounds */
  --ground:        {g['white']['hex']};
  --ink:           {g['asphalt']['hex']};
  --structure:     {g['graphite']['hex']};
  --surface:       {g['parchment']['hex']};

  /* Neutral working values, derived from the grounds */
  --rule-hairline: #c8cdc2;
  --label:         #55604f;
  --footer:        #6b7265;

  /* Semantic - used for meaning, never for branding */
  --warn:          {sem['caution']['deep']};
  --warn-rule:     {sem['caution']['hex']};

  /* Course accent. Defaults to Chemistry; the body class overrides. */
  --accent:        {c['chemistry']['primaryDeep']['hex']};
  --accent-display:{c['chemistry']['primary']['hex']};

  /* Type */
  --display: "{typ['primary']['family']}", "{typ['fallback']['family']}", "{typ['lastResort']['family']}", sans-serif;
  --body:    "{typ['primary']['family']}", "{typ['fallback']['family']}", "{typ['lastResort']['family']}", sans-serif;
}}

body.chem {{ --accent: {c['chemistry']['primaryDeep']['hex']}; --accent-display: {c['chemistry']['primary']['hex']}; }}
body.phys {{ --accent: {c['physics']['primaryDeep']['hex']};   --accent-display: {c['physics']['primary']['hex']}; }}
body.geo  {{ --accent: {c['geology']['primaryDeep']['hex']};   --accent-display: {c['geology']['primary']['hex']}; }}

/* The rule that makes this safe on paper: --accent is the text-safe deep
   variant and is the ONLY course colour permitted as type on a light ground.
   --accent-display is a fill, rule or marker. Never body text on white.
   See brand/SHULL_DESIGN_SYSTEM.md section 3 and SHULL-CHG-0008. */
"""
open(out, "w").write(css)
print(f"wrote {os.path.relpath(out, REPO)}")
for line in css.splitlines():
    if line.strip().startswith(("--accent", "body.")):
        print("  ", line.strip())
