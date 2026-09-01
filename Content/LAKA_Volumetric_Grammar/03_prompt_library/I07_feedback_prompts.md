# Feedback — 70 LAKA Prompts

**Status:** Proposed LAKA implementation material. The prompts operationalize the five user-defined change levels, ten internal variables, and fourteen meta-variables. They are not copied from the source book and have not been empirically validated.

Each entry is a question to answer, not a completed idea. Replace `[ACTOR]` and `[SCENARIO]`. An honest answer may be “not applicable,” “unknown,” or “not feasible under the stated assumptions.” The Baseline is the observed current system, even when it is already fast, automated, or structurally complex.

Coordinates use `LAKA-Cn-Inn-Mnn`. See `../05_machine_readable/axes.json` for labels. For every answer retain current state, proposed state, mechanism, evidence, uncertainty, dependencies, failure test, and reason for classification.

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
