# The record format

The record is `master_profile.json` in their folder. It is JSON validated
against `assets/master_profile.schema.json`. **Never write it by hand** — build
the new version in a temp file and pass it to `scripts/profile.py save`, which
validates, backs up, and writes atomically.

The person never sees this file. Never show them JSON, field names, or ids.

## Top-level shape

```json
{
  "meta": { … },
  "experiences": [ … ],
  "skills": [ … ],
  "projects": [ … ],
  "education": [ … ],
  "target_roles": [ … ],
  "development_areas": [ … ]
}
```

`init` creates all seven keys. Never remove one, even when empty — the save
script counts them to detect data loss.

## Ids

Every id is a prefix plus a number, unique within its array and never reused:
`exp_1`, `skill_1`, `proj_1`, `edu_1`, `story_1`. Stories are nested inside
their experience and numbered across the whole record, not per role.

The schema enforces the prefixes. `exp-1` or `experience_1` is rejected.

## The two tag vocabularies

Every claim carries both. They do different jobs and must never be conflated.

**`defensibility`** — how well it survives an interviewer pushing on it.

| Value | Means |
|---|---|
| `strong` | They can tell the whole story, with specifics, unprompted |
| `moderate` | Real, but thin on detail or numbers |
| `gap` | Partly supported; something material is missing |
| `do_not_claim` | Not supportable. Kept for their private awareness only |

**`sensitivity`** — whether it may leave the record at all.

| Value | Means |
|---|---|
| `public` | Safe to use outwardly |
| `private` | Real, but theirs alone — never exported |
| `confidential` | Under NDA, or someone else's to disclose — never exported |

**Filtering happens at export, never at capture.** Record the true thing, tag
it honestly, and let `references/resume-handoff.md` decide what leaves. A record
that only holds resume-safe material has failed at its job.

When you are unsure, tag the more restrictive value and ask. Fail closed.

## Entries

### experiences[]

The core array. Jobs, internships, contracts, volunteering, side projects, and
informal work all live here, separated by `type`:
`job` · `internship` · `contract` · `volunteer` · `side_project` · `informal`

`informal` is load-bearing. Unpaid work for family, a friend's business, a
club — the work people dismiss — is real experience and belongs in the record.

```json
{
  "id": "exp_1",
  "org": "Acme Ltd",
  "title": "Support Analyst",
  "type": "job",
  "start": "2020-01",
  "end": "2022-03",
  "summary": "Single point of contact for 60 staff.",
  "source": "user",
  "surfaced_by_probing": false,
  "responsibilities": ["Triaged the ticket queue"],
  "accomplishments": [
    {
      "text": "Cut the average ticket backlog",
      "metrics": "from ~40 open to under 10, over six months",
      "defensibility": "strong",
      "scope_note": "",
      "sensitivity": "public"
    }
  ],
  "stories": [],
  "skills_used": ["ITSM", "Windows admin"],
  "scope_note": "",
  "sensitivity": "public"
}
```

Dates are `YYYY-MM`, or `YYYY` when that is all they remember. `end` is
`"present"` for current roles. Never guess a date — leave it `""` and put the
question in `meta.open_questions`.

`source` records where the claim came from:
`user` · `inferred` · `user_note` · `from_material`

`surfaced_by_probing: true` marks experience they first dismissed as not worth
mentioning. It is worth knowing which parts of their record only exist because
someone dug.

`scope_note` right-sizes a claim that would otherwise read bigger than it was —
"one of four people on the team", "a two-week pilot, not a rollout". Use it
rather than quietly inflating or deleting the claim.

### stories[]

Nested inside an experience, in Situation / Task / Action / Result form.

```json
{
  "id": "story_1",
  "situation": "The queue had built up over a holiday period.",
  "task": "Clear it without dropping new incoming tickets.",
  "action": "Triaged by impact, batched the password resets, wrote a short FAQ.",
  "result": "Backlog cleared in nine days; repeat password tickets fell.",
  "defensibility": "strong",
  "sensitivity": "public"
}
```

Keep their words. Do not compress a story into a bullet — the whole point is
that the detail survives to interview day.

### skills[]

```json
{
  "id": "skill_1",
  "name": "SQL",
  "category": "Data",
  "proficiency": "working",
  "interview_confidence": "medium",
  "defensibility": "moderate",
  "use_cases": ["Ad-hoc reporting"],
  "project": "exp_1",
  "example": "Wrote the weekly ticket-volume query.",
  "sensitivity": "public"
}
```

A skill with no `example` is a claim with nothing behind it. Ask for one, or
tag it `gap`.

### education[], projects[], target_roles[], development_areas[]

See the schema for the full field list. Same rules: real dates or `""`, both
tags on anything claimable, no invented credentials.

`education` covers formal study, bootcamps, certifications, and substantial
self-teaching. For someone early-career this array often carries more weight
than `experiences`.

## meta

```json
"meta": {
  "owner_label": "Jordan Blake",
  "created": "2026-01-15T09:00:00Z",
  "last_updated": "2026-01-15T09:40:00Z",
  "interrogation_stage": "broad_mapping",
  "self_portrait": { … },
  "next_focus": "Deep dive on the Acme role",
  "open_questions": ["Dates for the 2018 contract"],
  "session_log": [
    {"date": "2026-01-15", "covered": "Self-portrait, Acme role", "added": "1 role, 1 story"}
  ]
}
```

`interrogation_stage` is one of `intake` · `broad_mapping` · `deep_dive` ·
`gap_filling` · `polish`, and drives where the interview resumes next sitting.

`next_focus` and `open_questions` are how a future session knows where to pick
up. Rewrite them at every save — a stale `next_focus` sends the next session
back over ground already covered.

`self_portrait` holds their own account of themselves: `in_their_words`,
`through_line`, `known_for`, `headed_toward`, `moving_away_from`,
`constraints`, `source`, `confirmed`. Collect it before mining any document
they hand over.

`session_log` gets one appended entry per sitting. Never rewrite past entries.

## Provenance markers

Two things the schema does not encode, kept in the text of a field:

- **`[inferred]`** — you concluded it rather than being told. Prefix the value.
  Confirm it with them, then remove the marker. Never let an inference harden
  into a fact.
- **`[UNRESOLVED]`** — two sources disagree. Keep **both** values in the field,
  marked, and add the question to `meta.open_questions`. Never silently pick one.
