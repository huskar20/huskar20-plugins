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

**Nobody needs Calibri installed.** Docs serves it from `fonts.gstatic.com` to
every document, so the resume and its exported PDF render in real Calibri on any
machine, including one that has never had Microsoft fonts. A local install is
irrelevant to the output, and a local copy is the *wrong* reference to measure
against — what governs line breaks is the font Docs serves, which is what
`scripts/fit.py` downloads.

## Docs also drops `@page` — the document lands at 1" margins

**The importer ignores `@page{margin:0.75in}` entirely.** Every resume created
through this route lands at Google Docs' default 1" margins, giving a **6.5"
text column, not the 7.0" the house style specifies**. Confirmed by exporting a
created Doc back to HTML: the body comes back as `padding:72pt` (1") with
`max-width:468pt` (6.5"), whatever `@page` said.

There is no HTML fix. Keep the `@page` rule anyway for the local preview file,
but never trust it for the Doc, and plan for 6.5" of usable width.

This matters more than it sounds, because **line-length budgets depend on it**.
Measured against the Calibri that Docs actually renders:

| Column | Full line | Detail line (0.28" indent) |
|---|---|---|
| 7.0" (house style, after manual fix) | ~111 chars | ~107 chars |
| **6.5" (what HTML import actually gives)** | **~103 chars** | **~99 chars** |

These are **physical wrap limits, not writing targets.** `house-style.md` sets a
one-line target of roughly 100 characters, and that stays the goal — it is a
style cap, deliberately tighter than what fits. Use the numbers above only to
answer "will this wrap," which is what silently costs a line.

Two options:

1. Tell the user to set margins once in the Doc: File → Page setup → 0.75" on
   all four sides. This restores the real house style, and is the same class of
   one-time touch-up as the tab stop below.
2. Accept 1" margins and size every line for the 6.5" column.

Pick one **before** writing the content, since it sets the line budget, and say
which one was used.

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
<p class="k0">First Last</p>
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

The shipped `.docx` template does this correctly with a real right tab stop at
7.0" (`<w:tab w:val="right" w:pos="10080"/>`). That property has no HTML
equivalent, so it cannot survive this route. Nothing is broken in the template
or the style — the gap is in the transport.

Options, in order of preference:

1. Generate the document, then set the tab stop in the Doc (or tell the user it
   is the one manual touch-up).
2. Separate the two with non-breaking spaces and accept approximate alignment.
3. **Never** use a two-column table to fake it — that breaks ATS parsing, which
   is the whole point of the format.

Say which one was used rather than leaving the user to notice.

### Sizing the non-breaking spaces for option 2

**Do not estimate this by eye — measure it.** `scripts/fit.py` fetches the exact
Calibri that Docs renders and does the arithmetic:

```
python3 scripts/fit.py pad  "Job Title, Company - (City, ST)" "Mon Year - Present"
python3 scripts/fit.py wrap "A detail line, without the bullet glyph"
python3 scripts/fit.py selftest
```

`pad` prints the `&nbsp;` count; `wrap` says which lines spill onto a second
line. Add `--col 504` for a 7.0" column after fixing margins. Run `pad` **once
per line** — role lines vary by 30 characters, so one reused count leaves some
dates near the margin and others stranded mid-line.

Why measuring beats estimating: hand estimates of "average character width" run
about 15% high, which compounds across a 50-character title. In one build that
error left every date **0.4" to 0.9" short of the margin** — no wrapping, but
visibly ragged down the right edge.

If fontTools or the network is unavailable, fall back to these measured
constants and **say that estimates were used**:

| | Width at 11pt |
|---|---|
| `&nbsp;` (space, 0.2261 em) | **2.49pt** |
| average regular character (0.412 em) | 4.53pt |
| average bold character (0.429 em) | 4.72pt |

```
pad = (column_width_pt - bold_chars x 4.72 - date_chars x 4.53) / 2.49 - 2
```

with `column_width_pt` = **468** at Docs' imported 1" margins, 504 at 0.75". The
trailing `- 2` is deliberate: undershoot leaves the date slightly left of flush,
which is cosmetic, while overshoot wraps the line and costs a whole line.

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
