# LAKA Operator Dictionary

**Status:** LAKA implementation extension. The 17 names come from the conversation’s draft. Contracts and safeguards below are newly specified for practical use. They are not a claim that the operator set is complete.

Operators include navigation, transformation, control, comparison, and composition. Not all operators physically transform a system. INVERT and stabilization concepts have inspiration in PI; the complete dictionary is a LAKA design proposal. See [PI-09] and [PI-14] in `../08_sources/SOURCE_NOTES.md`.

## SHIFT

**Category:** Navigation. Move something to another change level.

**Input:** A documented transformation and its claimed level.

**Output:** A revised level plus the actual transformation needed to justify it.

**Guardrail:** Changing a label alone changes no system.

**Illustrative example:** Changing a reporting interval is Minor; redesigning who can correct the process may be Structural.

## ROTATE

**Category:** Navigation. Examine the same variable through another meta-variable.

**Input:** One variable and change level.

**Output:** Questions about a different dynamic modifier.

**Guardrail:** Keep the mechanism fixed until the rotation reveals a reason to change it.

**Illustrative example:** Inspect the same Feedback loop for Frequency, then Detectability.

## INVERT

**Category:** Transformation. Reverse an assumption, direction, object, action, or outcome.

**Input:** An explicit assumption or direction.

**Output:** A candidate opposite or alternate assumption.

**Guardrail:** An inverted statement is a hypothesis, not a fact.

**Illustrative example:** Ask whether support should prevent confusion instead of only answer tickets.

## TRANSFER

**Category:** Transformation. Move responsibility from one internal variable to another.

**Input:** A Function or burden and its current carrier.

**Output:** A different carrier and a record of redistributed costs.

**Guardrail:** Do not disguise transferred harm or labor as eliminated cost.

**Illustrative example:** Move repetitive checking from users to a monitored validation process.

## SUBSTITUTE

**Category:** Transformation. Replace an object, action, tool, resource, or condition.

**Input:** An existing Object, Action, Tool, Resource, or Condition.

**Output:** An alternative with equivalent or revised acceptance criteria.

**Guardrail:** Check interfaces, dependencies, side effects, and stakeholder acceptance.

**Illustrative example:** Replace a scheduled report with an event-triggered signal.

## SPLIT

**Category:** Transformation. Divide one role, object, action, market, or outcome into several.

**Input:** An overloaded role, action, resource, or outcome.

**Output:** Separate pieces with interfaces and responsibilities.

**Guardrail:** Fragmentation can add coordination burden.

**Illustrative example:** Separate evidence collection from final decision authority.

## MERGE

**Category:** Transformation. Combine roles, actions, tools, resources, or outcomes.

**Input:** Several overlapping components or activities.

**Output:** A combined mechanism and retained required capabilities.

**Guardrail:** Consolidation can create a common failure point.

**Illustrative example:** Merge duplicate data-entry steps into one validated record.

## COUPLE

**Category:** Relationship. Make variables affect each other.

**Input:** Two independent or weakly linked variables.

**Output:** An explicit dependency or Feedback relationship.

**Guardrail:** Specify sign, delay, and saturation; coupling can destabilize.

**Illustrative example:** Route failed Outcome checks back to workflow owners.

## DECOUPLE

**Category:** Relationship. Remove a dependency between variables.

**Input:** A dependency and the reason it exists.

**Output:** A candidate reduced dependency and replacement coordination.

**Guardrail:** Removing a real prerequisite is not an implementable solution.

**Illustrative example:** Allow low-risk work to proceed independently of a long reporting cycle.

## STABILIZE

**Category:** Control. Preserve or return to a desired state.

**Input:** Desired reference state and permitted deviations.

**Output:** A keep, establish, or restore mechanism.

**Guardrail:** A constant target can itself be wrong; distinguish the three stable behaviors.

**Illustrative example:** Restore a known-good configuration after an unsafe change.

## DESTABILIZE

**Category:** Control. Intentionally disrupt an undesirable stable state.

**Input:** An undesirable persistent state or reinforcing loop.

**Output:** A bounded intervention that breaks persistence.

**Guardrail:** Use controlled tests and do not destabilize safety-critical functions.

**Illustrative example:** Break an internal backlog loop by limiting new work in progress.

## SEQUENCE

**Category:** Composition. Arrange alternatives into an implementation path.

**Input:** Candidate changes and prerequisite relationships.

**Output:** Ordered steps with gates and owners.

**Guardrail:** Ordering must follow real dependencies, not column order alone.

**Illustrative example:** Validate signals before enabling automatic changes.

## PARALLELIZE

**Category:** Composition. Allow several actions or paths to operate simultaneously.

**Input:** Independent or separable work.

**Output:** Concurrent branches with resource allocation and merge rules.

**Guardrail:** Parallel branches may compete for shared resources.

**Illustrative example:** Test two low-risk support explanations in separate experimental cohorts.

## RECURSE

**Category:** Navigation. Treat a cell as a complete new volume.

**Input:** A cell whose mechanism contains unresolved subproblems.

**Output:** A child context and a bounded child volume.

**Guardrail:** Set a depth and work budget; keep the parent Outcome and interfaces.

**Illustrative example:** Analyze signal quality as a child problem of Feedback.

## OVERLAY

**Category:** Comparison. Compare systems, competitors, users, scenarios, or periods.

**Input:** Representations with comparable context, units, and dates.

**Output:** Differences, similarities, unknowns, and evidence-linked gaps.

**Guardrail:** Different contexts can create misleading apparent gaps.

**Illustrative example:** Compare support models on the same user task and Outcome.

## PRUNE

**Category:** Selection. Remove alternatives that violate observable Outcomes.

**Input:** A candidate and explicit criterion.

**Output:** Rejected, deferred, or retained status with a reason.

**Guardrail:** Keep the record; insufficient evidence is not proven impossibility.

**Illustrative example:** Defer a tool-dependent idea until the required access is verified.

## COMPOSE

**Category:** Composition. Combine several voxels into a complete system idea.

**Input:** Several transformations with stated target states.

**Output:** A candidate system with coherent mechanism and shared tests.

**Guardrail:** Check contradictory states and higher-order interactions.

**Illustrative example:** Combine earlier detection, reversible correction, and shared learning.
