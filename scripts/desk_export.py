#!/usr/bin/env python3
"""Export governance/proposals/*.md as Secretary's Desk documents.

The records are authoritative; this only reads them. Output is a JSON list of
{id, data} objects, one per record, for an ArtifactData batch into the desk's
`proposals` collection. Run: python3 scripts/desk_export.py [out.json]
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROPOSALS = ROOT / "governance" / "proposals"
STATUSES = ["PARTIALLY IMPLEMENTED", "IMPLEMENTED", "APPROVED", "REJECTED", "DEFERRED", "PENDING"]


def strip_md(s):
    return re.sub(r"[*`]", "", s).strip()


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return fm, text[m.end():]


def table(body):
    rows = {}
    for line in body.splitlines():
        m = re.match(r"\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*$", line)
        if m and m.group(1).lower() not in rows:
            rows[m.group(1).lower()] = m.group(2)
    return rows


def status_of(raw):
    up = strip_md(raw).upper()
    for s in STATUSES:
        if s in up:
            return s
    return "UNKNOWN"


def trail(body, key):
    m = re.search(rf"^{key}:\s*(.+)$", body, re.M)
    return m.group(1).strip() if m else ""


def summary_of(rows, body):
    for k in ("reason", "new rule", "proposed rule", "recommendation"):
        if rows.get(k) and not rows[k].lower().startswith("see "):
            return strip_md(rows[k])[:400]
    for para in re.split(r"\n\s*\n", body):
        p = para.strip()
        if p and not p.startswith(("#", "|", "---", ">  ")):
            return strip_md(re.sub(r"^>\s?", "", p, flags=re.M))[:400]
    return ""


def export():
    docs = []
    for f in sorted(PROPOSALS.glob("SHULL-CHG-*.md")):
        text = f.read_text(encoding="utf-8")
        fm, body = frontmatter(text)
        rows = table(body)
        cid = f.name[:14]
        h1 = re.search(r"^#\s+SHULL-CHG-\d+\s*[—-]\s*(.+)$", body, re.M)
        raw_status = fm.get("status") or rows.get("status") or trail(body, "Status")
        decision = fm.get("decided_by") and f"Approved by {fm['decided_by']}" or ""
        decision = strip_md(rows.get("decision") or trail(body, "Decision") or decision)
        docs.append({"id": cid, "data": {
            "id": cid,
            "seq": int(cid[-4:]),
            "title": strip_md(fm.get("title") or (h1.group(1) if h1 else cid)),
            "status": status_of(raw_status),
            "date": strip_md(fm.get("opened") or rows.get("date") or ""),
            "risk": strip_md(rows.get("risk") or "")[:120],
            "affects": strip_md(rows.get("affected courses") or rows.get("affected skills") or "")[:200],
            "summary": summary_of(rows, body),
            "decision": decision[:500],
            "supersedes": strip_md(rows.get("supersedes") or "")[:300],
            "implemented_by": strip_md(rows.get("implemented by") or "")[:200],
            "file": f"governance/proposals/{f.name}",
        }})
    return docs


if __name__ == "__main__":
    docs = export()
    out = json.dumps(docs, ensure_ascii=False, indent=1)
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(out, encoding="utf-8")
        print(f"{len(docs)} records -> {sys.argv[1]}")
    else:
        print(out)
