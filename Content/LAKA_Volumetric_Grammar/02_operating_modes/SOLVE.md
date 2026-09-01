# SOLVE — LAKA Operating Playbook

**Status:** Implementation extension to the conversation’s six-mode architecture. This is a procedure to apply, not an already functioning software tool.

## Purpose

Find a workable intervention for a defined problem or dilemma.

## Inputs

Two conflicting desired Outcomes, current mechanism, hard boundaries, evidence of failure, acceptable trade-offs, and available response time.

## Procedure

1. State the conflict as: improving A appears to worsen B under Conditions C.
2. Separate observed Constraints from assumed Constraints and preferences. Physical limits and ethical requirements are not dismissed as assumptions.
3. Locate the affected internal variables and examine alternative Object definitions, Actions, Tools, Resources, and Conditions.
4. Use INVERT, TRANSFER, SUBSTITUTE, DECOUPLE, and STABILIZE to propose changes.
5. Check whether an apparent solution simply transfers costs, harms, or work to another actor or time period.
6. Test the minimum intervention against both Outcomes and monitor new Failure modes.
7. Keep a fallback and a rollback path; record why the accepted solution was chosen over alternatives.

## Output

Problem statement, assumption ledger, alternatives, chosen intervention, evidence, acceptance criteria, guardrails, and fallback.

## Stop condition

A practical solution meets the stated criteria within the accepted boundaries. A complete 700-cell sweep is not required to solve a narrow problem.

## Critical distinction

Failure to find a solution in a cell does not prove impossibility; filling a cell does not prove feasibility.

## Run template

```text
RUN LAKA
MODE: SOLVE
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
