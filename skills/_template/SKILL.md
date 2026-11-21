---
# Required. 1–64 characters. Lowercase letters, numbers, and hyphens only.
# Must match this skill's directory name. No leading, trailing, or doubled hyphen.
# Do not use the reserved words "anthropic" or "claude". No XML tags.
name: skill-name

# Required. 1–1024 characters. No XML tags.
# This is the trigger. Agents load only `name` and `description` at startup
# and use them to decide whether to read the rest of this file. Write in the
# third person. Say what the skill does and when to use it, in words a person
# would actually use for the task.
description: Does one specific thing for design-engineering work. Use when the user asks to do that thing, or is about to do it without the constraint this skill exists to apply.

# Optional. An SPDX identifier, or a path to a bundled license file.
# license: MIT

# Optional. Up to 500 characters. Omit unless the skill needs a specific
# product, package, or network.
# compatibility: Requires a repository on disk.

# Optional. A map of string keys to string values.
# metadata:
#   author: your-name
#   version: "0.1"

# Optional and experimental. A space-separated list of tools the skill may
# use without asking. Support varies by agent.
# allowed-tools: Read
---

# Skill name

Template. Copy `skills/_template` to `skills/<name>`, set `name` above to that directory, and replace this file. `name` and `description` are the only required frontmatter fields. The description is the trigger; everything below is loaded only after the skill is selected.

## When to use

The finer cut, once the skill is already loaded. Name the cases that should trigger it and the neighboring cases that belong to a different skill.

- Use when …
- Do not use when …

## Instructions

The procedure, and nothing the agent can already infer. Number the steps. Prefer constraints and a sequence over an essay.

Keep this file short. Point at sibling files instead of pasting them: `examples/` for a sample input and the output you expect, `references/` for detail the agent should open only when the step needs it, `scripts/` for a command that must run the same way every time.

## Examples

One or two concrete cases. A short inline example is enough; a longer one belongs in `examples/` and should be linked from here.

## Gotchas

The mistakes this skill exists to prevent. If you removed something company-specific while generalizing, restate the lesson as a rule that still holds on the next project.
