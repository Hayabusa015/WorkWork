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

def strip_code(path):
    tmp = path + ".tmp"
    with zipfile.ZipFile(path) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
        for it in zi.infolist():
            data = zi.read(it.filename)
            if it.filename.startswith("word/") and it.filename.endswith(".xml"):
                t = data.decode("utf-8")
                n0 = t.count("S3.2")
                t = t.replace("U03 / S3.2", "U03").replace("U03 · S3.2", "U03")
                if n0:
                    print(f"  {os.path.basename(path)} {it.filename}: removed {n0 - t.count('S3.2')} of {n0} code(s)")
                data = t.encode("utf-8")
            zo.writestr(it, data)
    shutil.move(tmp, path)

for p in (stu, key):
    strip_code(p)
print(stu); print(key)
