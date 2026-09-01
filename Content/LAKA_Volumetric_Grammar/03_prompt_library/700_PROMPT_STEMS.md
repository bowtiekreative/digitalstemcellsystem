# LAKA — 700 Prompt Stems

**Status:** Proposed LAKA implementation material. The prompts operationalize the five user-defined change levels, ten internal variables, and fourteen meta-variables. They are not copied from the source book and have not been empirically validated.

Each entry is a question to answer, not a completed idea. Replace `[ACTOR]` and `[SCENARIO]`. An honest answer may be “not applicable,” “unknown,” or “not feasible under the stated assumptions.” The Baseline is the observed current system, even when it is already fast, automated, or structurally complex.

Coordinates use `LAKA-Cn-Inn-Mnn`. See `../05_machine_readable/axes.json` for labels. For every answer retain current state, proposed state, mechanism, evidence, uncertainty, dependencies, failure test, and reason for classification.


---

# Internal variable: Object

## Baseline × Object

### LAKA-C0-I01-M01 — Magnitude

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document how much a relevant physical, informational, or categorical property of the Object changes. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M02 — Rate

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document how quickly the Object moves from its current state to its target state. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M03 — Direction

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document which target state the Object moves toward, away from, or around. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M04 — Scope

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document how many Objects, populations, locations, or object types are affected. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M05 — Depth

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document whether the change touches an attribute, function, relationship, or identity of the Object. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M06 — Duration

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document how long the changed state of the Object persists. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M07 — Frequency

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document how often the Object changes state or is acted upon. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M08 — Acceleration

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document whether successive changes in the Object occur faster or slower over time. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M09 — Variability

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document how the resulting state differs across Objects and repeated instances. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M10 — Detectability

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document how an observer can detect the state of the Object and the change in it. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M11 — Reversibility

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document what is required to restore the Object or recover an equivalent useful state. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M12 — Propagation

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document how a change in one Object spreads to connected Objects. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M13 — Amplification

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document what mechanism makes an initial change to the Object produce a larger effect. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I01-M14 — Accumulation

For [ACTOR] in [SCENARIO], establish the Baseline for Object. Document what retained modifications, information, wear, or capabilities build up in the Object. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Minor Change × Object

### LAKA-C1-I01-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on how much a relevant physical, informational, or categorical property of the Object changes. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on how quickly the Object moves from its current state to its target state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on which target state the Object moves toward, away from, or around. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on how many Objects, populations, locations, or object types are affected. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on whether the change touches an attribute, function, relationship, or identity of the Object. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on how long the changed state of the Object persists. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on how often the Object changes state or is acted upon. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on whether successive changes in the Object occur faster or slower over time. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on how the resulting state differs across Objects and repeated instances. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on how an observer can detect the state of the Object and the change in it. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on what is required to restore the Object or recover an equivalent useful state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on how a change in one Object spreads to connected Objects. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on what mechanism makes an initial change to the Object produce a larger effect. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I01-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Object using this starting lens: Tune an attribute. Focus on what retained modifications, information, wear, or capabilities build up in the Object. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Major Change × Object

### LAKA-C2-I01-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on how much a relevant physical, informational, or categorical property of the Object changes. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on how quickly the Object moves from its current state to its target state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on which target state the Object moves toward, away from, or around. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on how many Objects, populations, locations, or object types are affected. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on whether the change touches an attribute, function, relationship, or identity of the Object. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on how long the changed state of the Object persists. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on how often the Object changes state or is acted upon. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on whether successive changes in the Object occur faster or slower over time. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on how the resulting state differs across Objects and repeated instances. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on how an observer can detect the state of the Object and the change in it. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on what is required to restore the Object or recover an equivalent useful state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on how a change in one Object spreads to connected Objects. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on what mechanism makes an initial change to the Object produce a larger effect. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I01-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Object using this starting lens: Replace, split, combine, or relocate the object. Focus on what retained modifications, information, wear, or capabilities build up in the Object. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Structural Change × Object

### LAKA-C3-I01-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on how much a relevant physical, informational, or categorical property of the Object changes. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on how quickly the Object moves from its current state to its target state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on which target state the Object moves toward, away from, or around. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on how many Objects, populations, locations, or object types are affected. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on whether the change touches an attribute, function, relationship, or identity of the Object. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on how long the changed state of the Object persists. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on how often the Object changes state or is acted upon. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on whether successive changes in the Object occur faster or slower over time. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on how the resulting state differs across Objects and repeated instances. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on how an observer can detect the state of the Object and the change in it. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on what is required to restore the Object or recover an equivalent useful state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on how a change in one Object spreads to connected Objects. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on what mechanism makes an initial change to the Object produce a larger effect. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I01-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Object using this starting lens: Reconfigure relationships, ownership, or boundaries around the object. Focus on what retained modifications, information, wear, or capabilities build up in the Object. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Paradigm Change × Object

### LAKA-C4-I01-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on how much a relevant physical, informational, or categorical property of the Object changes. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on how quickly the Object moves from its current state to its target state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on which target state the Object moves toward, away from, or around. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on how many Objects, populations, locations, or object types are affected. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on whether the change touches an attribute, function, relationship, or identity of the Object. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on how long the changed state of the Object persists. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on how often the Object changes state or is acted upon. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on whether successive changes in the Object occur faster or slower over time. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on how the resulting state differs across Objects and repeated instances. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on how an observer can detect the state of the Object and the change in it. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on what is required to restore the Object or recover an equivalent useful state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on how a change in one Object spreads to connected Objects. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on what mechanism makes an initial change to the Object produce a larger effect. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I01-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Object using this starting lens: Eliminate the old object or create a new object category. Focus on what retained modifications, information, wear, or capabilities build up in the Object. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.


---

# Internal variable: Conditions

## Baseline × Conditions

### LAKA-C0-I02-M01 — Magnitude

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document how far operating Conditions differ from their reference range. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M02 — Rate

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document how quickly operating Conditions change relative to the system’s response. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M03 — Direction

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document which environmental state the Conditions are approaching or leaving. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M04 — Scope

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document which operating settings, locations, or populations share the Conditions. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M05 — Depth

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document whether changed Conditions affect a surface parameter or the assumptions required for operation. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M06 — Duration

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document how long a relevant Condition remains present. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M07 — Frequency

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document how often a Condition occurs, recurs, or crosses a threshold. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M08 — Acceleration

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document whether the pace of environmental change is increasing or decreasing. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M09 — Variability

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document how predictable the Conditions are across time and locations. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M10 — Detectability

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document which Condition changes can be observed, with what delay and measurement limits. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M11 — Reversibility

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document whether the Conditions can be restored, escaped, or buffered against. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M12 — Propagation

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document how a Condition moves through a process, network, or environment. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M13 — Amplification

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document which combinations of Conditions intensify their effects on operation. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I02-M14 — Accumulation

For [ACTOR] in [SCENARIO], establish the Baseline for Conditions. Document how repeated exposure to Conditions produces a retained burden or advantage. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Minor Change × Conditions

### LAKA-C1-I02-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on how far operating Conditions differ from their reference range. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on how quickly operating Conditions change relative to the system’s response. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on which environmental state the Conditions are approaching or leaving. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on which operating settings, locations, or populations share the Conditions. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on whether changed Conditions affect a surface parameter or the assumptions required for operation. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on how long a relevant Condition remains present. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on how often a Condition occurs, recurs, or crosses a threshold. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on whether the pace of environmental change is increasing or decreasing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on how predictable the Conditions are across time and locations. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on which Condition changes can be observed, with what delay and measurement limits. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on whether the Conditions can be restored, escaped, or buffered against. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on how a Condition moves through a process, network, or environment. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on which combinations of Conditions intensify their effects on operation. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I02-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Conditions using this starting lens: Adjust tolerances. Focus on how repeated exposure to Conditions produces a retained burden or advantage. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Major Change × Conditions

### LAKA-C2-I02-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on how far operating Conditions differ from their reference range. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on how quickly operating Conditions change relative to the system’s response. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on which environmental state the Conditions are approaching or leaving. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on which operating settings, locations, or populations share the Conditions. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on whether changed Conditions affect a surface parameter or the assumptions required for operation. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on how long a relevant Condition remains present. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on how often a Condition occurs, recurs, or crosses a threshold. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on whether the pace of environmental change is increasing or decreasing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on how predictable the Conditions are across time and locations. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on which Condition changes can be observed, with what delay and measurement limits. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on whether the Conditions can be restored, escaped, or buffered against. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on how a Condition moves through a process, network, or environment. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on which combinations of Conditions intensify their effects on operation. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I02-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Conditions using this starting lens: Operate under substantially different conditions. Focus on how repeated exposure to Conditions produces a retained burden or advantage. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Structural Change × Conditions

### LAKA-C3-I02-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on how far operating Conditions differ from their reference range. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on how quickly operating Conditions change relative to the system’s response. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on which environmental state the Conditions are approaching or leaving. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on which operating settings, locations, or populations share the Conditions. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on whether changed Conditions affect a surface parameter or the assumptions required for operation. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on how long a relevant Condition remains present. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on how often a Condition occurs, recurs, or crosses a threshold. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on whether the pace of environmental change is increasing or decreasing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on how predictable the Conditions are across time and locations. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on which Condition changes can be observed, with what delay and measurement limits. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on whether the Conditions can be restored, escaped, or buffered against. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on how a Condition moves through a process, network, or environment. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on which combinations of Conditions intensify their effects on operation. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I02-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Conditions using this starting lens: Sense, adapt to, or actively engineer conditions. Focus on how repeated exposure to Conditions produces a retained burden or advantage. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Paradigm Change × Conditions

### LAKA-C4-I02-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on how far operating Conditions differ from their reference range. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on how quickly operating Conditions change relative to the system’s response. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on which environmental state the Conditions are approaching or leaving. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on which operating settings, locations, or populations share the Conditions. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on whether changed Conditions affect a surface parameter or the assumptions required for operation. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on how long a relevant Condition remains present. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on how often a Condition occurs, recurs, or crosses a threshold. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on whether the pace of environmental change is increasing or decreasing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on how predictable the Conditions are across time and locations. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on which Condition changes can be observed, with what delay and measurement limits. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on whether the Conditions can be restored, escaped, or buffered against. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on how a Condition moves through a process, network, or environment. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on which combinations of Conditions intensify their effects on operation. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I02-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Conditions using this starting lens: Remove dependence on the condition or redefine the context. Focus on how repeated exposure to Conditions produces a retained burden or advantage. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.


---

# Internal variable: Actions

## Baseline × Actions

### LAKA-C0-I03-M01 — Magnitude

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document how much work, intensity, or state change an Action produces. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M02 — Rate

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document how quickly an Action is completed or changes the target state. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M03 — Direction

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document whether the Action advances, opposes, preserves, or redefines the intended result. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M04 — Scope

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document which tasks, objects, people, and locations the Action covers. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M05 — Depth

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document whether the Action changes a parameter, mechanism, workflow, or definition of the task. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M06 — Duration

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document how long the Action or its effect lasts. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M07 — Frequency

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document how often the Action is performed and whether triggering is scheduled or event-based. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M08 — Acceleration

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document whether the rate of performing or completing Actions increases or decreases. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M09 — Variability

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document how consistent the execution and results of the Action are. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M10 — Detectability

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document how execution, completion, and side effects of the Action can be observed. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M11 — Reversibility

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document which effects of the Action can be undone and at what cost. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M12 — Propagation

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document how one Action triggers or transfers to other Actions and actors. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M13 — Amplification

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document what leverage makes one Action produce disproportionately large effects. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I03-M14 — Accumulation

For [ACTOR] in [SCENARIO], establish the Baseline for Actions. Document how repeated Actions build progress, backlog, learning, or damage. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Minor Change × Actions

### LAKA-C1-I03-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on how much work, intensity, or state change an Action produces. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on how quickly an Action is completed or changes the target state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on whether the Action advances, opposes, preserves, or redefines the intended result. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on which tasks, objects, people, and locations the Action covers. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on whether the Action changes a parameter, mechanism, workflow, or definition of the task. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on how long the Action or its effect lasts. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on how often the Action is performed and whether triggering is scheduled or event-based. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on whether the rate of performing or completing Actions increases or decreases. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on how consistent the execution and results of the Action are. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on how execution, completion, and side effects of the Action can be observed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on which effects of the Action can be undone and at what cost. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on how one Action triggers or transfers to other Actions and actors. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on what leverage makes one Action produce disproportionately large effects. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I03-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Actions using this starting lens: Optimize speed, sequence, or effort. Focus on how repeated Actions build progress, backlog, learning, or damage. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Major Change × Actions

### LAKA-C2-I03-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on how much work, intensity, or state change an Action produces. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on how quickly an Action is completed or changes the target state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on whether the Action advances, opposes, preserves, or redefines the intended result. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on which tasks, objects, people, and locations the Action covers. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on whether the Action changes a parameter, mechanism, workflow, or definition of the task. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on how long the Action or its effect lasts. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on how often the Action is performed and whether triggering is scheduled or event-based. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on whether the rate of performing or completing Actions increases or decreases. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on how consistent the execution and results of the Action are. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on how execution, completion, and side effects of the Action can be observed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on which effects of the Action can be undone and at what cost. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on how one Action triggers or transfers to other Actions and actors. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on what leverage makes one Action produce disproportionately large effects. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I03-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Actions using this starting lens: Substitute, reverse, transfer, or automate the action. Focus on how repeated Actions build progress, backlog, learning, or damage. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Structural Change × Actions

### LAKA-C3-I03-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on how much work, intensity, or state change an Action produces. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on how quickly an Action is completed or changes the target state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on whether the Action advances, opposes, preserves, or redefines the intended result. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on which tasks, objects, people, and locations the Action covers. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on whether the Action changes a parameter, mechanism, workflow, or definition of the task. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on how long the Action or its effect lasts. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on how often the Action is performed and whether triggering is scheduled or event-based. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on whether the rate of performing or completing Actions increases or decreases. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on how consistent the execution and results of the Action are. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on how execution, completion, and side effects of the Action can be observed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on which effects of the Action can be undone and at what cost. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on how one Action triggers or transfers to other Actions and actors. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on what leverage makes one Action produce disproportionately large effects. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I03-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Actions using this starting lens: Redesign the network of actions and actors. Focus on how repeated Actions build progress, backlog, learning, or damage. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Paradigm Change × Actions

### LAKA-C4-I03-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on how much work, intensity, or state change an Action produces. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on how quickly an Action is completed or changes the target state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on whether the Action advances, opposes, preserves, or redefines the intended result. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on which tasks, objects, people, and locations the Action covers. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on whether the Action changes a parameter, mechanism, workflow, or definition of the task. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on how long the Action or its effect lasts. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on how often the Action is performed and whether triggering is scheduled or event-based. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on whether the rate of performing or completing Actions increases or decreases. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on how consistent the execution and results of the Action are. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on how execution, completion, and side effects of the Action can be observed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on which effects of the Action can be undone and at what cost. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on how one Action triggers or transfers to other Actions and actors. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on what leverage makes one Action produce disproportionately large effects. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I03-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Actions using this starting lens: Eliminate the action or achieve the outcome through different logic. Focus on how repeated Actions build progress, backlog, learning, or damage. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.


---

# Internal variable: Tools

## Baseline × Tools

### LAKA-C0-I04-M01 — Magnitude

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document how much capability, precision, capacity, or output the Tools provide. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M02 — Rate

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document how quickly the Tools perform, respond, or become usable. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M03 — Direction

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document which objective the Tools optimize and which objectives they neglect. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M04 — Scope

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document which tasks, users, systems, or contexts the Tools can serve. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M05 — Depth

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document whether a Tool change affects an interface, mechanism, architecture, or need for a tool. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M06 — Duration

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document how long the Tools remain useful, available, or supported. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M07 — Frequency

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document how often the Tools operate, require attention, or need replacement. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M08 — Acceleration

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document whether the pace of Tool capability improvement or degradation is changing. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M09 — Variability

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document how Tool performance varies across operating contexts and users. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M10 — Detectability

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document how Tool state, errors, and causal contribution are observable. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M11 — Reversibility

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document how Tools can be swapped, removed, rolled back, or replaced without lock-in. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M12 — Propagation

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document how Tools and their changes are distributed or adopted across a network. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M13 — Amplification

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document how Tools multiply the effect of the same Action or Resource. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I04-M14 — Accumulation

For [ACTOR] in [SCENARIO], establish the Baseline for Tools. Document how configurations, maintenance obligations, integrations, or reusable capabilities build up. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Minor Change × Tools

### LAKA-C1-I04-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on how much capability, precision, capacity, or output the Tools provide. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on how quickly the Tools perform, respond, or become usable. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on which objective the Tools optimize and which objectives they neglect. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on which tasks, users, systems, or contexts the Tools can serve. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on whether a Tool change affects an interface, mechanism, architecture, or need for a tool. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on how long the Tools remain useful, available, or supported. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on how often the Tools operate, require attention, or need replacement. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on whether the pace of Tool capability improvement or degradation is changing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on how Tool performance varies across operating contexts and users. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on how Tool state, errors, and causal contribution are observable. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on how Tools can be swapped, removed, rolled back, or replaced without lock-in. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on how Tools and their changes are distributed or adopted across a network. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on how Tools multiply the effect of the same Action or Resource. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I04-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Tools using this starting lens: Improve precision, usability, or performance. Focus on how configurations, maintenance obligations, integrations, or reusable capabilities build up. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Major Change × Tools

### LAKA-C2-I04-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on how much capability, precision, capacity, or output the Tools provide. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on how quickly the Tools perform, respond, or become usable. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on which objective the Tools optimize and which objectives they neglect. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on which tasks, users, systems, or contexts the Tools can serve. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on whether a Tool change affects an interface, mechanism, architecture, or need for a tool. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on how long the Tools remain useful, available, or supported. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on how often the Tools operate, require attention, or need replacement. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on whether the pace of Tool capability improvement or degradation is changing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on how Tool performance varies across operating contexts and users. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on how Tool state, errors, and causal contribution are observable. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on how Tools can be swapped, removed, rolled back, or replaced without lock-in. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on how Tools and their changes are distributed or adopted across a network. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on how Tools multiply the effect of the same Action or Resource. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I04-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Tools using this starting lens: Introduce a new tool class. Focus on how configurations, maintenance obligations, integrations, or reusable capabilities build up. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Structural Change × Tools

### LAKA-C3-I04-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on how much capability, precision, capacity, or output the Tools provide. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on how quickly the Tools perform, respond, or become usable. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on which objective the Tools optimize and which objectives they neglect. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on which tasks, users, systems, or contexts the Tools can serve. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on whether a Tool change affects an interface, mechanism, architecture, or need for a tool. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on how long the Tools remain useful, available, or supported. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on how often the Tools operate, require attention, or need replacement. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on whether the pace of Tool capability improvement or degradation is changing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on how Tool performance varies across operating contexts and users. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on how Tool state, errors, and causal contribution are observable. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on how Tools can be swapped, removed, rolled back, or replaced without lock-in. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on how Tools and their changes are distributed or adopted across a network. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on how Tools multiply the effect of the same Action or Resource. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I04-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Tools using this starting lens: Create a platform, toolchain, shared system, or infrastructure. Focus on how configurations, maintenance obligations, integrations, or reusable capabilities build up. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Paradigm Change × Tools

### LAKA-C4-I04-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on how much capability, precision, capacity, or output the Tools provide. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on how quickly the Tools perform, respond, or become usable. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on which objective the Tools optimize and which objectives they neglect. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on which tasks, users, systems, or contexts the Tools can serve. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on whether a Tool change affects an interface, mechanism, architecture, or need for a tool. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on how long the Tools remain useful, available, or supported. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on how often the Tools operate, require attention, or need replacement. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on whether the pace of Tool capability improvement or degradation is changing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on how Tool performance varies across operating contexts and users. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on how Tool state, errors, and causal contribution are observable. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on how Tools can be swapped, removed, rolled back, or replaced without lock-in. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on how Tools and their changes are distributed or adopted across a network. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on how Tools multiply the effect of the same Action or Resource. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I04-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Tools using this starting lens: Make the tool ambient, invisible, autonomous, or unnecessary. Focus on how configurations, maintenance obligations, integrations, or reusable capabilities build up. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.


---

# Internal variable: Resources

## Baseline × Resources

### LAKA-C0-I05-M01 — Magnitude

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document how much information, material, energy, labor, time, or capital is required. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M02 — Rate

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document how quickly Resources are consumed, acquired, replenished, or released. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M03 — Direction

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document whether Resource flows move toward reuse, depletion, substitution, or regeneration. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M04 — Scope

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document which people, operations, and locations share or compete for Resources. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M05 — Depth

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document whether the Resource change is an efficiency tweak or a change to the input model. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M06 — Duration

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document how long Resources remain available, usable, or committed. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M07 — Frequency

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document how often Resources are needed, supplied, or replenished. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M08 — Acceleration

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document whether the rate of Resource consumption or replenishment is accelerating or slowing. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M09 — Variability

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document how predictable Resource quality, cost, supply, and demand are. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M10 — Detectability

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document how Resource availability, consumption, and hidden dependencies are measured. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M11 — Reversibility

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document whether committed Resources can be recovered, redeployed, or replaced. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M12 — Propagation

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document how Resource availability and shortages spread between connected activities. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M13 — Amplification

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document which complementary Resources multiply the usefulness of a given input. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I05-M14 — Accumulation

For [ACTOR] in [SCENARIO], establish the Baseline for Resources. Document how Resource stocks, reserves, deficits, waste, or reusable assets build up. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Minor Change × Resources

### LAKA-C1-I05-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on how much information, material, energy, labor, time, or capital is required. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on how quickly Resources are consumed, acquired, replenished, or released. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on whether Resource flows move toward reuse, depletion, substitution, or regeneration. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on which people, operations, and locations share or compete for Resources. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on whether the Resource change is an efficiency tweak or a change to the input model. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on how long Resources remain available, usable, or committed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on how often Resources are needed, supplied, or replenished. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on whether the rate of Resource consumption or replenishment is accelerating or slowing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on how predictable Resource quality, cost, supply, and demand are. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on how Resource availability, consumption, and hidden dependencies are measured. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on whether committed Resources can be recovered, redeployed, or replaced. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on how Resource availability and shortages spread between connected activities. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on which complementary Resources multiply the usefulness of a given input. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I05-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Resources using this starting lens: Reduce waste or improve efficiency. Focus on how Resource stocks, reserves, deficits, waste, or reusable assets build up. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Major Change × Resources

### LAKA-C2-I05-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on how much information, material, energy, labor, time, or capital is required. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on how quickly Resources are consumed, acquired, replenished, or released. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on whether Resource flows move toward reuse, depletion, substitution, or regeneration. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on which people, operations, and locations share or compete for Resources. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on whether the Resource change is an efficiency tweak or a change to the input model. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on how long Resources remain available, usable, or committed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on how often Resources are needed, supplied, or replenished. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on whether the rate of Resource consumption or replenishment is accelerating or slowing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on how predictable Resource quality, cost, supply, and demand are. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on how Resource availability, consumption, and hidden dependencies are measured. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on whether committed Resources can be recovered, redeployed, or replaced. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on how Resource availability and shortages spread between connected activities. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on which complementary Resources multiply the usefulness of a given input. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I05-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Resources using this starting lens: Substitute a resource or add a new source. Focus on how Resource stocks, reserves, deficits, waste, or reusable assets build up. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Structural Change × Resources

### LAKA-C3-I05-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on how much information, material, energy, labor, time, or capital is required. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on how quickly Resources are consumed, acquired, replenished, or released. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on whether Resource flows move toward reuse, depletion, substitution, or regeneration. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on which people, operations, and locations share or compete for Resources. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on whether the Resource change is an efficiency tweak or a change to the input model. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on how long Resources remain available, usable, or committed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on how often Resources are needed, supplied, or replenished. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on whether the rate of Resource consumption or replenishment is accelerating or slowing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on how predictable Resource quality, cost, supply, and demand are. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on how Resource availability, consumption, and hidden dependencies are measured. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on whether committed Resources can be recovered, redeployed, or replaced. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on how Resource availability and shortages spread between connected activities. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on which complementary Resources multiply the usefulness of a given input. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I05-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Resources using this starting lens: Create circular, shared, on-demand, or autonomous resource flows. Focus on how Resource stocks, reserves, deficits, waste, or reusable assets build up. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Paradigm Change × Resources

### LAKA-C4-I05-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on how much information, material, energy, labor, time, or capital is required. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on how quickly Resources are consumed, acquired, replenished, or released. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on whether Resource flows move toward reuse, depletion, substitution, or regeneration. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on which people, operations, and locations share or compete for Resources. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on whether the Resource change is an efficiency tweak or a change to the input model. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on how long Resources remain available, usable, or committed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on how often Resources are needed, supplied, or replenished. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on whether the rate of Resource consumption or replenishment is accelerating or slowing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on how predictable Resource quality, cost, supply, and demand are. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on how Resource availability, consumption, and hidden dependencies are measured. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on whether committed Resources can be recovered, redeployed, or replaced. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on how Resource availability and shortages spread between connected activities. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on which complementary Resources multiply the usefulness of a given input. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I05-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Resources using this starting lens: Make the system generate its own resource or convert scarcity into abundance. Focus on how Resource stocks, reserves, deficits, waste, or reusable assets build up. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.


---

# Internal variable: Outcomes

## Baseline × Outcomes

### LAKA-C0-I06-M01 — Magnitude

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document how much the observable Outcome improves or worsens relative to the baseline. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M02 — Rate

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document how quickly the Outcome is reached and at what measurement interval. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M03 — Direction

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document which desired, undesired, or neutral state the Outcome approaches. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M04 — Scope

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document which beneficiaries, use cases, and related Outcomes are affected. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M05 — Depth

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document whether the Outcome changes in degree, kind, relationship, or definition of success. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M06 — Duration

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document how long the achieved Outcome persists. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M07 — Frequency

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document how often the desired Outcome is achieved or the undesired Outcome occurs. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M08 — Acceleration

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document whether progress toward the Outcome is speeding up, slowing down, or reversing. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M09 — Variability

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document how widely Outcome performance varies across trials, people, and conditions. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M10 — Detectability

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document how the Outcome can be distinguished from activity, proxy metrics, or appearances. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M11 — Reversibility

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document whether the Outcome can be reversed and whether lost benefits can be restored. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M12 — Propagation

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document how an Outcome for one part of the system changes Outcomes elsewhere. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M13 — Amplification

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document what mechanism magnifies the benefit or harm produced by an Outcome. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I06-M14 — Accumulation

For [ACTOR] in [SCENARIO], establish the Baseline for Outcomes. Document how successive Outcomes produce retained gains, obligations, or losses. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Minor Change × Outcomes

### LAKA-C1-I06-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on how much the observable Outcome improves or worsens relative to the baseline. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on how quickly the Outcome is reached and at what measurement interval. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on which desired, undesired, or neutral state the Outcome approaches. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on which beneficiaries, use cases, and related Outcomes are affected. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on whether the Outcome changes in degree, kind, relationship, or definition of success. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on how long the achieved Outcome persists. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on how often the desired Outcome is achieved or the undesired Outcome occurs. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on whether progress toward the Outcome is speeding up, slowing down, or reversing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on how widely Outcome performance varies across trials, people, and conditions. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on how the Outcome can be distinguished from activity, proxy metrics, or appearances. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on whether the Outcome can be reversed and whether lost benefits can be restored. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on how an Outcome for one part of the system changes Outcomes elsewhere. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on what mechanism magnifies the benefit or harm produced by an Outcome. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I06-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Outcomes using this starting lens: Improve amount or quality. Focus on how successive Outcomes produce retained gains, obligations, or losses. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Major Change × Outcomes

### LAKA-C2-I06-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on how much the observable Outcome improves or worsens relative to the baseline. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on how quickly the Outcome is reached and at what measurement interval. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on which desired, undesired, or neutral state the Outcome approaches. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on which beneficiaries, use cases, and related Outcomes are affected. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on whether the Outcome changes in degree, kind, relationship, or definition of success. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on how long the achieved Outcome persists. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on how often the desired Outcome is achieved or the undesired Outcome occurs. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on whether progress toward the Outcome is speeding up, slowing down, or reversing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on how widely Outcome performance varies across trials, people, and conditions. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on how the Outcome can be distinguished from activity, proxy metrics, or appearances. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on whether the Outcome can be reversed and whether lost benefits can be restored. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on how an Outcome for one part of the system changes Outcomes elsewhere. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on what mechanism magnifies the benefit or harm produced by an Outcome. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I06-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Outcomes using this starting lens: Add new outcomes or remove significant undesired outcomes. Focus on how successive Outcomes produce retained gains, obligations, or losses. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Structural Change × Outcomes

### LAKA-C3-I06-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on how much the observable Outcome improves or worsens relative to the baseline. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on how quickly the Outcome is reached and at what measurement interval. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on which desired, undesired, or neutral state the Outcome approaches. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on which beneficiaries, use cases, and related Outcomes are affected. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on whether the Outcome changes in degree, kind, relationship, or definition of success. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on how long the achieved Outcome persists. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on how often the desired Outcome is achieved or the undesired Outcome occurs. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on whether progress toward the Outcome is speeding up, slowing down, or reversing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on how widely Outcome performance varies across trials, people, and conditions. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on how the Outcome can be distinguished from activity, proxy metrics, or appearances. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on whether the Outcome can be reversed and whether lost benefits can be restored. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on how an Outcome for one part of the system changes Outcomes elsewhere. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on what mechanism magnifies the benefit or harm produced by an Outcome. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I06-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Outcomes using this starting lens: Balance interconnected Outcomes across the system. Focus on how successive Outcomes produce retained gains, obligations, or losses. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Paradigm Change × Outcomes

### LAKA-C4-I06-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on how much the observable Outcome improves or worsens relative to the baseline. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on how quickly the Outcome is reached and at what measurement interval. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on which desired, undesired, or neutral state the Outcome approaches. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on which beneficiaries, use cases, and related Outcomes are affected. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on whether the Outcome changes in degree, kind, relationship, or definition of success. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on how long the achieved Outcome persists. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on how often the desired Outcome is achieved or the undesired Outcome occurs. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on whether progress toward the Outcome is speeding up, slowing down, or reversing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on how widely Outcome performance varies across trials, people, and conditions. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on how the Outcome can be distinguished from activity, proxy metrics, or appearances. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on whether the Outcome can be reversed and whether lost benefits can be restored. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on how an Outcome for one part of the system changes Outcomes elsewhere. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on what mechanism magnifies the benefit or harm produced by an Outcome. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I06-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Outcomes using this starting lens: Redefine the purpose, desired result, or meaning of success. Focus on how successive Outcomes produce retained gains, obligations, or losses. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.


---

# Internal variable: Feedback

## Baseline × Feedback

### LAKA-C0-I07-M01 — Magnitude

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document how strongly a Feedback signal changes the next system decision or state. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M02 — Rate

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document how quickly observations become usable Feedback and corrective action. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M03 — Direction

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document whether Feedback steers toward the stated objective or reinforces the wrong behavior. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M04 — Scope

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document which actors, decisions, processes, and Outcomes are covered by Feedback. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M05 — Depth

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document whether Feedback changes a parameter, policy, architecture, or definition of the target. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M06 — Duration

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document how long a Feedback signal influences decisions before it expires or is reconsidered. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M07 — Frequency

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document how often Feedback is collected, evaluated, and used. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M08 — Acceleration

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document whether each learning cycle increases or decreases the pace of subsequent learning. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M09 — Variability

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document how signal quality and system responses vary across repeated Feedback cycles. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M10 — Detectability

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document how missing, biased, delayed, or misleading Feedback can be detected. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M11 — Reversibility

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document how a decision or update induced by Feedback can be rolled back. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M12 — Propagation

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document how Feedback from one actor or subsystem informs other actors or subsystems. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M13 — Amplification

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document what makes a Feedback loop reinforce or dampen an initial change. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I07-M14 — Accumulation

For [ACTOR] in [SCENARIO], establish the Baseline for Feedback. Document how retained Feedback becomes knowledge, bias, model drift, or organizational memory. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Minor Change × Feedback

### LAKA-C1-I07-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on how strongly a Feedback signal changes the next system decision or state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on how quickly observations become usable Feedback and corrective action. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on whether Feedback steers toward the stated objective or reinforces the wrong behavior. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on which actors, decisions, processes, and Outcomes are covered by Feedback. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on whether Feedback changes a parameter, policy, architecture, or definition of the target. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on how long a Feedback signal influences decisions before it expires or is reconsidered. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on how often Feedback is collected, evaluated, and used. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on whether each learning cycle increases or decreases the pace of subsequent learning. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on how signal quality and system responses vary across repeated Feedback cycles. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on how missing, biased, delayed, or misleading Feedback can be detected. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on how a decision or update induced by Feedback can be rolled back. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on how Feedback from one actor or subsystem informs other actors or subsystems. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on what makes a Feedback loop reinforce or dampen an initial change. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I07-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Feedback using this starting lens: Faster and more granular. Focus on how retained Feedback becomes knowledge, bias, model drift, or organizational memory. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Major Change × Feedback

### LAKA-C2-I07-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on how strongly a Feedback signal changes the next system decision or state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on how quickly observations become usable Feedback and corrective action. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on whether Feedback steers toward the stated objective or reinforces the wrong behavior. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on which actors, decisions, processes, and Outcomes are covered by Feedback. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on whether Feedback changes a parameter, policy, architecture, or definition of the target. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on how long a Feedback signal influences decisions before it expires or is reconsidered. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on how often Feedback is collected, evaluated, and used. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on whether each learning cycle increases or decreases the pace of subsequent learning. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on how signal quality and system responses vary across repeated Feedback cycles. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on how missing, biased, delayed, or misleading Feedback can be detected. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on how a decision or update induced by Feedback can be rolled back. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on how Feedback from one actor or subsystem informs other actors or subsystems. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on what makes a Feedback loop reinforce or dampen an initial change. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I07-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Feedback using this starting lens: Automated closed loop. Focus on how retained Feedback becomes knowledge, bias, model drift, or organizational memory. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Structural Change × Feedback

### LAKA-C3-I07-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on how strongly a Feedback signal changes the next system decision or state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on how quickly observations become usable Feedback and corrective action. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on whether Feedback steers toward the stated objective or reinforces the wrong behavior. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on which actors, decisions, processes, and Outcomes are covered by Feedback. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on whether Feedback changes a parameter, policy, architecture, or definition of the target. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on how long a Feedback signal influences decisions before it expires or is reconsidered. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on how often Feedback is collected, evaluated, and used. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on whether each learning cycle increases or decreases the pace of subsequent learning. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on how signal quality and system responses vary across repeated Feedback cycles. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on how missing, biased, delayed, or misleading Feedback can be detected. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on how a decision or update induced by Feedback can be rolled back. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on how Feedback from one actor or subsystem informs other actors or subsystems. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on what makes a Feedback loop reinforce or dampen an initial change. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I07-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Feedback using this starting lens: Multiple adaptive loops across the system. Focus on how retained Feedback becomes knowledge, bias, model drift, or organizational memory. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Paradigm Change × Feedback

### LAKA-C4-I07-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on how strongly a Feedback signal changes the next system decision or state. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on how quickly observations become usable Feedback and corrective action. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on whether Feedback steers toward the stated objective or reinforces the wrong behavior. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on which actors, decisions, processes, and Outcomes are covered by Feedback. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on whether Feedback changes a parameter, policy, architecture, or definition of the target. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on how long a Feedback signal influences decisions before it expires or is reconsidered. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on how often Feedback is collected, evaluated, and used. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on whether each learning cycle increases or decreases the pace of subsequent learning. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on how signal quality and system responses vary across repeated Feedback cycles. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on how missing, biased, delayed, or misleading Feedback can be detected. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on how a decision or update induced by Feedback can be rolled back. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on how Feedback from one actor or subsystem informs other actors or subsystems. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on what makes a Feedback loop reinforce or dampen an initial change. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I07-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Feedback using this starting lens: Anticipatory or self-governing feedback that can redefine targets. Focus on how retained Feedback becomes knowledge, bias, model drift, or organizational memory. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.


---

# Internal variable: Constraints

## Baseline × Constraints

### LAKA-C0-I08-M01 — Magnitude

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document how much a Constraint restricts feasible performance, capacity, or adoption. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M02 — Rate

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document how quickly a Constraint becomes binding, changes, or is relieved. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M03 — Direction

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document whether a Constraint is tightening, loosening, shifting, or being reframed. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M04 — Scope

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document which choices, actors, tasks, and environments the Constraint applies to. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M05 — Depth

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document whether the Constraint concerns a parameter, mechanism, architecture, or underlying assumption. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M06 — Duration

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document how long the Constraint remains binding. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M07 — Frequency

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document how often the Constraint is encountered or violated. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M08 — Acceleration

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document whether the pace of tightening or relief is increasing or decreasing. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M09 — Variability

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document how the Constraint differs across contexts and how predictable those differences are. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M10 — Detectability

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document how close the system is to the Constraint and how that proximity is observed. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M11 — Reversibility

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document whether relaxing the Constraint can be reversed without unacceptable loss. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M12 — Propagation

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document how a binding Constraint in one area restricts connected areas. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M13 — Amplification

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document what dependencies intensify the impact of a Constraint. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I08-M14 — Accumulation

For [ACTOR] in [SCENARIO], establish the Baseline for Constraints. Document how successive Constraints create debt, bottlenecks, fragility, or protective boundaries. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Minor Change × Constraints

### LAKA-C1-I08-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on how much a Constraint restricts feasible performance, capacity, or adoption. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on how quickly a Constraint becomes binding, changes, or is relieved. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on whether a Constraint is tightening, loosening, shifting, or being reframed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on which choices, actors, tasks, and environments the Constraint applies to. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on whether the Constraint concerns a parameter, mechanism, architecture, or underlying assumption. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on how long the Constraint remains binding. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on how often the Constraint is encountered or violated. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on whether the pace of tightening or relief is increasing or decreasing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on how the Constraint differs across contexts and how predictable those differences are. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on how close the system is to the Constraint and how that proximity is observed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on whether relaxing the Constraint can be reversed without unacceptable loss. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on how a binding Constraint in one area restricts connected areas. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on what dependencies intensify the impact of a Constraint. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I08-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Constraints using this starting lens: Relax or optimize around it. Focus on how successive Constraints create debt, bottlenecks, fragility, or protective boundaries. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Major Change × Constraints

### LAKA-C2-I08-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on how much a Constraint restricts feasible performance, capacity, or adoption. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on how quickly a Constraint becomes binding, changes, or is relieved. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on whether a Constraint is tightening, loosening, shifting, or being reframed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on which choices, actors, tasks, and environments the Constraint applies to. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on whether the Constraint concerns a parameter, mechanism, architecture, or underlying assumption. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on how long the Constraint remains binding. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on how often the Constraint is encountered or violated. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on whether the pace of tightening or relief is increasing or decreasing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on how the Constraint differs across contexts and how predictable those differences are. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on how close the system is to the Constraint and how that proximity is observed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on whether relaxing the Constraint can be reversed without unacceptable loss. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on how a binding Constraint in one area restricts connected areas. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on what dependencies intensify the impact of a Constraint. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I08-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Constraints using this starting lens: Remove, substitute, or transfer the limitation. Focus on how successive Constraints create debt, bottlenecks, fragility, or protective boundaries. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Structural Change × Constraints

### LAKA-C3-I08-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on how much a Constraint restricts feasible performance, capacity, or adoption. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on how quickly a Constraint becomes binding, changes, or is relieved. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on whether a Constraint is tightening, loosening, shifting, or being reframed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on which choices, actors, tasks, and environments the Constraint applies to. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on whether the Constraint concerns a parameter, mechanism, architecture, or underlying assumption. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on how long the Constraint remains binding. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on how often the Constraint is encountered or violated. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on whether the pace of tightening or relief is increasing or decreasing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on how the Constraint differs across contexts and how predictable those differences are. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on how close the system is to the Constraint and how that proximity is observed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on whether relaxing the Constraint can be reversed without unacceptable loss. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on how a binding Constraint in one area restricts connected areas. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on what dependencies intensify the impact of a Constraint. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I08-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Constraints using this starting lens: Redistribute the limitation or convert it into a design rule. Focus on how successive Constraints create debt, bottlenecks, fragility, or protective boundaries. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Paradigm Change × Constraints

### LAKA-C4-I08-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on how much a Constraint restricts feasible performance, capacity, or adoption. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on how quickly a Constraint becomes binding, changes, or is relieved. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on whether a Constraint is tightening, loosening, shifting, or being reframed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on which choices, actors, tasks, and environments the Constraint applies to. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on whether the Constraint concerns a parameter, mechanism, architecture, or underlying assumption. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on how long the Constraint remains binding. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on how often the Constraint is encountered or violated. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on whether the pace of tightening or relief is increasing or decreasing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on how the Constraint differs across contexts and how predictable those differences are. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on how close the system is to the Constraint and how that proximity is observed. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on whether relaxing the Constraint can be reversed without unacceptable loss. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on how a binding Constraint in one area restricts connected areas. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on what dependencies intensify the impact of a Constraint. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I08-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Constraints using this starting lens: Reframe the system so the old constraint is no longer relevant. Focus on how successive Constraints create debt, bottlenecks, fragility, or protective boundaries. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.


---

# Internal variable: Value

## Baseline × Value

### LAKA-C0-I09-M01 — Magnitude

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document how much benefit each stakeholder receives after relevant costs and harms. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M02 — Rate

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document how quickly useful Value is delivered, realized, or lost. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M03 — Direction

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document whose interests Value serves and which type of benefit is prioritized. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M04 — Scope

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document which beneficiaries, payers, providers, and communities receive or lose Value. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M05 — Depth

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document whether the change improves an existing benefit or redefines what counts as Value. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M06 — Duration

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document how long Value lasts and who continues to receive it. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M07 — Frequency

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document how often Value is delivered or experienced. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M08 — Acceleration

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document whether the rate of Value creation or erosion increases or decreases. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M09 — Variability

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document how Value differs across beneficiaries, contexts, and repeated use. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M10 — Detectability

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document how Value can be evidenced rather than merely asserted or inferred from activity. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M11 — Reversibility

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document whether the exchange can be undone and whether stakeholders can recover their position. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M12 — Propagation

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document how Value created for one stakeholder reaches or harms others. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M13 — Amplification

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document what complementarities multiply the Value of an initial benefit. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I09-M14 — Accumulation

For [ACTOR] in [SCENARIO], establish the Baseline for Value. Document how retained benefits, trust, capabilities, obligations, or extraction build up over time. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Minor Change × Value

### LAKA-C1-I09-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on how much benefit each stakeholder receives after relevant costs and harms. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on how quickly useful Value is delivered, realized, or lost. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on whose interests Value serves and which type of benefit is prioritized. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on which beneficiaries, payers, providers, and communities receive or lose Value. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on whether the change improves an existing benefit or redefines what counts as Value. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on how long Value lasts and who continues to receive it. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on how often Value is delivered or experienced. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on whether the rate of Value creation or erosion increases or decreases. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on how Value differs across beneficiaries, contexts, and repeated use. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on how Value can be evidenced rather than merely asserted or inferred from activity. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on whether the exchange can be undone and whether stakeholders can recover their position. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on how Value created for one stakeholder reaches or harms others. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on what complementarities multiply the Value of an initial benefit. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I09-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Value using this starting lens: More value for the same beneficiary. Focus on how retained benefits, trust, capabilities, obligations, or extraction build up over time. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Major Change × Value

### LAKA-C2-I09-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on how much benefit each stakeholder receives after relevant costs and harms. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on how quickly useful Value is delivered, realized, or lost. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on whose interests Value serves and which type of benefit is prioritized. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on which beneficiaries, payers, providers, and communities receive or lose Value. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on whether the change improves an existing benefit or redefines what counts as Value. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on how long Value lasts and who continues to receive it. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on how often Value is delivered or experienced. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on whether the rate of Value creation or erosion increases or decreases. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on how Value differs across beneficiaries, contexts, and repeated use. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on how Value can be evidenced rather than merely asserted or inferred from activity. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on whether the exchange can be undone and whether stakeholders can recover their position. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on how Value created for one stakeholder reaches or harms others. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on what complementarities multiply the Value of an initial benefit. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I09-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Value using this starting lens: New beneficiary, value type, offer, or revenue logic. Focus on how retained benefits, trust, capabilities, obligations, or extraction build up over time. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Structural Change × Value

### LAKA-C3-I09-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on how much benefit each stakeholder receives after relevant costs and harms. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on how quickly useful Value is delivered, realized, or lost. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on whose interests Value serves and which type of benefit is prioritized. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on which beneficiaries, payers, providers, and communities receive or lose Value. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on whether the change improves an existing benefit or redefines what counts as Value. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on how long Value lasts and who continues to receive it. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on how often Value is delivered or experienced. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on whether the rate of Value creation or erosion increases or decreases. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on how Value differs across beneficiaries, contexts, and repeated use. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on how Value can be evidenced rather than merely asserted or inferred from activity. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on whether the exchange can be undone and whether stakeholders can recover their position. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on how Value created for one stakeholder reaches or harms others. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on what complementarities multiply the Value of an initial benefit. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I09-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Value using this starting lens: Align value across several Actors or an ecosystem. Focus on how retained benefits, trust, capabilities, obligations, or extraction build up over time. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Paradigm Change × Value

### LAKA-C4-I09-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on how much benefit each stakeholder receives after relevant costs and harms. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on how quickly useful Value is delivered, realized, or lost. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on whose interests Value serves and which type of benefit is prioritized. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on which beneficiaries, payers, providers, and communities receive or lose Value. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on whether the change improves an existing benefit or redefines what counts as Value. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on how long Value lasts and who continues to receive it. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on how often Value is delivered or experienced. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on whether the rate of Value creation or erosion increases or decreases. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on how Value differs across beneficiaries, contexts, and repeated use. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on how Value can be evidenced rather than merely asserted or inferred from activity. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on whether the exchange can be undone and whether stakeholders can recover their position. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on how Value created for one stakeholder reaches or harms others. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on what complementarities multiply the Value of an initial benefit. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I09-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Value using this starting lens: Establish a new unit, source, exchange, or philosophy of value. Focus on how retained benefits, trust, capabilities, obligations, or extraction build up over time. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.


---

# Internal variable: Failure mode

## Baseline × Failure mode

### LAKA-C0-I10-M01 — Magnitude

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document how severe the damage or loss is when the Failure mode occurs. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M02 — Rate

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document how quickly a failure develops, causes harm, and can be contained. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M03 — Direction

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document which undesirable state failure drives the system toward. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M04 — Scope

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document which components, actors, and Outcomes are affected by a failure. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M05 — Depth

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document whether failure is local, functional, architectural, or a failure of the governing assumptions. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M06 — Duration

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document how long a failure and its consequences persist. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M07 — Frequency

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document how often the Failure mode occurs or nearly occurs. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M08 — Acceleration

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document whether the rate of failure incidence or damage is increasing or decreasing. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M09 — Variability

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document how failure severity and incidence vary across conditions and instances. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M10 — Detectability

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document how early and reliably the Failure mode can be detected without excessive false alarms. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M11 — Reversibility

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document which failure effects can be repaired and which losses cannot be recovered. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M12 — Propagation

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document how a failure spreads, cascades, or remains contained. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M13 — Amplification

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document what coupling, incentives, or loops make an initial failure worse. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C0-I10-M14 — Accumulation

For [ACTOR] in [SCENARIO], establish the Baseline for Failure mode. Document how small unresolved failures accumulate into debt, wear, backlog, or systemic breakdown. Describe what is currently observed, including existing dynamics; do not assume the baseline is static or matches a sample in the grid. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Minor Change × Failure mode

### LAKA-C1-I10-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on how severe the damage or loss is when the Failure mode occurs. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on how quickly a failure develops, causes harm, and can be contained. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on which undesirable state failure drives the system toward. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on which components, actors, and Outcomes are affected by a failure. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on whether failure is local, functional, architectural, or a failure of the governing assumptions. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on how long a failure and its consequences persist. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on how often the Failure mode occurs or nearly occurs. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on whether the rate of failure incidence or damage is increasing or decreasing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on how failure severity and incidence vary across conditions and instances. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on how early and reliably the Failure mode can be detected without excessive false alarms. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on which failure effects can be repaired and which losses cannot be recovered. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on how a failure spreads, cascades, or remains contained. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on what coupling, incentives, or loops make an initial failure worse. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C1-I10-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Minor Change alternative for Failure mode using this starting lens: Reduce probability or severity. Focus on how small unresolved failures accumulate into debt, wear, backlog, or systemic breakdown. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Major Change × Failure mode

### LAKA-C2-I10-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on how severe the damage or loss is when the Failure mode occurs. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on how quickly a failure develops, causes harm, and can be contained. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on which undesirable state failure drives the system toward. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on which components, actors, and Outcomes are affected by a failure. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on whether failure is local, functional, architectural, or a failure of the governing assumptions. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on how long a failure and its consequences persist. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on how often the Failure mode occurs or nearly occurs. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on whether the rate of failure incidence or damage is increasing or decreasing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on how failure severity and incidence vary across conditions and instances. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on how early and reliably the Failure mode can be detected without excessive false alarms. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on which failure effects can be repaired and which losses cannot be recovered. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on how a failure spreads, cascades, or remains contained. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on what coupling, incentives, or loops make an initial failure worse. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C2-I10-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Major Change alternative for Failure mode using this starting lens: Prevent, detect, isolate, or recover from failure. Focus on how small unresolved failures accumulate into debt, wear, backlog, or systemic breakdown. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Structural Change × Failure mode

### LAKA-C3-I10-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on how severe the damage or loss is when the Failure mode occurs. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on how quickly a failure develops, causes harm, and can be contained. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on which undesirable state failure drives the system toward. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on which components, actors, and Outcomes are affected by a failure. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on whether failure is local, functional, architectural, or a failure of the governing assumptions. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on how long a failure and its consequences persist. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on how often the Failure mode occurs or nearly occurs. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on whether the rate of failure incidence or damage is increasing or decreasing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on how failure severity and incidence vary across conditions and instances. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on how early and reliably the Failure mode can be detected without excessive false alarms. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on which failure effects can be repaired and which losses cannot be recovered. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on how a failure spreads, cascades, or remains contained. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on what coupling, incentives, or loops make an initial failure worse. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C3-I10-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Structural Change alternative for Failure mode using this starting lens: Create graceful degradation, redundancy, resilience, or self-repair. Focus on how small unresolved failures accumulate into debt, wear, backlog, or systemic breakdown. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

## Paradigm Change × Failure mode

### LAKA-C4-I10-M01 — Magnitude

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on how severe the damage or loss is when the Failure mode occurs. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the property, comparison reference, and unit or explicit category. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M02 — Rate

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on how quickly a failure develops, causes harm, and can be contained. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify change per unit of time; distinguish throughput from latency. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M03 — Direction

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on which undesirable state failure drives the system toward. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the target and sign or categorical direction; more is not always better. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M04 — Scope

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on which components, actors, and Outcomes are affected by a failure. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Specify affected units and total eligible units; describe boundaries. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M05 — Depth

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on whether failure is local, functional, architectural, or a failure of the governing assumptions. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name exactly which layer changes and what remains invariant. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M06 — Duration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on how long a failure and its consequences persist. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define start, end, and persistence interval; distinguish duration from recurrence. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M07 — Frequency

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on how often the Failure mode occurs or nearly occurs. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Define an event and count it per observation window. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M08 — Acceleration

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on whether the rate of failure incidence or damage is increasing or decreasing. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Compare rates across time intervals; do not confuse high rate with positive acceleration. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M09 — Variability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on how failure severity and incidence vary across conditions and instances. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Give a distribution, range, or stated uncertainty across comparable observations. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M10 — Detectability

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on how early and reliably the Failure mode can be detected without excessive false alarms. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Name the observation method, delay, blind spots, and false-alarm concerns. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M11 — Reversibility

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on which failure effects can be repaired and which losses cannot be recovered. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Describe rollback steps, cost, time, and residual effects. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M12 — Propagation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on how a failure spreads, cascades, or remains contained. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify source, path, recipient, transmission mechanism, and stopping conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M13 — Amplification

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on what coupling, incentives, or loops make an initial failure worse. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the causal gain mechanism, counteracting forces, and saturation limits. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.

### LAKA-C4-I10-M14 — Accumulation

For [ACTOR] in [SCENARIO], develop a Paradigm Change alternative for Failure mode using this starting lens: Transform failure into information, resources, adaptation, or another valid state. Focus on how small unresolved failures accumulate into debt, wear, backlog, or systemic breakdown. State the current-to-target transition, the enabling mechanism, and why the actual change fits the claimed level. Identify the stock, inflow, outflow, retention, decay, and reset conditions. State evidence, assumptions, dependencies, a plausible failure, and a test; record not applicable with a reason where necessary.
