---
name: build
description: Create a formatted resume as a Google Doc plus a named PDF, either from an existing resume file the user supplies (.docx, .pdf, .md, .txt, or pasted text) or from a guided interview when they are starting from scratch. Use when the user says "build my resume", "make me a resume", "create a resume", "format my resume", "turn this into a resume", "I need a resume", or hands over an old resume and asks for it to be rewritten or reformatted.
---

# Resume Forge — Build

Produce one correctly formatted resume in the house style: a Google Doc master
plus an exported PDF named for the target role.

**The rule that outranks everything else in this skill:** never invent an
achievement, metric, scale, employer, date, credential, or tool. Rewriting a
weak sentence into a strong one is the job. Manufacturing evidence is not. See
"Never fabricate" below before writing a single bullet.

## Step 1 — Find the starting material

Ask which the user has, or infer it if they already said:

- **An existing resume** — a path to `.docx`, `.pdf`, `.md`, `.txt`, or text
  pasted into the conversation. Read it and extract everything present.
- **A LinkedIn export or profile text** — treat as an existing resume.
- **Nothing** — run the interview in Step 3.

Also check for `career-profile.md` in the working folder or its parents. That
file is written by the `career-hunter` plugin and already contains name, email,
phone, city/state, LinkedIn, portfolio, target titles, and level. If it exists,
**read it and use it** rather than re-asking; confirm the values instead of
collecting them again. Never write to that file.

## Step 2 — Load the format

Read `references/house-style.md` in full before producing anything. It carries
every measurement, the section order for each experience level, and the rules
for each block. Do not improvise the format from memory.

Read `references/drive-formatting.md` before touching Drive. It documents the
HTML upload route, the font-import defect, and the tab-stop limitation.

## Step 3 — Collect what is missing

Ask only for what the starting material did not supply. Batch questions; do not
interrogate one field at a time.

Required:

1. **Target job title** — the role being applied for, not the one currently
   held. Drives the title line and the file name.
2. **Contact block** — name, city and state, phone, email, LinkedIn. GitHub or
   portfolio for technical roles.
3. **Experience** — for each role: title, organization, city/state, start and
   end dates, and what they actually did.
4. **Education** — institution, degree, dates. GPA only if 3.5+ and within three
   years.
5. **Skills** — grouped into three to five categories.

Optional, ask once: certifications (including in-progress), projects, languages,
publications, volunteering.

For a student or career changer with thin work history, push on projects,
coursework, internships, part-time and campus jobs, and volunteer work. These
count and belong on the page.

## Step 4 — Write the content

Follow `house-style.md` for structure. For the writing itself:

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

**The summary** is written last, after every other section exists.

## Step 5 — Create the Google Doc

Generate HTML per `references/drive-formatting.md` and create the file with the
Drive connector, `contentMimeType: "text/html"`.

Ask where it should go. Default to a `Resumes` folder in the user's Drive,
creating it if needed. If `career-hunter`'s working folder is in play, offer to
put the PDF where that plugin expects to find it.

Name the Doc `JobTitle_FirstNameLastName`.

Then, in order:

1. **Read the document back** with `read_file_content` and compare against the
   intended text. Silent character corruption is a known failure mode.
2. **Verify the font** actually imported as Calibri; if not, fix it (select all,
   set Calibri) via the browser.
3. **Check it fits** the page budget — one page under five years of experience.
   If it runs over, tighten wording before shrinking type, and never go below
   10pt.

## Step 6 — Export the PDF

Export to PDF as `JobTitle_FirstNameLastName.pdf`. If a browser is connected,
do it via File → Download → PDF Document; otherwise tell the user the exact
menu path.

## Step 7 — Report

Tell the user:

- Links to the Doc and the PDF, and where they live
- **Every `[ADD NUMBER]` placeholder left in the document**, quoted with its
  bullet, so they can fill them in
- Anything asked for and not received
- Any format compromise made (for example, dates not flush right because they
  came in through HTML import)
- The workflow: this Doc is the master, copy it per target role, export a fresh
  PDF per application, and send the PDF rather than the Doc

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
