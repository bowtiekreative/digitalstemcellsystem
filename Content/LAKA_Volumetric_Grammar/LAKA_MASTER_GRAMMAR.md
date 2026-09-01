# LAKA Volumetric Grammar — Master Specification

**Version:** 1.0-draft  
**Framework origin:** The user’s original LAKA columns, internal variables, and fourteen meta-variables.  
**Document basis:** The LAKA framework developed in this conversation, inspired by the user-supplied *Predictive Innovation: Core Skills* by Mark Proffitt. [PI-01]

**Status and provenance:** This is a proposed reasoning and design framework, not an empirically validated prediction system. All fifteen sections from the conversation are included. Packaging adds explicit attribution and qualifications where the draft could otherwise be read as a scientific guarantee. Original illustrative state ladders are retained. Operational safeguards, prompt stems, schemas, and templates are new implementation material and are identified as such. The complete ZIP includes the source book unchanged for reference; the framework-only ZIP omits the book.

The direction is not to copy Predictive Innovation’s grid, but to use its idea-space logic as inspiration for LAKA. Predictive Innovation organizes innovation through Actors, Desires, Scenarios, Alternatives, Outcomes, and Elements. [PI-02] Its core descriptive model uses Outcomes, Elements, and Alternatives as three dimensions of a system. [PI-03]

LAKA proposes a **bidirectional volumetric grammar**:

> LAKA does not only generate ideas. It represents a system, decodes an existing system, generates alternatives, diagnoses problems, develops conditional predictions, constructs strategies, and positions an offering.

“Bidirectional” means that the same representation can be used to compose candidate systems and to describe possible explanations of observed systems. It does not promise a unique reverse solution.

## Contents

1. The central architecture
2. The outer context envelope
3. Why it is a grammar
4. State transitions replace Begin State and End State
5. The five LAKA change modes
6. The 5 × 10 internal grammar matrix
7. The fourteen dynamic modifiers
8. The formal LAKA concept grammar
9. Movement through the volume
10. The transformation operators
11. The six LAKA operating modes
12. Standard “Run LAKA” syntax
13. Well-formedness rules
14. Example of the complete grammar
15. LAKA applied to itself

---

## 1. The central architecture

### The LAKA core volume

The three main axes are:

| Axis | Dimension | Count |
|---|---|---:|
| X | Change level | 5 |
| Y | Internal system variable | 10 |
| Z | Meta-variable | 14 |

**5 × 10 × 14 = 700 base voxels per Scenario.**

A voxel is not automatically a finished idea. It is a structured question, possibility, hypothesis, observation, or transformation.

For example:

```text
Structural Change × Feedback × Acceleration
```

Produces a question such as:

> How could the feedback architecture be redesigned so that learning accelerates as more evidence enters the system?

Another coordinate:

```text
Paradigm Change × Value × Direction
```

Produces:

> What happens when the definition of value changes, rather than merely increasing the amount of existing value?

---

## 2. The outer context envelope

Actors, desires, and scenarios should not become additional internal variables. They form the **context surrounding the volume**.

This preserves the ten-variable ontology while retaining one of the useful parts of Predictive Innovation: desires must be understood in context, and subjective desires should be converted into objective Outcomes. [PI-04]

Every LAKA analysis begins with:

```text
Actor:
Scenario:
Purpose:
Current desire:
Desired observable outcome:
Time horizon:
Evidence available:
```

The conceptual model is:

```text
LAKA Model = Context Envelope × 700-Cell Volume × Time × Evidence
```

The core remains three-dimensional. Time creates trajectories through the volume. Different Actors, markets, or competitors create overlaid volumes. Here the multiplication signs describe linked information layers, not a numerical probability or a measured physical volume.

---

## 3. Why it is a grammar

The internal variables form the grammatical roles of a system.

> Under **Conditions**, **Actions** transform an **Object** through **Tools**, using **Resources**, within **Constraints**, producing **Outcomes** and **Value**. **Feedback** alters the next cycle, while the **Failure mode** describes how the system breaks.

That is the basic **LAKA system sentence**.

### Grammar roles

| Internal variable | Grammar function |
|---|---|
| Object | The subject: what is being acted upon. |
| Conditions | Contextual clause: when, where, and under what circumstances. |
| Actions | Verb: what the system does. |
| Tools | Instrument: what directly carries out the action. |
| Resources | Inputs: what enables or supplies the action. |
| Outcomes | Result clause: what observable state is produced. |
| Feedback | Recursive clause: how results alter the next cycle. |
| Constraints | Boundary clause: what limits valid operation. |
| Value | Meaning clause: who benefits and why it matters. |
| Failure mode | Break clause: how the sentence becomes invalid. |

Predictive Innovation distinguishes an Outcome, which focuses on a resulting state, from a Function, which focuses on an action. [PI-05] LAKA preserves this distinction:

- Outcomes describe what becomes true.
- Actions describe what produces it.
- Tools and Resources describe implementation.
- Value describes why the result matters.
- Failure mode describes when the claimed result is no longer valid.

---

## 4. State transitions replace Begin State and End State

Predictive Innovation uses Begin State and End State as separate Elements. [PI-06]

LAKA does not add them as an eleventh and twelfth internal variable. Instead, every LAKA variable contains a state transition:

```text
Current State → Transformation → Target State
```

For example:

```text
Feedback:
Monthly manual reports
→ closed-loop automation
→ continuous adaptive correction
```

Every voxel has this structure:

```text
Coordinate:
Current state:
Transformation operator:
Target state:
Observable evidence:
Dependencies:
Confidence:
Failure test:
```

A compact record is `v = (c, i, m, s0, o, s1)`, where `c` is change level, `i` is internal variable, `m` is meta-variable, `s0` is current state, `o` is transformation operator, and `s1` is target state. Evidence and context attach to the record; the six-part shorthand does not replace them.

---

## 5. The five LAKA change modes

The five columns are not merely different amounts of change. They represent different **grammatical modes of transformation**.

| Level | Meaning | Typical operators |
|---|---|---|
| Baseline | Describe, preserve, measure, or standardize the current system. | Observe, map, maintain, measure. |
| Minor Change | Tune parameters without changing the system’s identity. | Increase, decrease, simplify, speed up. |
| Major Change | Introduce a functionally distinct mechanism while retaining the overall system. | Replace, automate, invert, split, merge. |
| Structural Change | Change relationships, flows, roles, dependencies, or control architecture. | Rewire, redistribute, decentralize, modularize. |
| Paradigm Change | Change assumptions, purpose, category, object, or the definition of value. | Redefine, eliminate, dematerialize, universalize. |

A useful boundary rule is:

```text
Minor = parameter changes
Major = mechanism changes
Structural = relationship changes
Paradigm = meaning or assumption changes
```

Predictive Innovation calls meaningful thresholds **Functional Distinctions**: differences that affect results or make something possible that was not previously possible. [PI-07]

LAKA uses Functional Distinctions to prevent false classification. A larger number is not necessarily a Major Change. A new tool is not necessarily Structural. Automation is not automatically Paradigm Change.

---

## 6. The 5 × 10 internal grammar matrix

| Variable | Baseline | Minor Change | Major Change | Structural Change | Paradigm Change |
|---|---|---|---|---|---|
| **Object** | Same object and category | Tune an attribute | Replace, split, combine, or relocate the object | Reconfigure relationships, ownership, or boundaries around the object | Eliminate the old object or create a new object category |
| **Conditions** | Accept current environment | Adjust tolerances | Operate under substantially different conditions | Sense, adapt to, or actively engineer conditions | Remove dependence on the condition or redefine the context |
| **Actions** | Repeat current action | Optimize speed, sequence, or effort | Substitute, reverse, transfer, or automate the action | Redesign the network of actions and actors | Eliminate the action or achieve the outcome through different logic |
| **Tools** | Use current tool | Improve precision, usability, or performance | Introduce a new tool class | Create a platform, toolchain, shared system, or infrastructure | Make the tool ambient, invisible, autonomous, or unnecessary |
| **Resources** | Use existing inputs | Reduce waste or improve efficiency | Substitute a resource or add a new source | Create circular, shared, on-demand, or autonomous resource flows | Make the system generate its own resource or convert scarcity into abundance |
| **Outcomes** | Preserve current result and metric | Improve amount or quality | Add new outcomes or remove significant undesired outcomes | Balance interconnected Outcomes across the system | Redefine the purpose, desired result, or meaning of success |
| **Feedback** | Manual, delayed, or periodic | Faster and more granular | Automated closed loop | Multiple adaptive loops across the system | Anticipatory or self-governing feedback that can redefine targets |
| **Constraints** | Treat boundary as fixed | Relax or optimize around it | Remove, substitute, or transfer the limitation | Redistribute the limitation or convert it into a design rule | Reframe the system so the old constraint is no longer relevant |
| **Value** | Same beneficiary and value type | More value for the same beneficiary | New beneficiary, value type, offer, or revenue logic | Align value across several Actors or an ecosystem | Establish a new unit, source, exchange, or philosophy of value |
| **Failure mode** | Observe known failure | Reduce probability or severity | Prevent, detect, isolate, or recover from failure | Create graceful degradation, redundancy, resilience, or self-repair | Transform failure into information, resources, adaptation, or another valid state |

---

## 7. The fourteen dynamic modifiers

The internal variable tells LAKA **what aspect of the system is changing**. The meta-variable tells LAKA **how that change behaves**. They function like adverbs in the grammar.

### Original illustrative state ladders

The vocabulary below preserves the draft’s ideation ladders. These are illustrative words, **not validated measurement scales and not assignments to the five change columns**. Actual baselines may already be fast, continuous, widespread, or difficult to reverse. See the separate implementation notes for operational distinctions.

| Meta-variable | Core question | Illustrative state ladder |
|---|---|---|
| **Magnitude** | How much change? | unchanged → slight → substantial → system-wide → category-defining |
| **Rate** | How quickly? | static → gradual → rapid → discontinuous → self-accelerating |
| **Direction** | Moving toward what? | no directional shift → local tendency → explicit target → system reorientation → new definition of progress |
| **Scope** | How broadly? | single point → local subset → multiple units → whole system → ecosystem or culture |
| **Depth** | How fundamentally? | surface → parameter → function → architecture → assumptions or ontology |
| **Duration** | For how long? | momentary → temporary → sustained → embedded → enduring default |
| **Frequency** | How often? | one-off → occasional → repeated → continuous → no discrete event or always-on |
| **Acceleration** | Is the rate increasing or decreasing? | flat → slightly increasing → compounding → nonlinear → self-propelling |
| **Variability** | How consistent or unpredictable? | fixed → bounded → broad → adaptive → emergent |
| **Detectability** | How visible or measurable? | invisible → weak signal → measurable → real-time transparent → anticipatory |
| **Reversibility** | Can it be undone? | effortless → easy → costly → path-dependent → effectively irreversible |
| **Propagation** | How does it spread? | contained → adjacent → networked → cascading → ecosystem-spanning |
| **Amplification** | What makes it stronger? | none → local leverage → multiplier → platform or network effect → self-reinforcing |
| **Accumulation** | How does it build over time? | none → additive → compounding → stock-and-flow shift → flywheel or lock-in |

Domain-specific vocabularies can replace these examples without changing the grammar. For instance, Detectability in a marketing analysis might distinguish untracked events, observable events, timely attribution, and predictive signals. A predictive signal remains a forecast, not an observed future event.

---

## 8. The formal LAKA concept grammar

```text
<LAKA-CONCEPT> ::=
    <CONTEXT>
    <TRANSFORMATION>
    <MECHANISM>
    <OBSERVABLE-RESULT>
    <VALUE-CLAIM>
    <LEARNING-LOOP>
    <RISK-TEST>

<CONTEXT> ::=
    actor + scenario + purpose + time horizon

<TRANSFORMATION> ::=
    change-level + internal-variable + meta-variable
    + current-state + operator + target-state

<MECHANISM> ::=
    action + tool + resource + conditions

<OBSERVABLE-RESULT> ::=
    outcome + measure + threshold

<VALUE-CLAIM> ::=
    beneficiary + value-type + value-exchange

<LEARNING-LOOP> ::=
    feedback + detection + adjustment

<RISK-TEST> ::=
    constraint + failure-mode + recovery
```

A well-formed LAKA idea reads like:

> For **[Actor]** in **[Scenario]**, change **[Internal Variable]** at the **[Change Level]** so that **[Meta-variable]** moves from **[Current State]** to **[Target State]**. Perform **[Action]** using **[Tool]** and **[Resources]** under **[Conditions]**. Produce **[Observable Outcome]** and **[Value]**. Use **[Feedback]** to adapt while controlling **[Constraint]** and **[Failure mode]**.

---

## 9. Movement through the volume

### Column sweep

Hold the internal and meta-variable constant while moving across change levels.

```text
Object × Scope:
Baseline → Minor → Major → Structural → Paradigm
```

This shows progressively more radical ways of changing the same aspect; it does not imply that radical change is better.

### Depth sweep

Hold the internal variable and change level constant while rotating through all fourteen meta-variables.

```text
Structural Feedback:
Magnitude / Rate / Direction / Scope / Depth / Duration / Frequency /
Acceleration / Variability / Detectability / Reversibility /
Propagation / Amplification / Accumulation
```

### Layer sweep

Hold one change level constant and examine all ten internal variables: everything that Structural Change could mean for this system.

### Diagonal sweep

Combine several related voxels:

```text
Major Tool × Detectability
+ Structural Feedback × Frequency
+ Paradigm Value × Direction
```

Diagonal sweeps generate complete concepts rather than isolated alternatives.

### Recursive sweep

Any Object, Outcome, Tool, Constraint, or Failure mode can become a new Scenario with its own 700-cell volume. This makes LAKA recursively decomposable. The draft’s “fractal” description is an analogy. Predictive Innovation similarly describes how results from previous steps affect future choices. [PI-08]

### Overlay

Place multiple volumes over each other:

```text
Current system
Competitor system
Customer ideal
Historical system
Predicted future
```

Differences reveal candidate gaps, convergence, copied positions, and potentially underserved spaces. Comparable definitions and evidence are needed before those gaps support a business claim.

---

## 10. The transformation operators

These operators let LAKA produce alternatives without relying only on random brainstorming.

| Operator | Function |
|---|---|
| **SHIFT** | Move something to another change level. |
| **ROTATE** | Examine the same variable through another meta-variable. |
| **INVERT** | Reverse an assumption, direction, object, action, or outcome. |
| **TRANSFER** | Move responsibility from one internal variable to another. |
| **SUBSTITUTE** | Replace an object, action, tool, resource, or condition. |
| **SPLIT** | Divide one role, object, action, market, or outcome into several. |
| **MERGE** | Combine roles, actions, tools, resources, or outcomes. |
| **COUPLE** | Make variables affect each other. |
| **DECOUPLE** | Remove a dependency between variables. |
| **STABILIZE** | Preserve or return to a desired state. |
| **DESTABILIZE** | Intentionally disrupt an undesirable stable state. |
| **SEQUENCE** | Arrange alternatives into an implementation path. |
| **PARALLELIZE** | Allow several actions or paths to operate simultaneously. |
| **RECURSE** | Treat a cell as a complete new volume. |
| **OVERLAY** | Compare systems, competitors, users, scenarios, or periods. |
| **PRUNE** | Remove alternatives that violate observable Outcomes. |
| **COMPOSE** | Combine several voxels into a complete system idea. |

Predictive Innovation’s problem-solving process considers dilemmas, assumptions, generalizations, and inversion. Inversion reverses parts of an assumption to reveal overlooked approaches. [PI-09] The proposed LAKA operator set expands this into operations on internal variables, dynamic modifiers, and relationships.

---

## 11. The six LAKA operating modes

The same volume is interpreted differently depending on the task.

| Mode | How it reads the volume | Primary result |
|---|---|---|
| GENERATE | Searches gaps, unusual coordinates, and compatible diagonals | Innovative concepts |
| SOLVE | Searches contradictions, constraints, failure cells, and assumptions | Practical solutions |
| DECODE | Reverse-parses observable evidence into possible system coordinates | Explanatory model |
| PREDICT | Reads trajectories, acceleration, propagation, and enabling dependencies | Conditional future sequences |
| PLAN | Finds a feasible path from current shape to target shape | Strategic roadmap |
| POSITION | Overlays customers, competitors, and outcomes | Differentiated market position |

### GENERATE mode

Generation begins with objective Outcomes rather than random ideas. Predictive Innovation multiplies Elements and Alternatives to organize possibilities and describes unfilled cells as places to search for innovation. [PI-10]

```text
1. Define Actor and Scenario.
2. Define current and ideal Outcomes.
3. Fill the Baseline column.
4. Sweep each internal variable across the five change levels.
5. Rotate promising cells through relevant meta-variables.
6. Identify empty, weak, contradictory, or overserved coordinates.
7. Compose three to seven compatible voxels.
8. Add Feedback, Constraints, Value, and Failure mode.
9. Convert the result into a testable concept.
```

An empty cell is a **hypothesis of opportunity**, not automatic proof that an idea is novel. Three to seven voxels is a working convenience, not a law of cognition or a completeness condition.

### SOLVE mode

Problem-solving begins with a conflict:

```text
Improving Outcome A appears to worsen Outcome B.
```

The solver asks:

```text
Which assumption created the conflict?
Is the assumed Object correct?
Is the Action necessary?
Could another Tool perform it?
Could the Condition change?
Could the burden be transferred to Feedback?
Could the Constraint become a Resource?
Could the Failure mode become an alternate Outcome?
```

SOLVE prioritizes Constraints, Failure modes, Conditions, Actions, Reversibility, Detectability, and Variability. A solution can come from a single voxel. Full innovation work normally combines multiple voxels. A real physical or ethical constraint must not be dismissed as merely a mistaken assumption.

### DECODE mode

DECODE runs the grammar backwards. Given an observable result, artifact, strategy, product, event, or message, LAKA asks:

```text
What Object must exist?
What Actions might have occurred?
What Tools could produce those actions?
What Resources were required?
Under what Conditions would this work?
What Constraints shaped the result?
What Feedback could explain its adaptation?
Who received Value?
What Failure mode could explain inconsistencies?
```

The result is a **morphological fingerprint** of the system, understood as an analytical representation rather than a unique identity or proof of intent.

```text
Minor Change in Tools
Major Change in Actions
Structural Change in Feedback
Baseline in Value
High in Propagation
Low in Reversibility
Increasing in Accumulation
```

This fingerprint can be compared with competitors, previous versions, or predicted successors. Observed facts must remain separate from inferred explanations, and multiple explanations may fit the same evidence.

### PREDICT mode

Prediction is not simply extrapolating a trend line. Predictive Innovation distinguishes exact dates from sequences of enabling innovations. [PI-11] Its prediction procedure is to diagram Outcomes, define Ideal States, divide the range into Functional Distinctions, and map the steps. [PI-12]

LAKA retains that logic and adds the fourteen meta-variables. The draft prioritizes Direction, Rate, Acceleration, Propagation, Amplification, Accumulation, and Detectability as useful starting lenses; this prioritization has not been empirically validated.

```text
Current coordinate:
Directional pressure:
Next functional distinction:
Required enabling condition:
Required resource or tool:
Leading indicators:
Possible branching paths:
Failure or reversal signal:
Confidence:
```

The prediction becomes:

```text
Current Shape → Adjacent Future → Enabling Step → Structural Shift → Possible Paradigm
```

It is not one unsupported leap from the present to science fiction. A desirable ideal is a planning target, not evidence that the future will converge to it.

### PLAN mode

Planning treats strategy as pathfinding through the volume.

```text
Current system shape = V0
Desired system shape = V*
Strategic path = P = {v1, v2, v3, ..., vn}
```

Each step specifies dependency, resource, tool, constraint, expected Outcome, Feedback signal, Reversibility, failure threshold, trigger for advancing, and trigger for retreating.

First steps should be considered for high learning, high Detectability, high Reversibility, low resource commitment, and useful Feedback. These are design priorities, not a guarantee of safety. Later steps may intentionally become less reversible after sufficient evidence accumulates.

### POSITION mode

Positioning is an overlay operation.

```text
Customer ideal
Current alternatives
Direct competitors
Indirect competitors
Your proposed system
```

Predictive Innovation combines Satisfaction and Importance to distinguish under-served, over-served, properly served, and limited-potential Outcomes. Under-served Outcomes suggest improvement opportunities; over-served Outcomes can suggest simpler or lower-cost alternatives. [PI-13]

The LAKA positioning sentence is:

> For **[Actor]** in **[Scenario]**, **[Brand]** changes **[Internal Variable]** from **[Current State]** to **[Target State]** at the **[Change Level]**, primarily altering **[Meta-variable]**. This produces **[Outcome and Value]**, unlike alternatives that remain at **[Competitor Coordinate]**, while avoiding **[Failure mode]**.

Illustrative example, not a researched competitor claim:

> For small businesses overwhelmed by disconnected marketing tools, the platform structurally changes Feedback from delayed reporting to continuous adaptive guidance. It creates decision confidence rather than merely more analytics, unlike dashboards that leave interpretation to the user.

---

## 12. Standard “Run LAKA” syntax

```text
RUN LAKA
MODE: [GENERATE | SOLVE | DECODE | PREDICT | PLAN | POSITION]

ON:
[system, product, problem, event, market, message, or strategy]

FOR:
[Actor or stakeholder]

IN:
[Scenario]

FROM:
[current observable state]

TOWARD:
[ideal observable outcome]

TIME HORIZON:
[period or event sequence]

EVIDENCE:
[known data, documents, observations, assumptions]

DEPTH:
[quick scan | focused sweep | complete volume]
```

A complete output contains:

```text
1. Context envelope
2. Objective Outcomes
3. Baseline system sentence
4. Baseline volume signature
5. Key tensions and assumptions
6. High-opportunity voxels
7. Generated concept sentences
8. Constraint and failure analysis
9. Prediction trajectories
10. Strategic path
11. Positioning statement
12. Evidence gaps and confidence
```

These are prompt instructions and a reporting format, not commands already installed in an application. Mode-specific work may mark irrelevant sections “not applicable” with a reason.

---

## 13. Well-formedness rules

A valid LAKA concept must pass these tests:

1. The Actor and Scenario are named.
2. The Outcome is observable or measurable.
3. The current and target states are both described.
4. The claimed change level matches the actual transformation.
5. The selected meta-variable has a clear direction.
6. The Action explains how the Outcome is produced.
7. The Tool directly participates in the Action.
8. Resources enable the mechanism but are not confused with Tools.
9. Value identifies who benefits and what form the benefit takes.
10. At least one plausible Failure mode is included.
11. Feedback explains how the system learns or corrects itself.
12. Predictions include dependencies, signals, and uncertainty.
13. Paradigm ideas alter assumptions, purpose, objects, or value logic—not merely performance.
14. Empty cells are treated as research questions rather than automatic breakthroughs.

Passing these rules makes a proposal more explicit. It does not establish that it is feasible, safe, new, profitable, causally correct, or predictively accurate.

---

## 14. Example of the complete grammar

### Scenario

A company wants to improve customer support. This is a hypothetical example, not measured customer research.

### Baseline sentence

> Under normal business hours, support agents act on customer tickets using a help-desk application and employee time, within staffing and knowledge constraints, producing ticket resolution and customer confidence. Surveys provide delayed Feedback. The primary Failure mode is a growing backlog.

### Selected opportunity voxels

```text
Major Change × Object × Scope
Ticket → complete customer journey

Structural Change × Feedback × Frequency
Post-resolution survey → continuous product-friction signals

Paradigm Change × Actions × Direction
Answer support requests → prevent the need for support

Structural Change × Value × Propagation
Value delivered to one requester → fix distributed to all affected users
```

The coordinate labels preserve the concept draft. They are provisional: for example, changing from answering tickets to preventing friction is Paradigm Change only if it truly changes the governing problem definition rather than simply adding a prevention mechanism.

### Generated concept

> Create a self-healing support system that treats product friction—not the ticket—as the Object. It detects repeated confusion, adjusts guidance or workflows, verifies whether the change reduces friction, and propagates successful fixes to affected users before additional tickets are created.

### Failure mode

> The system may incorrectly alter a workflow because it mistakes unusual user behavior for a general problem.

### Feedback guard

> Require repeated evidence, confidence thresholds, reversible changes, and human approval for high-impact modifications.

This is a coherent LAKA sentence assembled from several voxels rather than an isolated brainstorm. Whether it works requires implementation and testing.

---

## 15. LAKA applied to itself

The evolution of LAKA can be mapped through its own five columns:

| Level | LAKA form |
|---|---|
| Baseline | A worksheet containing five columns and ten internal variables |
| Minor Change | A guided worksheet with fourteen dynamic modifiers and controlled vocabulary |
| Major Change | A 700-cell idea-space generator that creates and compares alternatives |
| Structural Change | A shared knowledge graph used by generation, solving, decoding, prediction, planning, and positioning agents |
| Paradigm Change | A bidirectional grammar intended to represent, generate, parse, compare, and forecast systems across domains |

These are proposed development directions, not claims that a working knowledge graph or forecasting engine is delivered in this archive.

The proposed positioning is:

> **LAKA is not another brainstorming framework. It is a bidirectional volumetric grammar for systems. It uses the same underlying representation to generate innovations, solve problems, decode structures, predict adjacent futures, plan transformation paths, and establish positions.**

This positioning is a hypothesis to test against alternatives. Distinct wording or a larger grid does not by itself prove a blue-ocean market or defensibility.

Within this project, **“Run LAKA”** means:

```text
Define the context
→ construct the baseline system sentence
→ map the current volume
→ scan change levels and dynamics
→ compose opportunity voxels
→ stress-test constraints and failure
→ map future trajectories
→ produce strategy and positioning
```

The accompanying implementation files add the 700 prompt stems, operator dictionary, recursive rules, a proposed scoring rubric, templates, and a machine-readable data model. These additions are clearly marked as LAKA design work rather than content from the source book.

---

## Source references

All PI references point to the user-supplied PDF, included in the complete ZIP at `08_sources/Predictive_Innovation_Core_Skills_User_Supplied.pdf` and omitted from the framework-only ZIP. PDF pages below are **1-based file pages**; printed book numbering sometimes differs. No independent verification of the book’s performance claims was performed.

**[PI-01] Authorship and edition.** PDF pages 3–4. Title and copyright pages; authored by Mark Proffitt; first published 2012; ISBN 978-0-578-11728-7.

**[PI-02] Six dimensions.** PDF pages 31. Chapter 6, printed page 27. Actors, Desires, Scenarios, Alternatives, Outcomes, and Elements.

**[PI-03] Three-dimensional system description.** PDF pages 39. Chapter 7, printed page 35. Outcomes, 7-Elements, and 15-Alternatives.

**[PI-04] Desires, Scenarios, and observable Outcomes.** PDF pages 35. Chapter 6, printed page 31. Scenarios frame desires; Outcomes are observable criteria.

**[PI-05] Functions versus Outcomes.** PDF pages 85. Chapter 11, printed page 82. Functions focus on Actions; Outcomes focus on States.

**[PI-06] Begin and End States.** PDF pages 100. Chapter 13, printed page 98. States before and after an Action.

**[PI-07] Functional Distinctions.** PDF pages 24–26. Chapter 5, printed pages 19–21. Also glossary, PDF page 172, printed page 177.

**[PI-08] Recursion and fractal analogy.** PDF pages 28. Chapter 5, printed page 23. Prior choices influence subsequent choices.

**[PI-09] Dilemmas and assumption testing.** PDF pages 124–127. Chapter 16, printed pages 123–126. Dilemmas, assumptions, generalizations, and inversion.

**[PI-10] Multiplying Alternatives and empty cells.** PDF pages 112–113. Chapter 14, printed pages 111–112. Organized alternative types and unfilled possibilities.

**[PI-11] Prediction timing.** PDF pages 156. Chapter 21, printed page 159. Sequences of innovations, rather than claimed exact dates.

**[PI-12] Predicting Process.** PDF pages 158–161. Chapter 21, printed pages 161–164. Outcomes, Ideal States, Functional Distinctions, and mapped steps.

**[PI-13] Importance and satisfaction.** PDF pages 163–167. Chapter 21, printed pages 166–170. Opportunity Landscape, under-served and over-served Outcomes.

**[PI-14] PI Alternatives Grid.** PDF pages 42. Chapter 7, printed page 38. Three Scales by five Directions; not the LAKA change columns.

**[PI-15] Seven Elements and Tools/Resources.** PDF pages 36. Chapter 6, printed page 32; also PDF page 101, printed page 99, for Tools and Resources.

**[PI-16] Scenario Outcomes remain fixed in PI.** PDF pages 78. Chapter 10, printed page 74. PI treats required Outcomes as fixed for a given Scenario; LAKA purpose-redefinition is a separate extension.

**[PI-17] Opportunity Score.** PDF pages 167. Chapter 21, printed page 170. The source defines the score as the absolute difference between Importance and Satisfaction.
