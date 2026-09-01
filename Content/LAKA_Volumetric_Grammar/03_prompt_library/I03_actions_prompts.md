# Actions — 70 LAKA Prompts

**Status:** Proposed LAKA implementation material. The prompts operationalize the five user-defined change levels, ten internal variables, and fourteen meta-variables. They are not copied from the source book and have not been empirically validated.

Each entry is a question to answer, not a completed idea. Replace `[ACTOR]` and `[SCENARIO]`. An honest answer may be “not applicable,” “unknown,” or “not feasible under the stated assumptions.” The Baseline is the observed current system, even when it is already fast, automated, or structurally complex.

Coordinates use `LAKA-Cn-Inn-Mnn`. See `../05_machine_readable/axes.json` for labels. For every answer retain current state, proposed state, mechanism, evidence, uncertainty, dependencies, failure test, and reason for classification.

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
