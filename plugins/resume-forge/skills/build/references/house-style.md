# House style — the resume format

Every measurement the `build` skill produces. Follow it exactly; when the user
asks for something different, follow the user and note the deviation.

The blank template shipped at `../../../assets/Resume_Template_Clean.docx` is the
reference rendering of this spec. If a user asks to see the format, or wants to
start from a document instead of an interview, point them at it. Keep the two in
agreement: a change here means regenerating that file.

## Page setup

| Setting | Value | Why |
|---|---|---|
| Paper | US Letter, 8.5" × 11" | Set explicitly — defaults vary by machine |
| Margins | 0.75" all four sides | Leaves a 7.0" text column |
| Font | Calibri, black only | One family for the whole document |
| Body size | 11pt | 10.5pt to save a page. **Never below 10pt** |
| Line spacing | 1.0 (single) | Everywhere, no exceptions |
| Length | 1 page for 0–5 years, 2 pages maximum beyond | |
| Layout | Single column | No tables, text boxes, columns, or horizontal rules |

Applicant tracking systems flatten a document to text. Tables, text boxes, and
columns genuinely break that parse — content inside them can vanish entirely.
Empty paragraphs do **not** break parsing; do not claim otherwise.

## Type scale

| Element | Size | Style | Alignment |
|---|---|---|---|
| Name | 20pt | Bold | Centered |
| City, State | 11pt | Regular | Centered |
| Contact line | 11pt | Regular | Centered |
| Target job title | 16pt | Bold | Centered |
| Summary | 11pt | Regular | Left |
| Section headers | 11pt | Bold, ALL CAPS, underlined | Left |
| Body and bullets | 11pt | Regular | Left |

The name and the target title line are the only elements above 11pt. Section
headers are underlined; they carry no colour, and never a drawn rule line or
border beneath them — the underline belongs to the text itself.

## Spacing

Gaps come from a blank line whose font size is set deliberately:

- **1pt** between jobs
- **5–7pt** between main section titles
- **3pt** before and after the target role line

The equivalent paragraph-property route is Format → Line & paragraph spacing →
**Custom spacing**, where exact points can be typed. Avoid the one-click "Add
space after paragraph" — it applies a fixed chunk far too big for a resume.

When generating a document programmatically, use paragraph spacing (space
before/after) rather than blank paragraphs: 2pt after each bullet, 6pt after a
role's last bullet, 6pt before each section header, 8pt after the contact line.
That produces the same visual result and survives editing.

## Section order

**0–3 years / student:** header → target title → summary → Core Competencies →
**Education** → **Projects** → Professional Experience → Certifications

**3+ years:** header → target title → summary → Core Competencies →
**Professional Experience** → Education → Certifications → optional Projects

Move Education and Projects back down once the user has roughly two years of
full-time work.

## The header block — four lines

```
FIRST LAST
City, State
(000) 000-0000  •  first.last@email.com  •  linkedin.com/in/handle  •  github.com/handle
Target Job Title  |  Specialty or Top Credential
```

Never include: street address, photo, age, date of birth, marital status,
nationality, or "References available upon request."

The **target title line** names the job being applied for, not the job currently
held. Rewrite it per application so it echoes the posting's own words. It is the
highest-leverage line on the page.

## Summary — no section header

The paragraph flows directly out of the title line. Do **not** type the word
"Summary" — it saves a line and reads faster.

Formula: *what you are + field and scale + tools you actually know + one result
with a number in it.*

Two to four sentences, third person, never "I." Write it last.

Banned words: passionate, motivated, hardworking, guru, ninja, self-starter,
team player, dynamic.

## Core Competencies

Bold category label, colon, then items. Three to five categories, most relevant
first. Never a flat wall of comma-separated tools.

```
Languages: Python, Java, JavaScript, SQL, Bash
Cloud & DevOps: AWS (EC2, S3, Lambda, RDS), Docker, GitHub Actions, Linux
```

Category labels adapt to the field — Program Leadership / Operations & Data /
Community Engagement work identically for non-technical roles. Only list what
the user could discuss for two minutes in an interview.

## Experience

Role line: `Job Title, Organization – (City, State)` with dates flush right on a
**right tab stop at 7.0"**. Use a real tab, never spaces.

Bullets: `•` + tab, as literal text, with a 0.18" left indent and 0.18" hanging
indent so wrapped lines align under the first word.

- **Formula:** strong verb + what you did + the tool or method + the result or scale
- **How many:** 4–6 for the current or most relevant role, 2–3 for older roles,
  1–2 for anything over ten years old
- **Length:** one or two lines each; three lines means it's a paragraph — cut it
- **Tense:** present for the current role, past for everything else, never mixed
  within a role

## Projects

**Project name only.** No stack list on the line, and no printed URL. Tools go
inside the bullets, where they arrive with evidence attached, and in Core
Competencies. The LinkedIn and GitHub links in the header reach everything else.

```
CampusSwap — Student Marketplace
•  Built and shipped a full-stack textbook exchange in Python and Django on AWS
   EC2, reaching 340 registered students across two semesters.
```

Close to mandatory for students with thin work history. Two strong projects beat
five weak ones. Cut any project the user cannot walk through line by line.

## Education & certifications

Institution bold with dates on the right tab stop; degree line in italic
underneath. Reverse chronological.

- **GPA:** only if 3.5+ **and** within three years of graduation
- "Expected May 2026" is normal for students
- A coursework line is useful at 0–2 years, delete it after
- Community college, transfer credit, bootcamps, and certificate programs belong
  here and are legitimate

Certifications: bold name, then issuing body. Order by prestige and relevance,
not date. "In Progress (Expected Nov 2026)" is honest — use it. Spell exactly:
CompTIA not CompTia, CrowdStrike not Crowdstrike.

## File naming

`JobTitle_FirstNameLastName.pdf` — for example `SoftwareEngineer_AlexMoreno.pdf`.
It tells the reader what the applicant is targeting before they open it, and it
survives landing in a folder of two hundred files called `resume.pdf`.

## Drive workflow to recommend

Master lives in Google Docs; File → Make a copy per target role; export a fresh
PDF per application; send the PDF, never the editable Doc. Name a version under
File → Version history before every large rewrite so it can be rolled back.
