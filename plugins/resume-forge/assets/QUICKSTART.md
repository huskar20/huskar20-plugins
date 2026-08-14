# Resume Workshop — Quick Start

Four steps to a finished resume. About twenty minutes.

Written for the **Claude desktop app**. If you use the terminal instead, look
for the *Using the terminal?* boxes.

**Stuck for more than three minutes? Put your hand up.**

---

## Before you start

| | |
|---|---|
| The Claude desktop app | Downloaded and signed in |
| Google Drive turned on | **Settings** → **Connectors** → enable **Google Drive** |
| Your resume | Any format. No resume? Fine — Step 4 asks you questions instead |

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

Your resume is already in the folder, so it should find it. If it asks, drag
the file into the chat.

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

Or just: **"review my resume"**.

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

## If something goes wrong

| What you see | Fix |
|---|---|
| The `/resume-forge:` commands are missing | You did not restart. Quit Claude and reopen. Still missing? Type the plain sentence instead — **"build my resume"** works the same |
| Claude cannot see my resume | The folder is not attached. Redo Step 3 — you should see `job-search` on the conversation |
| "Drive is not connected" | **Settings** → **Connectors** → enable **Google Drive** |
| Cannot find **Plugins** | Open **Settings** first — it is under the **Customize** heading |
| Our repo is not in **Browse Anthropic sources** | It never will be. Go back and pick **Add from a repository** |
| No PDF appeared | Correct — File → Download → PDF Document |

---

## Take home

**github.com/huskar20/huskar20-plugins**

Want the longer version — templates, a worked example, and a ten-point
checklist? See [WORKSHOP.md](WORKSHOP.md) in the same folder.
