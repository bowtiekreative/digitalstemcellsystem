# System Sentence And State Transitions

Extracted from the master framework. PI source keys are documented in `../08_sources/SOURCE_NOTES.md`. See the implementation notes for scope and evidence safeguards.


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
