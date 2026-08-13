---
name: setup
description: One-time Career Hunter onboarding — interview the user about their target role, salary, location, work authorization, and preferences; generate their personal career-profile.md; create the Google Sheets job tracker; and configure automation options. Use when the user says "set up career hunter", "set up my job search", "onboard me", "create my job tracker", or invokes the plugin for the first time (the apply and sync skills also redirect here when no profile exists).
---

# Career Hunter — Setup

Onboard a new user end to end: interview → profile file → tracker spreadsheet →
automation config. Everything the `apply` and `sync` skills need is produced here.
Re-running setup is safe: offer to update the existing profile instead of starting over.

## Outputs (all in the user's working folder)

| File | Purpose |
|---|---|
| `career-profile.md` | Canonical answers for every application form. The user edits it by hand afterward; other skills re-read it every run. |
| `career-hunter-state/config.json` | Spreadsheet ID, resume path, submission mode, caps, schedule, notification prefs. |
| `career-hunter-state/seen_jobs.json` | Created empty; the apply skill's dedupe memory. |
| `career-hunter-state/last_run.json` | Created with null fields; the sync skill's watermark. |

## Step 1 — Check prerequisites

Verify each connector is actually present (list the available tools / connectors,
don't assume), and tell the user plainly what is missing rather than failing
later. A plugin cannot gate its own installation on connectors — this check is
the real gate, so do it thoroughly and stop if a required piece is absent.

1. **Gmail connector** — needed by sync (and apply, for email verification codes).
2. **Google Drive connector** — **creates** the tracker spreadsheet by copying the
   published template (`copy_file`) and **reads** it for dedupe in apply/sync.
3. **Google Calendar connector** — needed so sync can create an event when it
   detects a confirmed interview. If it's missing, say so; the user can still
   proceed (sync will fall back to notification-only) but flag it as a TODO.
4. **Claude-in-Chrome extension, connected** — `list_connected_browsers`; **writes**
   application rows and fills application forms, in the user's own Chrome session.
   Setup itself no longer needs it for the tracker (the template copy brings the
   structure with it), but apply and sync do — there is no Sheets-cell MCP, so
   every cell write goes through Chrome. If it's missing, setup can still finish;
   flag it as a TODO.
5. **Resume file** — ask the user to place their resume PDF in the working folder
   (or a subfolder) and confirm its path. Record it in config. If they don't have
   it ready, continue setup and leave a TODO in the summary.

   **Then smoke-test that the file is actually attachable.** `file_upload` only
   accepts files the user has shared with the session — attachments, the
   session's outputs/uploads folders, or a folder they have connected. A bare
   local path is rejected. Verify once here rather than letting `apply`
   rediscover it on every form:

   - Confirm the path resolves and the file is readable.
   - Confirm it sits somewhere `file_upload` can reach.
   - Record the result as `resume_uploadable: true | false` in config.

   If it is **false**, say so now and offer the fixes: move the resume into a
   folder shared with the session, or attach it to the conversation. Explain the
   consequence plainly — applications on systems with no cached resume will be
   filled but handed back for the user to attach and submit. Do not leave this
   to be discovered mid-run.

   If the user does not have a resume at all, point them at the `resume-forge`
   plugin, which builds one in an ATS-safe format.

If any required connector (Gmail, Drive, Calendar) is not connected, tell the user
exactly which one and how to enable it in their Claude app's connector settings
before the dependent skill will work.

## Step 2 — The interview

Use AskUserQuestion throughout, a few related questions per call, in this order.
Everything here maps to a section of `references/profile-template.md` — read that
template first so answers land in the right places. Never invent an answer the
user didn't give; leave the field marked `TODO (ask owner)` instead.

1. **Identity & contact** — full legal name, email, phone, city/state/zip,
   LinkedIn URL, GitHub/portfolio URL (optional).
2. **Target role** — free-text: what role are they hunting (e.g. "data engineer",
   "senior security engineer", "product manager")? Then confirm:
   - a list of 4–8 acceptable job titles (draft it for them from the role — e.g.
     data engineer → Data Engineer, Senior Data Engineer, Analytics Engineer,
     Data Platform Engineer — and let them edit),
   - level (intern / new-grad / junior / mid / senior / staff / lead) and whether
     management roles are acceptable — intern/new-grad additionally unlocks
     Handshake as a search source in apply; if chosen, ask whether they have a
     school-linked Handshake account (and note their resume should be uploaded
     to their Handshake profile for Quick Apply),
   - 5–10 key skills/keywords from their background for search queries and form
     keyword fields (ask them to list their real stack — do not guess).
3. **Location** — fully remote only? Or also onsite/hybrid within a metro area
   (which one, what radius)? Willing to relocate?
4. **Compensation** — target base, target total comp, and the **auto-skip floor**
   (posted max below which the apply skill never applies). Explain the floor's job.
5. **Work authorization** — authorized to work in-country? Need sponsorship now or
   in future? Citizen? Active security clearance? These are answered verbatim on
   forms and also drive hard skips (e.g. skip roles requiring citizenship or a
   clearance the user lacks).
6. **Availability** — earliest start, notice period, travel tolerance.
7. **Logins** — does the user sign in to LinkedIn/Indeed/ATS sites with
   **Google SSO**, and may the apply skill use "Continue with Google" when a login
   wall appears? (Passwords are never typed or stored regardless.)
8. **Voluntary EEO defaults** (explain these are optional self-identification
   questions on US applications; recording defaults avoids stopping mid-form) —
   gender, Hispanic/Latino, race/ethnicity, disability status, protected-veteran
   status, "how did you hear about us" convention.
9. **Submission mode** — the most important safety question. Present all three
   and say plainly that they differ enormously in cost:
   - **Fully automatic**: the apply skill submits applications without per-form
     confirmation (still bounded by every guardrail). Most expensive.
   - **Review before submit**: fills everything, then stops and asks the user to
     review and click Submit themselves. Similar cost to automatic — the filling
     is what costs, not the submitting.
   - **Prepare only**: never opens a form. Finds and scores roles, then writes
     every answer the user will need — screening answers and a tailored cover
     paragraph — into a queue file to work through by hand. A small fraction of
     the cost of the other two, and a good default for anyone cost-conscious or
     applying to roles that deserve a personal touch.
   Record the choice in config as `submission_mode: "auto" | "review" | "prepare"`.
10. **Caps & cadence** — daily application cap (default 10), per-company cap
    (default 2 per rolling 7 days), which days of the week apply runs are allowed.
11. **Notifications & calendar** — (a) push notification when an interview invite
    is detected? (default yes); (b) push a summary notification after each apply
    run? (default no; record as `push_on_apply`); (c) may sync auto-create a Google Calendar event
    on the user's own calendar for each confirmed interview? (default yes; record
    as `create_calendar_events`). Note it only creates events for interviews the
    user has confirmed, on their own calendar, with no external invitees.

## Step 3 — Write the profile

Fill `references/profile-template.md` with the interview answers and write it to
`career-profile.md` in the working folder. Keep the template's section structure
and its "Never answer / always skip-and-flag" list intact (add any user additions).
Tell the user this file is theirs to edit by hand any time.

## Step 4 — Create the tracker

Ask: create a new Google Sheets tracker, or connect an existing one (paste URL/ID)?

**Creating new — copy the published template. This is the default path and it is
one MCP call.** The template already contains all four tabs, the banners and
fills, the three dropdowns *with* their Status chip colors, and the live Dashboard
formulas. Copying carries all of that over; building the same thing through the
browser takes a couple hundred UI actions and is the most failure-prone step in
setup. Do not build by hand when the copy is available.

**Template file ID:** `11CJOGqPsBG-zgDBd-wu-uQUxMzB1W97ZYl-LTlENFWs`

1. **Copy it — Google Drive MCP `copy_file`:** `fileId: <template id above>`,
   `title: "Job_Search_Tracker_<year>"`. The user only has view access to the
   template, so the copy lands in **their own Drive root** — that is expected;
   tell them where it is rather than hunting for it.
2. **Record it before anything else.** Capture the returned file **id**, build
   `https://docs.google.com/spreadsheets/d/<id>/edit`, and write both to
   `config.json` immediately, so a later failure still leaves a usable sheet.
3. **Verify the copy in one read** (`read_file_content` on the new id): confirm the
   `Applications` tab exists and its row-2 header row matches
   `references/tracker-schema.md`, and check whether **row 3 is empty**.
   - Missing tab, or headers that don't match → the template has been damaged.
     **Build from scratch instead** (fallback below), and say why.
   - Sample rows below the header → the template is dirty but usable. Keep the
     copy; tell the user to delete rows 3+ before the first apply run, since
     apply/sync append after the last populated row.

**Never leave the user with no tracker.** Any failure on the template path — the
copy erroring out, or a copy that lands damaged — means **build it from scratch**,
in the same run, without asking. Say plainly what went wrong and that setup fell
back; don't retry the failing call, and don't stop and wait for the user to fix the
template. The tracker is a hard requirement for every other skill.

**Fallback — build it from scratch.** Full per-tab headers and Dashboard formulas
are in `references/tracker-schema.md`. Reasons this path runs: `copy_file` returned
an error (template deleted, sharing revoked, copying disabled on the template, Drive
permission error), the copy verified as damaged, or the Drive connector isn't
available at all.

**If a bad copy was already recorded in `config.json` at step 2, overwrite both
`spreadsheet_id` and `spreadsheet_url` with the newly built sheet**, and set
`tracker_created_from: "scratch"`. Mention the abandoned copy's URL so the user can
delete it — never delete it yourself.

1. **Create the file — `create_file`:** `title: "Job_Search_Tracker_<year>"`,
   `contentMimeType: application/vnd.google-apps.spreadsheet` (no content needed —
   returns a new blank spreadsheet). Record id and URL in `config.json` now.
2. **Populate the structure — Chrome**, all per `references/tracker-schema.md`:
   - rename the default tab to `Applications`; add its row-1 navy banner and row-2
     white-bold headers (Name Box method in `../sync/references/sheet-writing.md`),
     and the light-green fill on column C (Interview Date);
   - add the **Mode (F)**, **Stage (M)**, and **Status (N)** dropdowns, and set the
     **Status option chip colors** (Active/Interview Scheduling green, Rejected red,
     Withdrawn maroon, Offer purple, Completed gray, Applied gray) — that coloring
     comes from the dropdown, not conditional formatting;
   - add the **Interview Notes**, **Contacts**, and **Dashboard** tabs with their
     banners/headers; on Dashboard, apply the per-card fill colors and enter the
     `COUNTA`/`COUNTIF` formulas exactly as listed so it stays live.
   The apply/sync skills only ever write to `Applications`.
3. **If Chrome isn't connected either:** the spreadsheet still exists (the MCP made
   it), just empty — record it and flag in the summary that its tabs/headers/
   Dashboard need populating in Chrome before apply/sync can use it. (Optional
   shortcut to at least seed the `Applications` header row without Chrome: create
   the file via `create_file` with the 20 column headers as `textContent` CSV and
   `contentMimeType: text/csv`, which converts into a single populated sheet.)

**Connecting existing:** read the sheet via the Drive connector, read its header
row, and record the ID. If its columns differ from the schema, record the actual
header mapping in config — the other skills map by column NAME at runtime anyway.

## Step 5 — Optional scheduling

If the user's Claude app supports scheduled tasks, offer to create:
- an **apply run** on the days chosen in the interview (e.g. Tue/Wed/Thu mornings), and
- a **daily sync** run.
If scheduling isn't available, tell them the manual invocations: "run the job hunt"
(apply) and "sync my job search" (sync).

## Step 6 — Write config and finish

Write `career-hunter-state/config.json`:

```json
{
  "spreadsheet_id": "...",
  "spreadsheet_url": "...",
  "tracker_created_from": "template | scratch | existing",
  "resume_path": "...",
  "resume_uploadable": true,
  "submission_mode": "auto | review | prepare",
  "daily_cap": 10,
  "per_company_cap_7d": 2,
  "apply_days": ["Tue", "Wed", "Thu"],
  "push_on_interview": true,
  "push_on_apply": false,
  "create_calendar_events": true,
  "google_sso_allowed": true,
  "created_utc": "<ISO-8601>"
}
```

Create `career-hunter-state/seen_jobs.json` as `{"last_run_utc": null, "jobs": {}}`
and `career-hunter-state/last_run.json` as
`{"last_run_utc": null, "last_run_date": null, "note": null}`.

Close with a short summary: what was created, where the profile lives, how to edit
it, the two invocation phrases, and any TODOs (missing resume, unanswered fields).
