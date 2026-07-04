# Contributing

Thanks for adding to this Claude plugin marketplace. The rules that plugins must
follow live in [CLAUDE.md](./CLAUDE.md); this file is the practical workflow.

## Workflow

1. **Fork** this repository and clone your fork.
2. **Branch:** `git checkout -b add-<plugin-name>` (or `fix-<plugin-name>-<thing>`).
3. **Build your plugin** under `plugins/<plugin-name>/` following the structure in
   [CLAUDE.md](./CLAUDE.md). New plugins start at version `0.1.0`.
4. **Register it** by adding an entry to the `plugins` array in
   `.claude-plugin/marketplace.json`.
5. **Validate locally** — this is exactly what CI runs:
   ```
   python3 scripts/validate.py
   ```
   Fix everything it reports. If you have the Claude CLI, also run
   `claude plugin validate plugins/<plugin-name>/.claude-plugin/plugin.json`.
6. **Commit** with a clear message (e.g. `Add data-cleaner plugin`), **push** to
   your fork, and **open a pull request** against `main`.

## Pull request expectations

The PR template mirrors the reviewer checklist in [CLAUDE.md](./CLAUDE.md). Before
requesting review, confirm:

- The plugin directory name, its `plugin.json` `name`, and its `marketplace.json`
  entry all match (kebab-case).
- Versions are bumped in **both** `plugin.json` and `marketplace.json` for any
  change to an existing plugin.
- No personal data, secrets, tokens, document IDs, or absolute machine paths are
  committed.
- The plugin has its own `README.md`.
- `python3 scripts/validate.py` passes.

## Changing an existing plugin

Bump its `version` (semver: patch for fixes, minor for new features, major for
breaking changes) in both manifests, and note the change in the plugin's README or
a `CHANGELOG` if it keeps one.

## Reporting problems or proposing plugins

Open an issue. For a new-plugin idea, use the "Propose a plugin" issue template.

## Testing a plugin before you PR

Point Claude at your local checkout to try it end to end:

```
/plugin marketplace add /absolute/path/to/your/claude-plugins
/plugin install <plugin-name>
```

Then exercise the skills the way a user would.
