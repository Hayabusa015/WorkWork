"""One-time build, SHULL-CHG-0071 Part B. Not a precedent; no builder file is edited.
Overrides: RAMP["physics"] in memory for this call, and the section code removed from the
header chip and the footer of the saved files (U03 only)."""
import os, re, sys, zipfile, shutil
REPO = "/home/user/WorkWork"
WS = os.path.join(REPO, "templates", "worksheet")
sys.path.insert(0, WS); sys.path.insert(0, os.path.join(REPO, "templates"))
from _shull_name import document_name
SPEC = os.path.join(WS, "specs", "phys_u03_fbd_problem_set_1.json")
OUT = os.path.join(REPO, "output", "physics", "u03")
stu = os.path.join(OUT, document_name("Practice_Set", ["3.2", "x"], 3, descriptor="Free-Body Diagrams"))
key = os.path.join(OUT, document_name("Practice_Set", ["3.2", "x"], 3, descriptor="Free-Body Diagrams", key=True))

import build_worksheet_docx as b
b.RAMP["physics"] = {"warm-up": 3, "practice": 4, "challenge": 4, "multi-topic": 1}
sys.argv = ["build_worksheet_docx.py", SPEC, stu]
assert b.main() == 0
import build_worksheet_key_docx as k
sys.argv = ["build_worksheet_key_docx.py", SPEC, key]
assert k.main() == 0

# Any section code: "S3.2", "3.2", "U03 / S3.2", "U03 · S3.7" - in any visible text run.
CODE = re.compile(r"(?:\s*[/·]\s*)?\bS?3\.\d+\b")

def visible_text(xml):
    return " ".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", xml))

def strip_code(path):
    tmp = path + ".tmp"
    left = []
    with zipfile.ZipFile(path) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
        for it in zi.infolist():
            data = zi.read(it.filename)
            if it.filename.startswith("word/") and it.filename.endswith(".xml"):
                t = data.decode("utf-8")
                n = 0
                def fix(m):
                    nonlocal n
                    new, k = CODE.subn("", m.group(2))
                    n += k
                    return m.group(1) + new + m.group(3)
                t = re.sub(r"(<w:t(?: [^>]*)?>)([^<]*)(</w:t>)", fix, t)
                if n:
                    print(f"  {os.path.basename(path)} {it.filename}: removed {n} code(s)")
                left += [(it.filename, x) for x in CODE.findall(visible_text(t))]
                data = t.encode("utf-8")
            zo.writestr(it, data)
    shutil.move(tmp, path)
    assert not left, f"section codes remain in {os.path.basename(path)}: {left}"
    print(f"  {os.path.basename(path)}: no section code remains")

for p in (stu, key):
    strip_code(p)
print(stu); print(key)
