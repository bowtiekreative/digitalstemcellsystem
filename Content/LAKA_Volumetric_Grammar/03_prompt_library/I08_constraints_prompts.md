# Constraints — 70 LAKA Prompts

**Status:** Proposed LAKA implementation material. The prompts operationalize the five user-defined change levels, ten internal variables, and fourteen meta-variables. They are not copied from the source book and have not been empirically validated.

Each entry is a question to answer, not a completed idea. Replace `[ACTOR]` and `[SCENARIO]`. An honest answer may be “not applicable,” “unknown,” or “not feasible under the stated assumptions.” The Baseline is the observed current system, even when it is already fast, automated, or structurally complex.

Coordinates use `LAKA-Cn-Inn-Mnn`. See `../05_machine_readable/axes.json` for labels. For every answer retain current state, proposed state, mechanism, evidence, uncertainty, dependencies, failure test, and reason for classification.

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
