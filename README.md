# automation-hub

Automation Hub is a collection of reusable AI-powered workflows, skills, MCP integrations, and enterprise automations that can be executed through OpenCode slash commands.

## Repository layout

- `.opencode/skills/` contains project-local OpenCode skills.
- `.opencode/commands/` contains project-local OpenCode slash commands.
- `opencode.json` registers repo-local OpenCode configuration and points sessions at `AGENTS.md`.

## Sample assets

This repo includes:
- a skill at `.opencode/skills/automation-intake/SKILL.md`
- a skill at `.opencode/skills/career-ops/SKILL.md`
- a slash command at `.opencode/commands/automation-intake.md`, available as `/automation-intake`
- a slash command at `.opencode/commands/load-interview-guide.md`, available as `/load-interview-guide`

After adding or changing OpenCode config or skills, restart OpenCode so it reloads them.
