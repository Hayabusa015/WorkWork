#!/usr/bin/env python3
"""Add click-by-click entrance builds to a .pptx, driven by shape names.

pptxgenjs cannot write animation. A deck script names each object it wants revealed
"c<N>_<anything>"; this script finds those names on every slide and writes PowerPoint timing
XML so that click N fades in every object tagged N (the first with the click, the rest with
it). Objects named c0_* or anything else are always visible.

    python3 scripts/add_click_builds.py deck.pptx [builds.json]   # rewrites in place, then repacks

pptxgenjs drops objectName on placeholder text, so placeholder builds come in a side file:
[{"slide": 8, "idx": 110, "click": 1}, ...] - the slide number and the placeholder idx the
layout gave it.

Entrance only, by design: a static render or a printout shows every object, so an object that
leaves on a later click would print on top of whatever replaced it. A deck that needs a
"before and after" uses two slides.
"""
import re, sys, os, zipfile, shutil, tempfile, subprocess

NAME = re.compile(r'<p:cNvPr id="(\d+)" name="c(\d+)_[^"]*"')


def timing(groups, text_ids):
    ctn = [2]
    def nid():
        ctn[0] += 1
        return ctn[0]
    clicks = []
    for click in sorted(groups):
        effects = []
        for i, spid in enumerate(groups[click]):
            node = "clickEffect" if i == 0 else "withEffect"
            effects.append(
                f'<p:par><p:cTn id="{nid()}" presetID="10" presetClass="entr" presetSubtype="0" fill="hold" '
                f'grpId="0" nodeType="{node}"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
                f'<p:set><p:cBhvr><p:cTn id="{nid()}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/>'
                f'</p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst>'
                f'<p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr><p:to><p:strVal val="visible"/>'
                f'</p:to></p:set><p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{nid()}" dur="400"/>'
                f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect></p:childTnLst></p:cTn></p:par>')
        outer, inner = nid(), nid()
        clicks.append(
            f'<p:par><p:cTn id="{outer}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst>'
            f'<p:childTnLst><p:par><p:cTn id="{inner}" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst>'
            f'<p:childTnLst>{"".join(effects)}</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>')
    bld = "".join(f'<p:bldP spid="{s}" grpId="0"{"" if s in text_ids else " animBg=\"1\""}/>'
                  for c in sorted(groups) for s in groups[c])
    return ('<p:timing><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">'
            '<p:childTnLst><p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq">'
            f'<p:childTnLst>{"".join(clicks)}</p:childTnLst></p:cTn><p:prevCondLst><p:cond evt="onPrev" delay="0">'
            '<p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst><p:nextCondLst><p:cond evt="onNext" delay="0">'
            '<p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq></p:childTnLst></p:cTn></p:par>'
            f'</p:tnLst><p:bldLst>{bld}</p:bldLst></p:timing>')


def process(xml, ph_builds=()):
    groups = {}
    for spid, click in NAME.findall(xml):
        if int(click) > 0:
            groups.setdefault(int(click), []).append(spid)
    for b in ph_builds:
        m = re.search(r'<p:cNvPr id="(\d+)"[^>]*>(?:(?!</p:nvSpPr>).)*?<p:ph\s[^>]*idx="%d"' % b["idx"], xml, re.S)
        if not m:
            raise SystemExit(f"placeholder idx {b['idx']} not found on slide {b['slide']}")
        groups.setdefault(int(b["click"]), []).insert(0, m.group(1))
    if not groups:
        return xml, 0
    if "<p:timing>" in xml:
        raise SystemExit("slide already has timing XML; refusing to merge two animation sequences")
    # Objects carrying a text body animate by paragraph in PowerPoint unless marked otherwise;
    # shapes without text need animBg.
    text_ids = set()
    for m in re.finditer(r'<p:sp>.*?</p:sp>', xml, re.S):
        idm = re.search(r'<p:cNvPr id="(\d+)"', m.group(0))
        if idm and "<a:t>" in m.group(0):
            text_ids.add(idm.group(1))
    t = timing(groups, text_ids)
    xml = xml.replace("</p:clrMapOvr>", "</p:clrMapOvr>" + t, 1) if "</p:clrMapOvr>" in xml \
        else xml.replace("</p:sld>", t + "</p:sld>", 1)
    return xml, sum(len(v) for v in groups.values())


def main(path, side=None):
    import json
    builds = json.load(open(side)) if side else []
    tmp = tempfile.mktemp(suffix=".pptx")
    total, slides = 0, 0
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if re.match(r"ppt/slides/slide\d+\.xml$", item.filename):
                num = int(re.search(r"slide(\d+)\.xml", item.filename).group(1))
                xml, n = process(data.decode("utf8"), [b for b in builds if b["slide"] == num])
                if n:
                    total += n; slides += 1
                    data = xml.encode("utf8")
            zout.writestr(item, data)
    shutil.move(tmp, path)
    print(f"click builds: {total} objects on {slides} slides")
    repack = os.path.join(os.path.dirname(os.path.abspath(__file__)), "repack_pptx.py")
    r = subprocess.run([sys.executable, repack, path], capture_output=True, text=True)
    sys.stdout.write(r.stdout)


if __name__ == "__main__":
    main(*sys.argv[1:3])
