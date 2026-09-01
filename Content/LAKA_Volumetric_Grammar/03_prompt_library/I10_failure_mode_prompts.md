# Failure mode — 70 LAKA Prompts

**Status:** Proposed LAKA implementation material. The prompts operationalize the five user-defined change levels, ten internal variables, and fourteen meta-variables. They are not copied from the source book and have not been empirically validated.

Each entry is a question to answer, not a completed idea. Replace `[ACTOR]` and `[SCENARIO]`. An honest answer may be “not applicable,” “unknown,” or “not feasible under the stated assumptions.” The Baseline is the observed current system, even when it is already fast, automated, or structurally complex.

Coordinates use `LAKA-Cn-Inn-Mnn`. See `../05_machine_readable/axes.json` for labels. For every answer retain current state, proposed state, mechanism, evidence, uncertainty, dependencies, failure test, and reason for classification.

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
