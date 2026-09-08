# Shared Understanding

An output-first Agent Skill that makes an agent’s working interpretation and assumptions visible before they become hidden design decisions.

## The problem

You ask an agent to add sign-in to a web app. It validates credentials but keeps identity only in component memory. Reloading the page signs the user out. The agent reports “sign-in complete,” and you find the missing behavior later by reading the code or using the app.

With this skill, the agent should say:

> Credential validation works, but identity exists only in component memory. Reloading signs the user out. I introduced that limitation; it is not a requirement you chose, and I would not call the full sign-in experience complete.

The skill does not make the agent interview the user before working. It makes the view already guiding the work available for correction.

## The protocol

For substantive work, disclose:

- the outcome being treated as the task;
- what is observed versus inferred;
- assumptions and choices supplied by the agent;
- practical consequences, exclusions, and unverified claims.

Do this at the start, when the view changes, and at handoff. Keep a trivial task to one sentence. Lead with observable behavior, not implementation jargon.

## Install in Codex

This repository is currently private, so cloning it requires repository access.

```sh
gh repo clone Neighhhbor/shared-understanding-skill
cd shared-understanding-skill
skill_source="$PWD/skills/shared-understanding"
skill_destination="$HOME/.agents/skills/shared-understanding"
if [ -e "$skill_destination" ] || [ -L "$skill_destination" ]; then
  printf '%s\n' 'shared-understanding already exists; nothing was overwritten.'
else
  mkdir -p "$HOME/.agents/skills"
  ln -s "$skill_source" "$skill_destination"
fi
```

Codex follows symlinked skill directories. Restart Codex if the skill does not appear after installation. See the [official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Use

```text
$shared-understanding Add user sign-in to this web app.
```

For an existing task:

```text
$shared-understanding Present the working interpretation, evidence, assumptions,
choices, and gaps already guiding this task. Do not replace the disclosure with questions.
```

Implicit invocation is enabled, but explicit use is easier to verify during evaluation.

## Contents

- [`SKILL.md`](skills/shared-understanding/SKILL.md): the protocol loaded by the agent.
- [`examples.md`](skills/shared-understanding/references/examples.md): short contrasts.
- [`foundations.md`](skills/shared-understanding/references/foundations.md): the communication and analytic practices adapted by the skill.
- [`cases.json`](evals/cases.json): 12 behavioral evaluation fixtures.
- [`evals/README.md`](evals/README.md): the evaluation procedure and evidence boundary.

Run static package checks with:

```sh
python3 -m unittest discover -s tests -v
```

These checks validate packaging, English-only maintained text, references, and fixture structure. They do not show that a model follows the skill reliably or that a user understood a disclosure. The behavioral evaluations remain marked `not_run` until actual transcripts are collected and reviewed.

## Scope

The skill has no runtime dependencies, telemetry, hooks, or model caller. It does not replace implementation quality, testing, authorization, or safety rules. It asks for useful conclusions and reasons, not private chain-of-thought.
