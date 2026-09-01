# Run Laka And Validation Rules

Extracted from the master framework. PI source keys are documented in `../08_sources/SOURCE_NOTES.md`. See the implementation notes for scope and evidence safeguards.


## 12. Standard “Run LAKA” syntax

```text
RUN LAKA
MODE: [GENERATE | SOLVE | DECODE | PREDICT | PLAN | POSITION]

ON:
[system, product, problem, event, market, message, or strategy]

FOR:
[Actor or stakeholder]

IN:
[Scenario]

FROM:
[current observable state]

TOWARD:
[ideal observable outcome]

TIME HORIZON:
[period or event sequence]

EVIDENCE:
[known data, documents, observations, assumptions]

DEPTH:
[quick scan | focused sweep | complete volume]
```

A complete output contains:

```text
1. Context envelope
2. Objective Outcomes
3. Baseline system sentence
4. Baseline volume signature
5. Key tensions and assumptions
6. High-opportunity voxels
7. Generated concept sentences
8. Constraint and failure analysis
9. Prediction trajectories
10. Strategic path
11. Positioning statement
12. Evidence gaps and confidence
```

These are prompt instructions and a reporting format, not commands already installed in an application. Mode-specific work may mark irrelevant sections “not applicable” with a reason.



## 13. Well-formedness rules

A valid LAKA concept must pass these tests:

1. The Actor and Scenario are named.
2. The Outcome is observable or measurable.
3. The current and target states are both described.
4. The claimed change level matches the actual transformation.
5. The selected meta-variable has a clear direction.
6. The Action explains how the Outcome is produced.
7. The Tool directly participates in the Action.
8. Resources enable the mechanism but are not confused with Tools.
9. Value identifies who benefits and what form the benefit takes.
10. At least one plausible Failure mode is included.
11. Feedback explains how the system learns or corrects itself.
12. Predictions include dependencies, signals, and uncertainty.
13. Paradigm ideas alter assumptions, purpose, objects, or value logic—not merely performance.
14. Empty cells are treated as research questions rather than automatic breakthroughs.

Passing these rules makes a proposal more explicit. It does not establish that it is feasible, safe, new, profitable, causally correct, or predictively accurate.
