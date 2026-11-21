# skills

Small, focused agent skills for design engineering, design systems, and prototyping with agents.

A skill is a folder with a `SKILL.md` file. Agents read its `name` and `description` to decide when to load it, then follow the instructions in the body. The format is the [Agent Skills](https://agentskills.io/specification) specification, so the same folder works in Claude Code, Cursor, Codex, and any other agent that reads `SKILL.md`.

## Use

Copy a skill folder into the directory your agent scans. Copy the folder itself, not the root of this repository, and skip `skills/_template`.

| Agent | Personal (all projects) | Project |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Cursor | `~/.cursor/skills/` | `.cursor/skills/` |
| Codex | `~/.agents/skills/` | `.agents/skills/` |

Cursor also reads Claude and Codex skill directories. Codex also reads `~/.codex/skills/`. For any other agent, use whatever path it documents for `SKILL.md`; the file format does not change.

```bash
git clone https://github.com/nathanielfosten/skills.git
cd skills
cp -R skills/component-registry ~/.claude/skills/
```

Invoke a skill by name when you want it for the current turn: `/component-registry` in Claude Code and Cursor, `$component-registry` in Codex. Otherwise the agent loads it when the description matches the task.

## Skills

Starters. Each one states an intent; the procedure is left open.

| Name | Description | Link |
| --- | --- | --- |
| component-registry | Teach an agent to discover and use a project's component library instead of inventing UI. | [SKILL.md](skills/component-registry/SKILL.md) |
| design-system-guard | Enforce tokens, spacing, typography, and no off-brand components before finishing UI work. | [SKILL.md](skills/design-system-guard/SKILL.md) |
| prototype-brief | Turn a PM's rough request into a scoped prototype brief an agent can build. | [SKILL.md](skills/prototype-brief/SKILL.md) |

## Philosophy

**Small.** A skill should be short enough to load beside the task. If a reference is long, link a file and let the agent open it only when needed.

**Single-purpose.** One skill, one job. Split it when a second job shows up.

**Generalized.** No company names, internal URLs, or proprietary components. A skill should work on the next project without a rewrite.

## Contributing

New skills start from [`skills/_template`](skills/_template/SKILL.md). See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) © nathanielfosten
