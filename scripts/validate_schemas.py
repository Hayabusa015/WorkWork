#!/usr/bin/env python3
"""Check the SHULL OS schemas accept what they should and reject what they must.

A schema nobody validates against is decoration. These cases are the ones that
matter: WORK COMPLETE without a verified location, INCOMPLETE without saying
what is outstanding, a step marked "not required" with no reason, and an
IMPLEMENTED change record with no commit and no verification.

    python3 scripts/validate_schemas.py
"""
import json, os, sys
from jsonschema import Draft202012Validator

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = lambda n: Draft202012Validator(json.load(open(os.path.join(REPO, "schemas", n))))

OK = {"result": "pass"}
STEPS = {"overseer": OK, "designer": OK, "auditor": OK, "librarian": OK, "deployment": OK}
LOC = {"path": "Chemistry/Unit 01 .../Guided Notes/", "fileId": "abc123",
       "verifiedBy": "parentId lookup"}

CASES = [
    # (schema, must_be_valid, label, doc)
    ("task-report.schema.json", True, "complete report with a verified location",
     {"task": "Build notes", "subject": "Chemistry", "deliverable": "Guided notes",
      "steps": {**STEPS, "researcher": OK}, "status": "WORK COMPLETE", "location": LOC}),
    ("task-report.schema.json", False, "WORK COMPLETE with NO location",
     {"task": "Build notes", "subject": "Chemistry", "deliverable": "Guided notes",
      "steps": STEPS, "status": "WORK COMPLETE"}),
    ("task-report.schema.json", False, "INCOMPLETE that does not say what is outstanding",
     {"task": "Build notes", "subject": "Chemistry", "deliverable": "Guided notes",
      "steps": STEPS, "status": "INCOMPLETE"}),
    # T-10, 2026-09-08. The schema accepted both of these until the test built them.
    # A report that ticks WORK COMPLETE over a failed step is the dishonesty the whole
    # file exists to make impossible, and it was possible.
    ("task-report.schema.json", False, "WORK COMPLETE while the auditor FAILED",
     {"task": "Build a deck", "subject": "Chemistry", "deliverable": "Slides",
      "steps": {**STEPS, "auditor": {"result": "fail", "note": "clipped text on slide 6"}},
      "status": "WORK COMPLETE", "location": LOC}),
    ("task-report.schema.json", False, "WORK COMPLETE while the librarian FAILED",
     {"task": "Build a deck", "subject": "Chemistry", "deliverable": "Slides",
      "steps": {**STEPS, "librarian": {"result": "fail", "note": "parentId lookup found another folder"}},
      "status": "WORK COMPLETE", "location": LOC}),
    ("task-report.schema.json", True, "INCOMPLETE WITH a failed step - still legal, and the point",
     {"task": "Build a deck for a section that does not exist", "subject": "Chemistry",
      "deliverable": "Slides",
      "steps": {**STEPS, "overseer": {"result": "fail", "note": "1.9 is not in the decisions file"}},
      "status": "INCOMPLETE", "outstanding": ["Confirm the intended section, 1.1-1.5."]}),
    ("task-report.schema.json", False, "step skipped with no reason given",
     {"task": "Build notes", "subject": "Chemistry", "deliverable": "Guided notes",
      "steps": {**STEPS, "researcher": {"result": "not required"}},
      "status": "WORK COMPLETE", "location": LOC}),
    ("task-report.schema.json", True, "step skipped WITH a reason",
     {"task": "Rename a file", "subject": "Geology", "deliverable": "Rename",
      "steps": {**STEPS, "researcher": {"result": "not required", "note": "no content produced"}},
      "status": "WORK COMPLETE", "location": LOC}),
    ("task-report.schema.json", False, "invalid section code shape",
     {"task": "x", "subject": "Physics", "section": "S2.3", "deliverable": "d",
      "steps": STEPS, "status": "WORK COMPLETE", "location": LOC}),

    ("change-proposal.schema.json", True, "a PENDING proposal",
     {"changeId": "SHULL-CHG-0099", "date": "2026-09-08", "source": "Janitor",
      "currentRule": "x", "proposedRule": "y", "reason": "z", "risk": "low",
      "status": "PENDING"}),
    ("change-proposal.schema.json", False, "IMPLEMENTED with no commit and no verification",
     {"changeId": "SHULL-CHG-0099", "date": "2026-09-08", "source": "Janitor",
      "currentRule": "x", "proposedRule": "y", "reason": "z", "risk": "low",
      "status": "IMPLEMENTED"}),
    ("change-proposal.schema.json", False, "malformed change ID",
     {"changeId": "CHG-99", "date": "2026-09-08", "source": "User",
      "currentRule": "x", "proposedRule": "y", "reason": "z", "risk": "low",
      "status": "PENDING"}),
]

fails = []
for schema, want_valid, label, doc in CASES:
    errs = list(S(schema).iter_errors(doc))
    got_valid = not errs
    mark = "ok " if got_valid == want_valid else "FAIL"
    print(f"  {mark}  {'accepts' if want_valid else 'rejects':>7}  {label}")
    if got_valid != want_valid:
        fails.append(f"{label}: expected {'valid' if want_valid else 'invalid'}, "
                     f"got {'valid' if got_valid else errs[0].message}")

if fails:
    print("\nFAIL"); [print("  -", f) for f in fails]; sys.exit(1)
print(f"\nOK - {len(CASES)} schema cases behave as specified")
