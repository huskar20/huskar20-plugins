# Handing the record to a resume builder

Read this when the person asks for "material for my resume", or says they are
about to build a CV from this record.

The handoff is **not a filtered summary**. It is the full working inventory,
tags intact, so a resume tool can choose what to use and tailor per posting —
and so the person can see which claims still need work. Send across as much as
is safe to send.

**Save the profile first**, then build the export from the saved file. Never
export from an in-memory version that has not been through `profile.py save` —
if the save is refused, the export would carry data the record does not have.

## The one hard line

Two tag families, and only one of them is safe to delegate downstream.

**Defensibility travels.** `strong`, `moderate`, `gap`, `do_not_claim` are
quality judgements. Send them all, tagged. A tailoring tool legitimately needs
the weaker material — a niche posting may call for the thing that only
half-fits — and hiding weak claims means the person never fixes them.

**Sensitivity does not travel.** Never export anything whose `sensitivity` is
`private` or `confidential`, whatever its defensibility. `confidential` is
NDA-bound or client-identifying, and a resume goes to employers. `private` is
salary and negotiating position — resume tools deliberately refuse to take
that, and this file must not smuggle it in.

Also drop, wherever they appear: compensation, notice period, work
authorization, sponsorship, citizenship, clearance, and any voluntary
self-identification detail. Home address, if one was ever recorded. Everything
in `meta` — `session_log`, `open_questions`, `next_focus`, and the
`self_portrait` block — is working state, not resume material.

**The filter runs per item, not per entry.** A `public` experience can hold a
`confidential` accomplishment, and dropping the accomplishment does not drop the
role. Check `sensitivity` on each accomplishment, story, skill and project in
its own right, and check the parent entry too — a `private` or `confidential`
experience takes all of its children with it, including any skill whose
`example` describes work done there.

**An item with no `sensitivity` recorded is not automatically public.** The
field is optional, so absence means nobody decided — not that it is safe. Treat
an untagged item as `private` and leave it out, then tell the person which items
you held back so they can tag them. Fail closed: a claim withheld can be added
next session, a claim leaked cannot be recalled.

## Tag spelling changes at the export boundary

The record stores `do_not_claim` (JSON, underscores). The export writes
`[do-not-claim]` (markdown, hyphens), matching the hyphenated form `build`
strips. Same for the rest: write `[strong]`, `[moderate]`, `[gap]`, `[public]`
as bracketed lowercase tags, one defensibility and one sensitivity per bullet.

Since `private` and `confidential` never leave, `[public]` is the only
sensitivity tag that ever appears in the export.

## Structure carries the safety, not the tags

Do **not** mix `[gap]` and `[do-not-claim]` items in among usable bullets and
rely on a downstream model to notice the tag. Put them in their own section at
the end. Same information, same value to the person, far less chance of an
unsupported claim quietly becoming a resume line.

## Shape

Write it as `exports/resume-source.md`:

````markdown
# Resume source — <Name>

> Generated from an experience record. Every claim carries two tags.
> **[strong]** holds up under questioning · **[moderate]** real but thin on
> specifics · **[gap]** partially supported.
> **[public]** is the only sensitivity level present — private and confidential
> material was excluded and is not available.
> Items under "Not resume-ready" must not be used without new evidence.
> Do not invent, round, or infer any figure that is not written here.

## Contact
Name · City, State · email · phone · LinkedIn · GitHub or portfolio
<mark any missing field as TODO — do not omit the line>

## Target
Target job title(s), and level if known.
Years of professional experience: <number> — "<their own words>"

## Experience
### Organisation — Title (dates)
- Accomplishment or responsibility [strong] [public]

## Projects
### Project name (year)
- What it was and what they did [moderate] [public]
- Tools: …
- Link: …

## Skills
Grouped by category, not a flat wall of tool names. Keep levels and evidence.

## Education and training
### Credential — Institution (dates)

## Stories
### Story title — relates to <role or project>
Situation / Task / Action / Result, kept whole.

## Not resume-ready — needs evidence first
Items tagged [gap] or [do-not-claim], with a one-line note on what is missing.
Do not use these on a resume. They are here so the person knows what to work on.
````

Experience and projects newest first. Keep the person's own numbers exactly as
given — never round, scale, or infer a figure that is not in the record.

## Where each section comes from

| Export section | Source |
|---|---|
| Contact | `meta.owner_label` and the contact fields; `TODO` for anything unset |
| Target | `target_roles[].title`; years of experience from `meta` |
| Experience | `experiences[]` where `type` is not `side_project`, newest first |
| Projects | `projects[]`, plus `experiences[]` of type `side_project` |
| Skills | `skills[]`, grouped by `category`, keeping `proficiency` and `example` |
| Education | `education[]` |
| Stories | `experiences[].stories[]`, whole, attributed to their role |
| Not resume-ready | every item of any type whose defensibility is `gap` or `do_not_claim` |

`informal` and `volunteer` experience belongs under Experience like any other.
It is often the most interesting material in an early-career record, and the
person has usually already tried to talk you out of including it.

`scope_note`, where present, must survive into the bullet. It is what keeps a
right-sized claim right-sized once it leaves the record.

Strip provenance markers on the way out. An `[inferred]` value that has been
confirmed exports as a plain fact; one still unconfirmed does not export at all
— it goes to "Not resume-ready" with a note that it needs checking. Anything
marked `[UNRESOLVED]` also goes there, never into a bullet.

## Missing fields

If the basics block still has `TODO` values — no email, no phone, no
years-of-experience — **emit the line with `TODO` rather than omitting it**, and
list the gaps when you hand it over. A missing line reads as "this person has no
LinkedIn"; a `TODO` reads as "ask them." That distinction matters when someone
else's tool consumes this.

## Check before you hand it over

Read the finished file back and confirm all four:

1. No `private` or `confidential` material anywhere in it
2. Every `gap` and `do_not_claim` item is inside "Not resume-ready", not above it
3. Every bullet carries a defensibility tag and `[public]`
4. No JSON, no field names, no ids

If any check fails, fix the file before handing it over.

## Say this when you hand it over

Two or three lines, no more:

- this holds everything safe to use outwardly, tags included, so a resume tool
  can pick and tailor
- their full record stays where it is and is unaffected
- to build the resume, start a session with their resume tool and give it this
  file
- anything the resume needs that is missing should come back as a question, not
  be filled in by the resume tool
- name any `TODO` fields they may want to fill first

## What not to do

Do not write the resume yourself. Do not suggest wording, section order, or
formatting. Do not score the record against a posting or estimate how well it
matches. This skill collects; something else builds.
