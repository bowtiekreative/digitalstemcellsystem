# Proposed LAKA Decision Rubric

**Provenance:** This rubric is a new LAKA implementation choice. It is not the source book’s Opportunity Score and has not been empirically validated.

## Hard gates first

Check required permissions and safety, hard resources, required Outcomes, and physical/logical consistency. A failed hard gate prevents selection as presently designed. An unknown gate puts the concept on hold for investigation. A high score cannot compensate for a disqualifying condition.

## Comparison criteria

| Criterion | Weight |
|---|---:|
| Outcome contribution | 25% |
| Feasibility | 20% |
| Evidence | 15% |
| Adoption | 15% |
| Differentiation | 10% |
| Reversible learning | 10% |
| Robustness | 5% |

Rate each from 0 to 4 using the stated anchors in `../05_machine_readable/scoring_rubric.json`. Every rating needs a written reason and an evidence reference or explicit judgment label. Do not give an unknown criterion a zero merely to complete the arithmetic.

```text
Comparison index = 100 × sum(weight × rating / 4)
```

All ratings must be present before calculating this index. Any alternative weighting or omission must be explicitly documented and versioned before comparing candidates. The result is a decision aid, not a probability, a calibrated forecast, or an objective measure of innovation.

A small difference between candidates may not be meaningful. Recheck the ranking under plausible changes to weights and uncertain ratings. Keep dimension-level ratings visible, since a single score can hide tradeoffs. Compare only candidates evaluated for the same Actor, Scenario, time horizon, and required Outcomes.

## Separate source concept

The book defines its Opportunity Score as the absolute difference between Importance and Satisfaction [PI-17, PDF page 167; printed page 170]. Do not present the weighted LAKA rubric above as that source formula. Under-served and over-served Outcomes imply different possible responses, so retain the direction of the difference in descriptive notes even when an absolute gap is displayed.
