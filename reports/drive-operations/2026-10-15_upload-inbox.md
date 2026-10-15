# Upload Inbox, 2026-10-15

| Operation | Object | ID | Before | After | Status |
|---|---|---|---|---|---|
| Create (by gws, drive.file) | Folder `Upload Inbox` | 1ZDu0cSY2GKMspyboYQUH4t460p1_FYFy | n/a | My Drive root | done |
| Create (by gws) | `gws-upload-test.txt`, 37 bytes | 1b61cyUP3snc7-bwLZ-xw8IWGgrl7byLv | n/a | Upload Inbox | done |
| Move (connector, ID kept) | Folder `Upload Inbox` | 1ZDu0cSY2GKMspyboYQUH4t460p1_FYFy | My Drive root (0AN7jIuczxHMDUk9PVA) | SHULL Science (1FsFiaYfkwgSLnA62bpIHt2zGosFwcPec) | done |
| Trash | `gws-upload-test.txt` | 1b61cyUP3snc7-bwLZ-xw8IWGgrl7byLv | SHULL Science / Upload Inbox | trash (recoverable) | approved 2026-10-15; the guard hook accepted it (manifest in approved-trash/) but Drive refused the connector: "The caller does not have permission". The file was created by the gws app, so only that login (or the user) can trash it. **Not done.** |

Approval to trash `gws-upload-test.txt` was given by the user on 2026-10-15 and recorded as a manifest. The connector cannot trash a file made by the gws app. Trash it from a session that has the gws login, or by hand in Drive.
