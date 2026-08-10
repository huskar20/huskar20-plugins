# Student Guide — Explore the Career Plugins

Welcome! This is a hands-on walkthrough of two Claude plugins that help you run
a real job search: **resume-forge** (build, check, and tailor your resume) and
**career-hunter** (find roles, prepare or submit applications, and track
everything in a spreadsheet). Budget 30–45 minutes to try everything; each
station stands alone, so do as many as you have time for.

## What you need

- Claude Code (terminal) or the **Claude desktop app**
- A Google account with the **Gmail**, **Google Drive**, and **Google Calendar**
  connectors enabled (Settings → Connectors) — needed for the tracker and sync
- A resume file if you have one (.docx, .pdf, or even pasted text) — no resume
  is fine too, station 1 builds one from scratch
- For career-hunter's browser features: the desktop app with the
  **Claude-in-Chrome extension** connected

## Install (once, ~2 minutes)

**Claude Code (terminal)** — in an interactive `claude` session:

```
/plugin marketplace add huskar20/huskar20-plugins
/plugin install resume-forge
/plugin install career-hunter
```

Then restart Claude Code so the skills register.

**Claude desktop app** — Customize → Plugins → Personal plugins → **+** →
Add marketplace → paste `https://github.com/huskar20/huskar20-plugins` →
Install **Resume forge** and **Career hunter**.

---

## Station 1 — Build a resume (resume-forge)

Say:

> **build my resume**

- Have an old resume? Hand it over (attach the file or paste the text) and it
  gets rewritten into a clean, ATS-safe Google Doc.
- Starting from zero? It interviews you — education, projects, internships,
  part-time work all count — and builds the document from your answers.

It only uses facts you give it. It will never invent experience for you, and
that's a feature: everything on the page is something you can back up in an
interview.

## Station 2 — Get your resume critiqued

Say:

> **review my resume**

You get a concrete, quoted audit against a pre-submission checklist: passive
bullets, missing numbers, tense drift, filler words, misspelled tool names, and
layout choices that break resume-scanning software. Every finding quotes the
actual line it's about, so you can fix things one by one — no vague "make it
pop" advice.

## Station 3 — Tailor it to a real posting

Find a real job posting you'd genuinely apply to (LinkedIn, a company careers
page — anything). Paste the job description and say:

> **tailor my resume for this job**

Watch what it changes: the title line echoes the posting, your most relevant
bullets move to the top, and wording aligns with the posting's own vocabulary.
It finishes with a keyword-coverage table you can verify yourself — which of
the posting's keywords your resume now hits, and which it honestly can't
(because you don't have that experience — see the Station 1 rule).

## Station 4 — Set up your job-search HQ (career-hunter)

Open (or create) a folder to be your job-search workspace, then say:

> **set up career hunter**

This is a one-time interview: target titles, salary floor, location, work
authorization, and how automated you want things to be. It produces:

- `career-profile.md` — your answers, yours to edit by hand any time
- a **Job_Search_Tracker** Google Sheet with Applications, Interview Notes,
  Contacts, and Dashboard tabs

**When it asks for a submission mode, pick `prepare`.** That's the
try-it-safely mode (and the cheapest): the plugin never opens or submits an
application form. More on the modes below.

## Station 5 — Run the hunt

Say:

> **run the job hunt**

In `prepare` mode, the plugin searches LinkedIn Jobs, Indeed, and company
career boards (Greenhouse, Lever, Ashby), scores every role against your
profile, and writes the best matches to a queue file:
`career-hunter-state/prepared/<today>.md`.

Open that file. For each role you'll find the apply link, a one-line "why this
fits you," ready-to-paste answers to the screening questions, and a short cover
paragraph tailored from your resume and the job description. **You** click
apply and paste — the plugin did the research and drafting, you stay in
control of every submission.

## Station 6 — Keep the tracker honest

After you've applied to something (today or any day after), say:

> **sync my job search**

It scans your Gmail for application confirmations, rejections, and interview
invites, and updates the tracker rows to match. Cold recruiter spam and
job-board alert noise are filtered out. When a confirmed interview lands, it
can drop the event straight onto your Google Calendar and send you a push
notification.

---

## The three submission modes (read before leaving `prepare`)

| Mode | What happens | Who clicks Submit |
|---|---|---|
| `prepare` | Never opens a form; writes links + ready-to-paste answers to a queue file | You |
| `review` | Fills each form in your own Chrome, then stops | You |
| `auto` | Fills **and submits** in your name | The plugin |

Change modes any time by editing `submission_mode` in
`career-hunter-state/config.json`. `prepare` is the right choice for this
event and honestly a great default afterward: applications you personally
finish tend to be better applications.

## The safety model (why you can trust this)

- **Nothing is ever invented.** Every form answer comes from your
  `career-profile.md` or your resume. A question the profile can't answer means
  the application is skipped and flagged for you — never guessed.
- **Your sensitive data stays yours.** SSN, date of birth, and government IDs
  are never entered. Passwords are never typed. Captchas are never solved.
  Assessments and video interviews are never started on your behalf.
- **You own every submission.** Even in `auto` mode, applications go out in
  your name — which is exactly why the defaults keep a human click on every
  Submit.

## Troubleshooting

- **"Skill not found"** — restart Claude Code / reload the desktop app after
  installing; skills register on startup.
- **Setup says a connector is missing** — enable Gmail / Drive / Calendar in
  your Claude app's connector settings, then re-run setup.
- **Apply says no browser is connected** — career-hunter's browser features
  need the desktop app with the Claude-in-Chrome extension connected. `prepare`
  mode's search still needs the browser; resume-forge works without it.
- **apply/sync redirect you to setup** — they depend on the profile and config
  that setup creates. Run **"set up career hunter"** first, in your workspace
  folder.

## Take it home

Everything you made today is yours: the resume Google Doc, the tracker sheet,
`career-profile.md`, and the prepared-answers queue. The plugins stay
installed, so tomorrow the loop is just: **run the job hunt** → work the
queue → **sync my job search**. Good hunting!
