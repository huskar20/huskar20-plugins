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
| Margins | 0.5" all four sides | Leaves a **7.5" text column**: the ruler runs 0.00" to 7.50" |
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
| Summary | 11pt | Regular | Centered |
| Section headers | 11pt | Bold, ALL CAPS, underlined | Left |
| Role / institution line | 11pt | Bold | Left |
| Dates on those lines | 11pt | **Bold** | Right, on the 7.50" tab stop |
| Body and bullets | 11pt | Regular | Left |

The name and the target title line are the only elements above 11pt. Section
headers are underlined; they carry no colour, and never a drawn rule line or
border beneath them, since the underline belongs to the text itself.

**The name is written in title case — `First Last`, not `FIRST LAST`.** Section
headers are the only ALL CAPS text on the page.

**Never use italic anywhere in a resume.** Not for degree lines, not for
organizations, not for project stacks, not for dates. The document has exactly
three levels of emphasis: bold, underline on section headers, and regular
weight. Italic at 11pt prints faintly, adds a fourth signal the reader has to
decode, and buys nothing that bold and position do not already give. If a line
needs to stand out, make it bold or move it, never slant it.

## Bullet glyphs — pick one scheme per document

Which scheme depends on how much is on the page. Choose once and hold it for the
whole document; never mix the two.

**Short resume — one page, or fewer than about fifteen detail bullets:**

```
Software Engineer Intern, Northstar Analytics (Reston, VA)		May 2025 – Aug 2025
   •  Built three production REST endpoints in Python and FastAPI for 12 accounts.
   •  Cut median API response 610ms to 380ms (38%) with PostgreSQL indexes and Redis.
```

The title, organisation and date are all bold, and that gap is a real tab landing
on the 7.50" right stop. Titles sit flush at the left margin, aligned with the
section headers, and carry no glyph, so they form a clean vertical spine down the
left edge. Details indent beneath with a round bullet.

**Long resume — two or more pages, or many roles stacked together:**

```
•  Software Engineer Intern, Northstar Analytics (Reston, VA)		May 2025 – Aug 2025
      -  Built three production REST endpoints in Python and FastAPI for 12 accounts.
      -  Cut median API response 610ms to 380ms (38%) with PostgreSQL indexes and Redis.
```

Once a page carries twenty-plus bullets at one indent level it reads as a single
undifferentiated list, and the eye loses where each role begins. A second glyph
level restores that separation: round bullets mark roles and projects, hyphens
mark the details under them.

Either way the hyphen appears **only at the start of a detail line**. Inside a
sentence, see "Writing that does not read as machine-written" below.

## Spacing

Gaps come from a blank line whose font size is set deliberately. Every paragraph
keeps `space before = 0` and `space after = 0`; the blank line is the gap.

| Gap | Where |
|---|---|
| **1pt** | between jobs, and between education entries |
| **7pt** | before every section header |
| **3pt** | before and after the target role line |

**These three values are the whole spacing system. Use only 1, 3 and 7, and use
them every single time.** A resume where one section header has a 7pt gap above
it and the next has none reads as careless before a word is read. Apply the gap
at every occurrence, not just the first.

**It must be an empty paragraph carrying that font size, not paragraph
spacing.** `space after = 7pt` is not the same thing and does not match the
shipped template: an empty 7pt paragraph occupies its own line box, so the gap
is a genuine blank line. Setting a margin instead produces a visibly tighter
document that no longer matches the reference rendering.

To set one: press Enter once, click the empty line, and type the size into the
font-size box. The size lives on the paragraph mark, so an empty line really is
1pt or 7pt tall.

The equivalent paragraph-property route is Format → Line & paragraph spacing →
**Custom spacing**, where exact points can be typed. Avoid the one-click "Add
space after paragraph" — it applies a fixed chunk far too big for a resume.

When generating the document programmatically, `build_resume_docx.py` emits the
empty paragraph for you and refuses any gap that is not 1, 3, 5 or 7 point, so
the spacing cannot drift document to document.

## Section order

Decide this from the years of professional experience, which `build` asks for
before writing anything. The two orders are genuinely different documents, not a
preference.

**Student, new grad, or internship seeker (0–3 years):**

header → target title → summary → **Education** → skills section →
**Projects** → Professional Experience → Certifications

Education comes first, directly under the summary. Someone screening interns
filters on school, major, year, and graduation date before anything else, so
that block answers their first question immediately. Projects sit above work
history because for a student they usually *are* the evidence: coursework
builds, hackathons, home labs, and volunteer work all count.

**3+ years:**

header → target title → summary → skills section →
**Professional Experience** → Additional Experience (only on a long career) →
Education → Certifications → optional Projects

Once there is a real track record it leads, and Education drops below it.

Move Education and Projects down once the user has roughly two years of
full-time work. Part-time and campus jobs held while studying do not count
toward that two years.

## The header block — four lines

```
First Last
City, State
(000) 000-0000  •  first.last@email.com  •  linkedin.com/in/handle  •  github.com/handle
Target Job Title  |  Specialty or Top Credential
```

Never include: street address, photo, age, date of birth, marital status,
nationality, or "References available upon request."

The email is the candidate's name — `first.last@` — never a nickname, and never
a birth year, which leaks the age the rule above excludes. Dots are fine;
underscores are a trap, because the hyperlink underline swallows them. The
LinkedIn link is the claimed custom URL (`linkedin.com/in/handle`), not the
unclaimed default with its random suffix (`linkedin.com/in/name-8a2b91354`).
Print every link in display form — no `https://www.` — and keep it hyperlinked
in the exported PDF.

The **target title line** names the job being applied for, not the job currently
held. Rewrite it per application so it echoes the posting's own words. It is the
highest-leverage line on the page.

## Summary — no section header

The paragraph flows directly out of the title line. Do **not** type the word
"Summary" — it saves a line and reads faster.

**Centre the paragraph.** It is the one body block that is centred; every
section below it is left aligned. The summary belongs to the header group —
name, city, contact line, target title — and centring keeps that whole opening
block reading as a single unit before the page switches to left-aligned
sections. Left-aligning it makes it collide visually with the first section
header. This holds for every resume the skill produces, at every experience
level.

Formula: *what you are + field and scale + tools you actually know + one result
with a number in it.*

Two to four sentences, third person, never "I." Write it last.

Banned words: passionate, motivated, hardworking, guru, ninja, self-starter,
team player, dynamic.

## Skills section — the header depends on the field

| Resume type | Header |
|---|---|
| Technical (engineering, IT, security, data) | **TECHNICAL SKILLS** |
| Everything else (education, program, operations, clinical) | **CORE COMPETENCIES** |

The shipped blank template uses `TECHNICAL SKILLS`, since most people reaching
for it are in a technical field. Swap it for `CORE COMPETENCIES` when the resume
is not.

`TECHNICAL SKILLS` is the more standard header for ATS keyword extraction and is
what a technical reader expects. `CORE COMPETENCIES` carries the same content for
fields where "technical" would read oddly. Pick one and use it once.

Bold category label, colon, then items. Three to five categories, most relevant
first. Never a flat wall of comma-separated tools.

```
Languages: Python, Java, JavaScript, SQL, Bash
Cloud & DevOps: AWS (EC2, S3, Lambda, RDS), Docker, GitHub Actions, Linux
```

Category labels adapt to the field: Program Leadership / Operations & Data /
Community Engagement work identically for non-technical roles. Only list what
the user could discuss for two minutes in an interview.

## Experience

Role line: `Job Title, Organization (City, State)` with the date flush right on a
**right tab stop at 7.50"**. Use a real tab, never spaces.

**The title, the organization and the date are all bold.** The date is not a
secondary detail set in regular weight — it sits at the far right of the line
and carries the same weight as the title, so the eye can run down the right edge
and read the chronology on its own. The same holds for education and
certification lines.

A date that is merely *near* the right margin is wrong. It must land **on** the
7.50" stop, which is why this needs a real tab and a real tab stop.

Detail lines use the glyph scheme chosen above, as literal text plus a tab, with
a hanging indent so wrapped lines align under the first word rather than under
the glyph.

- **Formula:** strong verb + what you did + the tool or method + the result or scale
- **How many:** 4–6 for the current or most relevant role, 2–3 for older roles,
  1–2 for anything over ten years old
- **Length:** **one line is the target.** At 11pt across a 7.5" column that is
  roughly 100 characters. Take a second line only when it carries a number or a
  tool name that would otherwise be cut. Three lines is a paragraph — cut it.
- **Tense:** present for the current role, past for everything else, never mixed
  within a role

Getting to one line is mostly deletion, and it rarely costs the evidence:

| Two lines | One line |
|---|---|
| Reduced median API response time from 610ms to 380ms, a 38% cut, by adding PostgreSQL composite indexes and a Redis cache layer across 40,000 daily requests. | Cut median API response 610ms to 380ms (38%) with PostgreSQL indexes and a Redis cache. |
| Resolved 900+ help desk tickets across Windows, macOS, and campus network issues while enrolled full time, holding a 4.8 / 5.0 satisfaction rating over four semesters. | Resolved 900+ help desk tickets across Windows and macOS at 4.8/5.0 satisfaction. |

The verb, the tool, and the number all survive. What goes is the secondary
clause. That is the right thing to lose.

### Additional Experience — the compressed block for a long career

A candidate with fifteen or more years, or more than five or six roles, cannot
give every job four bullets without blowing the page budget. Give the recent and
relevant roles the full treatment, then collapse the rest under a second header:

```
ADDITIONAL EXPERIENCE
Systems Administrator, Meridian Health (Columbus, OH)                2011 – 2014
   •  Ran Active Directory and VMware for 600 staff across three sites.
Desktop Support Technician, Calloway Group (Dayton, OH)              2008 – 2011
```

Use it when the full history runs past the page budget, and put in it anything
older than roughly the last ten to fifteen years, plus any role unrelated to the
target title however recent. One detail bullet each, often none. The most recent
role in this block should still be the least interesting thing on the page.

**The role line does not change.** Same `Job Title, Organization (City, State)`,
same bold, same date flush right on the 7.50" tab stop. It is tempting to run
the location and dates inline in parentheses to save room, but that surrenders
the right-edge chronology, which is the one thing a reader scanning a long
career actually uses. Compress the bullets, never the spine.

**Compressing is not hiding.** Every role keeps its real dates and its real
title. A block that drops dates to disguise a gap, or to make a career look
shorter, is a different thing entirely and this skill does not produce it.

## Writing that does not read as machine-written

A resume that reads as generated gets discounted, and the tells are structural
rather than lexical. Watch for these while writing, not afterward.

**Dashes inside a sentence are the loudest signal.** An em dash or a hyphen used
as a mid-sentence break is the single most recognisable marker of generated
prose. Use a comma, a full stop, or parentheses instead. Hyphens are fine at the
start of a detail line and inside compound words such as `token-based` or
`full-stack`.

- Not: `Reduced latency 38% — a major win — by adding indexes.`
- Yes: `Cut latency 38% by adding PostgreSQL composite indexes.`

**Do not force a metric into every bullet.** Nobody has a number for everything.
A page where all sixteen bullets end in a percentage reads as fabricated even
when every figure is real. Two or three strong numbers per role is human; four
identical-looking ones are not.

**Vary the length on purpose.** Bullets that are all within a few characters of
each other look generated. Let a short, blunt bullet sit next to a longer one.

**Vary the opening verb.** Six bullets beginning `Built / Built / Developed /
Developed` is as mechanical as repeating one verb.

**Banned words**, on top of the summary's list: `leveraged`, `spearheaded`,
`utilized`, `orchestrated`, `seamless`, `robust`, `cutting-edge`, `synergy`,
`best-in-class`, `deep dive`. Say the plain thing instead — `used`, `led`,
`built`.

Read the finished bullets aloud. Anything that sounds like a press release gets
rewritten in the words the user actually used when describing the work.

## Projects

**Project name only.** No stack list on the line, and no printed URL. Tools go
inside the bullets, where they arrive with evidence attached, and in Core
Competencies. The LinkedIn and GitHub links in the header reach everything else.

```
CampusSwap, Student Marketplace
•  Built a full-stack textbook exchange in Python and Django on AWS EC2 for 340 students.
```

Close to mandatory for students with thin work history. Two strong projects beat
five weak ones. Cut any project the user cannot walk through line by line.

## Education & certifications

Institution bold with dates on the right tab stop; degree line in regular
weight underneath. Reverse chronological.

- **GPA:** only if 3.5+ **and** within three years of graduation
- "Expected May 2026" is normal for students
- A coursework line is useful at 0–2 years, delete it after
- Community college, transfer credit, bootcamps, and certificate programs belong
  here and are legitimate

Certifications: **the name is bold, the issuing body is not.** Put the issuer in
the spec's `issuer` field, which sets it in regular weight after the name. Order
by prestige and relevance, not date. "In Progress (Expected Nov 2026)" is honest
— use it. Spell exactly: CompTIA not CompTia, CrowdStrike not Crowdstrike.

Bold marks the entity that owns the date, not the important thing. That is why
the institution is bold and the degree beneath it is not, even though the degree
matters more. A certification owns its date the way a job does, so the name
takes the same weight, and the issuer describes it the way a degree line
describes a school.

### Two forms, chosen by count

**Up to four certifications — one dated line each:**

```
CompTIA Security+, CompTIA                                                  2024
AWS Certified Solutions Architect – Associate       In Progress (Expected Nov 2026)
```

**Five or more — collapse to grouped lines** with `"kind": "grouped"`, which
renders a bold category label and regular items, exactly like the skills block:

```
Cloud: AWS Solutions Architect Associate (2025), Azure Fundamentals (2024)
Security: CompTIA Security+ (2024), CompTIA Network+ (2024), CySA+ (2023)
```

Past four entries the one-per-line form becomes a wall of bold with a bold date
beside each, and bold that covers a whole block has stopped marking anything.
The grouped form drops eight lines to three, keeps every certification name
intact for keyword matching, and puts the year in parentheses instead of on the
tab stop. Cert dates carry far less than job dates — nobody reconstructs a
career from exam years — so losing the right-edge alignment costs little here
and would cost a lot in Professional Experience.

Count the certifications and pick the form before writing the section. Do not
mix the two.

## File naming

`JobTitle_FirstNameLastName.pdf` — for example `SoftwareEngineer_AlexMoreno.pdf`.
It tells the reader what the applicant is targeting before they open it, and it
survives landing in a folder of two hundred files called `resume.pdf`.

## Drive workflow to recommend

Master lives in Google Docs; File → Make a copy per target role; export a fresh
PDF per application; send the PDF, never the editable Doc. Name a version under
File → Version history before every large rewrite so it can be rolled back.
