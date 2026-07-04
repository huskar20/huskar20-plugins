# Writing a row to the Applications tab (worked example)

Google Sheets has no reliable DOM-append, so drive it like a user: jump to the
first empty cell with the **Name Box**, then type values separated by `Tab`.
Empty columns are just a `Tab` with no typing. Finish the row with `Enter`.

The Name Box is the small cell-reference field at the top-left of the grid (it
shows the current cell, e.g. `A1`), at roughly `(45, 115)` at default zoom —
click it, `cmd+a` (or `ctrl+a` on Windows/Linux), type the target cell, `Enter`.

## Example: append entry #21 at row 23

Column order here follows the default schema (see the setup skill's
`tracker-schema.md`) — **verify against the live header row first**, the owner
may have inserted columns.

```json
[
  {"name":"computer","input":{"action":"left_click","coordinate":[45,115],"tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"cmd+a","tabId":TAB}},
  {"name":"computer","input":{"action":"type","text":"A23","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Enter","tabId":TAB}},
  {"name":"computer","input":{"action":"type","text":"21","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"type","text":"Acme Corp","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"type","text":"Senior Data Engineer","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"type","text":"Remote - United States","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"type","text":"Remote","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"type","text":"Direct","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"type","text":"https://…","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"type","text":"Jun 17, 2026","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"type","text":"Jun 17, 2026","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"type","text":"Applied","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Tab","tabId":TAB}},
  {"name":"computer","input":{"action":"type","text":"Applied","tabId":TAB}},
  {"name":"computer","input":{"action":"key","text":"Enter","tabId":TAB}},
  {"name":"computer","input":{"action":"screenshot","tabId":TAB}}
]
```

Replace `TAB` with the real numeric tab id. One row per batch; read the
screenshot to confirm placement before the next row. If the active cell after
`Enter` isn't where you expect, re-anchor via the Name Box rather than guessing.

## Writing the Notes column

Long notes are easiest written directly: Name Box → `T<row>` → type → `Enter`.
**Count your Tabs carefully** when tabbing across blank columns — landing the
note one column early (e.g. in Next Step Date) is the classic mistake; if it
happens, cut the cell (`cmd+x`), Name-Box to the right cell, paste.

To APPEND to an existing note without retyping it: Name Box → `T<row>` → `F2`
(edit mode, cursor in cell) → `cmd+Right` (jump to end) → type ` | <new note>` →
`Enter`.

## Tips

- Dropdown values (Mode/Stage/Status) commit fine on `Tab`. Off-list values get
  a soft red validation flag — acceptable.
- If a typed date shows as left-aligned text, it still reads fine; don't fight
  cell formatting.
- Autocomplete sometimes offers a previous value mid-type; if the cell commits
  the wrong text, re-anchor and retype rather than arrow-key fixing.
- Only ever write to the `Applications` tab.
