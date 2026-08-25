# Architecture lifecycle

## Artifact progression

| Stage | Required evidence | Exit gate |
|---|---|---|
| Idea | Problem, outcome, scope direction | Material ambiguity is recorded or resolved |
| Business decision | Business problem, options, selected direction, success measures, authority | The decision is evidenced; skip rationale exists if no business choice is needed |
| Use case | Actors, flows, requirements, acceptance criteria | Stakeholder review is evidenced |
| Architecture design | Context, responsibilities, data, interfaces, quality attributes, operations | Blocking unknowns are closed and required decisions are identified |
| C4 and ADR | Evidence-backed views and independently changeable decisions | Binding decisions are accepted by an evidenced authority |
| Task preparation | Small deliverable scope and verification | Acceptance is testable and safeguards are included |
| Conformance review | Code, configuration, tests, deployment, and artifacts | Deviations are resolved or explicitly governed |
| Security review | Threat model, control implementation, security tests, and operational evidence | Blocking findings are resolved or covered by an evidenced exception |
| Azure review | Azure design, IaC/configuration, SLOs, operations, governance, and current platform guidance | Azure blockers and unverifiable platform assumptions are resolved |
| AI solution final review | Complete release candidate and current specialist-review evidence | Accountable authority receives a `Ready`, `Ready with conditions`, or `Not ready` recommendation |

## Traceability

Every artifact links upstream sources and known downstream consumers. A task should trace each binding requirement to verification evidence. A downstream artifact does not silently change an approved upstream artifact: update it through its lifecycle or create a superseding decision.

Conformance, security, and applicable platform reviews remain independent evidence inputs. The final AI solution review synthesizes them and must not turn missing specialist evidence into an implicit pass.

## BDR applicability

Create a BDR when an idea requires an authoritative business choice, such as build versus buy, product scope, target users, investment priority, operating ownership, risk acceptance, or a policy direction. A BDR can authorize or constrain later use cases. If no material business choice exists, record a short reason and proceed without one.

## Governance

Read the repository's `AGENTS.md` and `architecture/toolkit-profile.yaml`. Treat missing applicability, classifications, owners, and approvals as `To verify` or `Unknown`. A profile configures the review; it is not evidence that every listed regulation applies to every change.
