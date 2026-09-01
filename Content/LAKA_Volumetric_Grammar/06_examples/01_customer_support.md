# Customer Support

Extracted from the master framework. PI source keys are documented in `../08_sources/SOURCE_NOTES.md`. See the implementation notes for scope and evidence safeguards.


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
