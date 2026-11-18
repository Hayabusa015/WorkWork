"""Build the Physics 3.2 net-force practice set and its key. No builder file is edited.

The spec has three parts that all belong to S3.2, so `sections` repeats "3.2". The builders
print that span as "S3.2-S3.2" in the footer; this script collapses it to "S3.2" in the
saved files. The filename is taken from document_name() for one section, 3.2, which has no
short title in courses/physics/DECISIONS.md, so the name carries no topic."""
import os, sys, zipfile, shutil
REPO = "/home/user/WorkWork"
WS = os.path.join(REPO, "templates", "worksheet")
sys.path.insert(0, WS); sys.path.insert(0, os.path.join(REPO, "templates"))
from _shull_name import document_name, short_title
SPEC = os.path.join(WS, "specs", "phys_u03_s03.2_net_force.json")
OUT = os.path.join(REPO, "output", "physics", "u03")
topic = short_title("physics", "3.2")            # None today: no row, no topic
stu = os.path.join(OUT, document_name("Practice_Set", ["3.2"], 3, topic=topic))
key = os.path.join(OUT, document_name("Practice_Set", ["3.2"], 3, topic=topic, key=True))

import build_worksheet_docx as b
sys.argv = ["build_worksheet_docx.py", SPEC, stu]
assert b.main() == 0
import build_worksheet_key_docx as k
sys.argv = ["build_worksheet_key_docx.py", SPEC, key]
assert k.main() == 0


def collapse_span(path):
    tmp = path + ".tmp"
    n = 0
    with zipfile.ZipFile(path) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
        for it in zi.infolist():
            data = zi.read(it.filename)
            if it.filename.startswith("word/") and it.filename.endswith(".xml"):
                t = data.decode("utf-8")
                n += t.count("S3.2-S3.2")
                data = t.replace("S3.2-S3.2", "S3.2").encode("utf-8")
            zo.writestr(it, data)
    shutil.move(tmp, path)
    assert n, f"no footer span found in {path}"
    print(f"  {os.path.basename(path)}: footer span collapsed ({n})")


for p in (stu, key):
    collapse_span(p)
print(stu); print(key)
