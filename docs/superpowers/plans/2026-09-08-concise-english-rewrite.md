# Concise English Rewrite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite Shared Understanding as a concise English skill grounded in communication, analytic, uncertainty, and plain-language practice.

**Architecture:** Keep one instruction-only skill. Replace the six-part inventory and repeated caveats with one four-part disclosure and three trigger moments. Keep sources and examples outside the core file so the main protocol is immediately usable.

**Tech Stack:** Markdown, JSON, YAML metadata, Python standard-library tests.

---

The user requested direct execution. Work inline because no executing-plans skill is available, and do not use subagents. Preserve the existing private repository and user-scope symlink.

### Task 1: Make concision and English testable

**Files:**
- Modify: `tests/test_package.py`
- Test: `tests/test_package.py`

- [x] Replace the old generous size check with an 85-line core limit and add a repository-language check over the maintained text artifacts:

```python
CJK = re.compile(r"[\u3400-\u9fff]")
PUBLIC_TEXT = [ROOT / "README.md", ROOT / "evals" / "README.md", ROOT / "evals" / "cases.json", *SKILL.rglob("*")]
self.assertLessEqual(len(skill_text.splitlines()), 85)
self.assertIsNone(CJK.search(path.read_text(encoding="utf-8")))
```

- [x] Require links to both `references/examples.md` and `references/foundations.md`, and require the English display name `Shared Understanding`.
- [x] Run `python3 -m unittest discover -s tests -v`; expect failures for the current length, Chinese text, metadata, and missing foundations.

### Task 2: Replace the core with one direct protocol

**Files:**
- Modify: `skills/shared-understanding/SKILL.md`
- Modify: `skills/shared-understanding/agents/openai.yaml`
- Modify: `skills/shared-understanding/references/examples.md`
- Create: `skills/shared-understanding/references/foundations.md`

- [x] Write the complete core around this exact structure:

```markdown
# Shared Understanding

## Purpose
Expose the working model already guiding the work.

## The disclosure
- Working view
- Basis
- Assumptions and choices
- Consequences and gaps

## When to speak
- Start
- Change
- Handoff

## Rules
[direct safeguards against interrogation, boilerplate, blame, hidden reasoning, and false completion]
```

- [x] Use “observation / inference / assumption” consistently. Lead with the user-visible consequence, and scale the disclosure from one sentence to a short block.
- [x] Rewrite examples in English around sign-in persistence, cancellation semantics, evidence, correction, and trivial changes.
- [x] Document how Clark and Brennan, ICD 203, uncertainty guidance, and ISO 24495-1 informed the protocol; state that this is an adaptation, not a validated standard or endorsement.

### Task 3: Rewrite the package surface

**Files:**
- Modify: `README.md`
- Modify: `evals/README.md`
- Modify: `evals/cases.json`
- Modify: `docs/superpowers/plans/2026-08-31-shared-understanding.md`

- [x] Replace the README with a short English problem statement, one sign-in example, install/use instructions, file map, and validation boundary.
- [x] Translate and tighten all 12 evaluation fixtures without changing their IDs or coverage tags.
- [x] Translate the evaluation protocol and remove repeated rationale.
- [x] Add a short superseded marker to the original implementation plan so historical decisions are not mistaken for current design.

### Task 4: Verify and publish

**Files:**
- Test: all maintained repository files

- [x] Run:

```sh
python3 -m unittest discover -s tests -v
ruby -ryaml -e 'YAML.safe_load(File.read("skills/shared-understanding/agents/openai.yaml"))'
git diff --check
```

- [x] Confirm there are no CJK characters outside Git history and no machine-specific paths in the skill package.
- [x] Inspect the full diff and file sizes. Confirm the installed symlink still resolves to the edited skill.
- [x] Commit the rewrite and push `main`; verify local and remote commit IDs match.
