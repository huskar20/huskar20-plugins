# Keyword coverage against a job description

How to compare a resume to a posting honestly. The output is a coverage table
the user can verify — never a score.

## Why not a score

There is no access to any employer's actual ATS, its parser, or its ranking
model. A "78% match" would be a number with nothing behind it, and users act on
it. Report what is present, what is absent, and what the user can legitimately
claim.

## Step 1 — Extract requirements from the posting

Pull terms into four buckets, keeping the posting's exact wording:

| Bucket | What goes in it |
|---|---|
| **Hard requirements** | Named under "required", "must have", "minimum qualifications" |
| **Preferred** | "Preferred", "nice to have", "bonus" |
| **Tools & technologies** | Concrete named products, languages, platforms, frameworks |
| **Domain language** | Recurring phrases describing the work: "threat hunting", "incident response", "stakeholder management" |

Ignore boilerplate: benefits, EEO statements, culture copy, "fast-paced
environment".

## Step 2 — Classify each term against the resume

| Status | Meaning | Action |
|---|---|---|
| **Covered** | Term appears, with evidence attached | Nothing |
| **Covered, weak** | Appears only in a skills list, no bullet demonstrates it | Suggest moving it into a bullet where the user has real experience |
| **Wording mismatch** | User has the experience under a different name | Suggest adopting the posting's exact phrasing |
| **Absent** | Not in the resume at all | Ask whether the user actually has it. **Never add it on their behalf** |

Wording mismatch is where most of the value is. If the posting says "threat
hunting" and the resume says "threat detection", and the user genuinely does
threat hunting, use the posting's words — parsers match strings, not synonyms.
This is not keyword stuffing; it is describing real experience in the reader's
vocabulary.

## Step 3 — Report

```
COVERAGE — Senior Security Analyst @ <company>

Hard requirements (5)
  ✓ Splunk                covered — 2 bullets
  ✓ Incident response     covered — 3 bullets
  ~ SIEM                  weak — skills list only; consider moving into the QRadar bullet
  ≈ Threat hunting        you wrote "threat detection"; posting says "threat hunting"
  ✗ Terraform             absent — do you have this?

Preferred (3)
  ...
```

Close with:

1. The rewrites that need no new claims — pure wording changes
2. The absent terms, as **questions for the user**
3. One sentence on overall fit, in words

## Hard limits

- **Never add a skill, tool, or experience the user has not confirmed.** An
  absent term becomes a question, never an edit.
- Never invent metrics to satisfy a posting asking for "measurable impact."
- Never stuff keywords in white text, hidden layers, or a comma-dump at the
  bottom. Automated systems flag it and it ends the candidacy.
- If coverage is genuinely poor, say so. Telling someone a role is a stretch is
  more useful than tailoring a resume into a shape that gets them screened out
  in the first interview.
