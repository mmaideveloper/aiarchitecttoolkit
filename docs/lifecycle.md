# Architecture lifecycle

## Artifact progression

| Stage | Required evidence | Exit gate |
|---|---|---|
| Idea | Problem, outcome, scope direction | Material ambiguity is recorded or resolved |
| Use case | Actors, flows, requirements, acceptance criteria | Stakeholder review is evidenced |
| Business design | Capabilities, processes, roles, policy, value, ownership | Business constraints are reviewed; skip rationale exists if not applicable |
| Architecture design | Context, responsibilities, data, interfaces, quality attributes, operations | Blocking unknowns are closed and required decisions are identified |
| C4 and ADR | Evidence-backed views and independently changeable decisions | Binding decisions are accepted by an evidenced authority |
| Task preparation | Small deliverable scope and verification | Acceptance is testable and safeguards are included |
| Conformance review | Code, configuration, tests, deployment, and artifacts | Deviations are resolved or explicitly governed |

## Traceability

Every artifact links upstream sources and known downstream consumers. A task should trace each binding requirement to verification evidence. A downstream artifact does not silently change an approved upstream artifact: update it through its lifecycle or create a superseding decision.

## BDR applicability

Create a BDR when a change materially affects business capability, process, role, decision right, policy, value, ownership, information governance, service expectation, or operating model. If none apply, record a short reason and proceed from reviewed use cases to the ADD.

## Governance

Read the repository's `AGENTS.md` and `architecture/toolkit-profile.yaml`. Treat missing applicability, classifications, owners, and approvals as `To verify` or `Unknown`. A profile configures the review; it is not evidence that every listed regulation applies to every change.
