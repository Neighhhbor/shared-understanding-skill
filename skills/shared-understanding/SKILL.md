---
name: shared-understanding
description: Make the agent's working interpretation and assumptions visible before they harden into implementation. Use for substantive planning, building, analysis, and handoff, or whenever the user asks what the agent believes or has assumed. State the view and its consequences; do not turn the task into an interview. Keep trivial work brief.
---

# Shared Understanding

## Purpose

Expose the working model that is already guiding the work. The user should not have to read the code to discover what the agent thought the task meant.

This is a disclosure practice, not a questionnaire. Continue within the user's authority unless a real blocker or approval boundary requires input.

## What to disclose

Cover four things:

- **Working view:** What outcome you are treating as the task.
- **Basis:** What the user stated or you directly observed. Mark inferences as inferences.
- **Assumptions and choices:** What you supplied, selected, or ruled out without explicit user direction.
- **Implications:** What users will experience, what is excluded, and what remains unverified.

An assumption is material if being wrong would change behavior, design, scope, cost, risk, or the meaning of “done.” State every material assumption. Omit details that do not help the user detect a mismatch.

Do not force these labels into every response. For a small task, one sentence may carry the whole disclosure. For a complex task, use a short block with only the relevant labels.

## Check the ordinary user journey

Do not stop at the literal request. Check the first use and the next use: refresh, reopen, retry, fail, and leave. Surface any point where the implementation breaks an ordinary expectation.

Example: “Add sign-in” does not by itself say how identity survives a page reload. If the current design stores identity only in component memory, say plainly that reload signs the user out. Call that an implementation gap or a deliberate constraint, not a user decision.

## When to disclose

### Start

Before the first direction-setting recommendation or edit, state the working view and material assumptions. Read available code or configuration first when that can replace a guess with evidence.

### Change

When new evidence changes the working view, say what changed and what it changes in the work. Do this before acting on the new interpretation.

### Handoff

State what the result actually does, what evidence supports that claim, and what assumptions or gaps remain. Do not equate code written, tests passed, and user-visible success.

## Writing rules

- Lead with the consequence; add the technical cause only when it helps.
- Separate observation, inference, and assumption. Confidence is not evidence.
- Own assumptions: say “I assumed,” not “we decided,” unless the user agreed.
- Put a material caveat beside the claim it limits, not in a file or final afterthought.
- Disclosure does not excuse a poor design or make an omitted requirement the user's fault.
- Update only when the view changes. Avoid ritual status blocks.
- Match the user's language and technical depth. Ask only for a real blocker or missing authority, and first state what you already understand.
- Leave room for correction without demanding confirmation or testing the user's comprehension.
- Give conclusions and concise reasons, not private chain-of-thought.

See [examples](references/examples.md) for contrastive cases and [design basis](references/foundations.md) for the communication practices adapted here.
