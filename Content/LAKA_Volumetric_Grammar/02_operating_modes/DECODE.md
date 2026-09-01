# DECODE — LAKA Operating Playbook

**Status:** Implementation extension to the conversation’s six-mode architecture. This is a procedure to apply, not an already functioning software tool.

## Purpose

Describe plausible structures or mechanisms behind observable evidence.

## Inputs

The artifact or observations, provenance, dates, missing data, Scenario boundaries, and the questions the explanation must answer.

## Procedure

1. Extract what is directly observed without interpretation; attach source and locator to each observation.
2. Populate known internal variables and leave the others unknown.
3. Generate at least two materially different explanations where the evidence is underdetermined.
4. For each explanation, identify Actions, Tools, Resources, Conditions, Outcomes, Feedback, Constraints, Value, and Failure modes it would require.
5. Attach meta-variable observations only when their measurement or inference is explicit.
6. Find observations that discriminate between explanations and actively seek counterevidence.
7. Report the strongest supported explanation, alternatives, remaining ambiguity, and what evidence could change the conclusion.

## Output

Observation ledger, competing models, coordinate fingerprints, dependencies, contradictions, discriminating tests, and uncertainty.

## Stop condition

Stop when the available evidence no longer distinguishes models or when a predeclared decision threshold is reached.

## Critical distinction

A morphological fingerprint is not a unique identity, proof of intent, or evidence of guilt. Similar outputs can have different causes; correlation alone does not establish a mechanism.

## Run template

```text
RUN LAKA
MODE: DECODE
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
