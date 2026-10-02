# ADR-002: Use intake and evidence for architecture compliance review

- Status: Proposed
- Date: 2026-10-02
- Decision owner: Unknown
- Approval evidence: None supplied

## Context and observed facts

The user requested a skill that asks about business context, selects regulations, asks for internal compliance documents, compares obligations with architecture, and recommends changes with explanations and legal links. The user confirmed any-sector scope with a CZ/SK healthcare example. Repository rules require neutral skills, configurable governance and source traceability. The supplied archive index distinguishes several source types; it does not prove legal applicability or current content.

Evidence: [authoring source ledger](../../docs/compliance-skill-source-evidence.json). User instructions and clarification are conversation evidence dated 2026-10-02; no local file hash applies to them.

## Proposed decision and alternatives

Implement a reusable [compliance-review skill](../../skills/compliance-review/SKILL.md) with staged intake, candidate applicability, source verification and requirement-to-architecture comparison. Keep the [CZ/SK example](../../profiles/healthcare-cz-sk-compliance.example.md) outside core instructions. Use existing ACR artifacts for saved reviews, with local requirement/finding identifiers, preserving current validator compatibility.

Alternatives were a hard-coded healthcare checklist, which would infer applicability across unlike systems, and extending the security review, which would mix legal, contractual and internal-policy scope with threat assessment. A dedicated neutral skill supports independent specialist evidence and existing traceability. These trade-offs are architectural inference, not stakeholder approval.

## Consequences and risks

Benefits: explainable applicability, explicit evidence gaps and traceable actions across business decisions, use cases, design, C4, decisions, tasks and conformance. Costs: each review needs current legal research and often expert resolution of classification, policy conflicts and timing. The workflow is advisory; no static check or review completion certifies compliance.

## Security and assumptions

Sources remain read-only. No source material is uploaded without explicit authorization; public research does not contain internal content. Only permitted data is processed, with no patient-identifiable information in the pilot. Jurisdictions, classifications, ownership and approvals are not inferred. Official-source availability is an assumption; failures result in provisional findings.

## Validation and open questions

Validate the new skill with skill-creator and run the repository demo and artifact checks. Behavioral review should cover an unclassified healthcare system, unavailable internal policies, unread licensed standards and conflicting or stale sources. Accountable decision owner and adoption approval remain unknown. Downstream guidance is [compliance review usage](../../docs/compliance-review.md); no application-specific business or use-case approval is implied.
