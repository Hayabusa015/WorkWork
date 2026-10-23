#!/usr/bin/env python3
"""Physics direction reference: the angle circle and the eight direction names. Two pages, PDF.

    python3 templates/reference/build_direction_reference.py OUTDIR

Rebuilt from Matt's "physics direction reference" sheet. Every angle and every "standard angle" line
is computed from the direction words (theta_from in templates/quiz/vectors_22.py), so a diagram
cannot disagree with its caption. Colour comes from brand/tokens.json; none is typed here. Output
name follows standards/NAMING.md.

Follows brand/SHULL_DESIGN_SYSTEM.md and matches the Physics notes and quiz headers:
  - Coloured TYPE is ink or Quantum Gold Deep only. Deep Purple is never type on white (section 3);
    it appears only as a graphic: the final arrow and a small tag on the "words swapped" column.
  - Nothing is filled: colour is a thin rule, a small tag, or an arrow (section 8). No solid-fill
    headline word, no tinted chart.
  - Nothing below the 8 pt print floor except the running footer (section 4).
  - Page 2 is a real table, not a card grid (section 11).
  - The two columns are told apart by the words themselves, an outline round the gold arrow, and the
    tag, so a photocopy still works (section 3, grayscale survival).
"""
import json, math, os, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "templates"))
sys.path.insert(0, os.path.join(REPO, "templates", "quiz"))
from _shull_name import document_name          # noqa: E402
from vectors_22 import theta_from                # noqa: E402

T = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
G, PH = T["ground"], T["courses"]["physics"]
GOLD, GOLD_DEEP, PURPLE = PH["primary"]["hex"], PH["primaryDeep"]["hex"], PH["secondary"]["hex"]
INK, GRAPHITE, HAIR, LABEL, FOOT, WHITE = (G[k]["hex"] for k in
                                           ("asphalt", "graphite", "ruleHairline", "label", "footer", "white"))
FONT = T["typography"]["stack"]
M = T["print"]["margins"]
AXIS = {"east": 0, "north": 90, "west": 180, "south": 270}
UP = lambda w: w.upper()
CODE = "U02  ·  S02.1 – S02.3"        # the sections this unit-level sheet serves


# ---- svg helpers (1 user unit = 1 pt) ----------------------------------------------------

def pol(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy - r * math.sin(a)


def line(x1, y1, x2, y2, color, w=1.0, cap="round", op=1.0):
    o = f' stroke-opacity="{op}"' if op < 1 else ""
    return (f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" '
            f'stroke-width="{w}" stroke-linecap="{cap}"{o}/>')


def arrow(cx, cy, r, deg, color, w=1.6, head=6.5, outline=None):
    """A shaft from (cx, cy) to radius r at `deg`, with a drawn head (no SVG markers).
    `outline` puts a thin dark edge round it, so a pale arrow still shows when photocopied."""
    x2, y2 = pol(cx, cy, r, deg)
    bx, by = pol(cx, cy, r - head, deg)
    px, py = -math.sin(math.radians(deg)), -math.cos(math.radians(deg))      # perpendicular
    hw = head * 0.42
    pts = f"{x2:.2f},{y2:.2f} {bx + px * hw:.2f},{by + py * hw:.2f} {bx - px * hw:.2f},{by - py * hw:.2f}"
    out = []
    if outline:
        out.append(line(cx, cy, bx, by, outline, w + 1.8))
        out.append(f'<polygon points="{pts}" fill="{outline}" stroke="{outline}" stroke-width="1.8" stroke-linejoin="round"/>')
    out.append(line(cx, cy, bx, by, color, w))
    out.append(f'<polygon points="{pts}" fill="{color}"/>')
    return "".join(out)


def text(x, y, s, size, color, weight=400, anchor="middle", tracking=0):
    t = f' letter-spacing="{tracking}"' if tracking else ""
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{color}" font-weight="{weight}" '
            f'text-anchor="{anchor}" font-family="{html.escape(FONT)}"{t}>{html.escape(s)}</text>')


def arc(cx, cy, r, d0, d1, color, w=1.2, head=True):
    """An arc from d0 to d1 (the short way), sampled as a polyline, with a small head."""
    delta = (d1 - d0 + 180) % 360 - 180
    n = max(3, int(abs(delta) / 3))
    pts = [pol(cx, cy, r, d0 + delta * i / n) for i in range(n + 1)]
    out = [f'<polyline points="{" ".join(f"{x:.2f},{y:.2f}" for x, y in pts)}" fill="none" '
           f'stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>']
    if head:
        (x0, y0), (x1, y1) = pts[-2], pts[-1]
        ang = math.degrees(math.atan2(-(y1 - y0), x1 - x0))
        hx, hy = pol(x1, y1, 5.2, ang + 180 - 24)
        gx, gy = pol(x1, y1, 5.2, ang + 180 + 24)
        out.append(f'<polygon points="{x1:.2f},{y1:.2f} {hx:.2f},{hy:.2f} {gx:.2f},{gy:.2f}" fill="{color}"/>')
    return "".join(out)


# ---- diagrams --------------------------------------------------------------------------

def circle_svg():
    W, H, cx, cy, R = 452, 358, 226, 180, 140
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}pt" height="{H}pt">']
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{GRAPHITE}" stroke-width="1.2"/>')
    for d in range(0, 360, 15):
        major = d % 45 == 0
        x2, y2 = pol(cx, cy, R, d)
        s.append(line(cx, cy, x2, y2, GRAPHITE, 0.8, op=0.55 if major else 0.32))
        if d % 90:
            lx, ly = pol(cx, cy, R + 17, d)
            s.append(text(lx, ly + 2.8, f"{d}°", 8, LABEL if not major else INK, 700 if major else 400))
    for d in (0, 90, 180, 270):
        s.append(arrow(cx, cy, R + 24, d, INK, 1.5, 7))
    for d, off in ((0, (-36, -6)), (90, (20, 22)), (180, (34, -6)), (270, (20, -10))):
        x, y = pol(cx, cy, R, d)
        s.append(text(x + off[0], y + off[1], f"{d}°" if d else "0° / 360°", 13, GOLD_DEEP, 700))
    s.append(text(cx, cy - R - 30, "NORTH  /  +y", 9.5, INK, 700, tracking=0.6))
    s.append(text(cx, cy + R + 36, "SOUTH  /  −y", 9.5, INK, 700, tracking=0.6))
    s.append(text(cx - R - 28, cy - 4, "WEST", 9.5, INK, 700, "end", 0.6))
    s.append(text(cx - R - 28, cy + 8, "−x", 9.5, INK, 700, "end", 0.6))
    s.append(text(cx + R + 28, cy - 4, "EAST", 9.5, INK, 700, "start", 0.6))
    s.append(text(cx + R + 28, cy + 8, "+x", 9.5, INK, 700, "start", 0.6))
    s.append(arc(cx, cy, 52, 6, 74, INK, 1.4))
    cxl, cyl = pol(cx, cy, 70, 40)
    s.append(text(cxl, cyl + 3, "CCW", 8.5, INK, 700, "start", 0.8))
    s.append("</svg>")
    return "".join(s)


def standard_formula(a, first, second):
    th = theta_from(a, first, second)
    s0 = AXIS[second]
    delta = (th - s0 + 180) % 360 - 180
    if delta > 0:
        return f"{s0}° + {a}° = {th:.0f}°", th
    return f"{s0 if s0 else 360}° − {a}° = {th:.0f}°", th


def mini_svg(first, second, a, color, outlined, size=106):
    """One compass diagram: dark starting axis, coloured final arrow, the turn between them."""
    c = size / 2
    L = size / 2 - 17
    th = theta_from(a, first, second)
    s0 = AXIS[second]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}pt" height="{size}pt">']
    for d in (0, 90, 180, 270):
        s.append(line(*pol(c, c, 14, d), *pol(c, c, L + 2, d), GRAPHITE, 0.8, cap="butt", op=0.4))
    for d, lab in ((90, "N"), (270, "S"), (0, "E"), (180, "W")):
        x, y = pol(c, c, L + 11, d)
        s.append(text(x, y + 2.9, lab, 8.5, LABEL, 700))
    s.append(arrow(c, c, L, s0, GRAPHITE, 1.5, 6.5))
    s.append(arrow(c, c, L, th, color, 2.4, 8, outline=GRAPHITE if outlined else None))
    ar = L * 0.58
    s.append(arc(c, c, ar, s0, th, INK, 1.2))
    # A 30 degree wedge is too narrow to hold its own label, so the label sits just outside it,
    # beside the starting axis, on the side away from the turn.
    sd = 1 if (th - s0 + 180) % 360 - 180 > 0 else -1
    mx, my = pol(c, c, L * 0.80, s0 - sd * 23)
    s.append(text(mx, my + 3.2, f"{a}°", 9.5, INK, 700))
    s.append("</svg>")
    return "".join(s)


# ---- page content ------------------------------------------------------------------------

ORDER = [(("north", "east"), ("east", "north")), (("north", "west"), ("west", "north")),
         (("south", "west"), ("west", "south")), (("east", "south"), ("south", "east"))]


def cell(first, second, swapped):
    color = PURPLE if swapped else GOLD
    f, _ = standard_formula(30, first, second)
    return f"""
      <div class="ctitle"><span class="tag" style="background:{color}"></span>30° {first} of {second}</div>
      <table class="inner"><tr>
        <td class="cdiag">{mini_svg(first, second, 30, color, not swapped)}</td>
        <td class="csteps"><div class="s1">Start {UP(second)}.</div>
          <div>Turn 30° toward<br><b>{UP(first)}</b>.</div></td></tr></table>
      <div class="cform">Standard angle: <b>{f}</b></div>"""


def build_html():
    css = f"""
    @page {{ size: 8.5in 11in; margin: {M['top']} {M['right']} {M['bottom']} {M['left']};
      @bottom-left {{ content: "SHULL SCIENCE / PHYSICS / UNIT 02 / REFERENCE"; font: 7pt {FONT}; color: {FOOT}; letter-spacing: .04em; }}
      @bottom-right {{ content: "PAGE " counter(page) " OF " counter(pages); font: 7pt {FONT}; color: {FOOT}; letter-spacing: .04em; }} }}
    * {{ box-sizing: border-box; }}
    html {{ font-family: {FONT}; color: {INK}; font-size: 10.5pt; }}
    body {{ margin: 0; }}
    .page {{ page-break-after: always; }}
    .page:last-child {{ page-break-after: auto; }}
    table {{ border-collapse: collapse; }}
    td {{ padding: 0; vertical-align: top; }}
    .head {{ width: 100%; border-bottom: 2.25pt solid {GOLD}; margin-bottom: 8pt; }}
    .head td {{ padding-bottom: 6pt; }}
    .kicker {{ font-size: 8pt; font-weight: 700; letter-spacing: .14em; color: {GOLD_DEEP}; text-transform: uppercase; }}
    h1 {{ font-size: 15pt; line-height: 1.1; margin: 3pt 0 2pt; font-weight: 700; color: {INK}; text-transform: uppercase; letter-spacing: .01em; }}
    .doc {{ font-size: 8pt; font-weight: 700; letter-spacing: .14em; color: {LABEL}; text-transform: uppercase; }}
    .code {{ text-align: right; font-size: 8.5pt; font-weight: 700; letter-spacing: .14em; color: {GOLD_DEEP}; white-space: nowrap; padding-top: 1pt; }}
    .sub {{ font-size: 10.5pt; color: {GRAPHITE}; margin: 0; }}
    .eyebrow {{ font-size: 8pt; font-weight: 700; letter-spacing: .13em; text-transform: uppercase; color: {GOLD_DEEP}; margin: 7pt 0 2pt; }}
    .lead {{ font-size: 10pt; margin: 0 0 3pt; color: {GRAPHITE}; }}
    .circle {{ text-align: center; }}
    .rule {{ border-top: .75pt solid {HAIR}; margin-top: 2pt; }}
    .callout {{ border-left: 2.25pt solid {GOLD}; padding: 1pt 0 1pt 9pt; margin: 7pt 0 5pt; }}
    .callout .h {{ font-weight: 700; font-size: 11.5pt; margin: 0 0 1pt; color: {INK}; }}
    .callout p {{ margin: 0; font-size: 10pt; color: {GRAPHITE}; }}
    .pair {{ width: 100%; }}
    .pair td {{ width: 50%; text-align: center; padding: 0 6pt; }}
    .pair td + td {{ border-left: .75pt solid {HAIR}; }}
    .big {{ font-size: 13pt; font-weight: 700; margin: 2pt 0 0; color: {INK}; }}
    .cap {{ font-size: 9.5pt; margin: 0; }}
    .cap b {{ font-weight: 700; }}
    .tag {{ display: inline-block; width: 2.25pt; height: 11pt; vertical-align: -1.5pt; margin-right: 6pt; }}
    .center {{ text-align: center; font-weight: 700; font-size: 10.5pt; margin: 6pt 0 1pt; }}
    .note {{ text-align: center; font-size: 9pt; color: {GRAPHITE}; margin: 0; }}
    .conv {{ border-top: .75pt solid {HAIR}; margin-top: 7pt; padding-top: 4pt; font-size: 8.5pt; color: {GRAPHITE}; }}
    .key {{ font-size: 8.5pt; color: {GRAPHITE}; margin: 3pt 0 5pt; }}
    .key svg {{ vertical-align: middle; margin: 0 4pt 0 10pt; }}
    .grid {{ width: 100%; table-layout: fixed; }}
    .grid > tbody > tr > td {{ width: 50%; padding: 5pt 9pt 3pt 0; border-top: .75pt solid {HAIR}; }}
    .grid > tbody > tr > td + td {{ padding: 5pt 0 3pt 14pt; border-left: .75pt solid {HAIR}; }}
    .ctitle {{ font-size: 13pt; font-weight: 700; margin-bottom: 1pt; color: {INK}; }}
    .inner td {{ vertical-align: middle; }}
    .cdiag {{ width: 106pt; height: 106pt; }}
    .csteps {{ padding-left: 8pt; font-size: 10.5pt; line-height: 1.45; }}
    .s1 {{ font-weight: 700; letter-spacing: .02em; }}
    .cform {{ font-size: 10pt; }}
    .why {{ border-left: 2.25pt solid {GOLD}; padding: 1pt 0 1pt 9pt; margin-top: 8pt; }}
    .why .h {{ font-weight: 700; font-size: 10.5pt; margin: 0 0 1pt; color: {INK}; }}
    .why p {{ margin: 0; font-size: 9.5pt; color: {GRAPHITE}; }}
    """
    head = lambda title: f"""
      <table class="head"><tr><td>
        <div class="kicker">SHULL SCIENCE &nbsp;·&nbsp; JAMES A. GARFIELD LOCAL SCHOOLS</div>
        <h1>{title}</h1>
        <div class="doc">Physics reference</div></td>
        <td class="code">{CODE}</td></tr></table>"""
    pa = standard_formula(30, "west", "north")[0]
    pb = standard_formula(30, "north", "west")[0]
    p1 = f"""
    <div class="page">
      {head('Angles &amp; directions')}
      <p class="sub">A full turn is 360°. A quarter turn is 90°.</p>
      <div class="eyebrow">Standard physics angles</div>
      <p class="lead">Start at EAST (0°). Measure counterclockwise.</p>
      <div class="circle">{circle_svg()}</div>
      <div class="rule"></div>
      <div class="callout"><p class="h">Read the direction after “of” first.</p>
        <p>That is your starting axis. Turn toward the direction before “of.”</p></div>
      <table class="pair"><tr>
        <td><div class="big"><span class="tag" style="background:{GOLD}"></span>30° west of north</div>
          {mini_svg('west', 'north', 30, GOLD, True, size=128)}
          <p class="cap">Start NORTH. Turn 30° toward WEST.</p>
          <p class="cap"><b>Standard angle: {pa}</b></p></td>
        <td><div class="big"><span class="tag" style="background:{PURPLE}"></span>30° north of west</div>
          {mini_svg('north', 'west', 30, PURPLE, False, size=128)}
          <p class="cap">Start WEST. Turn 30° toward NORTH.</p>
          <p class="cap"><b>Standard angle: {pb}</b></p></td></tr></table>
      <div class="center">Same quadrant. Different directions. The starting axis matters!</div>
      <p class="note">Same direction, two names: 30° west of north = 60° north of west.</p>
      <div class="conv">Convention note: compass bearings start at north and increase clockwise.</div>
    </div>"""
    rows = "".join(f"<tr><td>{cell(*l, False)}</td><td>{cell(*r, True)}</td></tr>" for l, r in ORDER)
    sw = lambda c, w, ol=None: (f'<svg width="22pt" height="7pt" viewBox="0 0 22 7">'
                                + (f'<line x1="0" y1="3.5" x2="22" y2="3.5" stroke="{ol}" stroke-width="{w + 1.8}" stroke-linecap="round"/>' if ol else "")
                                + f'<line x1="0" y1="3.5" x2="22" y2="3.5" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/></svg>')
    p2 = f"""
    <div class="page">
      {head('Directions in every quadrant')}
      <p class="sub">Start with the direction AFTER “of.” Then turn toward the other direction.</p>
      <p class="key">{sw(GRAPHITE, 1.6)}Starting axis
        {sw(GOLD, 2.4, GRAPHITE)}Final direction
        {sw(PURPLE, 2.4)}Final direction, the same words swapped</p>
      <table class="grid"><tbody>{rows}</tbody></table>
      <div class="why"><p class="h">Why use 30°? Swapping the words changes the direction.</p>
        <p>At 45°, the two names match: 45° north of east = 45° east of north.</p>
        <p>All standard angles here start at east and increase counterclockwise. A negative angle runs clockwise from east: −30° = 330°.</p></div>
    </div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>Angles &amp; directions</title>"
            f"<style>{css}</style></head><body>{p1}{p2}</body></html>")


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    pdf = os.path.join(outdir, document_name("Reference", ["2.1", "2.2", "2.3"], 2, ext="pdf"))
    from weasyprint import HTML
    HTML(string=build_html(), base_url=outdir).write_pdf(pdf)
    print("wrote", pdf)
    return 0


if __name__ == "__main__":
    sys.exit(main())
