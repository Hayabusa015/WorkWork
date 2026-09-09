#!/usr/bin/env python3
"""Build a guided/Cornell notes packet as PDF from a JSON spec. Option B.

Structure preserved from the GEO U1 packet Matthew already uses and likes -
the Cornell 1.28in/6.22in split, the section rhythm, the closed-notes summary
box, the self-check, the "still fuzzy on" box. Colour and type come from
brand/tokens.json via the generated CSS, so a packet cannot carry a hex.

    python3 templates/notes/build_notes.py specs/<spec>.json out.pdf

Rules it enforces rather than trusts:
  - the section code must exist in that course's DECISIONS.md
  - nothing below the print body floor in tokens.json
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "scripts"))

COURSE_CODE = {"chemistry": "CHEM", "physics": "PHYS", "geology": "GEO"}
CLASS = {"chemistry": "chem", "physics": "phys", "geology": "geo"}


def known_sections(course):
    """The curriculum map is the only authority. Never a filename, never a skill."""
    path = os.path.join(REPO, "courses", course, "DECISIONS.md")
    text = open(path).read()
    end = text.find("## Course sequencing rules")
    return set(re.findall(r"(?<![\d.])\d{1,2}\.\d(?![\d])", text[:end] if end > 0 else text))


def esc(s):
    return html.escape(str(s))


def lines(n):
    return '<div class="rule"></div>' * n


def li(items):
    # The source packet wrote its own bullets into the text. A <li> supplies one, so a
    # kept "•" renders as two.
    return "".join(f"<li>{esc(str(x).lstrip('•·-– ').strip())}</li>" for x in items)


def checkrow(items, size=None):
    return "".join(f'<div><span class="box"></span>{esc(x)}</div>' for x in items)


def build_section(s):
    rows = []
    for r in s["rows"]:
        cue = f'<div class="lbl">{esc(r["cueLabel"])}</div>' + "".join(
            f"<p>{esc(q)}</p>" for q in r["cues"])
        # A note line that is a bare prompt gets ruled writing space under it.
        body = [f'<div class="lbl">{esc(r["notesLabel"])}</div>']
        for n in r["notes"]:
            # Must-write. The original marked these with a sage-green left rule and a
            # pencil glyph; the glyph is not in Archivo and pulled DejaVu Sans into the
            # PDF, so the marker is now a prefix and the rule is drawn in CSS.
            mw = n.startswith(('*', '✎'))
            cls = ' class="mw"' if mw else ''
            body.append(f"<p{cls}>{esc(n.lstrip('*✎').strip())}</p>")
            body.append(lines(2 if n.rstrip().endswith("?") else 1))
        rows.append(f'<tr><td class="cue">{cue}</td>'
                    f'<td class="notes">{"".join(body)}</td></tr>')
    checks = checkrow(s.get("selfCheck", []))
    return f"""
<div class="section">
  <div class="sechead"><div class="t">{esc(s['title'])}</div><div class="c">{esc(s['code'])}</div></div>
  <div class="target"><b>LEARNING TARGET</b>&nbsp;&nbsp;{esc(s['learningTarget'])}</div>
  <table class="cornell">{''.join(rows)}</table>
  <div class="summary">
    <div class="lbl">SECTION SUMMARY — close your notes before you write this</div>
    <p class="prompt">{esc(s['summaryPrompt'])}</p>
    {lines(4)}
    <div class="selfcheck"><div class="lbl">SELF-CHECK</div>{checks}</div>
  </div>
</div>"""


def main():
    spec = json.load(open(sys.argv[1] if len(sys.argv) > 1
                          else os.path.join(HERE, "specs", "geo_u01_s01.2-s01.4.json")))
    course = spec["course"]
    code = COURSE_CODE[course]
    valid = known_sections(course)
    bad = [s for s in spec["sections"] if s not in valid]
    if bad:
        print(f"build_notes: section(s) {', '.join(bad)} are not in "
              f"courses/{course}/DECISIONS.md. Nothing is built against a code that is not "
              f"in the decisions file.", file=sys.stderr)
        return 1

    # Option B renders the Cornell structure and nothing else. It has no work box
    # (SHULL-CHG-0016), no stacked fractions or equation bar and no diagram block
    # (SHULL-CHG-0017), and it used to drop them silently - a worked-example row came
    # out as an empty cell and the packet still said it built. A renderer that cannot
    # print what the spec asks for says so instead of printing a lie.
    unsupported = set()
    if spec.get("equations"):
        unsupported.add("equations (the equation bar and stacked fractions)")
    def scan(node):
        if isinstance(node, dict):
            if "problem" in node:
                unsupported.add("problem (the work box students solve in)")
            if "diagram" in node:
                unsupported.add("diagram (the figure students label)")
            for v in node.values():
                scan(v)
        elif isinstance(node, list):
            for v in node:
                scan(v)
    scan(spec)
    if unsupported:
        print("build_notes: this spec uses " + "; ".join(sorted(unsupported)) +
              ". Option B (HTML/PDF) does not render those. Build it with "
              "build_notes_docx.py, which is the production path.", file=sys.stderr)
        return 1

    unit = f"U{int(spec['unit']):02d}"
    span = f"S{spec['sections'][0]}-S{spec['sections'][-1]}" if len(spec["sections"]) > 1 \
        else f"S{spec['sections'][0]}"
    out = sys.argv[2] if len(sys.argv) > 2 else \
        os.path.join(HERE, f"SHULL_{code}_Guided_Notes_{unit}_{span}.pdf")

    tpl = open(os.path.join(HERE, "SHULL_Notes_TEMPLATE.html")).read()
    doc = (tpl
           .replace("{{UNITTITLE}}", esc(spec["unitTitle"]))
           .replace("{{KICKER}}", esc(spec["kicker"]))
           .replace("{{FIELDS}}", esc(spec["fields"]))
           .replace("{{FOOTCODE}}", esc(f"{unit} · {span}"))
           .replace("{{TARGETS}}", li(spec["unitTargets"]))
           .replace("{{TERMS}}", li(spec["keyTerms"]))
           .replace("{{HOWITWORKS}}", li(spec["howItWorks"]))
           .replace("{{SECTIONLIST}}", checkrow(spec["sectionList"]))
           .replace("{{SECTIONS}}", "".join(build_section(s) for s in spec["sectionsContent"]))
           .replace("{{CLOSEBANNER}}", esc(spec["close"]["banner"]))
           .replace("{{CLOSECHECK}}", checkrow(spec["close"]["checklist"]))
           .replace("{{BIGPICTURE}}", esc(spec["close"]["bigPicture"]))
           .replace("{{FUZZY}}", esc(spec["close"]["fuzzyLabel"])))
    doc = doc.replace("<body", f'<body class="{CLASS[course]}"', 1) \
        if "<body" in doc else f'<body class="{CLASS[course]}">' + doc

    import weasyprint
    weasyprint.HTML(string=doc, base_url=HERE).write_pdf(out)
    print(f"wrote {out}  —  {code} {unit} {span}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
