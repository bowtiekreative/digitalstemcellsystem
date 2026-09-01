# PREDICT — LAKA Operating Playbook

**Status:** Implementation extension to the conversation’s six-mode architecture. This is a procedure to apply, not an already functioning software tool.

## Purpose

Construct conditional future sequences and testable forecasts rather than unsupported certainty.

## Inputs

Dated baseline, historical observations, Outcome definition, time horizon or event horizon, candidate drivers, and alternative scenarios.

## Procedure

1. Define an event that can be resolved as occurring or not occurring, or a quantity with a measurement rule.
2. Distinguish a desired Ideal State from an expected future state.
3. Map functional steps and dependencies; name what would have to become technically, operationally, or socially available.
4. Inspect Direction, Rate, Acceleration, Propagation, Amplification, Accumulation, and Detectability without assuming these are universally predictive.
5. Include continuation, slower adoption or stagnation, and reversal or substitution branches where relevant.
6. Specify leading indicators, disconfirming indicators, review dates, and resolution rules.
7. Use numeric probabilities only with an explicit estimation basis. Record unknown rather than inventing precision.
8. After resolution, compare forecasts with outcomes and update the method; do not rewrite earlier predictions after seeing results.

## Output

Forecast ledger, dependency map, scenario branches, leading indicators, conditions, uncertainty, review date, and resolution criteria.

## Stop condition

A usable forecast is specific enough to be checked and has stated assumptions. More elaborate stories are not necessarily more accurate.

## Critical distinction

PI describes innovation sequences rather than exact dates [PI-11]. LAKA’s probabilistic tracking and calibration requirements are additional design choices, not claims made or validated by the source.

## Run template

```text
RUN LAKA
MODE: PREDICT
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
