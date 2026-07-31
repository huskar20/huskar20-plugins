# Career Hunter

End-to-end job-search automation for Claude. Interview once, then let Claude
hunt matching roles, submit applications in your name, and keep a Google Sheets
tracker in sync with your Gmail — for any role type (data engineer, security
engineer, PM, designer…), tuned to your titles, salary floor, location, and
work-authorization answers.

## What's inside

| Skill | Invoke with | What it does |
|---|---|---|
| **setup** | "set up career hunter" | Guided interview → generates your personal `career-profile.md`, creates the Google Sheets tracker from scratch, configures caps/schedule/notifications, and asks the key safety question: fully-automatic submission, or review-each-application-before-submit. |
| **apply** | "run the job hunt" | Searches LinkedIn Jobs, Indeed, and Greenhouse/Lever/Ashby boards for roles matching your profile, scores them, then — depending on your submission mode — submits applications, stages them for your review, or just prepares every answer for you to paste. Logs submissions to the tracker and reports a summary. |
| **sync** | "sync my job search" | Scans Gmail since the last sync for confirmations, rejections, interview invites, and engaged recruiter threads; appends/updates tracker rows; creates a calendar event for each confirmed interview; and pushes a notification when an interview lands. |

## Requirements

- **Claude desktop app** with the **Claude-in-Chrome extension** connected
  (all form-filling and sheet edits happen in your own Chrome, with your own
  logged-in sessions).
- **Gmail**, **Google Drive**, and **Google Calendar** connectors enabled.
- A resume PDF.

> Installing the plugin only adds the skills — it can't turn connectors on for
> you. The first time you run **"set up career hunter,"** setup checks that
> Gmail, Drive, and Calendar are connected and tells you exactly what's missing
> before continuing.

## Quick start

1. Install the plugin (see the marketplace README for terminal vs. desktop steps),
   then **restart Claude Code / reload the desktop app** so the skills register.
2. Open or create a folder to use as your job-search workspace and say
   **"set up career hunter"** — always run setup **first**; the other skills depend
   on the profile and config it creates and will redirect you here if they're missing.
3. Answer the interview (role, titles, salary, location, work auth, EEO defaults,
   submission mode). Setup creates:
   - `career-profile.md` — your answers; edit it by hand any time
   - `career-hunter-state/` — config and run state
   - a `Job_Search_Tracker` Google Sheet with **Applications, Interview Notes,
     Contacts, and Dashboard** tabs
4. Say **"run the job hunt"** to apply, **"sync my job search"** to reconcile
   Gmail with the tracker — or let setup schedule both.

## Submission modes — and what they cost

Setup asks you to pick one. They differ enormously in how many tokens a run
burns, because the expensive part is driving a browser through a form, not
clicking Submit.

| Mode | What happens | Relative cost |
|---|---|---|
| `auto` | Fills and submits in your name | Highest |
| `review` | Fills everything, stops, you review and click Submit | Roughly the same as `auto` — the filling is the cost |
| `prepare` | **Never opens a form.** Finds and scores roles, then writes every answer you'll need — screening answers and a tailored cover paragraph — into `career-hunter-state/prepared/<date>.md` for you to paste | A small fraction |

`prepare` is the right choice if you're cost-conscious, or applying to a handful
of roles that deserve a personal touch. It writes nothing to the tracker — the
Applications tab means "I applied", and the Dashboard funnel depends on that
staying true. Log rows as you work the queue, or run `sync` afterward to pick up
the confirmation emails.

You can change modes any time by editing `submission_mode` in
`career-hunter-state/config.json`.

## About your resume file

`file_upload` can only attach files you've shared with the session — a bare
local path gets rejected. Setup smoke-tests this once and records
`resume_uploadable` in config, so `apply` doesn't rediscover it on every form.

If it comes back false, move the resume somewhere the session can reach or
attach it to the conversation. Otherwise applications on systems with no cached
resume get filled and handed back to you to attach and submit — nothing is ever
submitted without your resume attached.

Greenhouse (MyGreenhouse) and LinkedIn Easy Apply keep a cached resume, so those
work regardless. Ashby caches per company, so the first application to any
company needs a real upload.

No resume yet? The [`resume-forge`](../resume-forge) plugin in this marketplace
builds one in an ATS-safe format.

## Safety model

- Every form answer comes from `career-profile.md` or your resume — nothing is
  ever invented. Unanswerable questions mean the application is skipped and
  flagged, never guessed.
- SSN/DOB/government IDs are never entered. Assessments and video interviews
  are never started. Captchas are never solved. Passwords are never typed —
  only "Continue with Google" SSO, and only if you allowed it in setup.
- "Review before submit" keeps a human click on every submission; "prepare" never
  opens a form at all.
- Applications are sent in your name: even in fully-automatic mode, you own the
  results. Check the tracker and summaries regularly.
