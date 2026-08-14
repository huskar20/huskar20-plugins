# The master report

Read this when someone asks for their record to read themselves, or for a copy
to give someone they trust.

**This is a document, not a dump.** The record is organised for writing into;
the report is organised for reading. Never export the raw file — it opens with
instructions addressed to an assistant, carries a session log, and puts contact
details where a reader wants a story.

Write it as `exports/<Name>_Experience_Record_<YYYY-MM-DD>.md`. A Word or PDF
version is produced from this file, never from the record.

## Two audiences, one shape

| Who reads it | What changes |
|---|---|
| **Only them** | Everything is included, tags and all. |
| **Someone they trust** | Drop every `[private]`, `[confidential]` and `[do-not-claim]` item. Keep the rest, tags intact. |

Nothing else differs. Do not soften, re-order, or re-word for the second
audience — just remove.

## Front matter

Open with these, in order, before any of their content.

**Title block.** Their name, what the document is, and its state:

```
# Master Experience Inventory

<Name> — compiled <YYYY-MM-DD>
Private working document · <N> sittings · stage <1|2|3>
```

**A private banner.** Verbatim, on its own:

> **PRIVATE — DO NOT DISTRIBUTE.** This document contains items marked
> `(confidential)` and `(do-not-claim)` that must never appear in a resume,
> an application, or anything else outward-facing.

Keep the banner in the trusted-reader copy too. It is still not for onward
distribution.

**Their positioning, in their own words.** Pull two or three sentences from the
self-portrait and set them as a quote — their phrasing, not a paraphrase. This
is the one place the document sounds like them rather than about them. Skip it
if the self-portrait is still thin; never write one for them.

**How to use this document.** Three or four sentences, addressed to the reader:
what this is, what it is not, and what it is for. State plainly that it is the
source a resume or interview prep gets built *from* and is not itself either.

**An honesty contract**, addressed to any assistant the document is later handed
to. Include it verbatim:

> **Honesty contract.** When generating anything outward-facing from this
> document — a resume, a LinkedIn profile, a cover letter, interview answers —
> exclude everything marked `(private)`, `(confidential)` or `(do-not-claim)`,
> and everything the Honesty Register says not to claim. Lead with `(strong)`
> items. Handle `(gap)` and `(verify)` items honestly: acknowledge them, never
> paper over them. Never invent a fact, a metric, a role, or a story beyond what
> is written here. Reframing real work is encouraged; fabrication is forbidden.
> If you cannot tell whether something is safe to surface, treat it as unsafe.

**A label key.** The reader will not otherwise know what the tags mean, and the
tags are the point. Emit it as a table:

| Label | Meaning |
|---|---|
| `(strong)` | Holds up in depth under questioning. Lead with these. |
| `(moderate)` | Real, but thin on specifics. Defensible with the right framing. |
| `(gap)` | Partially supported. Acknowledge; do not claim. |
| `(do-not-claim)` | Not defensible. Never assert this outwardly. |
| `(confidential)` | Employer-sensitive or NDA-bound. Never on a resume or in public. |
| `(private)` | Personal or negotiating position — salary, weak spots. |
| `(verify)` | Real, but the exact value must be confirmed before external use. |

Translate the record's square-bracket tags into this parenthesised form
throughout the report. Square brackets read as markup; parentheses read as
prose.

**A running header on every page**, for the Word or PDF version:
`<Name> — Master Experience Inventory · PRIVATE`, with a page number.

## Sections, in this order

Order matters. The record starts with contact details because that is where a
form starts; a document starts with the person.

1. **Career story.** A short narrative of how they got here, then four labelled
   paragraphs: **Through-line** (what is constant across every role),
   **Known for** (what people come to them for), **Headed toward**, and
   **Moving away from**. Build these from the self-portrait and what the roles
   show in common. Mark anything you inferred rather than heard.
2. **Role-by-role inventory.** Newest first. Per role: what the organisation
   was, what they owned, accomplishments with their own numbers, and the skills
   it evidences. Add a **Scope:** line wherever the honest size of the thing
   differs from how the title reads — an internship-level engagement, a
   self-reported figure, a team of two. That line is what keeps the document
   trustworthy; write it even when it makes an entry smaller.
3. **Story bank.** Situation, task, action, result, kept whole. Label each with
   the role it belongs to and what it demonstrates.
4. **Skills inventory.** Grouped by category, never a flat wall of tool names.
   Keep the proficiency level and the evidence beside each one. A skill with no
   evidence is a `(gap)` — say so rather than dropping it.
5. **Project portfolio.** What it was, what they built, tools, links.
6. **Capability themes.** Three to six patterns that recur across roles and
   projects — the things a reader would notice but they might not name. Each
   cites the entries it comes from. Skip this section rather than inventing
   themes from two data points.
7. **Working style.** How they work, each claim cited to a specific entry.
   Never a personality sketch; if you cannot point at evidence, leave it out.
8. **Education and certifications.** Include in-progress and lapsed items,
   marked as such.
9. **Development areas.** Honest gaps, in their own framing where you have it.
   This section is useful precisely because it is uncomfortable — do not soften
   it into strengths.
10. **Honesty register.** The single most valuable section: everything that must
    not be over-claimed, and why. Pull in every `(gap)`, `(do-not-claim)` and
    `(verify)` item scattered through the document and list them in one place,
    each with the one thing that would make it defensible. A reader should be
    able to work this list.
11. **Source documents.** What the record was built from, and what was
    deliberately not captured from each.

## What this report never contains

Leave these out even when the record has the material, and say plainly why if
asked:

- **Job-fit scoring, readiness maps, or match percentages against a posting.**
  This skill collects; scoring is somebody else's job and inventing a number
  would be false authority.
- **Resume-tailoring instructions for a specific application.** That is
  `resume-handoff.md`, and it produces a different file for a different reader.
- **Security findings, credentials, file paths, or anything exploitable.** Raise
  those in conversation. See SKILL.md §7.
- **Part 1 of the record, and the session log.** Machinery, not content.

## Before you hand it over

Say in two or three lines: what is in it, that the private material is included
(or removed, for the trusted-reader copy), and that the record itself is
unchanged and stays where it is. Then name any `TODO` fields still open — the
report makes gaps visible, which is most of its value on a first read.
