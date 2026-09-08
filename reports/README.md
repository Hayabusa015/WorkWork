# reports

Output from the Researcher, Janitor, and Auditor. Findings only — no agent applies its own findings.

Also holds `drive-operations/`, the mutation log. **Every Drive mutation is recorded before it
happens**: object ID, prior name, prior parent. A mutation that was not logged cannot be rolled
back.

Audit output uses one format, sorted blocking first, then shortest fix first:

| # | File | Problem | Your action | Time |
|---|---|---|---|---|

Tables, not prose.
