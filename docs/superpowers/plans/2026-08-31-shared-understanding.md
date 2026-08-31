# Shared Understanding Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Deliver one installable skill that keeps the agent's working understanding, evidence, assumptions, and changes legible to the user throughout a task.

**Architecture:** A standalone, instruction-only Agent Skill, with optional Codex display metadata, concrete examples, and human-scored behavioral evaluation cases. Repository tests check package structure, not whether a model or user actually understands anything.

**Tech Stack:** Markdown, JSON, YAML metadata, Python standard-library unittest, Git/GitHub.

---

## Product clarification

This is output-first presentation of the agent's already-formed working understanding, not an interview, Socratic questioning, or a decision-approval workflow. The agent presents interpretation, evidence, inference, assumptions, adopted choices, and resulting boundaries without requiring user input. Corrections are welcome but are not a ritual prerequisite. Completeness covers every premise that materially shapes the result, even for low-risk tasks, using layered presentation rather than exposing private chain-of-thought. Existing authorization requirements remain separate and unchanged.

## Execution choice and boundaries

The user requested implementation, so proceed inline in this task without a separate planning approval round. The named executing-plans skill is unavailable in this session; follow this checklist directly, with visible checkpoints. No subagents or external model evaluations are required for v0.1.0.

Use the existing empty repository. Create only the new skill package and supporting documentation. Publish to a new private repository named `shared-understanding-skill` on the authenticated personal GitHub account if that name is free. Do not publish other projects, conversations, memory, local paths, or credentials. Do not change global agent instructions. Install only the new skill via a non-overwriting symlink.

## Files and responsibilities

- `skills/shared-understanding/SKILL.md`: complete core behavior; no scripts or tools required during use.
- `skills/shared-understanding/agents/openai.yaml`: optional Codex name, prompt, and implicit invocation policy.
- `skills/shared-understanding/references/examples.md`: compact good/bad examples and a multi-turn correction example.
- `README.md`: Chinese-first purpose, scope, installation, invocation, limitations, and upstream format references.
- `evals/cases.json`: twelve isolated and multi-turn test scenarios with observable pass/fail criteria.
- `evals/README.md`: manual paired evaluation protocol and honest validation status.
- `tests/test_package.py`: deterministic package tests, using only the Python standard library.
- `.gitignore`: exclude local evaluation transcripts and temporary Python files.

## Task 1: Package checks first

- [x] Add unittest cases for required frontmatter, name-directory consistency, bounded skill size, optional metadata, example reference, JSON case schema, unique scenario identifiers, and evaluation coverage.
- [x] Run `python3 -m unittest discover -s tests -v`; confirm failure because the skill package does not yet exist.

## Task 2: Core behavior and examples

- [x] Write the skill with five invariants: working interpretation is visible; facts and assumptions stay distinct; implications use the user's language; meaningful changes are announced before dependent action; completion preserves unresolved limits.
- [x] Require layered working-view summaries rather than hidden chain-of-thought, explanations rather than status chatter, and correction uptake rather than routine permission requests. Make questions exceptional, not the default output.
- [x] Keep ordinary clear tasks direct; compress summaries for short tasks and disclose meaningful assumptions even when confidence is high or the task is low-risk. Distinguish provisional user interpretations from established shared agreement.
- [x] Add examples for low-risk semantic assumptions, unsupported confidence, mid-task drift, corrections, delegation, unavailable services, and handoff limitations.
- [x] Add optional metadata with the exact `$shared-understanding` invocation.

## Task 3: Evaluation material and user instructions

- [x] Add twelve cases covering opening, ordinary low-risk assumptions, mid-task changes, correction, carry-over, closeout, explicit delegation, audience adaptation, trivial tasks, fact discovery, and chain-of-thought boundaries.
- [x] Document paired baseline/skill runs with identical inputs, transcript capture, evidence-based scoring, and separation of package validity from behavioral effectiveness.
- [x] Document non-overwriting local installation, explicit invocation, optional project reminder, and that implicit selection is not guaranteed across turns or hosts.
- [x] Run `python3 -m unittest discover -s tests -v` and `git diff --check`.

## Task 4: Install and publish

- [x] Check that the personal skill destination does not exist, then symlink this repository's skill directory into the user skill discovery directory.
- [x] Verify the link resolves to the authored skill; do not claim runtime activation from filesystem presence alone.
- [ ] Review the exact tracked file list and scan for private paths/credentials before committing.
- [ ] Create the private GitHub repository without overwriting an existing remote; push the initial commit.
- [ ] Verify remote privacy, default branch, and remote commit identity.
- [ ] Hand off the repository URL, local skill entry, invocation text, and what has/has not been tested.
