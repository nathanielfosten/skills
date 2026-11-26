# skills

Small, focused agent skills for design engineering, design systems, and prototyping with agents.

A skill is a folder with a `SKILL.md` file. Agents read its `name` and `description` to decide when to load it, then follow the instructions in the body. The format is the [Agent Skills](https://agentskills.io/specification) specification, so the same folder works in Claude Code, Cursor, Codex, and any other agent that reads `SKILL.md`.

## Skills

| Name | Description | Link |
| --- | --- | --- |
| audit-skills | Audit skill quality and report observed usage over the past 90 days. | [SKILL.md](skills/audit-skills/SKILL.md) |
| extract-skill | Turn completed work into a reusable skill grounded in observed results. | [SKILL.md](skills/extract-skill/SKILL.md) |

## Philosophy

**Small.** A skill should be short enough to load beside the task. If a reference is long, link a file and let the agent open it only when needed.

**Single-purpose.** One skill, one job. Split it when a second job shows up.

**Generalized.** No company names, internal URLs, or proprietary components. A skill should work on the next project without a rewrite.

## Contributing

New skills start from [`skills/_template`](skills/_template/SKILL.md). See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) © nathanielfosten
