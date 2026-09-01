# PLAN — LAKA Operating Playbook

**Status:** Implementation extension to the conversation’s six-mode architecture. This is a procedure to apply, not an already functioning software tool.

## Purpose

Turn a target state into a feasible sequence of decisions and reversible experiments.

## Inputs

Current and desired system representations, decision deadline, resource budget, dependencies, stakeholders, and hard Constraints.

## Procedure

1. Express the destination as observable Outcomes and specify what must not deteriorate.
2. Compose candidate paths from the current representation to the target representation.
3. Attach prerequisite relationships and check resource conflicts, timing conflicts, and incompatible target states.
4. Prioritize early tests that provide useful learning with affordable cost and recoverable downside.
5. Assign each step an owner, required Resources, expected Outcome, Feedback signal, and decision date or event trigger.
6. Create advance, pause, pivot, rollback, and abandon conditions.
7. Review new evidence and update the path while retaining a versioned record of earlier decisions.

## Output

Roadmap, dependency table, resource allocation, decision gates, tests, owners, risks, rollback procedures, and contingency paths.

## Stop condition

The next executable step is clear and the downstream plan is appropriately conditional on evidence.

## Critical distinction

A route through conceptual coordinates is not automatically operationally possible. Validate sequencing, resources, incentives, and implementation constraints.

## Run template

```text
RUN LAKA
MODE: PLAN
ON: [SYSTEM OR QUESTION]
FOR: [ACTOR]
IN: [SCENARIO]
FROM: [OBSERVED BASELINE]
TOWARD: [OBSERVABLE OUTCOME]
TIME HORIZON: [DATE RANGE OR EVENT SEQUENCE]
EVIDENCE: [SOURCES AND ASSUMPTIONS]
DEPTH: [QUICK SCAN | FOCUSED SWEEP | COMPLETE VOLUME]
```

Preserve the user-defined axes exactly. Track unknowns, not-applicable cells, and counterevidence. PI reference keys are in `../08_sources/SOURCE_NOTES.md`.
