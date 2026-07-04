---
name: sync
description: Reconcile the user's Gmail with their Career Hunter job tracker — scan mail since the last sync for application confirmations, rejections, interview invites, and engaged recruiter conversations, then append or update rows in the Google Sheets tracker and push-notify on interview events. Use when the user says "sync my job search", "check my email for job updates", "update the job tracker", "update my tracker from Gmail", or a scheduled sync task fires.
---

# Career Hunter — Sync

Reconcile recent Gmail with the tracker: detect application events from email,
write them into the sheet, notify on interviews.

## Load configuration first

From the working folder (missing → route to `career-hunter: setup`):
- `career-hunter-state/config.json` — `spreadsheet_id`, `spreadsheet_url`,
  `push_on_interview`, `create_calendar_events`.
- `career-hunter-state/last_run.json` — `{ "last_run_utc": "...",
  "last_run_date": "YYYY/MM/DD" }`. Missing/unreadable → default to the last
  7 days and say so.
- The user's email address (from `career-profile.md`) — needed to detect replies.

## Workflow

### 1. Search Gmail for the window

Use the Gmail connector `search_threads` with `after:<last_run_date>` plus a
broad OR of application keywords: `application OR applied OR "thank you for
applying" OR recruiter OR "your application" OR candidate OR interview OR
position OR role OR hiring OR offer OR "moving forward" OR "next steps" OR
unfortunately OR assessment`. Request minimal view first to scan snippets
cheaply; pull full content only for threads that look like real events (fall
back to metadata-only if a thread is too large).

### 2. Classify — signal vs. noise

**Keep (real events):**
- Application confirmations ("we received your application") → Stage `Applied`,
  Status `Applied`.
- Rejections ("decided to proceed with other candidates", "unfortunately") →
  Stage `Closed`, Status `Rejected`.
- Interview/next-step invites, availability requests, confirmations,
  reschedules → update Stage/Status/Interview Date/Next Step accordingly.
- Recruiter outreach **only if the user has actually engaged** (see policy).

**Discard as noise (never add rows):**
- Cold recruiter outreach with no reply — especially LinkedIn InMails and
  staffing-agency cold emails.
- Job-board alerts ("You may be a fit for…", posting digests), "your application
  was viewed" notices (no stage change), ATS marketing (e.g. Greenhouse "Dream
  Job"), newsletters, promos.

Sender is the tell: real confirmations come from ATS domains (greenhouse,
ashbyhq, lever, smartrecruiters, workable, icims, workday) or the company;
alerts come from `jobs-noreply@linkedin.com` and digest senders.

**Recruiter-outreach policy:** add a recruiter row only with evidence of
engagement — a SENT reply from the user in the thread, a scheduled call, or the
user saying so. LinkedIn InMail replies happen inside LinkedIn and won't show in
Gmail: when in doubt, skip it and list it in the summary for the user to decide.

### 3. Read the tracker, dedupe, decide writes

Read the sheet via the Drive connector. Build the `(Company, Role)` set and find
the highest entry #. An email about an already-tracked application **updates**
that row (Status, Last Activity, dated note appended to Notes) instead of adding
a new one. Never delete rows; never double-add.

### 4. Write via Chrome

Navigate to the edit URL from config, confirm the `Applications` tab is active,
and use the Name Box method in `references/sheet-writing.md` — one row or one
row-update per `browser_batch`, ending with a screenshot to verify. Re-read the
header row (row 2) first and map columns by NAME; the owner edits the schema by
hand. Notes stay short, factual, dated, appended with ` | `.

### 5. Interview events — calendar + push

For each **confirmed** interview detected this run (a specific date/time the user
has accepted — not a bare invite awaiting scheduling):

- **Calendar** — if `create_calendar_events` is enabled and the Calendar
  connector is available: create an event on the user's **own** calendar (no
  external invitees) titled e.g. `Interview — <Company> (<role/round>)`, at the
  stated local date/time, with the recruiter/contact and JD link in the
  description. **Dedupe:** before creating, check for an existing event at the
  same company+time (a prior sync may have made one); update it on reschedule
  rather than adding a duplicate. If Calendar isn't connected, skip silently and
  note it — the tracker + push still cover the user.

- **Push** — if `push_on_interview` is enabled, send ONE push covering all of
  this run's interview events, most imminent first: `Interview: <Co> <type>
  <day/time>; <Co2> … Details in tracker.`

Rejections and routine confirmations never create events or push.

### 6. Update state and report

Write `last_run.json` with the current timestamp, date, and a `note` field
summarizing what was written/skipped (the next run's context). If the sheet
write could not complete, do NOT advance the state past the unwritten items.

Summarize for the user: rows added, rows updated, noise discarded (grouped),
and anything ambiguous flagged for their call.

## Robustness notes

- Gmail `after:` is day-granular; same-day re-runs re-surface threads — the
  step-3 dedupe is what prevents double entry.
- Email dates are UTC; convert to the user's local day for Applied/Last
  Activity dates.
- The Dashboard tab auto-counts via `COUNTIF`/`COUNTA` over `Applications!…3:180`;
  new rows within that range update it automatically. Only ever write to the
  `Applications` tab — never edit Dashboard, Interview Notes, or Contacts. If a
  logged row would land past row 180, note that the Dashboard ranges need
  widening rather than editing the Dashboard mid-run.
