<!-- Thanks for contributing! Confirm each box before requesting review. -->

## What does this PR do?



## Checklist (see CLAUDE.md)

- [ ] Plugin lives in `plugins/<kebab-name>/` and matches its `plugin.json` `name`
- [ ] Registered in `.claude-plugin/marketplace.json` with matching `name` / `version` / `source`
- [ ] Version bumped in **both** `plugin.json` and `marketplace.json` (for changes to existing plugins)
- [ ] `python3 scripts/validate.py` passes locally
- [ ] Plugin has its own `README.md` (purpose, requirements, install)
- [ ] No personal data, secrets, tokens, document IDs, or machine-specific paths committed
- [ ] Skills use frontmatter with trigger-phrase descriptions; heavy detail lives in `references/`
- [ ] If the plugin acts on the user's behalf, it follows the safety rules in CLAUDE.md
