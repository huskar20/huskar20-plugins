# Pre-submission checklist

Every item is objectively checkable against the document. Report the ones that
fail with the offending text quoted, not a generic warning.

## Blocking — fix before sending

| # | Check | How to test |
|---|---|---|
| 1 | No tables, text boxes, columns, or embedded images | These break ATS parsing; content inside can vanish |
| 2 | Fits the page budget | 1 page for 0–5 years, 2 max beyond. No orphan line alone on the last page |
| 3 | Nothing below 10pt | Body 11pt (10.5pt only to save a page) |
| 4 | One font family throughout | Calibri in this house style; any second family is a defect |
| 5 | Contact block complete | Name, city/state, phone, email, LinkedIn. GitHub for technical roles |
| 6 | No prohibited personal data | Street address, photo, age, DOB, marital status, nationality |
| 7 | No "References available upon request" | Assumed; wastes a line |
| 8 | Every bullet opens with a verb | Flag "Responsible for", "Helped with", "Worked on", "Duties included", "Tasked with" |
| 9 | Tense is consistent | Present for the current role, past for all others, never mixed inside one role |
| 10 | Spelling of tools and certifications | CompTIA not CompTia · CrowdStrike not Crowdstrike · VirusTotal not Virus Total · PostgreSQL not Postgresql · JavaScript not Javascript · GitHub not Github · Kubernetes not Kubernets |

## Strong warnings

| # | Check | Threshold |
|---|---|---|
| 11 | Bullets containing a number | At least four across the whole document. Zero is the single most common failure |
| 12 | Target title line present | Bold, centered, under the contact line, naming the role being applied for |
| 13 | Summary quality | 2–4 sentences, no "I", no banned words: passionate, motivated, hardworking, guru, ninja, self-starter, team player, dynamic |
| 14 | Skills grouped | Bold category labels, not one flat comma-separated wall |
| 15 | Bullet length | One or two lines each. Three lines is a paragraph |
| 16 | Bullets per role | 4–6 for the most recent, 2–3 for older, 1–2 beyond ten years |
| 17 | Section headers standard | "Professional Experience", not "Where I've Worked" |
| 18 | GPA rule | Present only if 3.5+ and within three years of graduation |
| 19 | Section order | Students lead with Education and Projects; 3+ years leads with Experience |
| 20 | Project lines | Name only — no stack list, no printed URL |

## Advisory

| # | Check |
|---|---|
| 21 | Vague quantifiers: "many", "various", "several", "numerous", "etc." |
| 22 | Passive constructions: "was tasked with", "was responsible for" |
| 23 | Filler adjectives with no evidence behind them |
| 24 | Acronyms never expanded — spell out once, e.g. "Security Information and Event Management (SIEM)" |
| 25 | Dead or malformed URLs in the header |
| 26 | Inconsistent date formats between roles |
| 27 | File name is `JobTitle_FirstNameLastName.pdf` |

## Reporting format

Group by severity, most severe first. For each finding give the quoted text, why
it fails, and a concrete rewrite where one applies.

```
BLOCKING — 2 findings

1. Bullet opens with a passive phrase  (Professional Experience, role 1, bullet 3)
   "Responsible for monitoring security logs and escalating issues."
   Why: no verb, no tool, no outcome — describes a job description, not a person.
   Rewrite: "Monitored and triaged security alerts across Splunk, escalating
   confirmed incidents to the response team."
```

End with a count by severity and the single highest-impact fix.

## What not to do

- **Do not invent the numbers the resume is missing.** Item 11 failing means
  telling the user which bullets need a figure and asking them for it — never
  supplying a plausible one.
- **Do not produce an "ATS score."** No real scoring engine is available, so any
  number would be invented authority. Report concrete findings instead.
- Do not rewrite the whole resume during a review. Report, then offer to fix.
