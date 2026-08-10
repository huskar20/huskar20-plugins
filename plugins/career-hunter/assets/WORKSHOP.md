# Job-Hunt Workshop — Student Handout

Follow the steps in order. Setup is Steps 1–5 and takes about fifteen minutes.
The job-hunt work is Steps 6–9.

**Stuck for more than three minutes? Put your hand up, or jump to
[No laptop, no account](#no-laptop-no-account) and keep going on paper.**

---

## What you need

| | |
|---|---|
| A laptop | |
| A Claude account | Check you can sign in **before** you start |
| A Google account | Gmail, Drive, and Calendar are all used |
| Your resume as a PDF | No resume? The **Resume forge** plugin from the same marketplace builds one — ideally do that workshop first |
| Claude desktop app + Claude in Chrome extension | Needed for the job search itself (Step 7 onward) |

### What a plugin is, in 30 seconds

**Claude** is an AI assistant. **A skill** is a written set of instructions
telling it how to do one job properly. **A plugin** is a bundle of skills
someone already wrote and tested, that you install once.

You are installing one called **Career hunter**. It has three skills.

---

## Step 1 — Open Claude

For this workshop you want the **Claude desktop app** — the job search drives
your own Chrome browser, and that needs the app plus the extension. Claude Code
(the terminal) works for setup too, but Steps 7–9 need the app.

---

## Step 2 — Turn on the Google connectors

1. Open **Settings** → **Connectors**
2. Enable **Gmail**, **Google Drive**, and **Google Calendar**

All three are used: Drive holds your tracker spreadsheet, Gmail is scanned for
application replies, Calendar gets your interview events. If one is off, setup
stops and tells you which — that is intended, not a crash.

---

## Step 3 — Chrome extension

1. Open **Google Chrome** (Chrome only — not Edge, Safari, or Firefox)
2. Chrome Web Store → search **Claude in Chrome**
3. **Add to Chrome**
4. Sign in, then pin it: puzzle-piece icon → thumbtack next to **Claude**

The plugin does its searching and any form work in **your** Chrome, with your
own logged-in LinkedIn/Google sessions. Nothing runs on someone else's account.

---

## Step 4 — Install the plugin

### In Claude Code

Type these two, one at a time:

```
/plugin marketplace add huskar20/huskar20-plugins
```

```
/plugin install career-hunter
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

7. Click **Install** on the **Career hunter** card

> The card says **Career hunter** with a space. The hyphenated `career-hunter`
> is only used in commands.

---

## Step 5 — Check it worked

Type a single forward slash:

```
/
```

A menu appears. You should see:

```
/career-hunter:setup
/career-hunter:apply
/career-hunter:sync
```

If they are not there, you did not restart. Quit Claude and reopen.

---

## The three commands

| Command | What it does |
|---|---|
| `/career-hunter:setup` | One-time interview → your profile file + a Google Sheets tracker |
| `/career-hunter:apply` | Hunts matching roles and prepares (or submits) applications |
| `/career-hunter:sync` | Reads your Gmail and updates the tracker — confirmations, rejections, interviews |

Plain sentences work too — "run the job hunt" does the same as
`/career-hunter:apply` — but the slash commands are faster.

---

## Step 6 — The setup interview

Open (or create) a folder to be your job-search workspace, then type:

```
/career-hunter:setup
```

It interviews you: target job titles, salary floor, location, work
authorization, notice period. Answer honestly — **every application answer
comes from this profile**, so a wrong answer here goes on real forms later.

Two moments matter:

- **When it asks for a submission mode, pick `prepare`.** That is the
  try-it-safely mode: the plugin never opens or submits a form. The other two
  modes are explained in Step 8 — you can switch any time.
- **Salary floor** — the number below which it never even shows you a role.
  Look up a realistic entry figure for your title and city first.

Setup creates two things you own:

- `career-profile.md` — your answers, in your folder, yours to edit by hand
- a **Job_Search_Tracker** Google Sheet in your Drive, with Applications,
  Interview Notes, Contacts, and Dashboard tabs

Open the sheet and keep it in a tab. It fills up in Step 7.

---

## Step 7 — Run the hunt

```
/career-hunter:apply
```

In `prepare` mode it searches **LinkedIn Jobs, Indeed, and company career
boards** (Greenhouse, Lever, Ashby) in your Chrome, scores every role against
your profile, and writes the best matches to a queue file:

```
career-hunter-state/prepared/<today>.md
```

Open that file. For each role you get:

- the apply link
- a one-line "why this fits you"
- **ready-to-paste answers** to the screening questions, drawn from your profile
- a short tailored cover paragraph

**You** click apply and paste. The plugin did the research and drafting; every
actual submission is your own click.

> First time, Chrome will ask permission per site (linkedin.com, indeed.com…).
> Allow them — that per-site gate is a feature, not a bug.

---

## Step 8 — The three modes (read before changing anything)

| Mode | What happens | Who clicks Submit |
|---|---|---|
| `prepare` | Never opens a form; writes links + answers to the queue file | **You** |
| `review` | Fills each form in your Chrome, then stops | **You** |
| `auto` | Fills **and submits** in your name | The plugin |

Switch by editing `submission_mode` in `career-hunter-state/config.json`.

`prepare` is today's mode and an honest recommendation beyond today:
applications you personally finish tend to be better applications. Whatever
the mode, the plugin **never** invents an answer, never enters SSN/DOB/IDs,
never types a password, and never touches a captcha — anything it can't answer
from your profile gets skipped and flagged for you instead.

---

## Step 9 — Sync your inbox

After you have applied to something (today or later), type:

```
/career-hunter:sync
```

It scans your Gmail since the last run and updates the tracker: application
confirmations, rejections, interview invites. Cold recruiter spam and
job-board alert noise are filtered out, not logged. A confirmed interview can
land straight on your Google Calendar, with a push notification.

This is the habit that makes the tracker worth having: **apply → sync →
Dashboard tab tells you the truth** about your funnel.

---

## No laptop, no account

The system still works on paper:

1. Rule a page into five columns: **Company / Role / Date applied / Last
   activity / Next step**
2. Pick three real postings you would apply to this week
3. For each, write the two facts every screening form asks: your work-auth
   answer, and your salary answer
4. Write a three-sentence "why this company" for your favorite one — facts
   from your own experience only, no adjectives about yourself

That column layout is exactly the tracker the plugin builds; the two facts are
exactly what `career-profile.md` stores.

---

## Troubleshooting

| What you see | Fix |
|---|---|
| The `/career-hunter:` commands are not in the `/` menu | You did not restart. Quit Claude completely and reopen |
| Setup says a connector is missing | Settings → Connectors → enable Gmail, Drive, and Calendar |
| "No browser connected" during apply | Desktop app + Claude in Chrome extension (Step 3), then click **Connect** when asked |
| Apply or sync sends you back to setup | Intended — they need the profile setup creates. Run Step 6 first, in your workspace folder |
| A site won't load during the hunt | Allow it in the extension's site permissions when Chrome asks |
| It skipped a role and "flagged" it | Working as intended — the form asked something your profile can't answer. The summary tells you which and why |
| The queue file is empty | Your filters may be too tight — check the salary floor and titles in `career-profile.md`, edit by hand, re-run |

---

## Take home

**github.com/huskar20/huskar20-plugins**

The plugin, this handout, and **Resume forge** — the companion plugin that
builds and tailors the resume this one applies with.

**Tonight:** work through today's queue file — even two real applications beats
a perfectly configured tracker with zero rows. Then `/career-hunter:sync`
tomorrow and watch the tracker catch the confirmations.
