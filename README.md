# Claude Plugins

A community marketplace of [Claude](https://claude.com) plugins — skills, agents,
and automations you can install into Claude Code or the Claude desktop app.

## Installing

Every plugin here installs the same way. There are two environments:

### Claude Code (terminal)

Run these in an **interactive** `claude` session — the `/plugin` commands aren't
available in non-interactive or embedded runs:

```
/plugin marketplace add huskar20/huskar20-plugins
/plugin install career-hunter
/plugin install resume-forge
```

Install only the ones you want; they work independently.

Then **restart Claude Code** (start a fresh session) so the plugin's skills
register. Update later with `/plugin marketplace update huskar20-plugins`.

### Claude desktop app

1. Click **Customize** in the left sidebar
2. Open the **Plugins** tab
3. Under **Personal plugins**, click **+** → **Add marketplace** → **Add from a repository**
4. Paste `https://github.com/huskar20/huskar20-plugins`
5. Click **Install** on **Career hunter** or **Resume forge**

The cards use display names with a space, so look for **Resume forge** rather
than `resume-forge`. If your version accepts the `/plugin` slash commands in
chat, the two commands above work there too.

### First thing after installing (both environments)

**career-hunter** — open or create a folder to use as your job-search workspace,
then say:

> **set up career hunter**

This one-time onboarding interviews you and builds your profile + tracker. **Run it
before** "run the job hunt" or "sync my job search" — those skills depend on the
profile and config it creates, and will send you back to setup if they're missing.

**resume-forge** — no setup step. Say:

> **build my resume**

It checks your Google Drive connector first, then either reads a resume you
already have or interviews you from scratch.

## Available plugins

| Plugin | What it does | Version |
|---|---|---|
| **career-hunter** | End-to-end job-search automation: guided onboarding builds your profile + a Google Sheets tracker, then auto-apply and Gmail-sync skills hunt roles, submit applications, keep the tracker current, and add confirmed interviews to your calendar. | 0.3.4 |
| **resume-forge** | Build, tailor, and review resumes in a single-column ATS-safe house style: writes a formatted Google Doc from an interview or an existing resume file, aims a copy at a specific job description, and audits any resume against a pre-submission checklist — without ever inventing achievements. | 0.5.4 |

The two work well together: `resume-forge` produces the resume `career-hunter`
asks you to supply, and reads its `career-profile.md` when it's there.

Each plugin has its own README under [`plugins/`](./plugins/) with full details
and requirements.

## Contributing

New plugins and improvements are welcome. Two documents govern the process:

- **[CLAUDE.md](./CLAUDE.md)** — the rules every plugin in this marketplace must
  follow (structure, writing style, safety, versioning). Read it before building.
  If you develop with Claude, it will load these rules automatically.
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** — the practical workflow: fork, branch,
  validate, open a PR.

A GitHub Action validates every pull request against the structural rules, so
check locally first:

```
python3 scripts/validate.py
```

All changes land through pull requests reviewed and approved by the repo owner —
direct pushes to `main` are blocked. See [MAINTAINERS.md](./MAINTAINERS.md) for
the governance model.

## Repository layout

```
huskar20-plugins/
├── .claude-plugin/
│   └── marketplace.json      # the marketplace manifest (lists every plugin)
├── plugins/
│   └── <plugin-name>/        # one directory per plugin
│       ├── .claude-plugin/plugin.json
│       ├── skills/…
│       └── README.md
├── scripts/validate.py       # portable structural validator (used by CI)
├── CLAUDE.md                 # rules for plugin authors
├── CONTRIBUTING.md           # contribution workflow
└── LICENSE                   # MIT
```

## License

[MIT](./LICENSE). Plugins in this marketplace are free to use and adapt. Each
plugin generates and stores its users' personal data locally on their own
machine — nothing personal is committed to this repository.
