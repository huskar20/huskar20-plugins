---
name: build
description: Create a formatted resume as a Google Doc, either from an existing resume file the user supplies (.docx, .pdf, .md, .txt, or pasted text) or from a guided interview when they are starting from scratch, then hand off PDF export. Use when the user says "build my resume", "make me a resume", "create a resume", "format my resume", "turn this into a resume", "I need a resume", or hands over an old resume and asks for it to be rewritten or reformatted.
---

# Resume Forge — Build

Produce one correctly formatted resume in the house style as a Google Doc. The
Doc is the deliverable and the master copy.

**The rule that outranks everything else in this skill:** never invent an
achievement, metric, scale, employer, date, credential, or tool. Rewriting a
weak sentence into a strong one is the job. Manufacturing evidence is not. See
"Never fabricate" in Step 5 before writing a single bullet.

## Step 1 — Check prerequisites

Do this **before** collecting anything. Nothing is more annoying than answering
a twenty-question interview and then being told Drive isn't connected.

List the available tools and confirm each is actually present — do not assume:

1. **Google Drive connector** — required. Creates the document. Without it there
   is nowhere to put the result: stop, and tell the user to enable it in their
   Claude app's connector settings.
2. **Claude-in-Chrome extension** — optional but recommended. Needed to edit an
   existing Doc, and to export a PDF. If missing, say so and continue; the Doc
   still gets created and the manual steps get handed over at the end.

   It is **not** needed for the font. The `.docx` route sets Calibri on every
   run, so nothing lands in Arial, and `download_file_content` confirms it
   without a browser. Do not tell the user they need Chrome to fix a font.

A plugin cannot gate its own installation on connectors, so this check is the
real gate. Be thorough, and stop if Drive is absent.

## Step 2 — Find the starting material

Ask which the user has, or infer it if they already said:

- **An existing resume** — a path to `.docx`, `.pdf`, `.md`, `.txt`, or text
  pasted into the conversation. Read it and extract everything present.
- **A LinkedIn export or profile text** — treat as an existing resume.
- **Nothing** — run the interview in Step 4.

Also check for `career-profile.md` in the working folder or its parents. That
file is written by the `career-hunter` plugin. If it exists, read it and use it
rather than re-asking; confirm the values instead of collecting them again.
Never write to that file.

**Take only these fields from it — the rest of the file must never reach the
resume:**

| Use | Ignore completely |
|---|---|
| Name, email, phone, city and state | Work authorization, sponsorship, citizenship, security clearance |
| LinkedIn, GitHub, portfolio | Compensation and salary expectations |
| Target titles and level | Availability, start date, notice period |
| | Voluntary/EEO answers — gender, race, disability, veteran status |

That file exists to answer **application forms**, which ask legitimate questions
a resume must never carry. Everything in the right-hand column either invites
discrimination or hands over negotiating position; see the "Never on a resume"
rule in `house-style.md`.

## Step 3 — Load the format

Read `references/house-style.md` in full before producing anything. It carries
every measurement, the section order for each experience level, and the rules
for each block. Do not improvise the format from memory.

Read `references/drive-formatting.md` before touching Drive. It documents the
.docx build route, why HTML cannot carry the format, and the verification steps.

## Step 4 — Collect what is missing

Ask only for what the starting material did not supply. Batch questions; do not
interrogate one field at a time.

Required:

1. **Target job title** — the role being applied for, not the one currently
   held. Drives the title line and the file name. Note whether this is an
   internship.
2. **Years of professional experience** — ask directly; do not infer it from
   dates. This decides the section order and the page budget, and the two orders
   in `house-style.md` produce genuinely different documents. Part-time and
   campus jobs held while studying do not count toward the total.
3. **Contact block** — name, city and state, phone, email, LinkedIn. GitHub or
   portfolio for technical roles. If the email is a nickname or carries a birth
   year, or the LinkedIn URL still has the default random suffix
   (`linkedin.com/in/name-8a2b91354`), say so once: suggest a
   `first.last@gmail.com`-style address and claiming the custom URL (LinkedIn →
   Settings → Public profile) before applications go out. Then build with
   whatever the user confirms — it is their call.
4. **Experience** — for each role: title, organization, city/state, start and
   end dates, and what they actually did.
5. **Education** — institution, degree, dates. GPA only if 3.5+ and within three
   years.
6. **Skills** — grouped into three to five categories. Header is TECHNICAL SKILLS
   on a technical resume, CORE COMPETENCIES otherwise.

Optional, ask once: certifications (including in-progress), projects, languages,
publications, volunteering.

For a student or career changer with thin work history, push on projects,
internships, part-time and campus jobs, and volunteer work. These count and
belong on the page. Ask about coursework last and only if the page still looks
thin after all of those — it is a space filler of last resort, and
`house-style.md` sets the bar it has to clear.

**Then decide the bullet-glyph scheme, and state it before writing.** It is a
document-wide decision like section order, not a per-line choice, and mixing
the two is a defect `review` flags. Count the roles and detail lines collected
above, then pick per `house-style.md`:

- **One page, or fewer than about fifteen detail lines** → titles flush left
  with **no glyph**, details indented with `•`.
- **Two or more pages, or many roles stacked together** → `•` marks the role
  and project title lines, `-` marks the details beneath them.

Borderline, or the user supplied a resume that already uses one scheme
consistently? Keep theirs. Hold whichever you pick for every section of the
document, Education and Projects included.

## Step 5 — Write the content

Follow `house-style.md` for structure, including **the section order for the
experience level established in Step 4** — a student leads with Education, a
mid-career candidate leads with Professional Experience. For the writing itself:

**Bullets** use strong verb + what they did + the tool or method + the result or
scale. Convert everything passive: "Responsible for monitoring logs" becomes
"Monitored and triaged security alerts across Splunk and QRadar." Present tense
for the current role, past for all others.

**Finding numbers.** Most people have them and have not counted. Ask directly:
how many (tickets, users, students, machines, records)? how often (per day, per
semester, per shift)? how much faster (before and after)? how much bigger (a
percentage, or the raw pair)? how many people (team size, people trained)? over
how long (four semesters, two years)? An honest estimate the user can defend is
fine — "roughly 900 tickets," "about 40% fewer escalations."

**Never fabricate.** If a bullet would be stronger with a number and the user
does not have one, write the bullet without it and leave `[ADD NUMBER]` in
place, then list every placeholder in the final summary. Do not guess a
plausible figure, do not round an unknown up, and do not infer scale from job
title. This document is used to get hired; a number the user cannot defend in an
interview is worse than no number. The same applies to tools — never list
something the user did not say they know.

**Keep it one line.** A detail line should fit one line at 11pt across the 7.5"
column, roughly 100 characters. Take a second line only when it carries a number
or tool that would otherwise be cut.

**Do not let it read as machine-written.** No dashes inside a sentence — that is
the loudest generated-prose tell; use a comma, a full stop, or parentheses.
Hyphens are fine at the start of a detail line and in compounds. Do not force a
metric into every bullet, vary bullet length and opening verbs deliberately, and
avoid leveraged / spearheaded / utilized / seamless / robust. `house-style.md`
has the full list.

**The summary** is written last, after every other section exists.

## Step 6 — Create the Google Doc

Write a spec JSON and build a `.docx` with `scripts/build_resume_docx.py`, then
upload it with `base64Content` per `references/drive-formatting.md`. Drive
converts it to a Google Doc.

Before the upload, run the script's `--verify` step from that reference:
reproducing a 4KB payload inside a tool call has corrupted single characters in
practice, and `--verify` catches that before the connector sees it. Do not skip
it because the payload "looks right" — a wrong character is invisible by eye
and can survive all the way into the finished document.

Do **not** hand-write HTML. Page margins and the 7.50" right tab stop cannot
survive the HTML importer, so dates land near the right margin instead of on it
and the page comes out at the wrong width. The script carries the house style —
margins, tab stop, bold dates, and the 1 / 3 / 7 point gaps — so it does not
have to be re-derived per document. It is standard library only and runs the
same on macOS, Windows and Linux.

Ask where it should go. Default to a `Resumes` folder in the user's Drive,
creating it if needed.

Name the Doc `JobTitle_FirstNameLastName`.

The `.docx` route gives a **7.5" column, 540pt**, so a detail line fits about
118 characters and a one-line bullet is comfortable. That is headroom, not
permission: `house-style.md` still sets a one-line target of roughly 100
characters, and that remains the writing goal.

Do not eyeball whether a line fits. `scripts/fit.py` measures against the real
Calibri that Docs renders — `fit.py --col 540 wrap "<line>"` says which lines
spill onto a second line. It needs fontTools and network on first run; without
them, fall back to its documented constants and say estimates were used. The
`pad` mode is only for the HTML fallback, since the `.docx` route uses real tab
stops and needs no padding at all.

Then, in order:

1. **Read the document back** with `read_file_content` and compare against the
   intended text. Silent character corruption is a known failure mode.
2. **Verify the font** actually imported as Calibri; if not, fix it (select all,
   set Calibri) via the browser. `download_file_content` with
   `exportMimeType: "text/html"` verifies this without a browser — every text
   run should carry `font-family:"Calibri"`. The same export reports the real
   margins and column width, so it checks step 4 at the same time.
3. **Check it fits** the page budget — one page under five years of experience.
   If it runs over, tighten wording before shrinking type, and never go below
   10pt.
4. **Check no line wrapped that should not have.** Detail lines are meant to be
   one line, and role and education lines must never wrap, since a wrapped date
   reads as a formatting error.

Get this right before creating the file. The Drive connector has no update,
rename, or delete tool, so a rebuild leaves a duplicate the user has to trash by
hand.

## Step 7 — Report, then offer the PDF

Tell the user:

- A link to the Doc and where it lives
- **Every `[ADD NUMBER]` placeholder left in the document**, quoted with its
  bullet, so they can fill them in
- Anything asked for and not received
- Any format compromise made (for example, dates not flush right because they
  came in through HTML import)
- The workflow: this Doc is the master. Copy it per target role, export a fresh
  PDF per application, and send the PDF rather than the Doc

**On the PDF:** do not generate one as part of the build. Google Docs exports a
PDF in two clicks, a stored PDF goes stale the moment the Doc is edited, and
there is no reliable way to place a PDF *in Drive* from here — the base64
round-trip is the same path that silently corrupts characters. Instead, offer:

- If Chrome is connected and the user wants one, do File → Download → PDF
  Document, and say plainly that it lands in their local Downloads folder, not
  in Drive.
- Otherwise give the exact menu path and the file name
  `JobTitle_FirstNameLastName.pdf`.

Mention that `career-hunter`'s setup asks for a resume PDF path, so a user
running both will want to export once and point that plugin at the file.

Then offer the obvious next step: `review` to audit it, or `tailor` to aim it at
a specific posting.

## Boundaries

- Do not send, share, publish, or change sharing permissions on anything. The
  user distributes their own resume.
- Do not fill in employment gaps, adjust dates, or soften a job title into
  something more senior.
- If the user asks for content that would misrepresent them — a degree not
  finished, a tool never used, a metric invented — say plainly that it goes on a
  document used for hiring and offer the honest version instead.
