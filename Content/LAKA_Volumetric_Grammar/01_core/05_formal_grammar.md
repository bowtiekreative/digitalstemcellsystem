# Formal Grammar

Extracted from the master framework. PI source keys are documented in `../08_sources/SOURCE_NOTES.md`. See the implementation notes for scope and evidence safeguards.


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
