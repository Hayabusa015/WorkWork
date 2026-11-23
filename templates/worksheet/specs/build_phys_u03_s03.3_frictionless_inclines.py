"""Build: Physics 3.3 practice set, Frictionless Inclines (6 problems).

Standard Physics ramp (2/2/1/1), so no override. Tier tags are hidden by the spec's
"tierTags": false (builder opt-in, default unchanged). Binding margin and hole guides come
from the builders by default (SHULL-CHG-0103).
Name: document_name(..., descriptor="Frictionless Inclines") - pending Matt's OK (3.3 has no
short-title row)."""
import os, sys
REPO = "/home/user/WorkWork"
WS = os.path.join(REPO, "templates", "worksheet")
sys.path.insert(0, WS); sys.path.insert(0, os.path.join(REPO, "templates"))
from _shull_name import document_name
SPEC = os.path.join(WS, "specs", "phys_u03_s03.3_frictionless_inclines.json")
OUT = os.path.join(REPO, "output", "physics", "u03")
stu = os.path.join(OUT, document_name("Practice_Set", ["3.3"], 3, descriptor="Frictionless Inclines"))
key = os.path.join(OUT, document_name("Practice_Set", ["3.3"], 3, descriptor="Frictionless Inclines", key=True))

import build_worksheet_docx as b
sys.argv = ["build_worksheet_docx.py", SPEC, stu]
assert b.main() == 0
import build_worksheet_key_docx as k
sys.argv = ["build_worksheet_key_docx.py", SPEC, key]
assert k.main() == 0
print(stu); print(key)
