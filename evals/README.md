# Behavioral evaluation

Status: `not_run`.

The repository contains 12 fixtures, not 12 successful evaluations. Keep three kinds of evidence separate:

1. **Package validity:** metadata, links, and fixture structure are valid.
2. **Agent behavior:** the agent discloses the working view without turning the task into an interview.
3. **User outcome:** a reader can identify the behavior, assumptions, and limits without inspecting the implementation.

`python3 -m unittest discover -s tests -v` establishes only the first.

## Minimal paired evaluation

- Use the same model, settings, tools, and project context for both runs.
- Start two clean sessions per case: baseline and explicit `$shared-understanding`.
- Give the agent the case `context`, then send each item in `turns`. Do not reveal the rubric or later turns in advance.
- Treat fixtures as simulations. Do not run tools or claim tool results unless the case supplies them.
- Preserve actual earlier responses in multi-turn cases.
- Store transcripts, model settings, date, and skill commit under `evals/runs/`. Remove private project information before publishing results.
- Score every `must` and `must_not` item with quoted evidence. Missing evidence is not a pass.

## Scoring

Rate each dimension 0, 1, or 2:

- **Visible view:** the adopted task interpretation is explicit.
- **Epistemic clarity:** observations, inferences, and assumptions are distinct.
- **Practical meaning:** implementation choices are translated into user-visible effects.
- **Coverage:** material assumptions and ordinary-use gaps are included.
- **Repair:** changed or corrected views change the stated course of action.
- **Input burden:** useful disclosure does not depend on answering routine questions.

Treat fabricated evidence, fabricated agreement, unauthorized action, question-only responses, and disclosure used to excuse a known defect as severe failures. Record length and unnecessary question count so verbosity cannot inflate the score.

This repository includes no model runner or automatic judge. Examples are design targets, not evaluation evidence.
