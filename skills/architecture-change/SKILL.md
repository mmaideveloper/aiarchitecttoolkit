---
name: architecture-change
description: Coordinate a traceable architecture change from an idea or stakeholder use case through Business Design Records, Architecture Design Documents, C4 views, Architecture Decision Records, implementation-ready tasks, and post-implementation conformance review. Use when starting, governing, assessing, or continuing a significant architecture change from any artifact reference.
---

# Architecture Change

Coordinate the lifecycle and use focused skills to author artifacts.

## Workflow

1. Read `AGENTS.md`, `architecture/toolkit-profile.yaml` when present, repository sources, existing artifacts, and stakeholder evidence.
2. Resolve the starting point and change slug. Do not recreate an artifact already supplied by reference.
3. Use `$idea-task` only when the problem or intended outcome is still ambiguous.
4. Use `$generate-use-case`; require `Reviewed` before business or architecture baselining.
5. Use `$generate-bdr` when business capabilities, operating model, value, policy, ownership, or decision rights materially constrain the design. Require a reviewed BDR before architecture baselining when applicable.
6. Use `$generate-add` from reviewed upstream artifacts and source evidence.
7. Use `$generate-c4` only for views that answer concrete stakeholder questions.
8. Use `$generate-adr` once per independently changeable decision.
9. Reconcile the ADD, BDR impacts, and target-state C4 views after ADR acceptance.
10. Use `$prepare-task` to create one or more implementation-ready task specifications. Do not mark a task ready while a blocking decision or compliance question remains open.
11. After implementation, use `$review-architecture-conformance` and resolve or explicitly govern deviations.

Read [references/artifact-contract.md](references/artifact-contract.md) when creating, linking, or changing lifecycle state for any artifact.

## Gates

- Label material claims `Confirmed`, `Assumption`, `To verify`, or `Unknown`.
- Apply the project profile and applicable privacy, AI, security, safety, accessibility, and sector rules. Stop on unresolved conflicts.
- Never put regulated records, credentials, secrets, or sensitive operational details in artifacts.
- Never infer approval or authority.
- Architecture work does not authorize implementation or external task creation unless the user requests it.

## Completion

Report artifact paths and states, traceability gaps, accepted versus proposed decisions, governance outcome, task readiness, and the next responsible action.
