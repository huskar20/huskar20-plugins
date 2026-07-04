# ATS playbook — mechanics and hard-won lessons

Field-tested notes per applicant-tracking system. Read before the first apply of
each run; consult again when a form misbehaves.

## Greenhouse (`job-boards.greenhouse.io`, embedded on company sites)

- **MyGreenhouse autofill is the fast path.** If the user has applied via
  Greenhouse before in this Chrome profile, clicking Apply shows "Autofilled from
  MyGreenhouse" — contact fields AND the cached resume attach automatically.
  Verify the resume chip appears, fill the remaining dropdowns, submit. When a
  role is posted on both Greenhouse and another ATS, prefer Greenhouse for this
  reason.
- **Email verification codes:** some boards email an 8-character security code to
  confirm the submission. Search Gmail for the code (`from:greenhouse` or the
  literal subject "Security code"), type it into the code boxes, resubmit. This
  is a normal part of the flow, not a captcha — completing it is fine.
- **Embedded cross-origin iframes** (Greenhouse form inside a company's own
  careers page): react-select dropdowns inside the iframe sometimes refuse
  synthetic clicks (menu never opens). Try the standalone
  `job-boards.greenhouse.io` URL for the same job; if none exists and required
  dropdowns won't open, flag for manual apply — don't fight it.

## Ashby (`jobs.ashbyhq.com`)

- **Resume upload is the recurring blocker.** Ashby caches resumes per company
  workspace; a company the user never applied to has nothing cached, and the
  `file_upload` tool only accepts files the user has shared with the session —
  local filesystem paths are rejected. When upload is blocked: fill every other
  field (contact, work auth, EEO), then flag the role for the user to attach the
  resume and click Submit (include the exact URL). If the resume was shared into
  the session (attachment/uploads folder), `file_upload` works — try that first.
- Location fields are typeahead comboboxes: type the city, wait for the dropdown,
  click the correct option — don't just type-and-tab.
- Yes/No toggles and consent widgets (e.g. AI-notetaker consent) are custom
  components; screenshot after clicking to verify state.

## LinkedIn Easy Apply

- Multi-step wizard; the user's LinkedIn profile pre-fills most of it. Resume:
  LinkedIn keeps previously-uploaded resumes — select the right one rather than
  re-uploading.
- Some employers append NDAs or agreements as a final step — that's an unusual
  legal attestation: in `auto` mode, stop and ask the user before accepting.
- "Responses managed off LinkedIn" postings just link out to the company ATS —
  follow the link and use the ATS playbook section instead.

## Lever (`jobs.lever.co`)

- Simple single-page forms; standard `file_upload` rules apply (session-shared
  files only). No account needed. Watch for "Full remote in <country>" location
  restrictions in the title.

## Workday / iCIMS / SmartRecruiters / Workable

- Usually require account creation. If Google SSO is offered and allowed by
  config, use it; password-only signup → flag for manual apply. Workday flows
  are long (6+ pages) — verify each page committed before advancing.

## Cross-ATS rules

- **Captcha / 2FA anywhere → stop, flag, never solve or bypass.**
- **The form is the truth, the listing lies:** forms reveal hidden onsite
  requirements, citizenship demands, or consent clauses the listing omitted.
  Any contradiction with the profile's filters → do not submit; flag with
  specifics.
- Screenshot the review page before submit and the confirmation page after —
  both go in the run record.
- Salary fields: follow the profile's compensation section exactly (blank/
  "Negotiable" when optional; the profile's numbers when required).
- Demographic/EEO sections: use the profile's recorded defaults; anything the
  profile doesn't cover stays unanswered ("Decline to self-identify" where
  offered).
