# Resume Workshop — Student Handout

Follow the steps in order. Setup is Steps 1–5 and takes about ten minutes. The
resume work is Steps 6–9.

**Stuck for more than three minutes? Put your hand up, or jump to
[No laptop, no account](#no-laptop-no-account) and keep going on paper.**

---

## What you need

| | |
|---|---|
| A laptop | |
| A Claude account | Check you can sign in **before** you start |
| Your resume | Any format. No resume? See Step 8 |
| Google Drive | Required — the plugin writes your resume there |
| Claude in Chrome extension | Optional. **Highly recommended if you have a paid plan** |

### What a plugin is, in 30 seconds

**Claude** is an AI assistant. **A skill** is a written set of instructions
telling it how to do one job properly. **A plugin** is a bundle of skills
someone already wrote and tested, that you install once.

You are installing one called **Resume forge**. It has three skills.

---

## Step 1 — Open Claude

Use whichever you have. Both work.

- **Claude Code** — the terminal one. Run `claude` in a terminal window.
- **The Claude app** — desktop or web.

---

## Step 2 — Turn on Google Drive

The plugin writes your finished resume into your own Google Drive.

1. Open **Settings** → **Connectors**
2. Enable **Google Drive**

If Drive is off, the plugin stops and tells you before asking any questions.
That is intended, not a crash.

---

## Step 3 — Chrome extension (optional)

Skip this if you are on a free plan.

**If you have a paid plan (Pro, Max, Team, Enterprise), this is highly
recommended** — it exports your PDF for you and can edit a Doc in place. Without
it, both are quick manual jobs (see [Troubleshooting](#troubleshooting)).

1. Open **Google Chrome** (Chrome only — not Edge, Safari, or Firefox)
2. Chrome Web Store → search **Claude in Chrome**
3. **Add to Chrome**
4. Sign in, then pin it: puzzle-piece icon → thumbtack next to **Claude**

---

## Step 4 — Install the plugin

### In Claude Code

Type these two, one at a time:

```
/plugin marketplace add huskar20/huskar20-plugins
```

```
/plugin install resume-forge
```

Then **quit Claude Code and reopen it.** People forget this and nothing works.

### In the Claude app

1. **Customize** in the left sidebar
2. **Plugins** tab
3. Under **Personal plugins**, click **+**
4. **Add marketplace**
5. **Add from a repository**
6. Paste this:

```
https://github.com/huskar20/huskar20-plugins
```

7. Click **Install** on the **Resume forge** card

> The card says **Resume forge** with a space. The hyphenated `resume-forge` is
> only used in commands.

---

## Step 5 — Check it worked

Type a single forward slash:

```
/
```

A menu appears. You should see:

```
/resume-forge:review
/resume-forge:build
/resume-forge:tailor
```

If they are not there, you did not restart. Quit Claude and reopen.

---

## The three commands

| Command | What it does |
|---|---|
| `/resume-forge:review` | Checks your resume and tells you exactly what is wrong |
| `/resume-forge:build` | Writes a properly formatted resume into your Google Drive |
| `/resume-forge:tailor` | Aims a copy at one specific job posting |

Typing the plain sentence works too — "review my resume" does the same thing —
but the slash commands are faster and you can see them in the `/` menu.

---

## Step 6 — Review what you already have

Type:

```
/resume-forge:review
```

Then give it your resume. Any of these work:

- **Drag the file** into the chat
- **Paste the text** of your resume
- **Paste a Google Doc link**
- **In Claude Code**, put the path straight after the command:

```
/resume-forge:review ~/Documents/my-resume.docx
```

You get back a list of findings. Each one quotes the actual line that failed.

**Read them. Do not fix anything yet.**

---

## Step 7 — Fix your three worst bullets

Do this part yourself. Use this shape:

**strong verb + what you did + the tool + the result**

Before:

```
Responsible for monitoring security logs and escalating issues.
```

After:

```
Monitored and triaged alerts across Splunk, escalating confirmed incidents.
```

Three rules while you rewrite:

1. **One line per bullet.** Roughly 100 characters.
2. **No dashes inside a sentence.** Use a comma or a full stop.
3. **Do not force a number into every bullet.** Some, not all.

**No numbers?** You have them, you just have not counted. How many tickets,
users, or machines? How often — per day, per shift, per semester? How much
faster: "40 minutes to 12"? How many people on the team? An honest estimate you
can defend is fine.

---

## Step 8 — Build the clean version

```
/resume-forge:build
```

It asks for your target job title, how many years of experience you have, and
your contact details. Then it writes a formatted Google Doc into your Drive.

**No resume at all?** Start from the blank template, fill it in, then run the
command and hand it that file:

- [Resume_Template_Clean.docx](Resume_Template_Clean.docx) — blank
- [SoftwareEngineer_AlexMoreno.docx](SoftwareEngineer_AlexMoreno.docx) — a finished example

> Alex Moreno is invented. Study how the bullets are written; do not copy them.

**Then export the PDF yourself:** File → Download → PDF Document. Name it
`JobTitle_FirstNameLastName.pdf`.

---

## Step 9 — Aim it at a real job

Find one posting you would actually apply to.

```
/resume-forge:tailor
```

Paste the posting when it asks. You get a table showing which of their
requirements your resume already demonstrates, which you have but describe
differently, and which are missing.

Missing ones come back as **questions**, not edits. If you have the experience,
say where. If you do not, leave it.

---

## It will not invent anything about you

Not a number, not a tool, not a job, not a date. If a bullet needs a number and
you do not have one, it writes `[ADD NUMBER]` and asks you.

It also gives no "ATS score" — nobody outside the employer has their real
system, so any percentage would be made up.

---

## No laptop, no account

Everything that matters works on paper.

1. Take a printed template, or use your existing resume
2. Pick your four weakest bullets — the ones starting "Responsible for"
3. Rewrite each: strong verb + what you did + the tool + the result
4. Get each to one line
5. Run the ten checks below, then swap with the person next to you

---

## The ten checks

- [ ] Name is the biggest text, in title case — `First Last`, not `FIRST LAST`
- [ ] A **bold job title line** under your contact info, naming the job you *want*
- [ ] Summary is 2–4 sentences, no "I", no "hardworking and motivated"
- [ ] Skills **grouped** by category, not one long comma list
- [ ] Every bullet opens with a strong verb
- [ ] At least four bullets contain a number
- [ ] Every bullet fits one line
- [ ] No dashes in the middle of a sentence
- [ ] No italic, no tables, no columns, no photo
- [ ] One page, saved as `JobTitle_FirstNameLastName.pdf`

---

## Troubleshooting

| What you see | Fix |
|---|---|
| The `/resume-forge:` commands are not in the `/` menu | You did not restart. Quit Claude completely and reopen |
| "Drive is not connected" | Settings → Connectors → enable Google Drive |
| Cannot find **Customize** | Left sidebar of the Claude app |
| My resume is in **Arial**, not Calibri | Should not happen — the resume is built as a .docx with Calibri set throughout. If it does, select all and pick Calibri, ten seconds |
| The **dates are not flush right** | Should not happen now. They sit on a real 7.50" tab stop. If they do not, the resume was built as HTML instead of .docx — say so and rebuild |
| **Margins look wrong** | Should be 0.5" all round, ruler 0.00" to 7.50". Check under File → Page setup |
| No PDF appeared | Correct. File → Download → PDF Document |
| It asks for a number I do not have | Working as intended. Give a real estimate, or leave the placeholder |
| Cannot sign in at all | Go to [No laptop, no account](#no-laptop-no-account) |

---

## Take home

**github.com/huskar20/huskar20-plugins**

Template, example, this handout, and the plugin.

**Tonight:** rewrite the four bullets you did not get to. Twenty minutes beats a
perfect resume you never finish.
