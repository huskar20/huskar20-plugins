# Writing a formatted resume into Google Drive

How to get a correctly formatted Google Doc out of the Drive connector. These
notes come from failures observed in practice — follow them rather than
rediscovering them.

## Use the HTML route, not base64 .docx

The Drive connector's `create_file` accepts either `textContent` (plain text) or
`base64Content` (binary). Both convert to a Google Doc. **Use HTML via
`textContent`.**

```
create_file(
  title            = "SoftwareEngineer_AlexMoreno",
  parentId         = <folder id>,
  contentMimeType  = "text/html",
  textContent      = <the HTML>
)
```

### Why not .docx

Uploading a `.docx` as base64 is unreliable at any nontrivial size:

- A payload large enough to matter fails outright with `Request contains an
  invalid argument`, and fails **deterministically** — retrying the identical
  payload reproduces the error.
- Worse, a payload can succeed while **silently corrupting a character**. An
  observed case turned `linkedin.com` into `linxedin.com` in a finished resume.
  A single wrong byte inside the compressed stream survives to the document.

Both failure modes are invisible unless the result is read back. HTML is plain
text, is far more compact for the same content, and degrades gracefully — a
transcription slip yields a small visual glitch instead of a corrupt file.

## Google Docs ignores some CSS on import — set the font afterward

Docs' HTML importer applies class-based CSS reliably but **drops
`font-family` declared on element selectors** (`p { font-family: Calibri }`).
Documents silently land in Arial.

Two options, in order of preference:

1. Put `font-family` inside every generated class, not on a bare element
   selector.
2. After creating the file, open it and set the font explicitly: select all
   (Cmd/Ctrl+A) → font dropdown → Calibri.

Always verify. A resume template that teaches typography must not itself be in
the wrong font.

## Structuring the HTML

Emit one `<style>` block of numbered classes and reference them per paragraph.
This is exactly what Google Docs' own HTML export does, so the importer handles
it well, and it keeps the payload small.

```html
<meta charset="utf-8"><style>
@page{size:8.5in 11in;margin:0.75in}
p{margin:0}
.k0{font-family:Calibri,sans-serif;font-size:20pt;text-align:center;
    margin-top:0pt;margin-bottom:2pt;font-weight:bold}
</style>
<p class="k0">FIRST LAST</p>
```

- Express gaps as `margin-bottom` in points — that becomes paragraph spacing.
- `line-height:1.0` on every class.
- Bullets: `margin-left:0.18in; text-indent:-0.18in` with a literal `•` and
  non-breaking spaces. Do **not** use `<ul>`/`<li>` — Docs converts those into
  real list objects that resist the exact indent values.
- `&nbsp;` for the separators in the contact line so they don't collapse.

## What HTML import cannot do

**Right-aligned tab stops.** There is no CSS for a right tab stop, so
`Job Title, Company` … `Mon Year – Present` cannot be flush-right from HTML.

Options, in order of preference:

1. Generate the document, then set the tab stop in the Doc (or tell the user it
   is the one manual touch-up).
2. Separate the two with non-breaking spaces and accept left flow.
3. **Never** use a two-column table to fake it — that breaks ATS parsing, which
   is the whole point of the format.

Say which one was used rather than leaving the user to notice.

## Always read the document back

After creating or editing, call `read_file_content` on the new file and compare
against the intended text. This is the only way to catch a silent corruption or
a dropped line. Do it every time; it costs one call.

## Editing an existing Doc

The Drive connector has **no update, rename, move, or delete tool** — only
`create_file`, `copy_file`, and readers. Consequences:

- To change a Doc, either create a new one, or edit it in the browser through
  the Chrome extension. Prefer browser editing for small changes; re-uploading
  creates a duplicate you cannot remove through the connector.
- When editing in the browser, note that literal `•` + tab bullets are plain
  text: a triple-click selects the bullet character too, so retype it or select
  only from after the tab.
- Verify with `read_file_content` afterward, not by eye.

## Exporting the PDF

Google Docs → File → Download → PDF Document, saved as
`JobTitle_FirstNameLastName.pdf`. The PDF is what employers receive; it locks
the formatting so nothing shifts on their screen. Never share the editable Doc
with a recruiter.
