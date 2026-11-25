---
name: audit-skills
description: Audits agent skills for actionable instructions, supported claims, and working references, and reports observed usage over the past 90 days. Use when asked to review a skill collection, identify unfinished or misleading skills, or report how often skills are used.
---

# Audit skills

Produce an evidence-backed quality audit and a 90-day usage report for the requested skill collection. Honor a narrower quality-only or usage-only request.

## Establish scope

Locate the requested repository or installed skill directories. Inventory each `SKILL.md` by name and path. Identify authoring templates separately so their instructional placeholders do not become findings against implemented skills. Distinguish duplicate installations by source path until their identity can be established.

For usage, default to the 90 days ending at report generation time. Record the exact start and end timestamps and the user's timezone. Include events at the start and exclude events at the end. Honor an explicitly requested reporting window.

## Check quality

Read each skill and its referenced resources. Evaluate whether another agent could carry out the advertised task using the supplied instructions.

- Check required frontmatter, the match between name and directory, and whether the description identifies a concrete trigger.
- Flag unfinished procedures, empty scaffolding, and examples presented as implemented capabilities.
- Compare promised outputs with the actual procedure, scripts, and dependencies. Identify missing steps that prevent the promised result.
- Resolve relative paths from the containing file and verify local references exist. Inspect scripts and tool references against the available environment or authoritative documentation. Record inaccessible dependencies as unverified. Distinguish optional integrations from broken requirements.
- Check claims of validation, automation, or successful execution against available evidence. Treat absent evidence as uncertainty unless the content itself establishes a contradiction.
- Flag conflicting instructions, unsupported assumptions about the user's environment, or scope expansion that could cause unintended edits or external actions.

For each finding, provide the skill, file and line reference, concrete evidence, effect on execution, and a focused suggested fix. Prioritize blocked execution and misleading capabilities before wording improvements. A short skill with a complete procedure can pass.

## Measure usage

Discover accessible session history, tool-call records, or telemetry using the available tools. Inspect the source format and event semantics before counting. Use read-only access and collect only the fields needed for the report. Avoid copying unrelated chat content or secrets into the report.

Record each source's location or identifier, available date range, retention gaps, and which projects or installations it covers. If logs are unavailable, finish the quality audit and report usage as unknown with the specific missing source.

Use the strongest available evidence and label its meaning in the report.

- A structured skill-invocation event supports a call count when its documented semantics establish invocation.
- A successful tool read of a skill's instructions supports an observed load count. Inspect surrounding context to exclude reads made for audits, editing, indexing, or installation. Loading alone cannot establish completion or successful application.
- A catalog entry, mention in a prompt, recommendation, or search hit establishes availability or mention only. Exclude these from call and load counts.

Prefer invocation events when available. When only instruction loads are observable, label the metric `observed loads` and mark calls unknown. Keep these metrics distinct when both exist. Explain the counting method and its limitations.

Deduplicate exported copies of the same event using its stable identifier and source session. If identifiers are missing, establish a reliable composite key from the source format and disclose remaining ambiguity. Preserve distinct repeated invocations. Resolve relative paths using recorded working directories. Map historical names or moved files only with supporting history, and report unresolved identities separately.

For every counted event retain the timestamp, skill identity, session identifier, evidence type, source reference, and selection mode. Classify selection as explicit only when a direct user invocation can be linked to that event, automatic only when the records establish agent selection, and unknown otherwise. A user request without evidence of a subsequent call remains an unconfirmed request.

Compute per-skill totals, distinct sessions, latest observed use within the window, and explicit, automatic, and unknown selection counts. Selection counts must sum to the corresponding event total. Include every inventoried skill, including those with no observed events, and identify historical events for removed skills when present.

Use zero only for a metric that the inspected source can capture within its stated coverage. For partial coverage, label totals as observed counts within that coverage and disclose the missing period or scope. Use unknown when the source cannot establish the metric. Low observed usage alone does not establish that a skill should be removed.

## Deliver the report

Start with the collection, exact reporting window, sources, coverage, and counting method. Include a compact table with one row per skill and these columns.

| Skill | Quality findings | Calls or observed loads | Distinct sessions | Latest observed use | Explicit / automatic / unknown |
| --- | --- | --- | --- | --- | --- |

Populate the table from inspected evidence. Follow it with prioritized findings and suggested fixes, each linked to supporting files or records. State any unverified claims and unavailable usage metrics. Keep the report in chat unless the user requests a saved artifact or the task establishes a destination.

Apply changes only within the user's requested scope. Obtain approval for proposed skill deletions unless that deletion is already authorized. A report request by itself authorizes inspection and reporting.
