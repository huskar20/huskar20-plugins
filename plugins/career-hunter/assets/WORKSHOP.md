# Job-Hunt Workshop — Student Handout

Follow the steps in order. Setup is Steps 1–6 and takes about fifteen minutes.
The job-hunt work is Steps 7–9. Everything after that is reference — read it
when you need it.

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
| Claude desktop app + Claude in Chrome extension | **Required from Step 8 on** — the job search, the applications, and every write to your tracker all run in your own Chrome |

> **About your resume:** in today's `prepare` mode the plugin never uploads
> your resume anywhere — you attach it yourself when you apply from the queue.
> It just needs to read it to answer screening questions well.

### What a plugin is, in 30 seconds

**Claude** is an AI assistant. **A skill** is a written set of instructions
telling it how to do one job properly. **A plugin** is a bundle of skills
someone already wrote and tested, that you install once.

You are installing one called **Career hunter**. It has three skills.

---

## Step 1 — Make your job-search folder

Everything the plugin creates — your profile, your run state, your prepared
applications — lives in one folder that you own. Make it **before** you open
Claude, so Claude starts in the right place.

- **Mac:** Finder → **Documents** → File → **New Folder** → name it `job-search`
- **Windows:** File Explorer → **Documents** → right-click → **New** →
  **Folder** → name it `job-search`

Then **move your resume PDF into that folder.** One folder, everything in it.

---

## Step 2 — Open Claude in that folder

This is the step people skip, and then Claude writes your profile somewhere you
cannot find. **Claude only works in a folder you point it at.**

Use the **Claude desktop app** for this workshop. The job search drives your
own Chrome, and that needs the app plus the extension.

Start a new chat and give it the folder: drag `job-search` from Finder/File
Explorer into the chat window, or use the **+** button → add folder. You should
see the folder's name attached to the conversation before you continue.

> **Using the terminal?** `cd Documents/job-search`, then run `claude`. Setup
> works fine there, but Steps 8 and 9 need the desktop app.

---

## Step 3 — Turn on the Google connectors

1. Open **Settings** → **Connectors**
2. Enable **Gmail**, **Google Drive**, and **Google Calendar**

All three are used: Drive holds your tracker spreadsheet, Gmail is scanned for
application replies, Calendar gets your interview events. If one is off, setup
stops and tells you which — that is intended, not a crash.

---

## Step 4 — Chrome extension

Do not skip this. From Step 8 on, everything happens in your own Chrome: the
job search, the applications, and every row written to your tracker.

1. Open **Google Chrome** (Chrome only — not Edge, Safari, or Firefox)
2. Chrome Web Store → search **Claude in Chrome**
3. **Add to Chrome**
4. **Sign in to the extension**, then pin it: puzzle-piece icon → thumbtack
   next to **Claude**
5. In that same Chrome, make sure you are **signed in to LinkedIn and to
   Google** — the plugin uses your own logged-in sessions

Nothing runs on someone else's account, and nothing is posted without you.

> Extension not working? You can still finish Steps 5–7 — setup does not need
> Chrome. Come back to this before Step 8.

---

## Step 5 — Install the plugin

1. Open **Settings**
2. In the sidebar, under **Customize**, click **Plugins**
3. Click **Add** at the top right
4. **Add marketplace**
5. **Add from a repository** — the second option. Not **Browse Anthropic
   sources**, which only lists Anthropic's own plugins and will not find ours
6. Paste this:

```
https://github.com/huskar20/huskar20-plugins
```

7. Click **Install** on the **Career hunter** card

**Then quit Claude and reopen it.** Nothing works until you do.

> The card says **Career hunter** with a space. The hyphenated `career-hunter`
> is only used in commands.

> **Using the terminal?** Run
> `/plugin marketplace add huskar20/huskar20-plugins` and
> `/plugin install career-hunter`, then quit and reopen **from the same
> folder** (`cd Documents/job-search`, then `claude`).

---

## Step 6 — Check it worked

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

Plain sentences work too — the slash commands are just faster. All of these
work as typed:

```
set up career hunter
```

```
run the job hunt
```

```
find me remote data analyst internships
```

```
sync my job search
```

```
check my email for job updates
```

---

## Step 7 — The setup interview

You should still be in the `job-search` folder from Steps 1–2 — that is where
your profile gets written. Type:

```
/career-hunter:setup
```

No slash menu in your app? Type **"set up career hunter"** instead — same thing.

It interviews you: target job titles, salary floor, location, work
authorization, notice period. Answer honestly — **every application answer
comes from this profile**, so a wrong answer here goes on real forms later.

Two moments matter:

- **When it asks for a submission mode, pick `prepare`.** That is the
  try-it-safely mode: the plugin never opens or submits a form. The other two
  modes are explained in **The three modes** below — you can switch any time.
- **Salary floor** — the number below which it never even shows you a role.
  Look up a realistic entry figure for your title and city first.

Setup creates two things you own:

- `career-profile.md` — your answers, in your folder, yours to edit by hand
- a **Job_Search_Tracker** Google Sheet in your Drive, with Applications,
  Interview Notes, Contacts, and Dashboard tabs

Open the sheet and keep it in a tab. It fills up in Step 8.

---

## Step 8 — Run the hunt

```
/career-hunter:apply
```

Or just: **"run the job hunt"**.

In `prepare` mode it searches **LinkedIn Jobs, Indeed, and company career
boards** (Greenhouse, Lever, Ashby) in your Chrome, scores every role against
your profile, and writes the best matches to a queue file.

**Hunting for an internship?** If you picked **intern** or **new-grad** as your
level in Step 7, it also searches **Handshake** — the campus board where many
internships are posted nowhere else. Two things must be true first: you are
signed in to your school's Handshake in Chrome, and your resume is uploaded to
your Handshake profile.

The queue file lands here:

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

## Step 9 — Sync your inbox

After you have applied to something (today or later), type:

```
/career-hunter:sync
```

Or just: **"sync my job search"**.

It scans your Gmail since the last run and updates the tracker: application
confirmations, rejections, interview invites. Cold recruiter spam and
job-board alert noise are filtered out, not logged. A confirmed interview can
land straight on your Google Calendar, with a push notification.

This is the habit that makes the tracker worth having: **apply → sync →
Dashboard tab tells you the truth** about your funnel.

---

## The three modes

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
| Cannot find **Plugins** | Open **Settings** first — **Plugins** sits in the settings sidebar under the **Customize** heading, below **Skills** and **Connectors** |
| The repository is not in **Browse Anthropic sources** | Correct, it never will be — that list is Anthropic's own. Back up and choose **Add from a repository** |
| Setup says a connector is missing | Settings → Connectors → enable Gmail, Drive, and Calendar |
| "No browser connected" during apply | Desktop app + Claude in Chrome extension (Step 4), then click **Connect** when asked |
| Apply or sync sends you back to setup | Intended — they need the profile setup creates. Run Step 7 first, from your `job-search` folder |
| A site won't load during the hunt | Allow it in the extension's site permissions when Chrome asks |
| It skipped a role and "flagged" it | Working as intended — the form asked something your profile can't answer. The summary tells you which and why |
| The queue file is empty | Your filters may be too tight — check the salary floor and titles in `career-profile.md`, edit by hand, re-run |
| I cannot find `career-profile.md` on my laptop | Claude wrote it wherever it was pointed. Open your `job-search` folder (Steps 1–2) and re-run setup from there — or ask Claude "where did you save my career profile?" |

---

## Take home

**github.com/huskar20/huskar20-plugins**

The plugin, this handout, and **Resume forge** — the companion plugin that
builds and tailors the resume this one applies with.

**Tonight:** work through today's queue file — even two real applications beats
a perfectly configured tracker with zero rows. Then `/career-hunter:sync`
tomorrow and watch the tracker catch the confirmations.
