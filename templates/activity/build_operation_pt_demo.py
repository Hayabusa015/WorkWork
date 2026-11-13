#!/usr/bin/env python3
"""Build the Operation Periodic Table drag-and-drop classroom demo (one HTML page).

    python3 templates/activity/build_operation_pt_demo.py OUT.html

The page is the printed activity on a screen: the same 25 code-lettered cards and the ? card,
the same 6 x 5 grid with its no-element squares, so the teacher can model a placement in front
of the class. Card data comes from specs/chem_u03_operation_periodic_table.json and nowhere
else; the template holds only layout and behaviour. Published as a claude.ai artifact.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(HERE, "specs", "chem_u03_operation_periodic_table.json")))
keep = ("code", "symbol", "element", "group", "period", "appearance", "mp", "radius", "ie", "en", "ion")
data = {
    "cards": [{k: c[k] for k in keep} for c in spec["cards"]],
    "missing": {k: spec["missing"][k] for k in ("symbol", "element", "group", "period", "mp", "radius", "ie", "en", "ion")},
    "cols": spec["grid"]["columns"], "rows": spec["grid"]["rows"], "ions": spec["columnIons"],
}
page = open(os.path.join(HERE, "web", "operation_periodic_table_demo.template.html")).read()
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "operation-periodic-table.html")
open(out, "w").write(page.replace("__DATA__", json.dumps(data, ensure_ascii=False)))
print("wrote", out)
