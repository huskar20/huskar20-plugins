---
name: review
description: Audit an existing resume against a pre-submission checklist and report concrete, quoted findings — passive bullets, missing metrics, tense drift, ATS-breaking layout, banned filler words, misspelled tool and certification names, and length problems. Use when the user says "review my resume", "check my resume", "critique this resume", "is my resume any good", "what's wrong with my resume", or asks for feedback before sending an application.
---

# Resume Forge — Review

Audit a resume and report what actually fails. Read-only by default: report
first, offer to fix second.

## Step 1 — Get the resume

Accept a Google Doc link or Drive file, a local `.docx` / `.pdf` / `.md` /
`.txt`, or pasted text. Read the whole document before judging any part of it.

Ask for two things if not obvious, because several checks depend on them:

- **Years of professional experience** — sets the page budget and the section order
- **Target role** — sets whether the title line and skills are aimed correctly

If a target job description is available, say that `tailor` does the
posting-specific comparison, and keep this review about the document itself.

## Step 2 — Run the checklist

Read `references/checklist.md` and work through all 34 items. Check every one;
do not sample. Each is written to be objectively testable against the text.

Some checks need a whole-document view rather than a line-by-line pass:

- **Metric count** — count bullets containing a figure across the entire resume.
  Fewer than four is a strong warning; zero is the most common failure there is.
  The opposite also matters: if nearly *every* bullet ends in a figure, flag it —
  that reads fabricated even when each number is true.
- **Machine-written tells** — these need the whole document too: dash density
  inside sentences, bullets all landing at the same length, repeated opening
  verbs across a role.
- **Tense consistency** — evaluate within each role, not globally. Present tense
  is correct for a current role and wrong for a past one.
- **Page budget** — estimate from content volume if the source is text rather
  than a rendered document, and say the estimate is an estimate.
- **Section order** — depends on the years-of-experience answer from Step 1.

## Step 3 — Report

Group findings by severity, most severe first, in the format shown at the end of
`references/checklist.md`. For every finding: quote the offending text, name why
it fails, and give a concrete rewrite where one applies.

Finish with a count by severity and the single highest-impact fix. If the resume
passes cleanly, say so plainly — do not manufacture findings to look thorough. A
short, honest "three advisory items, nothing blocking" is a better result than a
padded list.

## Step 4 — Offer to fix

Ask before changing anything. If the user says yes:

- Editing a Google Doc requires the browser — the Drive connector has no update
  tool. See `../build/references/drive-formatting.md`.
- Re-verify with `read_file_content` after editing.
- Apply fixes in severity order and report what changed.

## Never fabricate

The checklist will surface bullets that need a number. **Ask the user for it.**
Do not supply a plausible figure, do not infer scale from the job title, and do
not round an unknown quantity up. Leave `[ADD NUMBER]` and list the placeholders.

Do not produce an "ATS score", "resume score", or percentage match. No real
scoring engine is available here, so any number would be invented authority
dressed up as analysis. Concrete findings are more useful and are checkable.
