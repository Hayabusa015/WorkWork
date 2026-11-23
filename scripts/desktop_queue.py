"""Expose outstanding desktop implementation requests to the next Claude session."""
import subprocess
from pathlib import Path
from repository_desk import RECORD, git, record

MARKER = "Implementation requested via desktop."


def outstanding(root, ref):
    result = subprocess.run(["git", "-C", str(root), "grep", "-l", "-F", MARKER,
                             ref, "--", "governance/proposals"], capture_output=True, text=True)
    if result.returncode not in (0, 1):
        raise ValueError(result.stderr.strip())
    files = result.stdout
    for line in files.splitlines():
        file = line.split(":", 1)[-1]
        if RECORD.fullmatch(file):
            item = record(Path(file), git(root, "show", ref + ":" + file))["data"]
            if item["status"] == "APPROVED" and MARKER in item["decision"]:
                yield file


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    try:
        git(root, "fetch", "--quiet", "origin", "main")
        for file in outstanding(root, "FETCH_HEAD"):
            print("Secretary implementation requested:", file)
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print("Desktop approval queue could not refresh:", exc)
