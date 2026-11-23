#!/usr/bin/env python3
"""Unit Roadmap builder (SHULL-CHG-0100).

    python3 templates/unit-roadmap/build_unit_roadmap.py templates/unit-roadmap/specs/chem_u06.json

One page, filed at the front of a unit's binder section. Writes the HTML and PDF to
output/<course>/u<NN>/ under the standards/NAMING.md name, then checks:
  · every taught section in courses/<course>/DECISIONS.md has an entry in the spec, and the spec
    names no section the decisions file does not (codes are never built from a spec alone)
  · the page count is exactly 1

The unit title, phase and section titles are read from DECISIONS.md, never typed in the spec:
a fact lives in one place. The spec holds only what is particular to this page.
"""
import html, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "templates"))
from _shull_name import document_name, short_title  # noqa: E402

SKIP = re.compile(r"RETIRED|DROPPED|FOLDED", re.I)


def unit_from_decisions(course, unit):
    """(phase name, unit title, [(code, title)] of taught sections) from the curriculum map."""
    text = (REPO / "courses" / course / "DECISIONS.md").read_text()
    phase = None
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^### Phase \d+ — (.+?) \(", line)
        if m:
            phase = m.group(1)
        m = re.match(rf"^\*\*U{unit} (.+?)\*\*", line)
        if not m:
            continue
        title = m.group(1)
        body = []
        for nxt in lines[i + 1:]:
            if not nxt.strip() or nxt.startswith(("**U", "#", "*")):
                break
            body.append(nxt.strip())
        sections = []
        for part in " ".join(body).split(" · "):
            m2 = re.match(rf"^({unit}\.\d+)\s+(.+)$", part.strip())
            if m2 and not SKIP.search(part):
                sections.append((m2.group(1), m2.group(2).strip()))
        return phase, title, sections
    raise SystemExit(f"U{unit} is not in courses/{course}/DECISIONS.md. Never build against a code "
                     "that is not there (CLAUDE.md §3).")


def md(s):
    """Spec text: escape, then **bold**, _{sub}, ^{sup}, [[no line break]]."""
    s = html.escape(s)
    s = re.sub(r"\[\[(.+?)\]\]", r'<span class="nw">\1</span>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"_\{([^}]*)\}", r"<sub>\1</sub>", s)
    return re.sub(r"\^\{([^}]*)\}", r"<sup>\1</sup>", s)


def render(spec):
    course, unit = spec["course"], int(spec["unit"])
    phase, title, sections = unit_from_decisions(course, unit)

    have, want = set(spec["sections"]), {c for c, _ in sections}
    if have != want:
        raise SystemExit(f"spec and DECISIONS.md disagree on U{unit} sections: "
                         f"missing from spec {sorted(want - have)}, not in DECISIONS {sorted(have - want)}")

    words = title.split()
    head = " ".join(words[:-1]) + (" " if len(words) > 1 else "")
    rows = []
    for code, stitle in sections:
        s = spec["sections"][code]
        ican = "".join(f"<li>{md(t)}</li>" for t in s["ican"])
        stds = "".join(f'<span class="std main">{html.escape(c)}</span>' for c in s["standards"]["main"]) + \
               "".join(f'<span class="std sup">{html.escape(c)}</span>' for c in s["standards"].get("support", []))
        rows.append(f'<tr><td><span class="num">{code}</span><div class="sname">{html.escape(stitle)}</div>'
                    f'<div class="focus">{md(s.get("focus", ""))}</div></td>'
                    f'<td><ul class="ican">{ican}</ul></td><td>{stds}</td></tr>')
    key = "".join(f"<div><b>{html.escape(c)} {html.escape(n)}:</b> {md(d)}</div>" for c, n, d in spec["standards_key"])
    prior = "".join(f"<li>{md(p)}</li>" for p in spec["builds_on"])
    measured = "".join(f"<li>{md(m)}</li>" for m in spec["measured"])
    codes = f"U{unit} / S{sections[0][0]}–{sections[-1][0]}" if len(sections) > 1 else f"U{unit} / S{sections[0][0]}"
    course_word = course.title()

    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Unit {unit} Roadmap</title>
<link rel="stylesheet" href="../../../templates/lab/shull-lab-tokens.css">
<link rel="stylesheet" href="../../../templates/unit-roadmap/unit_roadmap.css">
</head><body class="{ {"chemistry": "chem", "physics": "phys", "geology": "geo"}[course] }">
<span class="code-string">SHULL SCIENCE · {course_word.upper()} · {codes}</span>
<header class="head"><div>
<div class="chip">U{unit} · UNIT ROADMAP</div>
<div class="kicker">{course_word}{(" · " + html.escape(phase)) if phase else ""}</div>
<h1>{html.escape(head)}<span class="acc">{html.escape(words[-1])}</span></h1></div>
<div class="meta"><b>{html.escape(spec["teacher"])}</b> · High School {course_word}<br>{html.escape(spec["school"])}<br>
{len(sections)} sections · {html.escape(spec["grades"])}</div></header>
<div class="double"></div>
<section class="intro"><div class="idea"><div class="label">Big Idea</div><p>{md(spec["big_idea"])}</p></div>
<div class="prior"><div class="label">Builds On</div><ul>{prior}</ul></div></section>
<table class="sec"><colgroup><col style="width:22%"><col style="width:57%"><col style="width:21%"></colgroup>
<thead><tr><th>Section</th><th>I Can… (Learning Targets)</th><th>{html.escape(spec["standards_label"])}</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table>
<section class="bottom"><div class="keyblock"><div class="label">{html.escape(spec["standards_source"])}</div>
<div class="key">{key}</div>
<p class="legend"><span class="std main">Bold box</span> main standard · <span class="std sup">Dashed box</span> supporting standard</p></div>
<div class="box"><div class="label">How Learning Is Measured</div><ul class="assess">{measured}</ul></div></section>
</body></html>''', course, unit, title


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    spec = json.loads(Path(sys.argv[1]).read_text())
    page, course, unit, title = render(spec)
    out = REPO / "output" / course / f"u{unit:02d}"
    out.mkdir(parents=True, exist_ok=True)
    name = document_name("Roadmap", ["a", "b"], unit, unit_title=short_title(course, f"U{unit}"), ext="pdf")
    html_path = out / name.replace(".pdf", ".html")
    html_path.write_text(page)

    from weasyprint import HTML
    doc = HTML(filename=str(html_path)).render()
    pdf = out / name
    doc.write_pdf(pdf)
    pages = len(doc.pages)
    print(f"{pdf.relative_to(REPO)}  pages={pages}")
    if pages != 1:
        print("FAIL: a Unit Roadmap is one page. Shorten the spec text; never shrink the type.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
