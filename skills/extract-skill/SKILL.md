---
name: extract-skill
description: Turns a completed task into a reusable agent skill grounded in the actual workflow and verified results. Use when asked to capture a workflow, extract a skill from a chat or project, or preserve a successful procedure for future tasks.
---

# Extract skill

Create or improve one focused skill from completed work. Preserve the decisions and procedures that another agent would need to repeat the result.

## Establish the source

Use the task, chat, repository, or artifacts the user identifies. When the request follows completed work in the current conversation, use that work as the source. Inspect relevant instructions, final changes, tool results, and validation evidence. Use connected history tools when the source is another accessible chat.

Identify the original request, successful outcome, required inputs, consequential decisions, failures and recoveries, and verification performed. Separate observed outcomes from proposed steps or untested claims. If missing evidence prevents a usable procedure, ask for the specific missing source or fact. A partial task may support a smaller completed workflow.

Identify the destination from the user's request and project context. Follow repository contribution instructions and inspect existing skills for overlap. Extend an existing skill when the extracted procedure belongs to its advertised task. Create a new skill when it has a distinct trigger and outcome. If the user requests only a proposal or draft, deliver that scope.

## Extract the reusable procedure

Choose the smallest coherent task whose result can be checked. Retain useful ordering constraints, decision criteria, required inputs, and verification steps. Include a recovery only when the source demonstrates the failure condition and a successful response.

Generalize project-specific details into inputs or discovery steps. For example, resolve the active repository and its remote from local configuration before describing a push. Preserve a specific command or tool identifier only when its existence and role are established. State genuine environment dependencies and how to identify them.

Omit exploratory dead ends and incidental preferences unless they affect future decisions. Carry user preferences into a personal skill when their intended scope is clear. Shared skills should express such choices as task inputs. Authorization for a past action applies to that task; future actions must follow the current request and permissions.

If the source contains only a generic action with no reusable guidance, explain the evidence gap before creating a new file. When a coherent procedure exists but broader applicability is untested, keep the scope narrow and disclose that limitation.

## Write the skill

Create a directory named with lowercase words joined by hyphens, matching the frontmatter `name`. Use the repository's template when supplied and replace its scaffold guidance completely.

Write a `SKILL.md` with these elements, using only as much structure as the workflow needs.

- A frontmatter `name` and a concise `description` stating the capability and concrete requests that should trigger it.
- The expected result and inputs the agent must obtain or discover.
- An actionable procedure with the decision criteria established by the source.
- Checks that demonstrate completion and any specific limitations on the procedure.

Add a short example only when it clarifies a consequential decision or expected output. Generalize sensitive details and label illustrative examples accurately. Keep secrets, personal data, internal URLs, and proprietary material out of shared skills.

Add scripts only for repeated operations that benefit from deterministic execution, and run them on safe representative inputs. Add reference files only when necessary detail would otherwise overwhelm the entrypoint, and link them where needed. Use available skill-authoring guidance when it helps with formatting or validation. Keep the skill usable without assumed access to the original chat.

## Validate and deliver

Check frontmatter, naming, local links, referenced resources, and unfinished scaffolding. Run an available skill validator and disclose any unavailable checks.

Walk through the procedure against the original task. Confirm that the supplied inputs and instructions are sufficient to reach the observed result. Check a relevant variation, such as a missing dependency or a different project path, when the instructions claim to support it. Distinguish a walkthrough from an executed test. Exercise safe local steps where practical and evaluate external mutations through available evidence or an isolated fixture unless current authorization covers them.

Review each mandatory instruction against the evidence or a genuine technical requirement. Revise unsupported requirements and promises. Update the repository's skill index when applicable.

Deliver the skill location, intended trigger, workflow captured, source evidence used, and checks actually performed. Keep source provenance in the delivery summary unless the repository requires it in an artifact. State remaining uncertainties. Follow the user's established commit and publication preferences for the current work.
