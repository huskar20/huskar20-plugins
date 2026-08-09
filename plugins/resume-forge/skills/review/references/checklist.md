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
| 5 | No italic anywhere | Bold, underlined section headers, and regular weight only. Flag any italic run |
| 6 | Contact block complete | Name, city/state, phone, email, LinkedIn. GitHub for technical roles |
| 7 | No prohibited personal data | Street address, photo, age, DOB, marital status, nationality |
| 8 | No "References available upon request" | Assumed; wastes a line |
| 9 | Every bullet opens with a verb | Flag "Responsible for", "Helped with", "Worked on", "Duties included", "Tasked with" |
| 10 | Tense is consistent | Present for the current role, past for all others, never mixed inside one role |
| 11 | Name is title case (`First Last`), not ALL CAPS | Section headers are the only all-caps text |
| 12 | Spelling of tools and certifications | CompTIA not CompTia · CrowdStrike not Crowdstrike · VirusTotal not Virus Total · PostgreSQL not Postgresql · JavaScript not Javascript · GitHub not Github · LinkedIn not Linkedin · Kubernetes not Kubernets |

## Reads as machine-written

The tells are structural, not lexical. Report these with the offending text quoted.

| # | Check | How to test |
|---|---|---|
| 13 | **Dashes inside a sentence** | Any em dash or hyphen used as a mid-sentence break. The loudest generated-prose signal. Hyphens are fine at the start of a detail line and in compounds (`token-based`) |
| 14 | Metric forced into every bullet | If nearly every bullet ends in a figure, it reads fabricated even when true. Two or three per role is human |
| 15 | Bullets all the same length | Within a few characters of each other across a whole role |
| 16 | Repeated opening verbs | `Built / Built / Developed / Developed` in sequence |
| 17 | Press-release vocabulary | leveraged, spearheaded, utilized, orchestrated, seamless, robust, cutting-edge, synergy, best-in-class, deep dive |

## Strong warnings

| # | Check | Threshold |
|---|---|---|
| 18 | Target title line present | Bold, centered, under the contact line, naming the role being applied for |
| 19 | Summary quality | 2–4 sentences, no "I", no banned words: passionate, motivated, hardworking, guru, ninja, self-starter, team player, dynamic |
| 20 | Skills grouped, header fits the field | Bold category labels, not a flat wall. TECHNICAL SKILLS on technical resumes, CORE COMPETENCIES otherwise |
| 21 | Bullets containing a number | At least four across the whole document. Zero is the single most common failure |
| 22 | Bullet length | One line is the target; a second only to save a number or tool. Three lines is a paragraph |
| 23 | Bullets per role | 4–6 for the most recent, 2–3 for older, 1–2 beyond ten years |
| 24 | Section headers standard | "Professional Experience", not "Where I've Worked" |
| 25 | GPA rule | Present only if 3.5+ and within three years of graduation |
| 26 | Section order | 0–3 years: Education directly under the summary, then skills, then Projects, then Experience. 3+ years: skills, then Experience, then Education |
| 27 | Project lines | Name only, no stack list and no printed URL |
| 28 | Bullet glyph scheme consistent | One scheme per document. Short: plain titles + • details. Long: • titles + - details. Never mixed |
| 29 | Email address is professional | Recognizably the candidate's name — `first.last@` is the standard, and dots are fine. Flag nicknames or slang, birth years (leaks the age #7 prohibits), and underscores, which vanish under a hyperlink underline. The fix is a new `first.last@gmail.com`-style address; remind the user the new inbox must be live before applications go out |
| 30 | LinkedIn URL is claimed | The default URL ends in a random suffix — `linkedin.com/in/name-8a2b91354`. The fix is claiming the custom URL (LinkedIn → Settings → Public profile), not retyping the link. Hyphens alone are fine. Same standard for the GitHub username on technical resumes |

## Advisory

| # | Check |
|---|---|
| 31 | Vague quantifiers: "many", "various", "several", "numerous", "etc." |
| 32 | Passive constructions: "was tasked with", "was responsible for" |
| 33 | Filler adjectives with no evidence behind them |
| 34 | Acronyms never expanded — spell out once, e.g. "Security Information and Event Management (SIEM)" |
| 35 | Dead or malformed URLs in the header |
| 36 | Header links in display form — `linkedin.com/in/handle`, no printed `https://www.`, and still hyperlinked in the exported PDF |
| 37 | Inconsistent date formats between roles |
| 38 | File name is `JobTitle_FirstNameLastName.pdf` |

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

- **Do not invent the numbers the resume is missing.** Item 21 failing means
  telling the user which bullets need a figure and asking them for it — never
  supplying a plausible one.
- **Do not produce an "ATS score."** No real scoring engine is available, so any
  number would be invented authority. Report concrete findings instead.
- Do not rewrite the whole resume during a review. Report, then offer to fix.
