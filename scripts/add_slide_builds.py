#!/usr/bin/env python3
"""Add click-to-reveal builds to a deck written by templates/slide/build_deck.js.

    python3 scripts/add_slide_builds.py deck.pptx templates/slide/decks/<spec>.json PH_MAP.json

build_deck.js runs it and writes PH_MAP: per slide, its master's placeholder names in declared
order. pptxgenjs drops objectName on placeholder text, so a placeholder is found by its layout
index: the layout's placeholder indexes, ascending, are in that same declared order.

pptxgenjs cannot write animations, so this writes the slide's <p:timing> afterwards. A spec
slide's "builds" is a list of click groups in order; each group is a list of shape names as
build_deck.js tagged them ("a2_b" for a placeholder, "img:diagram", "reveal:diagram").
Every shape in a group appears on the same click, with a short fade. Shapes not named are
on the slide from the start.

Fade, 0.3 s, is the only effect. Slide System v2: subtle, purposeful, never animated
because the software permits it. The prediction-then-answer slides are the purpose.

A rendered PDF shows every slide in its final state, so QA rasters still see everything.
"""
import json, os, re, shutil, sys, tempfile, zipfile

P = "http://schemas.openxmlformats.org/presentationml/2006/main"


def effect(ids, spid, first):
    """One fade-in for one shape. `ids` hands out the cTn ids the timing tree needs."""
    node = "clickEffect" if first else "withEffect"
    return (
        f'<p:par><p:cTn id="{next(ids)}" presetID="10" presetClass="entr" presetSubtype="0" '
        f'fill="hold" grpId="0" nodeType="{node}"><p:stCondLst><p:cond delay="0"/></p:stCondLst>'
        f'<p:childTnLst>'
        f'<p:set><p:cBhvr><p:cTn id="{next(ids)}" dur="1" fill="hold"><p:stCondLst>'
        f'<p:cond delay="0"/></p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl>'
        f'<p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
        f'<p:to><p:strVal val="visible"/></p:to></p:set>'
        f'<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{next(ids)}" dur="300"/>'
        f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>'
        f'</p:childTnLst></p:cTn></p:par>'
    )


def timing(groups, text_ids):
    counter = iter(range(3, 10_000))
    clicks = []
    for g in groups:
        inner = "".join(effect(counter, spid, i == 0) for i, spid in enumerate(g))
        clicks.append(
            f'<p:par><p:cTn id="{next(counter)}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/>'
            f'</p:stCondLst><p:childTnLst><p:par><p:cTn id="{next(counter)}" fill="hold"><p:stCondLst>'
            f'<p:cond delay="0"/></p:stCondLst><p:childTnLst>{inner}</p:childTnLst></p:cTn></p:par>'
            f'</p:childTnLst></p:cTn></p:par>')
    bld = "".join(f'<p:bldP spid="{i}" grpId="0"/>' for i in text_ids)
    return (
        '<p:timing><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">'
        '<p:childTnLst><p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" '
        f'nodeType="mainSeq"><p:childTnLst>{"".join(clicks)}</p:childTnLst></p:cTn>'
        '<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond>'
        '</p:prevCondLst><p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/>'
        '</p:tgtEl></p:cond></p:nextCondLst></p:seq></p:childTnLst></p:cTn></p:par></p:tnLst>'
        + (f'<p:bldLst>{bld}</p:bldLst>' if bld else '') + '</p:timing>'
    )


def main():
    deck, spec_path, ph_path = sys.argv[1], sys.argv[2], sys.argv[3]
    spec = json.load(open(spec_path))
    ph_names = json.load(open(ph_path))
    done = 0
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(deck) as z:
            names = z.namelist()
            z.extractall(tmp)
        for n, slide in enumerate(spec["slides"], 1):
            groups = slide.get("builds") or []
            if not groups:
                continue
            path = os.path.join(tmp, "ppt", "slides", f"slide{n}.xml")
            xml = open(path, encoding="utf-8").read()
            # Layout placeholder indexes, ascending, pair with the master's declared names.
            rels = open(os.path.join(tmp, "ppt", "slides", "_rels", f"slide{n}.xml.rels")).read()
            layout = re.search(r'Target="\.\./slideLayouts/(slideLayout\d+\.xml)"', rels).group(1)
            lxml = open(os.path.join(tmp, "ppt", "slideLayouts", layout), encoding="utf-8").read()
            idxs = sorted({int(i) for i in re.findall(r'<p:ph[^>]*idx="(\d+)"', lxml)})
            name_of_idx = dict(zip(idxs, ph_names[n - 1]))
            # shape name -> (id, is text shape): images by build_deck.js objectName,
            # placeholders as "ph:<name>" through their index.
            shapes = {}
            for m in re.finditer(r'<p:(sp|pic)>.*?</p:\1>', xml, re.S):
                c = re.search(r'<p:cNvPr id="(\d+)" name="([^"]*)"', m.group(0))
                if not c:
                    continue
                ph = re.search(r'<p:ph[^>]*idx="(\d+)"', m.group(0))
                if m.group(1) == "sp" and ph and int(ph.group(1)) in name_of_idx:
                    shapes[f"ph:{name_of_idx[int(ph.group(1))]}"] = (c.group(1), True)
                else:
                    shapes[c.group(2)] = (c.group(1), m.group(1) == "sp")
            ids, text_ids = [], []
            for g in groups:
                row = []
                for nm in g:
                    full = nm if ":" in nm else f"ph:{nm}"
                    if full not in shapes:
                        sys.exit(f"add_slide_builds: slide {n} has no shape named {full!r}")
                    spid, is_text = shapes[full]
                    row.append(spid)
                    if is_text:
                        text_ids.append(spid)
                ids.append(row)
            xml = re.sub(r"<p:timing>.*?</p:timing>", "", xml, flags=re.S)
            t = timing(ids, text_ids)
            if "</p:clrMapOvr>" in xml:
                xml = xml.replace("</p:clrMapOvr>", "</p:clrMapOvr>" + t, 1)
            else:
                xml = xml.replace("</p:cSld>", "</p:cSld>" + t, 1)
            open(path, "w", encoding="utf-8").write(xml)
            done += 1
        out = deck + ".builds"
        names.sort(key=lambda x: (x != "[Content_Types].xml", x))
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for nm in names:
                p = os.path.join(tmp, nm)
                if os.path.isfile(p):
                    z.write(p, nm)
        shutil.move(out, deck)
    print(f"add_slide_builds: click builds written on {done} slide(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
