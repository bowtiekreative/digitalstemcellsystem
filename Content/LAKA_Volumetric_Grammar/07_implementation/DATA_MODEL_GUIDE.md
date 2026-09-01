# Data Model and Validation Guide

**Status:** Proposed implementation contract, not a running reasoning engine.

## Files

`axes.json` holds exact vocabulary and stable codes. `internal_grid.json` holds the 50 internal-variable/change-level prompts. `operators.json` defines the 17 operators. `laka_run.schema.json` defines a draft run record. `blank_run.json` is an unfilled but structurally valid record. The support example is in `../06_examples/customer_support_run.json`.

The 700 prompt records are in `../03_prompt_library/700_prompt_stems.json`. A coordinate ID identifies a type of question, not one universal answer. Different Actors, Scenarios, versions, and hypotheses can share a coordinate.

## Record hierarchy

```text
Run
  Context
  Baseline: all ten internal variables
  Evidence records
  Concepts
    System sentence and ten-variable state
    Transformations with coordinate, states, operators, and mechanism
    Expected Outcomes and measurement definitions
    Dependencies
    Tests, stop conditions, and rollback
    Evidence references and uncertainty
```

Unknown text fields use JSON `null` where allowed. Empty arrays mean no records have been entered; they do not prove no evidence or alternatives exist. Preserve rejected concepts and earlier forecast versions in a separate version history rather than silently deleting them.

## Validation layers

JSON Schema checks required keys, types, allowed codes, and record shapes. It cannot verify scientific plausibility, actual evidence, a unique explanation, market novelty, or correct change-level classification.

Application-level checks must also verify unique run/concept/transformation/evidence IDs, valid evidence references, appropriate Scenario comparisons, meaningful measurement definitions, and consistent dependencies. Human or domain review remains necessary for semantic claims.

## Suggested recursive rule

Recurse into a child Scenario when an unresolved mechanism materially blocks the decision. Give the child a parent ID, narrower scope, interface, evidence requirement, and stopping rule. Close it when the required decision is supported, the analysis budget is reached, or new evidence is necessary. A child volume does not by itself create evidence for its parent.

## Suggested relationship record

```json
{
  "from_transformation": "T-001",
  "to_transformation": "T-002",
  "relationship": "enables",
  "mechanism": "Describe the enabling mechanism.",
  "delay": null,
  "evidence_ids": [],
  "uncertainty": "Not established."
}
```

This relationship extension is illustrative and is not part of the current run schema. Version the schema before adding it to validated run records. Useful relationship types include requires, enables, inhibits, conflicts_with, substitutes_for, and feeds_back_to. Pairwise compatibility is not sufficient to establish whole-system compatibility.
