# Application Profile — {{FULL_NAME}}

Canonical answers for job-application forms. The `career-hunter` apply skill fills
every form **only** from this file and the resume — if an answer isn't here, the
rule is skip-and-flag, never guess. Owner: edit this file freely; the skills
re-read it every run.

## Identity & contact

- **Full name:** {{FULL_NAME}}
- **Email:** {{EMAIL}}
- **Phone:** {{PHONE}}
- **Location:** {{CITY}}, {{STATE}} {{ZIP}}, {{COUNTRY}}
- **LinkedIn:** {{LINKEDIN_URL}}
- **GitHub / portfolio:** {{PORTFOLIO_URL}}
- **Resume file:** {{RESUME_PATH}} (relative to this folder)

## Work authorization (verified with owner {{SETUP_DATE}})

- **Work authorization:** {{WORK_AUTH_ANSWER}}
- **Sponsorship required (now or in future):** {{SPONSORSHIP_ANSWER}}
- **Citizen:** {{CITIZEN_ANSWER}}. {{CITIZENSHIP_SKIP_RULE}}
- **Security clearance:** {{CLEARANCE_ANSWER}}

## Compensation (verified with owner {{SETUP_DATE}})

- **Target:** {{BASE_TARGET}} base / {{TC_TARGET}} total compensation.
- If the form field is optional or accepts text → leave blank or write "Negotiable".
- If a required numeric field asks for **base salary** → `{{BASE_TARGET_NUMBER}}`.
- If it asks for **total comp / OTE / desired salary** (or is ambiguous) → `{{TC_TARGET_NUMBER}}`.
- Don't auto-apply to roles whose posted salary max is below **{{COMP_FLOOR}}**.

## Availability

- **Earliest start date:** {{START_DATE}}
- **Notice period:** {{NOTICE_PERIOD}}
- **Willing to relocate:** {{RELOCATE_ANSWER}}
- **Travel:** {{TRAVEL_ANSWER}}

## Target roles & filters

- **Titles:** {{TITLE_LIST}}
- **Level:** {{LEVEL}}. {{MANAGEMENT_RULE}}
- **Location:** {{LOCATION_RULE}}
- **Employment type:** Full-time direct hire only. Skip contract, C2C, and
  staffing-agency posts for unnamed clients ("our client").
- **Skip:** {{HARD_SKIP_LIST}}

## Experience quick facts (for form fields)

- **Years of experience:** {{YOE_SUMMARY}}
- **Most recent role:** {{RECENT_ROLE}}
- **Degrees:** {{DEGREES}} (Highest level: {{HIGHEST_DEGREE}}.)
- **Certifications:** {{CERTIFICATIONS}}
- **Key skills for keyword fields:** {{KEYWORD_LIST}}
- **"Years of experience with X" answers:** {{YOE_PER_SKILL_LIST}}
  Anything not listed here → skip-and-flag, don't extrapolate.

## Standard voluntary/EEO answers (confirmed by owner {{SETUP_DATE}})

- **Hispanic or Latino:** {{EEO_HISPANIC}}
- **Race / ethnicity:** {{EEO_RACE}}
- **Gender:** {{EEO_GENDER}}
- **Disability (form CC-305):** {{EEO_DISABILITY}}
- **Protected veteran:** {{EEO_VETERAN}}
- **How did you hear about us?:** "LinkedIn", "Indeed", or "Company careers page" —
  whichever matches where the posting was found.

## Never answer / always skip-and-flag

- SSN, date of birth, government ID numbers, driver's license — **never** enter these.
- Reference names/contact info — flag for owner.
- Take-home assessments, HackerRank/CodeSignal links, video-interview recordings
  (HireVue etc.) — never start these automatically; flag with the deadline.
- Legal attestations beyond routine "I certify my answers are true" (e.g. background
  check consent forms with unusual terms, non-compete acknowledgments) — flag.
{{EXTRA_SKIP_ITEMS}}

<!--
Template notes for the setup skill (delete this comment block from the generated file):
- Replace every {{PLACEHOLDER}} with the interview answer, or the literal text
  "TODO (ask owner)" if the user skipped the question.
- {{CITIZENSHIP_SKIP_RULE}}: if not a citizen / no clearance, write the explicit
  rule, e.g. "Skip roles that hard-require citizenship or an active clearance."
- {{HARD_SKIP_LIST}}: build from the interview — adjacent-but-wrong specialties
  the user does NOT want (e.g. for a data engineer: pure DBA, pure BI/reporting
  analyst; for a security engineer: pure GRC, pure red team), plus the
  clearance/citizenship rule when applicable.
- {{YOE_PER_SKILL_LIST}}: only skills the user explicitly gave years for.
-->
