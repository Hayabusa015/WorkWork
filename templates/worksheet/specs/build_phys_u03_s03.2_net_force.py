"""One-time build: Physics 3.2 practice set, Net Force (Matt's 7-problem version). Not a precedent.

One in-memory override, for this call only: RAMP["physics"] = 2 warm-up / 3 practice /
1 challenge / 1 multi-topic, because the set has 7 problems and the standard ramp is 2/2/1/1
(6). Same mechanism as build_phys_u03_fbd_problem_set_1.py. No builder file is overridden.
Tier tags are hidden by the spec's "tierTags": false, a builder opt-in (default unchanged).
Name: document_name(..., descriptor="Net Force"), Matt's choice (3.2 has no short-title row)."""
import os, sys
REPO = "/home/user/WorkWork"
WS = os.path.join(REPO, "templates", "worksheet")
sys.path.insert(0, WS); sys.path.insert(0, os.path.join(REPO, "templates"))
from _shull_name import document_name
SPEC = os.path.join(WS, "specs", "phys_u03_s03.2_net_force.json")
OUT = os.path.join(REPO, "output", "physics", "u03")
stu = os.path.join(OUT, document_name("Practice_Set", ["3.2"], 3, descriptor="Net Force"))
key = os.path.join(OUT, document_name("Practice_Set", ["3.2"], 3, descriptor="Net Force", key=True))

import build_worksheet_docx as b
b.RAMP["physics"] = {"warm-up": 2, "practice": 3, "challenge": 1, "multi-topic": 1}
sys.argv = ["build_worksheet_docx.py", SPEC, stu]
assert b.main() == 0
import build_worksheet_key_docx as k
sys.argv = ["build_worksheet_key_docx.py", SPEC, key]
assert k.main() == 0
print(stu); print(key)
