# The record format

Read this before your first save of a session. It carries the file's structure,
the anchors you insert at, the tag vocabularies, and every entry format.

## File shape

```
experience-record.md
├── header block     ← eight lines, kept current
├── Part 1  Instructions for the assistant   ← never edit
├── Part 2  Session log                      ← one line per sitting
├── Part 3  The record                       ← everything goes here
└── Part 4  Loose notes                      ← stays empty while a skill is running
```

Part 4 exists for people using the file by hand with no skill installed. While
you are running, keep it empty — put entries straight into their Part 3 section.

## Insertion anchors

Every section is bracketed by HTML comments. **Insert new entries immediately
above the `:end` anchor of the matching section.** Never infer a position from
surrounding prose.

| Section | Anchor pair |
|---|---|
| Basics | `<!-- basics:start -->` … `<!-- basics:end -->` |
| Self-portrait | `<!-- self-portrait:start -->` … `<!-- self-portrait:end -->` |
| Roles and experience | `<!-- roles:start -->` … `<!-- roles:end -->` |
| Projects | `<!-- projects:start -->` … `<!-- projects:end -->` |
| Skills | `<!-- skills:start -->` … `<!-- skills:end -->` |
| Stories | `<!-- stories:start -->` … `<!-- stories:end -->` |
| Education and training | `<!-- education:start -->` … `<!-- education:end -->` |
| Development areas | `<!-- development:start -->` … `<!-- development:end -->` |
| Source documents | `<!-- sources:start -->` … `<!-- sources:end -->` |
| Session log (Part 2) | `<!-- sessions:start -->` … `<!-- sessions:end -->` |
| Loose notes (Part 4) | `<!-- notes:start -->` … `<!-- notes:end -->` |

The anchors are the contract. Never remove, rename, or reorder them.

## The header

Exactly these eight lines, directly under the `# Experience Record` title.
Rewrite the whole block whenever any of it changes — it is small enough that
this costs nothing.

```
FORMAT: experience-record v1
SKILL: experience-record 1.0.0
UPDATED: 2026-08-15
SESSIONS: 3
STAGE: 2
COUNTS: roles 4 · projects 2 · stories 6 · skills 11 · education 2
NEXT FOCUS: the two years of volunteer work at the community centre
OPEN QUESTIONS: rough dates for the first support job
```

- **SKILL** — the version of the skill that last wrote the file. Leave the
  value that is there if you do not know your own version.
- **UPDATED** — ISO date, `YYYY-MM-DD`, set on every save.
- **SESSIONS** — incremented once per sitting, at the first save of that
  sitting, not at every save.
- **STAGE** — 1, 2 or 3, from the interview engine. Advance it when that
  stage's exit condition is met: **1 → 2** once a first-pass self-portrait
  exists; **2 → 3** once their history is listed at one line each and they
  confirm nothing is missing. Never go backwards.
- **COUNTS** — literal counts of entries in Part 3. Check them against the file
  rather than remembering. There is deliberately no word count; you cannot
  count words reliably, so do not pretend to.
- **NEXT FOCUS** — one line, what you would cover next sitting.
- **OPEN QUESTIONS** — one line. Separate multiple with `;`. Keep at most three
  — the three most useful. If more accumulate, fold the rest into NEXT FOCUS or
  drop the ones that no longer matter.

## Tags

**Defensibility** — how well a claim survives an interviewer pushing on it:

| Tag | Meaning |
|---|---|
| `[strong]` | They can talk about it for ten minutes under questioning |
| `[moderate]` | Real, but thin on specifics |
| `[gap]` | Partially supported; needs backing up before it goes anywhere public |
| `[do-not-claim]` | Must never appear on a resume or in an interview answer |

**Sensitivity** — whether it may leave this file:

| Tag | Meaning |
|---|---|
| `[public]` | Safe to use outwardly |
| `[private]` | Personal or negotiating-position — salary, weak spots, home address |
| `[confidential]` | Employer-confidential, NDA-bound, or client-identifying |

**Two extra markers, used sparingly:**

- `[inferred]` — you derived this rather than being told it. This is
  **provenance, not quality.** Confirm it with the person, then delete the
  marker. An `[inferred]` item that has sat unconfirmed for a whole session
  should be asked about or removed.
- `[UNRESOLVED]` — two versions of a fact conflict and the person could not say
  which is right. Keep both inside the entry, marked. Never quietly pick one.

**Where filtering happens.** `[do-not-claim]` and `[confidential]` items stay in
the record permanently. The file holds the whole truth, including parts that
must never reach a resume. **Filtering happens at export, never at capture.**

When unsure how to tag something, ask — or tag it more cautiously and say so.

## Entry formats

Match these exactly. Consistency is what lets the file be read by anything
later.

### Basics

One block, written in the first session, edited in place afterwards. Anything
they decline or you have not asked yet stays as `TODO`.

```
- Name: Jordan Blake
- Based in: Manchester, UK · can work in: UK
- Email: jordan.blake@email.com [public]
- Phone: +44 7700 900000 [public]
- LinkedIn: linkedin.com/in/jordanblake [public]
- Portfolio or GitHub: github.com/jblake [public]
- Target roles: TODO
- Years of professional experience: 0 — "two years of part-time retail while studying, no full-time yet"
- Hard constraints: cannot relocate before June
```

**Years of professional experience** carries both a number and their own words,
because "zero" and "zero, but two years part-time" produce different resumes.

**Home address:** do not ask for it. If they volunteer a full street address,
record city and region only. If they insist on the full address, tag it
`[private]` — it never exports.

### A role

Anything someone paid or supervised them to do, including unpaid and informal
work.

```
### Acme Ltd — Support Technician (2019–2022)
- Type: paid
- What it was: 40-person print shop, only IT person on site
- Responsibilities:
  - Ran the ticket queue for all staff [strong] [public]
- Accomplishments:
  - Cut repeat printer faults by roughly half over a year [moderate] [public]
- Skills used: Windows admin, ticketing, hardware repair
- Notes:
```

`Type`: paid, internship, contract, volunteer, informal.

### A project

Something they decided to build or make themselves.

**The boundary rule:** was someone paying or supervising them to do it? If yes
it is a role, even if unpaid — volunteering, a club officer position. If they
scoped it themselves, it is a project — coursework, personal builds,
hackathons, freelance work they defined.

```
### Recipe scaling app (2024)
- Type: personal
- What it was: React app that rescales recipes; ~200 users after a Reddit post
- What they did:
  - Built it solo, front end and API [strong] [public]
- Tools: React, Node, Postgres
- Link: github.com/jblake/recipe-scale [public]
- Notes:
```

`Type`: personal, academic, hackathon, freelance, open source.

### A story

```
### Story — The Friday migration
- Relates to: Acme Ltd
- Situation:
- Task:
- Action:
- Result:
- Tags: [strong] [public]
```

Never say "STAR method" to the person. Ask what happened, what they did, and
how it turned out.

### A skill

```
- Python — level: working · used at: Acme, recipe app · evidence: built the stock reorder script [moderate] [public]
```

`level`: aware, working, strong, expert — set from evidence, not from how
confident they sound.

### Education or training

```
### BSc Computer Science — University of X (2016–2019)
- Type: degree
- Notable: final-year project on network monitoring [moderate] [public]
```

`Type`: degree, certification, course, training, bootcamp.

### A development area

```
- Has never worked to a formal ticketing SLA; would need ramp-up [private]
```

Honest weak spots, plainly written. Useful, not shameful. `[private]` by
default.

### A source document

One line per document they hand over. This section is the index — check it
before re-reading any source file.

```
- `2026-08-15-resume.pdf` — 2-page resume · added 2026-08-15 · captured: 3 roles, education, contact block · status: fully captured
```

`status`: not yet read, partly captured, fully captured.

Record what was **extracted**, not just that it was processed — otherwise a
later pass cannot tell what it missed.

## Corrections

When something new contradicts the file, ask about it, then **edit the existing
entry in place** and add one line to the session log saying what changed. You
have file access; superseding markers are not needed.

If they are not sure which version is right, keep both in the entry and mark it
`[UNRESOLVED]`.

## Session log

One line per sitting, appended above `<!-- sessions:end -->`:

```
- 2026-08-15 · session 3 · covered the Acme years · added 1 role, 3 stories, 4 skills · corrected Acme end date
```
