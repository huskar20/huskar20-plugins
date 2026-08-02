# Resume Forge

Build, tailor, and review resumes in a single-column, ATS-safe house style.
Generates a formatted **Google Doc** master, aims a copy at a specific job
posting, and audits any resume against a pre-submission checklist.

Works standalone. If the [`career-hunter`](../career-hunter) plugin is also
installed, Resume Forge reads its `career-profile.md` so you don't re-enter
your contact details and target titles.

## What's inside

| Skill | Invoke with | What it does |
|---|---|---|
| **build** | "build my resume" | Reads an existing resume (`.docx`, `.pdf`, `.md`, `.txt`, or pasted text) **or** interviews you from scratch → writes a formatted Google Doc named `JobTitle_FirstNameLastName`. |
| **tailor** | "tailor my resume to this job" | Takes a job description → rewrites the target title line, reorders bullets and skill categories, aligns wording with the posting, and reports keyword coverage as a table. Always produces a new copy; never edits your master. |
| **review** | "review my resume" | Audits a resume against a 35-item checklist and reports quoted, concrete findings: passive bullets, missing metrics, tense drift, ATS-breaking layout, filler words, misspelled tool names, length problems. |

## The format it produces

Calibri throughout, US Letter, 0.75" margins, single column. No tables, text
boxes, columns, or horizontal rules — those are what actually break applicant
tracking parsers.

- Name 20pt bold, centered, in title case
- City/State, then a one-line contact block
- **Target job title line**, 16pt bold — the job you want, not the one you have
- Summary with **no section header**, flowing straight out of the title line
- Underlined ALL-CAPS section headers at 11pt; 11pt body throughout
- Skills grouped by category, never a flat wall of tool names (TECHNICAL SKILLS on
  technical resumes, CORE COMPETENCIES elsewhere)
- Experience with dates flush right, verb + tool + result, one line per bullet
- Projects: name only, tools inside the bullets where they carry evidence
- Bullet glyphs scale with length: short resumes use plain titles with `•` details;
  longer ones use `•` on titles and `-` on details
- One page under five years of experience

Full spec: [`skills/build/references/house-style.md`](skills/build/references/house-style.md).

## Download the blank template

A ready-to-use Word copy of the format, with placeholders instead of content:

**[⬇ Resume_Template_Clean.docx](assets/Resume_Template_Clean.docx)** — 8 KB

Direct link, safe to share with anyone:

```
https://github.com/huskar20/huskar20-plugins/raw/main/plugins/resume-forge/assets/Resume_Template_Clean.docx
```

Open it in Word, Google Docs (File → Open → Upload), or Pages, then type over
the placeholders. It contains no personal data — every field is a placeholder
like `First Last` and `first.last@email.com`.

This is the same format the `build` skill produces, so the two agree: use the
file if you'd rather start from a document, or the skill if you'd rather be
interviewed.

## Download the worked example

A completed one-page resume in the same format, so you can see what the writing
should look like, not just the structure:

**[⬇ SoftwareEngineer_AlexMoreno.docx](assets/SoftwareEngineer_AlexMoreno.docx)** — 9 KB

```
https://github.com/huskar20/huskar20-plugins/raw/main/plugins/resume-forge/assets/SoftwareEngineer_AlexMoreno.docx
```

**Alex Moreno is not a real person.** The name, schools, employers, projects, and
every number in it are invented for illustration. Study how the bullets are
written; do not copy them into your own resume.

It shows the short-resume glyph scheme (plain titles, `•` details), one-line
bullets, `TECHNICAL SKILLS` as the header for a technical field, and the file
naming convention `JobTitle_FirstNameLastName`.

## Requirements

- **Google Drive connector** enabled — required. Creates the Doc.
- **Claude-in-Chrome extension** connected — optional but recommended. Needed to
  edit an existing Doc, fix the font after import, and export a PDF. The Drive
  connector can create files but has no update, rename, or delete tool.

Installing the plugin cannot turn connectors on for you, so every skill checks
before it collects anything: if Drive isn't connected, it stops and tells you,
rather than asking twenty interview questions first.

## About PDFs

The plugin deliberately **does not generate a PDF for you.** Google Docs exports
one in two clicks (File → Download → PDF Document), a stored PDF goes stale the
moment you edit the Doc, and there is no reliable way to place a PDF *into*
Drive from here — the only route is a binary round-trip that has been observed
to silently corrupt characters.

So the Doc is the deliverable. When you want a PDF, the plugin offers to do the
export through Chrome (it lands in your local Downloads folder, not Drive) or
gives you the menu path and the file name `JobTitle_FirstNameLastName.pdf`. Send
the PDF to employers, never the editable Doc.

## Quick start

1. Install the plugin, then restart Claude Code / reload the desktop app so the
   skills register.
2. Say **"build my resume"** — hand over an existing resume, or answer the
   interview.
3. Say **"review my resume"** before you send anything.
4. Say **"tailor my resume to this job"** with a posting pasted in, for each
   application.

## It will not invent anything about you

This is the load-bearing rule, not a disclaimer.

Rewriting "Responsible for monitoring logs" into "Monitored and triaged security
alerts across Splunk and QRadar" is editing — the facts are yours, the sentence
is better. Turning it into "reducing investigation time by 40%" is fabricating
evidence on a document used to get you hired, and you are the one who has to
defend it in the interview.

So:

- Achievements, metrics, scale, employers, dates, credentials, and tools come
  from **you**. Never generated, never rounded up, never inferred from a job
  title.
- Where a bullet would be stronger with a number you don't have, you get
  `[ADD NUMBER]` and a list of every placeholder — not a plausible figure.
- A requirement in a posting that's missing from your resume becomes a
  **question**, never a silent edit.
- No "ATS score" or "match percentage." Nobody here has an employer's actual
  parser, so a number would be invented authority. You get a coverage table you
  can check instead.
- No keyword stuffing, hidden text, or white-on-white. Automated systems detect
  it and it ends the candidacy.

Nothing is sent, shared, or published. Sharing permissions are never changed.
You distribute your own resume.

## Working with career-hunter

`career-hunter` needs a resume PDF and asks you to supply one. Resume Forge
makes it:

1. `build` → the Doc
2. `review` → fix what it finds, then export the PDF
3. Point `career-hunter`'s setup at the PDF
4. `tailor` per posting when a role is worth the extra fifteen minutes

Resume Forge reads `career-profile.md` when it's there, and never writes to it.
