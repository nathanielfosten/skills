---
name: brand-audit
description: Audits how well an artifact, experience, or proposed decision follows a company's brand guidance. Use when asked to check whether work is on-brand, review brand adherence, compare brand fit across options, or identify brand-specific changes.
---

# Brand audit

Assess the supplied work against the company's actual brand guidance. Produce an evidence-backed judgment and prioritized corrections that anyone acting for the brand can use.

## Establish the work and brand

Identify the artifact or decision under review, the company, its intended audience, purpose, channel, and relevant version or state. Use the request and accessible project context to resolve these. Ask for missing inputs when they materially affect the judgment, while continuing checks that have sufficient evidence.

Locate the brand guidance and its supporting examples. Follow the user's designated source of truth and any documented precedence or exceptions. Record source versions or dates when available. Public materials can supply examples, but their existence alone does not establish an approved rule. If no authoritative guidance is available, ask for it or offer a provisional consistency review based on identified reference work, clearly labeling that basis.

For a Brand OS collection, start with `signature-moves.md`, then consult the relevant guides under `brand/verbal/` and `brand/visual/`, plus `brand/styles/` and `brand/assets/` when exact values or approved files matter. Treat bracketed prompts, illustrative examples, and open questions as unfinished guidance. These paths are a discovery convention; other brand systems can supply the same evidence in different formats.

Resolve applicable audience, channel, campaign, product, and regional exceptions before raising a violation. If sources conflict and precedence is unclear, show the conflict and how it affects the assessment. Continue findings supported by unambiguous guidance.

## Inspect the actual experience

Read the copy or decision and inspect the artifact in its intended form using available tools. Render documents or slides when layout matters, view images, and inspect accessible interface states for websites and apps. For motion or interaction, use a recording or live behavior when available. Use source code and tokens to verify implementation details where relevant.

State exactly what was inspected, including pages, screens, states, viewport sizes, or timestamps. Disclose sampling. A screenshot supports visible findings but cannot verify unseen interactions, exact font files, or runtime behavior. Code supports implementation claims but cannot establish rendered quality by itself. Mark inaccessible or unobservable aspects as unassessed.

## Compare applicable brand decisions

Build a working set of applicable rules with their source, context, and observable evidence. Review the dimensions supported by both the artifact and the brand material.

- Audience and positioning, including whether the work serves the intended need and expresses the brand's role and promise.
- Messaging and claims, including required proof, differentiation, product names, and approved terminology.
- Voice and tone, including how delivery changes with the situation and the audience's state.
- Visual expression, including logos and assets, art direction, typography, color roles, composition, spacing, graphic elements, and effects.
- Behavior and motion, including interaction choices, transitions, timing, and documented reduced-motion treatments.
- Signature moves, including whether recognizable choices are used effectively in contexts where they fit. Their absence is a violation only when the guidance requires them for that context.

Assess the combined impression as well as individual rules. Correct token values can coexist with a composition or message that conflicts with the brand. Explain that judgment through concrete choices and cited guidance. Avoid treating personal taste or general design advice as a brand requirement. Report an independently important usability or accessibility issue with its own basis and explain any conflict with the brand guidance.

Use exact measurements only when the source and inspection method support them. Label interpretive judgments and explain the evidence. An unspecified choice remains a gap in guidance unless other applicable rules establish a mismatch.

## Report findings and corrections

Lead with a concise judgment of brand fit, the most consequential reason, and the limits of the review. Name the reviewed work and brand sources. Use qualitative conclusions by default. If the user requests a score, define the rubric, weighting, treatment of unassessed criteria, and coverage before presenting it. A numeric score must be traceable to assessed criteria.

For each actionable finding provide the following information, combining fields when that improves readability.

- The exact location in the work, such as a quoted line, page, screen element, interaction state, or timestamp.
- The observed choice and the applicable brand rule, with a source reference for each.
- Its effect on brand recognition, meaning, trust, or consistency in the stated context.
- A priority based on that effect and reach. Distinguish a documented violation from an interpretive mismatch or unresolved guidance.
- A concrete correction that preserves the artifact's purpose. Cite the rule the correction satisfies and label proposed wording or design treatments as suggestions until approved.

Group repeated instances of the same issue and identify their extent. Include a few specific choices that already express the brand well when supported by evidence, so they can be preserved during revision. List unresolved questions and unassessed dimensions that could change the judgment.

Before delivering, check that every alleged violation has an applicable rule and observed evidence, every proposed correction fits the same guidance, and inaccessible aspects have not silently passed. If no supported violations are found, state the inspected scope and remaining uncertainty.

An audit produces findings and proposed corrections. Apply edits when the current request authorizes them, then recheck the affected work against the same criteria and report what was verified. Use the user's requested report format and destination; otherwise deliver the report in chat.
