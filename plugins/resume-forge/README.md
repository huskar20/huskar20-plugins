# Resume Forge

Build, tailor, and review resumes in a single-column, ATS-safe house style.
Generates a formatted **Google Doc** master plus a **named PDF**, aims a copy at
a specific job posting, and audits any resume against a pre-submission
checklist.

Works standalone. If the [`career-hunter`](../career-hunter) plugin is also
installed, Resume Forge reads its `career-profile.md` so you don't re-enter
your contact details and target titles.

## What's inside

| Skill | Invoke with | What it does |
|---|---|---|
| **build** | "build my resume" | Reads an existing resume (`.docx`, `.pdf`, `.md`, `.txt`, or pasted text) **or** interviews you from scratch → writes a formatted Google Doc and exports `JobTitle_FirstNameLastName.pdf`. |
| **tailor** | "tailor my resume to this job" | Takes a job description → rewrites the target title line, reorders bullets and skill categories, aligns wording with the posting, and reports keyword coverage as a table. Always produces a new copy; never edits your master. |
| **review** | "review my resume" | Audits a resume against a 27-item checklist and reports quoted, concrete findings: passive bullets, missing metrics, tense drift, ATS-breaking layout, filler words, misspelled tool names, length problems. |

## The format it produces

Calibri throughout, US Letter, 0.75" margins, single column. No tables, text
boxes, columns, or horizontal rules — those are what actually break applicant
tracking parsers.

- Name 22pt bold, centered — the only element above 12pt
- City/State, then a one-line contact block
- **Target job title line**, 12pt bold — the job you want, not the one you have
- Summary with **no section header**, flowing straight out of the title line
- Core Competencies grouped by category, never a flat wall of tool names
- Experience with dates flush right, `•` bullets, verb + tool + result
- Projects: name only, tools inside the bullets where they carry evidence
- One page under five years of experience

Full spec: [`skills/build/references/house-style.md`](skills/build/references/house-style.md).

## Requirements

- **Google Drive connector** enabled — creates the Doc.
- **Claude-in-Chrome extension** connected — recommended. Needed to edit an
  existing Doc, export the PDF, and fix the font after import. The Drive
  connector can create files but has no update, rename, or delete tool.

Installing the plugin cannot turn connectors on for you. If Drive isn't
connected, `build` will say so before it starts collecting your details.

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

1. `build` → Doc + PDF
2. `review` → fix what it finds
3. Point `career-hunter`'s setup at the PDF
4. `tailor` per posting when a role is worth the extra fifteen minutes

Resume Forge reads `career-profile.md` when it's there, and never writes to it.
