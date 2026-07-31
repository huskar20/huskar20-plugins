---
name: tailor
description: Aim an existing resume at one specific job posting — rewrite the target title line to echo the posting, reorder bullets and skill categories so the most relevant land first, align wording with the posting's own vocabulary, and report keyword coverage as a verifiable table rather than a score. Use when the user says "tailor my resume", "customize my resume for this job", "match my resume to this posting", "I'm applying to this role", or pastes a job description and asks what to change.
---

# Resume Forge — Tailor

Produce a copy of the resume aimed at one posting. The master is never edited in
place — tailoring always yields a new document, because the user will apply to
other roles.

Roughly fifteen minutes of tailoring per application is the highest-return time
in a job search. It is also where fabrication is most tempting: the posting
names something the user lacks, and adding it is one keystroke away. Do not.

## Step 1 — Check prerequisites

Confirm the **Google Drive connector** is present before collecting inputs — the
tailored copy has to land somewhere. List the available tools rather than
assuming; stop and say what is missing if it is absent.

Chrome is optional here but needed to edit an existing Doc or export a PDF.

## Step 2 — Collect both inputs

1. **The resume** — Google Doc link, local file, or pasted text.
2. **The job posting** — pasted text, a URL to fetch, or a file. Get the actual
   text; a job title alone is not enough to tailor against.

Capture the **company name** and **exact job title** as written — both go into
the new file name and the title line.

## Step 3 — Analyze coverage

Read `references/keyword-coverage.md` and follow it. It defines the four
requirement buckets, the four coverage states, and the report format.

The high-value finding is **wording mismatch**: the user has the experience but
describes it differently from the posting. Adopting the posting's exact phrasing
for experience they genuinely have is legitimate and effective. Inventing
experience is not.

## Step 4 — Apply the changes that need no new claims

In order of impact:

1. **Target title line** — rewrite it to echo the posting's own job title.
   Highest-leverage single line on the page.
2. **Summary** — rewrite one or two sentences to speak to what this posting
   actually asks for. Keep it 2–4 sentences and keep every fact true.
3. **Core Competencies** — move the most relevant category to the top, and the
   most relevant items to the front within each category. Do not add items.
4. **Bullet order inside each role** — move the bullet closest to this posting
   to the top of its role. Do not reorder the roles themselves; reverse
   chronological is not negotiable.
5. **Vocabulary alignment** — swap the user's phrasing for the posting's where
   they describe the same real work.

Every one of these is a reordering or a rewording of something already true.
None adds a claim.

## Step 5 — Surface what needs the user

Anything absent from the resume is a **question**, not an edit:

> The posting lists Terraform under required qualifications and it is not on
> your resume. Do you have experience with it? If yes, tell me where and I will
> add it. If no, leave it — a claim you cannot defend in the interview costs you
> more than a missing keyword.

Same for metrics. If the posting asks for measurable impact and the bullets have
no numbers, ask for the numbers. Never generate them.

## Step 6 — Produce the tailored copy

Create a **new** document — never overwrite the master:

- Copy the master, then edit the copy, or generate a fresh Doc per
  `../build/references/drive-formatting.md`
- Name it `JobTitle_FirstNameLastName`, using the posting's job title
- Keep it in the same folder as the master unless told otherwise
- **Read the document back** and verify before reporting

Do not generate a PDF as part of this. Offer it: if Chrome is connected, File →
Download → PDF Document (it lands in local Downloads, not Drive); otherwise give
the menu path and the file name `JobTitle_FirstNameLastName.pdf`.

Re-check the page budget. Tailoring adds words more often than it removes them,
and a resume that silently spills onto a second page is a regression.

## Step 7 — Report

- Coverage table from Step 3
- Every change made, grouped as title line / summary / skills / bullet order
- **Open questions** for absent requirements — listed, not buried
- A link to the new Doc, and the PDF export offer
- An honest sentence on fit. If the posting is a stretch, say so; that is more
  useful than a confident tailoring job that falls apart in a screen

## Boundaries

- Never submit the application. That is `career-hunter`'s job and requires the
  user's explicit submission-mode choice.
- Never edit the master resume in place.
- Never add a skill, tool, employer, date, credential, or metric the user has
  not confirmed.
- Never keyword-stuff — no white text, hidden layers, or trailing keyword dumps.
  Automated systems detect it and it ends the candidacy.
