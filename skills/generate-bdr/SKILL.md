---
name: generate-bdr
description: Create, update, and review source-backed Business Design Records (BDRs) that translate reviewed use cases and stakeholder evidence into business capabilities, operating-model changes, business rules, ownership, value measures, governance obligations, and architecture constraints. Use when business design must be agreed before technical architecture, when a BDR reference such as BDR-001 is supplied, or when an ADD lacks an authoritative business baseline.
---

# Generate Business Design Record

## Workflow

1. Read `AGENTS.md`, `architecture/toolkit-profile.yaml` when present, reviewed use cases, existing BDRs, stakeholder evidence, and relevant business documentation.
2. Decide whether a BDR is required. Skip it only when the change has no material effect on business capability, process, roles, decision rights, policy, value, ownership, or operating model; record the reason.
3. Resolve the next unused `BDR-NNN` or the referenced record. Never reuse or renumber an identifier.
4. Copy [assets/bdr-template.md](assets/bdr-template.md), replace every placeholder, and remove irrelevant optional sections.
5. Separate current state, target state, transition, confirmed facts, proposals, assumptions, and open questions.
6. Apply [references/bdr-quality.md](references/bdr-quality.md). Do not prescribe technical components unless documenting a confirmed constraint.
7. Keep status `Draft` or `In Review` until authoritative approval is cited. Never infer an approver.
8. Save under `architecture/business/BDR-NNN-<slug>.md` unless the project profile or repository establishes another path.
9. Link upstream use cases and downstream ADDs, ADRs, C4 views, and tasks reciprocally when those artifacts exist.

## Rules

- Define measurable business outcomes and explicitly identify non-goals.
- Identify affected capabilities, processes, roles, decision rights, policies, information ownership, and service expectations.
- Apply applicable privacy, AI, security, accessibility, safety, and sector governance without guessing applicability or classification.
- Record human decisions and automation boundaries for material outcomes.
- Do not invent cost, benefit, owner, deadline, approval, classification, or policy values.
- Exclude personal records, credentials, secrets, and sensitive operational details.

## Output

Return path, status, linked use cases, business outcomes, constraints handed to architecture, assumptions, governance result, blocking questions, and recommended next step (`stakeholder review` or `$generate-add`).
