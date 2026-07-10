# AGENTS

- Repo purpose: this is an OpenCode asset library for reusable workflows, skills, MCP integrations, and enterprise automations invoked through slash commands.
- Primary project-specific files live under `.opencode/` and in `opencode.json`; treat those as the main integration surface before inventing app code structure.
- The repo includes sample skills under `.opencode/skills/`; use `.opencode/skills/automation-intake/SKILL.md` as a local convention reference for future skills.
- Commands are defined under `.opencode/commands/*.md`; keep command bodies simple and have them explicitly load the matching skill when needed.
- Keep `opencode.json` minimal and prefer file-based assets under `.opencode/skills/`, `.opencode/commands/`, and `.opencode/agents/` for non-trivial additions.
- Before making code changes, inspect `git status` because untracked or user-local files may exist outside the committed tree.
- Do not assume a Node/Python/etc. toolchain unless manifests are added later. There are still no verified build, test, lint, CI, or package-manager files in the tracked tree.
- After editing `opencode.json` or files under `.opencode/`, remind the user to restart OpenCode because config and skills are loaded at startup.
