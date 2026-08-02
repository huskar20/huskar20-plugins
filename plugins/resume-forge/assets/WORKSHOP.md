# Resume Workshop — Student Handout

Work through this at your own pace. Nothing here assumes you have used Claude,
a plugin, or a terminal before.

**If anything blocks you, skip to [Lane C](#lane-c--no-laptop-no-account-no-problem)
and keep going.** You will finish the workshop either way.

---

## Before you start

| You need | Notes |
|---|---|
| A laptop | Phone works for Lane C only |
| Your resume | Any format. No resume yet? That is fine, see Step 5 |
| A Claude account | Check you can sign in **before** the session |
| Google Drive | **Required.** The plugin writes your resume there |
| Claude in Chrome extension | **Required.** Needs Google Chrome and a paid Claude plan — see below |

> **Check first.** Sign in to Claude and confirm you can open it. If you cannot,
> you are on **Lane C** — the workshop still works, you just do the writing by
> hand instead of with the tool. Nobody sits idle.

---

## Part 1 — What is a plugin?

Three words, in plain language:

**Claude** is an AI assistant. You type, it answers.

**A skill** is a set of written instructions that tells Claude how to do one
specific job properly. Not magic — a document Claude reads before it starts.

**A plugin** is a bundle of skills someone has already written and tested, that
you install once so Claude knows how to do those jobs for you.

You are installing a plugin called **`resume-forge`**. It contains three skills:

| Say this | It does |
|---|---|
| "review my resume" | Checks your resume against 35 things and tells you exactly what is wrong |
| "build my resume" | Turns an old resume, or an interview, into a properly formatted Google Doc |
| "tailor my resume to this job" | Aims a copy of your resume at one specific job posting |

### What it will not do

This matters more than what it does.

**It will never invent anything about you.** Not a number, not a tool, not a
job, not a date. If a bullet would be stronger with a number and you do not have
one, it writes `[ADD NUMBER]` and asks you. It does not guess a believable
figure.

That is deliberate. A number you cannot defend in an interview is worse than no
number at all — you are the one sitting in that room, not the tool.

It also gives **no "ATS score"**. Nobody outside the employer has their actual
scoring system, so any percentage would be invented authority. You get a list of
real findings instead.

---

## Part 2 — Install it

Two ways. Use whichever Claude you have.

### If you use Claude Code (the terminal one)

Type these two lines into a Claude session, one at a time:

```
/plugin marketplace add huskar20/huskar20-plugins
```

```
/plugin install resume-forge
```

Then **quit and reopen** Claude Code so the skills load. This step is easy to
skip and nothing will work if you do.

### If you use the Claude app (desktop or web)

1. Click **Customize** in the left sidebar
2. Open the **Plugins** tab
3. Under **Personal plugins**, click the **+** button
4. Choose **Add marketplace**
5. Choose **Add from a repository**
6. Paste this and confirm:

```
https://github.com/huskar20/huskar20-plugins
```

7. Two plugin cards appear: **Career hunter** and **Resume forge**
8. Click **Install** on **Resume forge**

> The cards show display names with a space — you are looking for
> **Resume forge**, not `resume-forge`. The hyphenated name is only used for the
> Claude Code commands above.

You should not need to restart the app; the skills become available in chat once
installed. If they do not respond, quit Claude and reopen it.

### Turn on Google Drive

The plugin writes your resume into your own Google Drive, so it needs
permission.

Open your **connector settings** and enable **Google Drive**. Installing the
plugin cannot do this for you.

If Drive is off, the plugin will stop and tell you so before asking you any
questions — that is intended, not a crash.

### Install the Claude in Chrome extension

The plugin uses this to fix the font on your finished resume and to export your
PDF. Install it before the session if you can.

1. Open **Google Chrome**
2. Go to the **Chrome Web Store** and search for **Claude in Chrome**
3. Click **Add to Chrome**
4. Sign in with your Claude account
5. Pin it: click the puzzle-piece icon, then the thumbtack next to **Claude**
6. Grant the permissions it asks for

**Check these before you try:**

| Requirement | Why it matters |
|---|---|
| **Google Chrome** | Not Edge, Brave, Safari, Firefox, or any other browser |
| **A paid Claude plan** | Pro, Max, Team, or Enterprise. A free account cannot use it |
| **A computer** | Not available on mobile |

**If any of those do not apply to you, go to [Lane B or Lane C](#lane-c--no-laptop-no-account-no-problem).**
You are not stuck — the writing is the part that matters, and it works on paper.

Without the extension, two things fall to you by hand, about ten seconds each:

- Your resume may arrive in **Arial** — select all, then pick Calibri
- Export the PDF yourself: File → Download → PDF Document

---

## Part 3 — Use it

### Step 1 — Review what you already have

Open a Claude session and say:

> **review my resume**

Attach or paste your current resume when it asks.

You will get back a list of findings, each one quoting the actual line that
failed and why. Not "improve your bullets" — the specific sentence.

**Read them. Do not fix them yet.** Notice how many are about the same handful
of habits.

### Step 2 — Fix the top three

Pick the three worst findings and fix them yourself, by hand. Use this shape:

> **strong verb + what you did + the tool you used + the result**

Before:

```
Responsible for monitoring security logs and escalating issues.
```

After:

```
Monitored and triaged alerts across Splunk, escalating confirmed incidents.
```

Rules while you rewrite:

- **One line per bullet.** About 100 characters. If it runs to two, cut the part
  that is not doing work.
- **No dashes inside a sentence.** Use a comma or a full stop. Mid-sentence
  dashes are the loudest sign a computer wrote it, and recruiters notice now.
- **Do not force a number into every bullet.** Some, not all. Sixteen bullets
  all ending in a percentage reads as invented even when every figure is true.

### Step 3 — Find your numbers

Most people have numbers and have never counted them. Ask yourself:

| Question | Examples |
|---|---|
| How many? | Tickets, users, students, machines, records |
| How often? | Per day, per week, per semester, per shift |
| How much faster? | "40 minutes to 12" beats "faster" |
| How much bigger? | A percentage, or the raw before-and-after |
| How many people? | Team size, students taught, people trained |
| Over how long? | Four semesters. Two years |

An honest estimate you can defend is fine. "Roughly 900 tickets" is a real
number. Do not round it up to sound better.

### Step 4 — Rebuild it properly

Once your bullets are stronger:

> **build my resume**

It will ask for your target job title, how many years of experience you have,
and your contact details, then write a formatted Google Doc into your Drive.

Two things it does that are easy to miss:

- **Your section order changes with experience.** As a student, Education goes
  directly under your summary — a recruiter screening interns filters on school,
  major, and graduation date first. With three or more years of work, experience
  leads instead.
- **It will not generate the PDF for you.** Google Docs does that in two clicks
  (File → Download → PDF Document), a stored PDF goes stale the moment you edit
  the Doc, and a PDF cannot be reliably written into Drive from here. Export it
  yourself when you are ready to send.

### Step 5 — No resume yet?

Start from the blank template instead:

**[Resume_Template_Clean.docx](Resume_Template_Clean.docx)**

Open it in Word, Pages, or Google Docs (File → Open → Upload), and type over the
placeholders. Then run **build my resume** and hand it that file.

Want to see a finished one first?

**[SoftwareEngineer_AlexMoreno.docx](SoftwareEngineer_AlexMoreno.docx)**

Alex Moreno is not a real person. Study how the bullets are written. Do not copy
them into your own resume — the whole point is that yours has to be true.

### Step 6 — Aim it at a real job

Find one posting you would actually apply to. Then:

> **tailor my resume to this job**

Paste the posting. You get a coverage table showing which of their requirements
your resume already demonstrates, which you have but describe differently, and
which are genuinely missing.

The missing ones come back as **questions**, not edits. If you have the
experience, say where and it gets added. If you do not, leave it — a claim you
cannot defend costs more than a missing keyword.

---

## Lane C — No laptop, no account, no problem

Everything that matters here works on paper.

1. **Take the printed template** (or write on your existing resume)
2. **Pick your four weakest bullets** — the ones starting "Responsible for" are
   always the weakest
3. **Rewrite each one:** strong verb + what you did + the tool + the result
4. **Get each to one line**
5. **Run the ten checks below** on your own resume, then swap with the person
   next to you and run them on theirs

Do this and you have done the most valuable 80% of the session. The tool is a
faster way to find these problems, not a different set of problems.

---

## The ten checks

Run these on any resume, yours or a friend's, with or without a computer.

- [ ] Your name is the biggest text on the page, in title case — `First Last`, not `FIRST LAST`
- [ ] A **bold job title line** sits under your contact info, naming the job you *want*
- [ ] Summary is 2–4 sentences, no "I", no "hardworking and motivated"
- [ ] Skills are **grouped** by category, not one long comma list
- [ ] Every bullet opens with a strong verb
- [ ] At least four bullets across the resume contain a number
- [ ] Every bullet fits on one line
- [ ] No dashes in the middle of a sentence
- [ ] No italic anywhere, no tables, no columns, no photo
- [ ] One page, saved as `JobTitle_FirstNameLastName.pdf`

---

## When it does not work

| What you see | What to do |
|---|---|
| The skills do not respond | You did not restart. Quit Claude fully and reopen |
| "Drive is not connected" | Enable the Google Drive connector in settings, then try again |
| Cannot find plugin settings | Menu wording varies by version. Ask — do not hunt |
| Cannot sign in at all | Go to Lane C. You lose nothing important |
| It asks for a number you do not have | Correct behaviour. Give it a real estimate or tell it to leave the placeholder |
| **My resume is in Arial, not Calibri** | Google Docs sometimes drops the font when it imports. Select all (Cmd/Ctrl+A), open the font menu, pick Calibri. Ten seconds |
| No PDF appeared | Correct — the plugin does not make one. File → Download → PDF Document |
| The output feels generic | Give it more to work with. It cannot invent detail you did not provide |

---

## Take home

Everything from today lives here:

**github.com/huskar20/huskar20-plugins**

- The blank template
- The worked example
- This handout
- The plugin itself

**Tonight, do one thing:** rewrite the four bullets you did not get to. Twenty
minutes now beats a perfect resume you never finish.
