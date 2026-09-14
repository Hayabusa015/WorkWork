#!/usr/bin/env python3
"""Render a SHULL deck spec as a self-contained HTML presentation.

Same input as templates/slide/build_deck.js - the deck JSON in
templates/slide/decks/ - so a section can be built as .pptx or as HTML from one
spec, and the two cannot drift into different lessons.

The geometry is not reinterpreted. SHULL Slide System v2 is 13.333in x 7.5in; at
144 px/in that is the 1920x1080 stage the vendored frontend-slides skill mandates,
so every locked measurement converts by x144 (inches) or x2 (points). The layout
constants below are read from brand/tokens.json at build time, never typed.

Archivo is embedded as base64 woff2 so the file is genuinely standalone - it opens
from a USB stick on a classroom machine with no network and no PowerPoint.

    python3 scripts/build_slide_html.py <deck.json> [out.html]
"""
import base64, io, json, os, sys, html

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
SCALE = json.loads(open(os.path.join(REPO, "templates", "slide", "tokens.generated.js"))
                   .read().split("module.exports =", 1)[1].rstrip().rstrip(";"))["type"]
G, COURSES, GEOM = T["ground"], T["courses"], T["slideGeometry"]

PX, PT = 144, 2
inpx = lambda v: round(v * PX)
ptpx = lambda v: round(v * PT)
e = lambda s: html.escape(str(s or ""))
# A spec writes "\n" for a line break; on a slide that is a real break, not a space.
lines = lambda s: "<br>".join(e(x) for x in str(s or "").split("\n"))


def font_face(name, weight):
    from fontTools.ttLib import TTFont
    f = TTFont(os.path.join(REPO, "brand", "fonts", f"Archivo-{name}.ttf"))
    f.flavor = "woff2"
    buf = io.BytesIO(); f.save(buf)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return (f"@font-face{{font-family:Archivo;font-style:normal;font-weight:{weight};"
            f"font-display:block;src:url(data:font/woff2;base64,{b64}) format('woff2')}}")


def card(label, body, *, wide=False):
    return (f'<div class="card{" wide" if wide else ""}">'
            f'<div class="card-l">{e(label)}</div>'
            f'<div class="card-b">{lines(body)}</div></div>')


def slide_html(s, deck, n, total):
    m, f = s["master"], s.get("fields", {})
    dark = m in GEOM["darkGroundLayouts"]
    unit = f"U{int(deck['unit']):02d}"
    sect = f"S{deck['section']}"
    foot = (f'<div class="foot"><span>SHULL SCIENCE</span>'
            f'<span>{unit} &middot; {sect}</span></div>')
    eyebrow = f.get("eyebrow") or f"UNIT {int(deck['unit'])} &middot; {deck['course'].upper()}"
    head = f'<div class="eyebrow">{eyebrow}</div><div class="hair"></div>'
    head += f'<h1>{lines(f.get("headline"))}</h1>'
    if f.get("subhead"):
        head += f'<p class="sub">{lines(f["subhead"])}</p>'

    body = ""
    if m == "02_SECTION_TITLE":
        head = (f'<div class="num">{e(f.get("number"))}</div>'
                f'<h1 class="big">{lines(f.get("headline"))}</h1>'
                f'<p class="sub">{lines(f.get("subhead"))}</p>')
    elif m == "12_DECK_INDEX":
        body = ('<ol class="index">' + "".join(
            f'<li><span>{i:02d}</span>{e(x.get("fields", {}).get("headline", "").splitlines()[0] if x.get("fields", {}).get("headline") else x["master"])}</li>'
            for i, x in enumerate(deck["slides"], 1)) + "</ol>")
    elif m == "06_CONCEPT_IMAGE":
        body = f'<div class="keyq">{lines(f.get("keyq"))}</div>'
    elif m in ("03_GROUPED_CONCEPT",):
        body = ('<div class="row two">' + card(f.get("c1_l"), f.get("c1_b"))
                + card(f.get("c2_l"), f.get("c2_b")) + "</div>")
    elif m == "07_COMPARISON_CARDS":
        body = ('<div class="row three">' + "".join(
            card(f.get(f"k{i}_l"), f.get(f"k{i}_b")) for i in (1, 2, 3)) + "</div>")
    elif m == "08_DIAGRAM_ANNOTATION":
        body = ('<div class="row three">' + "".join(
            card(f.get(f"a{i}_l"), f.get(f"a{i}_b")) for i in (1, 2, 3)) + "</div>")
    elif m == "05_PROCESS_TIMELINE":
        body = ('<div class="row four">' + "".join(
            f'<div class="step"><div class="step-n">{i}</div>'
            f'<div class="card-l">{e(f.get(f"s{i}_l"))}</div>'
            f'<div class="card-b">{lines(f.get(f"s{i}_b"))}</div></div>' for i in (1, 2, 3, 4))
            + "</div>")
    elif m == "09_EXAMPLE_PROBLEM":
        body = (f'<div class="problem">{lines(f.get("problem"))}</div><div class="row two">'
                + card(f.get("g1_l"), f.get("g1_b")) + card(f.get("g2_l"), f.get("g2_b"))
                + '</div><div class="work empty"><div class="card-l">WORK</div></div>')
    elif m == "10_WORKED_SOLUTION":
        body = ('<div class="row two">' + card(f.get("f1_l"), f.get("f1_b"))
                + f'<div class="work"><div class="card-l">WORK</div>'
                f'<div class="work-b">{lines(f.get("work"))}</div></div></div>')

    if f.get("mustwrite"):
        body += (f'<div class="mustwrite"><span>MUST WRITE</span>'
                 f'<b>{lines(f["mustwrite"])}</b></div>')

    return (f'<section class="slide{" dark" if dark else ""}" data-n="{n}" '
            f'aria-label="Slide {n} of {total}">{head}{body}{foot}</section>')


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip().splitlines()[-1], file=sys.stderr); return 1
    deck = json.load(open(sys.argv[1], encoding="utf-8"))
    course = COURSES[deck["course"]]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(sys.argv[1])[0] + ".html"
    m = GEOM["margins"]
    total = len(deck["slides"])

    css = f"""
:root{{
 --accent:{course['primary']['hex']};--accent2:{course['secondary']['hex']};
 --ink:{G['asphalt']['hex']};--paper:{G['white']['hex']};--dark:{G['asphalt']['hex']};
 --muted:{G['footer']['hex']};--onDark:{G['mutedOnDark']['hex']};
 --surface:{G['parchment']['hex']};--hair:{G['ruleHairline']['hex']};
 --ml:{inpx(m['left'])}px;--mt:{inpx(m['top'])}px;
 /* The footer is absolutely placed at footerY. Content must stop above it, or a
    must-write bar lands on top of the section code. */
 --mb:{1080 - inpx(GEOM['footerY']) + ptpx(SCALE['footer']) + 16}px;
 --rail:{inpx(GEOM['railWidthIn'])}px;
 --t-head:{ptpx(SCALE['headline'])}px;--t-sub:{ptpx(SCALE['subhead'])}px;
 --t-body:{ptpx(SCALE['body'])}px;--t-work:{ptpx(SCALE['workArea'])}px;
 --t-label:{ptpx(SCALE['cardLabel'])}px;--t-eyebrow:{ptpx(SCALE['eyebrow'])}px;
 --t-foot:{ptpx(SCALE['footer'])}px;--t-num:{ptpx(SCALE['sectionNumber'])}px;
 --t-unit:{ptpx(SCALE['unitTitle'])}px;
}}
*{{box-sizing:border-box;margin:0}}
html,body{{height:100%;overflow:hidden;background:#000}}
body{{font-family:Archivo,'Liberation Sans',sans-serif;display:grid;place-items:center}}
/* The stage scales as a whole; content never reflows. 1920x1080 always. */
#viewport{{width:100vw;height:100vh;display:grid;place-items:center}}
#stage{{width:1920px;height:1080px;position:relative;transform-origin:center;flex:none}}
.slide{{position:absolute;inset:0;background:var(--paper);color:var(--ink);
 padding:var(--mt) var(--ml) var(--mb);display:none;flex-direction:column}}
.slide.on{{display:flex}}
.slide.dark{{background:var(--dark);color:var(--paper)}}
.eyebrow{{font-size:var(--t-eyebrow);font-weight:700;letter-spacing:.16em;
 color:var(--accent);text-transform:uppercase}}
.slide:not(.dark) .eyebrow{{color:{course['primaryDeep']['hex']}}}
.hair{{width:{inpx(GEOM['hairlineWidthIn'])}px;height:3px;background:var(--accent);margin:14px 0 26px}}
h1{{font-size:var(--t-head);font-weight:700;line-height:1.1;letter-spacing:-.01em;
 border-left:var(--rail) solid var(--accent);padding-left:28px;margin-left:-28px}}
h1.big{{font-size:var(--t-unit);border:0;padding:0;margin:0}}
.num{{font-size:var(--t-num);font-weight:700;color:var(--accent);line-height:1}}
.sub{{font-size:var(--t-sub);color:var(--muted);margin-top:18px;max-width:1400px;line-height:1.4}}
.dark .sub{{color:var(--onDark)}}
.row{{display:grid;gap:20px;margin-top:34px}}
.row.two{{grid-template-columns:repeat(2,1fr)}}
.row.three{{grid-template-columns:repeat(3,1fr)}}
.row.four{{grid-template-columns:repeat(4,1fr)}}
.card,.step,.work{{background:var(--surface);border:2px solid var(--hair);
 padding:{inpx(GEOM['cardPaddingIn']['vertical'])}px {inpx(GEOM['cardPaddingIn']['horizontal'])}px}}
.dark .card,.dark .step{{background:transparent;border-color:var(--accent)}}
.card-l{{font-size:var(--t-label);font-weight:700;letter-spacing:.14em;
 color:{course['primaryDeep']['hex']};text-transform:uppercase;margin-bottom:12px}}
.dark .card-l{{color:var(--accent)}}
.card-b{{font-size:var(--t-body);line-height:1.45}}
.step-n{{font-size:var(--t-label);font-weight:700;color:var(--accent);margin-bottom:6px}}
.keyq{{font-size:var(--t-unit);font-weight:600;line-height:1.2;margin-top:auto;
 padding-left:28px;border-left:var(--rail) solid var(--accent);max-width:1500px}}
.problem{{font-size:var(--t-work);line-height:1.4;margin-top:30px;padding:24px 28px;
 background:var(--surface);border-left:var(--rail) solid var(--accent)}}
.work{{min-height:200px}}
.work-b{{font-size:var(--t-work);line-height:1.5}}
.work.empty{{margin-top:20px;min-height:220px;border-style:dashed}}
.mustwrite{{margin-top:auto;background:var(--ink);color:var(--paper);
 padding:20px 26px;display:flex;gap:22px;align-items:baseline}}
.dark .mustwrite{{background:var(--accent);color:var(--ink)}}
.mustwrite span{{font-size:var(--t-label);font-weight:700;letter-spacing:.14em;
 color:var(--accent);flex:none}}
.dark .mustwrite span{{color:var(--ink)}}
.mustwrite b{{font-size:var(--t-body);line-height:1.4}}
.index{{margin-top:30px;columns:2;gap:60px;font-size:var(--t-body);list-style:none}}
.index li{{margin-bottom:14px;break-inside:avoid}}
.index span{{color:var(--accent);font-weight:700;margin-right:14px}}
.foot{{position:absolute;left:var(--ml);right:var(--ml);top:{inpx(GEOM['footerY'])}px;
 display:flex;justify-content:space-between;font-size:var(--t-foot);
 letter-spacing:.1em;color:var(--muted)}}
.dark .foot{{color:var(--onDark)}}
#hud{{position:fixed;bottom:18px;right:22px;font:600 14px Archivo,sans-serif;
 color:#7d8578;letter-spacing:.1em}}
@media print{{#hud{{display:none}}}}
"""
    js = """
const slides=[...document.querySelectorAll('.slide')];let i=0;
const show=n=>{i=Math.max(0,Math.min(slides.length-1,n));
 slides.forEach((s,k)=>s.classList.toggle('on',k===i));
 document.querySelector('#hud').textContent=(i+1)+' / '+slides.length;};
addEventListener('keydown',ev=>{
 if(['ArrowRight','PageDown',' '].includes(ev.key)){ev.preventDefault();show(i+1);}
 if(['ArrowLeft','PageUp'].includes(ev.key)){ev.preventDefault();show(i-1);}
 if(ev.key==='Home')show(0); if(ev.key==='End')show(slides.length-1);});
addEventListener('click',ev=>show(i+(ev.clientX<innerWidth*0.25?-1:1)));
// Scale the whole stage. Never re-layout: a projector and a phone get the same slide.
const fit=()=>{const s=Math.min(innerWidth/1920,innerHeight/1080);
 document.querySelector('#stage').style.transform='scale('+s+')';};
addEventListener('resize',fit);fit();show(0);
"""
    body = "".join(slide_html(s, deck, n, total) for n, s in enumerate(deck["slides"], 1))
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
           f'<title>SHULL {deck["course"].title()} &middot; U{int(deck["unit"]):02d} S{deck["section"]} '
           f'{e(deck["sectionTitle"])}</title>'
           f'<style>{font_face("Regular", 400)}{font_face("Bold", 700)}{css}</style></head>'
           f'<body><div id="viewport"><div id="stage">{body}</div></div>'
           f'<div id="hud"></div><script>{js}</script></body></html>')
    open(out, "w", encoding="utf-8").write(doc)
    print(f"build_slide_html: wrote {out} — {total} slides, {len(doc)//1024} KB standalone")
    return 0


if __name__ == "__main__":
    sys.exit(main())
