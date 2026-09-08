#!/usr/bin/env python3
"""Check every agent definition against the authority matrix in governance/GOVERNANCE.md.

Catches the failure mode that matters: an agent whose prose says it may not change
a rule while its tools: line hands it Edit on the whole repository.
"""
import os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTS = os.path.join(REPO, ".claude", "agents")

# Agents that may NOT hold a write tool that can reach authoritative files.
REPORT_ONLY = {"researcher", "janitor", "auditor"}
# Only this agent may hold Edit.
MAY_EDIT = {"secretary", "designer"}
# Drive mutation tools; only the librarian may hold them.
DRIVE_WRITE = ("create_file", "update_file", "copy_file", "trash_file")
MAY_DRIVE_WRITE = {"librarian"}

REQUIRED = ("name", "description", "tools")
errors, notes = [], []

files = sorted(f for f in os.listdir(AGENTS) if f.endswith(".md") and f != "README.md")
if len(files) != 7:
    errors.append(f"expected 7 agents, found {len(files)}: {files}")

for fn in files:
    path = os.path.join(AGENTS, fn)
    text = open(path).read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{fn}: no YAML frontmatter")
        continue
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()

    for key in REQUIRED:
        if key not in fm:
            errors.append(f"{fn}: frontmatter missing '{key}'")

    name = fm.get("name", "")
    if name != fn[:-3]:
        errors.append(f"{fn}: name '{name}' does not match filename")
    if len(fm.get("description", "")) < 80:
        errors.append(f"{fn}: description too thin to route on")

    tools = [t.strip() for t in fm.get("tools", "").split(",") if t.strip()]
    body = text[m.end():]

    if name in REPORT_ONLY:
        if "Edit" in tools:
            errors.append(f"{fn}: report-only agent holds Edit")
        if "Write" in tools and "reports/" not in body:
            errors.append(f"{fn}: holds Write but never scopes it to reports/")
    if "Edit" in tools and name not in MAY_EDIT:
        errors.append(f"{fn}: holds Edit but is not permitted to modify files")
    for dw in DRIVE_WRITE:
        if any(dw in t for t in tools) and name not in MAY_DRIVE_WRITE:
            errors.append(f"{fn}: holds Drive write tool '{dw}'")

    # Every agent must state a limit.
    if not re.search(r"(may not|never|Hard limits|BLOCKED|Authority)", body, re.I):
        errors.append(f"{fn}: states no limit on its own authority")

    notes.append(f"  {name:11} {len(tools):>2} tools   "
                 f"{'report-only' if name in REPORT_ONLY else 'can produce artifacts'}")

print("\n".join(notes))
if errors:
    print("\nFAIL")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("\nOK - all 7 agents match the authority matrix")
