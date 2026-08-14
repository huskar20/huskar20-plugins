# Resume Workshop — Student Handout

Six steps to a finished resume. About twenty minutes. Anything after Step 6 is
optional — do it if you have time, or take it home.

Written for the **Claude desktop app**. If you use the terminal instead, look
for the *Using the terminal?* boxes.

**Stuck for more than three minutes? Put your hand up.**

---

## Before you start

| | |
|---|---|
| The Claude desktop app | Downloaded and signed in |
| Google Drive turned on | **Settings** → **Connectors** → enable **Google Drive** |
| Your resume | A file in any format, **or a Google Doc link**. No resume? Fine — Step 4 asks you questions instead |

---

## Step 1 — Install the plugin

1. **Settings** → under **Customize**, click **Plugins**
2. **Add** (top right) → **Add marketplace**
3. **Add from a repository** — the second option, not **Browse Anthropic sources**
4. Paste:

```
https://github.com/huskar20/huskar20-plugins
```

5. **Install** on the **Resume forge** card

**Then quit Claude and reopen it.** Nothing works until you do.

> **Using the terminal?** Run these in Claude Code instead, then restart it:
> `/plugin marketplace add huskar20/huskar20-plugins` and
> `/plugin install resume-forge`

---

## Step 2 — Make your folder

- **Mac:** Finder → **Documents** → File → **New Folder** → name it `job-search`
- **Windows:** File Explorer → **Documents** → right-click → **New** → **Folder** → `job-search`

**Put your resume inside it.**

---

## Step 3 — Open Claude in that folder

Claude only reads and writes where you point it.

Start a new chat and **drag the `job-search` folder into the chat window**
(or use the **+** button → add folder). You should see the folder's name
attached to the conversation before you carry on.

> **Using the terminal?** `cd Documents/job-search`, then run `claude`.

---

## Step 4 — Build your resume

Type:

```
/resume-forge:build
```

No slash menu in your app? Type this instead — it does the same thing:

```
build my resume
```

Your resume is already in the folder, so it should find it. Any of these also
work:

- **drag the file** into the chat
- **paste a Google Doc link** — share it as *anyone with the link can view*
  first, or make sure it is in the same Google account
- **paste the text** of your resume

Your original is never changed. You always get a new document.

It asks a few things: the job title you want, how many years you have worked,
your contact details. Answer plainly.

You get a formatted Google Doc in your Drive.

**Save the PDF yourself:** File → Download → PDF Document. Name it
`JobTitle_FirstNameLastName.pdf`.

---

## Step 5 — Check it

```
/resume-forge:review
```

Or just: **"review my resume"**. Same three ways to hand it over — the file, a
Google Doc link, or pasted text.

It quotes the exact lines that need work:

```
Bullet opens with a passive phrase (Experience, role 1, bullet 3)
  "Responsible for monitoring security logs and escalating issues."
  → Start with a verb: "Monitored and triaged alerts across Splunk."

No number in this role
  Add one real figure — tickets per week, users supported, hours saved.
```

Fix your three worst bullets yourself. Shape: **verb + what you did + the tool
+ the result**.

---

## Step 6 — Aim it at one job

Find a real posting you would apply to.

```
/resume-forge:tailor
```

Or just: **"tailor my resume for this job"**.

Paste the posting. You get a table:

```
Python            ✓ already on your resume
Incident response ~ you have it, worded differently → "triaged alerts"
Terraform         ✗ missing — do you have this?
```

Missing items come back as **questions**, not edits. If you have it, say where.
If you do not, leave it.

---

## Good to know

- **It never invents anything** — no fake numbers, tools, jobs, or dates. If a
  bullet needs a number you do not have, it asks you.
- **One page** if you have under five years of experience.
- Your email should be your name: `first.last@gmail.com`.

---

## Troubleshooting

| What you see | Fix |
|---|---|
| The `/resume-forge:` commands are missing | You did not restart. Quit Claude and reopen. Still missing? Type the plain sentence instead — **"build my resume"** works the same |
| Claude cannot see my resume | The folder is not attached. Redo Step 3 — you should see `job-search` on the conversation |
| "I can't open that link" | The Doc is private. Share → **anyone with the link can view**, or use the Google account Drive is connected to |
| "Drive is not connected" | **Settings** → **Connectors** → enable **Google Drive** |
| Cannot find **Plugins** | Open **Settings** first — it is under the **Customize** heading |
| Our repo is not in **Browse Anthropic sources** | It never will be. Go back and pick **Add from a repository** |
| No PDF appeared | Correct — File → Download → PDF Document |
| It asks for a number I do not have | Working as intended. Give a real estimate, or leave the placeholder |
| My resume is in **Arial**, not Calibri | Should not happen. If it does, select all and pick Calibri — ten seconds |
| The **dates are not flush right** | Should not happen. If they are not, say so and ask for a rebuild |
| Cannot sign in at all | Go to [No laptop, no account](#no-laptop-no-account) |

---

## If you have time — fix your three worst bullets

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

## If you have time — keep a record for next time

The hardest part of a resume is remembering what you did.

```
/resume-forge:experience-record
```

Or just: **"start my experience record"**.

It interviews you across several sittings and keeps one honest file holding
every role, project and story — including the small informal work most people
forget. Nothing is lost between sittings. Come back any time with **"continue
my experience record"**.

It needs **no Google Drive and no Chrome**, so start here if you could not get
Drive working today. It also keeps things a resume must never show — salary,
work under NDA, claims you cannot back up yet — and filters them out only when
you export.

> In the desktop app it may hand you the file back instead of saving it. That
> is normal. Keep the file and bring it to the next session.

When you want a resume out of it, say **"give me material for my resume"**,
then hand that file to `build`.

**No resume at all?** Start here rather than with a blank template.

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
- [ ] Email is your name, LinkedIn URL is claimed — no nicknames, no `-8a2b91354` tail
- [ ] Summary is 2–4 sentences, no "I", no "hardworking and motivated"
- [ ] Skills **grouped** by category, not one long comma list
- [ ] Every bullet opens with a strong verb and fits one line
- [ ] At least four bullets contain a number
- [ ] No dashes in the middle of a sentence
- [ ] No italic, no tables, no columns, no photo
- [ ] One page, saved as `JobTitle_FirstNameLastName.pdf`

---

## Starting from nothing

No resume at all? Fill in the blank template, then hand it to `build`:

- [Resume_Template_Clean.docx](Resume_Template_Clean.docx) — blank
- [SoftwareEngineer_AlexMoreno.docx](SoftwareEngineer_AlexMoreno.docx) — a finished example

> Alex Moreno is invented. Study how the bullets are written; do not copy them.

---

## Take home

**github.com/huskar20/huskar20-plugins**

**Tonight:** rewrite the bullets you did not get to. Twenty minutes beats a
perfect resume you never finish.
