---
name: apply
description: Hunt for roles matching the user's career profile and submit applications end to end — searches LinkedIn Jobs, Indeed, and company ATS boards (Greenhouse/Lever/Ashby) in Chrome, filters against career-profile.md, fills and submits forms (or stages them for review, per the user's configured submission mode), logs every application to the Google Sheets tracker, and sends a summary. Use when the user says "run the job hunt", "find me jobs", "apply to jobs", "run career hunter", or a scheduled apply task fires.
---

# Career Hunter — Apply

Hunt for matching roles and submit applications in the user's name, end to end,
within the guardrails below. When a form demands something outside the profile,
the answer is always **skip-and-flag** — a skipped application costs a day; a
wrong or invented answer costs the job.

## Load configuration first

Read from the working folder; if any is missing, stop and route the user to
`career-hunter: setup`:

- `career-profile.md` — single source of truth for every answer. Re-read every
  run; the owner edits it by hand.
- `career-hunter-state/config.json` — spreadsheet ID, resume path,
  **submission_mode** (`auto` = submit without per-form confirmation;
  `review` = fill everything, then stop and let the user review and click
  Submit themselves), daily cap, per-company cap, allowed days, SSO permission.
- `career-hunter-state/seen_jobs.json` — dedupe memory. Schema:

```json
{
  "last_run_utc": "...",
  "jobs": {
    "<normalized company|title>": {
      "disposition": "applied | skipped | flagged | failed | queued-blocked-domain",
      "date": "YYYY-MM-DD",
      "reason": "short note"
    }
  }
}
```

If today is not one of `apply_days` and this is a scheduled run, note that and
stop (a manual "run the job hunt" always proceeds).

## Guardrails (non-negotiable)

1. **Answers come only from `career-profile.md` and the resume.** Never invent,
   round up, or embellish experience, certifications, degrees, or eligibility.
   Free-text answers ("why this company") are built strictly from resume facts +
   the JD.
2. **Honor the profile's "Never answer / always skip-and-flag" list** (SSN/DOB/IDs,
   references, assessments, unusual legal attestations). Abandon the form without
   submitting and list the role in the summary with the reason.
3. **Work-auth/citizenship/clearance questions:** answer exactly as the profile
   states. If a role hard-requires something the profile says the user lacks
   (citizenship, active clearance), skip it entirely.
4. **Logins:** prefer no-account flows. If a login wall appears and config says
   `google_sso_allowed`, use **Continue with Google** — never type or store a
   password. Password-only signup, captcha, or 2FA → skip and flag. Never attempt
   to solve or bypass a captcha.
5. **Stop-and-verify before submit:** on each review page, screenshot and check
   name/email/phone/resume-attached/screening answers. In `review` mode, stop
   here and hand off to the user. After any submit, screenshot the confirmation.
6. **No assessments, no interviews:** never start a coding test, recorded video,
   or scheduling flow. Flag them.
7. **Hidden-requirement check:** application forms sometimes reveal requirements
   the listing hid (mandatory onsite days in another city, citizenship, unusual
   consents). If a form contradicts the profile's location/level/auth filters,
   do NOT submit — flag with what you found.
8. Anything ambiguous about *whether the user would want the job at all* (weird
   comp structure, heavy on-call, relocation-coded "hybrid") → don't apply; flag.

## Workflow

### 1. Domain preflight

Browser site access is granted per domain and varies by session. Probe each
source family with a **standalone** `navigate` call (denials inside
`browser_batch` never prompt the user): `linkedin.com`, `indeed.com`, one ATS
domain (e.g. `job-boards.greenhouse.io`), and `docs.google.com` for the tracker.
A flat denial = that source is unavailable this run; don't retry it. If nothing
is reachable, mark strong candidates `queued-blocked-domain` and tell the user
the fix: site access lives in the Claude app / Chrome extension "Allowed sites"
settings. Retry `queued-blocked-domain` items FIRST on the next run that can
reach them.

### 2. Read the tracker for dedupe

Read the sheet with the Drive connector using `spreadsheet_id` from config.
Build the set of existing `(Company, Role)` pairs and note the highest entry # /
last filled row (data starts at row 3; entry N = row N+2). **Never apply to a
(Company, Role) already in the tracker or in `seen_jobs.json`.** Count this
week's per-company applications for the per-company cap.

### 3. Hunt

Ensure a browser is connected (`list_connected_browsers`; if none, `switch_browser`
and ask the user to click Connect — never fall back to unauthenticated scraping).

Build search queries from the profile's **Titles** list (quote multi-word titles,
OR them together). Search all three source families, newest-first, posted within
the last ~3 days (first run: 14 days):

- **LinkedIn Jobs** — the title query; filters: Remote (user's country) and
  separately the profile's metro area; Experience level matching the profile;
  Date posted: past week.
- **Indeed** — same queries; remote + metro radius; last 3 days.
- **ATS x-ray** — Google/Bing: `site:job-boards.greenhouse.io OR
  site:jobs.lever.co OR site:jobs.ashbyhq.com "<top title>" <2-3 profile
  keywords>` with a recency filter.

Collect candidates as (company, title, location/mode, comp if posted, JD URL,
source). Normalize URLs (strip tracking params) before using as state keys.
Skim each JD enough to score fit.

### 4. Score and select

Score against the profile's target-roles/filters section: title/level match,
skill overlap with the resume, location rule, comp floor, employment type.
Drop hard-filter failures (record as `skipped` with reason). Take the top
matches up to the daily cap. **Quality over volume** — a 6/10 fit does not get
submitted just because the cap has room.

### 5. Apply

For each selected role, follow `references/ats-playbook.md` (per-ATS mechanics,
resume upload limitations, email verification codes, iframe gotchas). In brief:

1. Prefer the company's own ATS posting over LinkedIn/Indeed quick-apply.
2. Fill contact/identity from the profile; upload the resume (see playbook for
   what to do when upload is blocked); answer screening questions per profile.
3. Cover letter: text field → write 3–4 tailored sentences from resume facts +
   the JD; file-upload-only → flag for manual apply.
4. Guardrail 5 verification, then submit (`auto`) or hand off (`review`).
5. A form that errors repeatedly or dead-ends → mark `failed`, move on. Never
   brute-force a live form.

### 6. Log to the tracker

Append one row per submitted application using the Name Box method in
`../sync/references/sheet-writing.md`. Re-read the header row (row 2) and map
by column NAME (the owner may have edited the schema). Values per the schema in
`../setup/references/tracker-schema.md`: Source `LinkedIn`/`Indeed`/`Direct`,
Applied Date + Last Activity = today (`Jul 1, 2026` format), Stage `Applied`,
Status `Applied`, Notes `Auto-applied by Claude <date> — <one-line fit rationale>`.
Verify each row with a screenshot; if the write fails, still record the
application in `seen_jobs.json` (it WAS submitted) and lead the summary with the
unlogged rows.

### 7. State, notify, report

1. Update `seen_jobs.json` with every candidate touched (applied/skipped/
   flagged/failed) and `last_run_utc`. Include a short `run_notes` field with
   anything the next run should know (blocked domains, ATS quirks discovered).
2. If config `push_on_interview`-style notifications are enabled and anything
   was applied or flagged, send one push: `Job hunt: applied to N roles (…).
   M flagged for manual finish.`
3. Report a summary table: applied (company, role, source), skipped + why,
   flagged + why, sources unavailable.

## Robustness notes

- LinkedIn and Indeed rate-limit and A/B their UIs; if a page looks unfamiliar,
  re-read it rather than clicking from memory.
- The tracker dedupe is the last line of defense against double-applying;
  `seen_jobs.json` is the first. Rely on both.
- Titles like "Engineer II" or requirements far below the profile's level are a
  level mismatch — skip, don't stretch.
