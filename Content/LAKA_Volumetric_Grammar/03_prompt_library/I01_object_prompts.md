# Object — 70 LAKA Prompts

**Status:** Proposed LAKA implementation material. The prompts operationalize the five user-defined change levels, ten internal variables, and fourteen meta-variables. They are not copied from the source book and have not been empirically validated.

Each entry is a question to answer, not a completed idea. Replace `[ACTOR]` and `[SCENARIO]`. An honest answer may be “not applicable,” “unknown,” or “not feasible under the stated assumptions.” The Baseline is the observed current system, even when it is already fast, automated, or structurally complex.

Coordinates use `LAKA-Cn-Inn-Mnn`. See `../05_machine_readable/axes.json` for labels. For every answer retain current state, proposed state, mechanism, evidence, uncertainty, dependencies, failure test, and reason for classification.

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
