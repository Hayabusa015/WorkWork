#!/usr/bin/env python3
"""Publish standards/ and brand/ to Drive _Brand/Standards/ so Claude Projects can read them.

ONE DIRECTION ONLY. Projects never write back, and nothing in _Brand/Standards/ is
authoritative - this repository is. The Drive copy is a published rendering.

This script does not call Drive itself; it produces the upload plan the Librarian
executes, so every write still goes through the Librarian's log-then-verify
protocol rather than around it.

    python3 scripts/publish_standards.py            print the plan
    python3 scripts/publish_standards.py --json     machine-readable
"""
import json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = json.load(open(os.path.join(REPO, "config", "drive.json")))["brand"]["children"]["Standards"]

PUBLISH = [
    "standards/ANTI_AI_SLOP_STANDARD.md",
    "standards/VOICE.md",
    "standards/NAMING.md",
    "standards/DRIVE_ARCHITECTURE.md",
    "standards/QA_GATE.md",
    "brand/SHULL_DESIGN_SYSTEM.md",
    "brand/tokens.json",
]

def main():
    plan = []
    for rel in PUBLISH:
        path = os.path.join(REPO, rel)
        if not os.path.exists(path):
            print(f"MISSING: {rel}", file=sys.stderr)
            return 1
        plan.append({
            "source": rel,
            "title": os.path.basename(rel),
            "parentId": DEST,
            "bytes": os.path.getsize(path),
            # Without these two, Drive silently converts markdown into a Google Doc
            # and the file stops being diffable.
            "contentMimeType": "text/plain",
            "disableConversionToGoogleType": True,
        })
    if "--json" in sys.argv:
        print(json.dumps({"destination": DEST, "files": plan}, indent=2))
    else:
        print(f"Publish plan → _Brand/Standards/  ({DEST})\n")
        for f in plan:
            print(f"  {f['bytes']:>7}  {f['source']}")
        print(f"\n{len(plan)} files. Hand this to the Librarian — it logs and verifies each write.")
        print("Existing copies are OVERWRITTEN, which needs workflow authorisation.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
