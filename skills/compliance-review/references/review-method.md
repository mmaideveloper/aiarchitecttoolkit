# Compliance intake and evidence method

## Intake

On repeat runs, apply [parameter reuse](repeat-runs.md) before intake. Ask only for missing or materially changed facts, grouped into a few short questions. Do not request actual personal records or secrets.

- Business: sector, service, intended purpose, affected users and consequences, research/pilot/production stage, planned launch and review date.
- Geography: operating entities, countries of establishment, markets/users, processing and storage locations, transfers and suppliers. CZ and SK must be considered separately when both are in scope.
- Roles: who develops, supplies, deploys, modifies or imports the AI/product; who determines processing purposes or processes on another's behalf. Record supplied roles and evidence; unresolved legal roles remain questions.
- AI and safety: intended use, clinical or other consequential decisions, autonomy, human intervention, model changes, product integration and any evidenced classification or conformity assessment. Sector labels alone do not settle classification.
- Data: stated categories, provenance, flows, recipients, retention, deletion, logging and training/reuse. Unknown classifications stay unknown. Ask about categories, not sample patient records.
- Evidence: paths/IDs for idea, BDR, use case, ADD, C4, ADR, tasks, prior reviews, implementation/configuration and tests; distinguish proposed versus approved baselines.
- Internal compliance: ask for a folder/document register, access constraints, scope, policy versions, effective dates, documented authority and exceptions. Ask whether it is absent or inaccessible if no source is supplied; never interpret absence as no internal obligations.

For a clinical AI request, useful follow-ups include whether output influences diagnosis/treatment, whether it is only administrative, who can override it, intended product claims, in-house versus supplied use, and any available device/AI classification assessment. These facts route research; they do not automatically assign a classification.

## Preliminary and final applicability registers

Use a stable local identifier for each candidate (for example REG-01). These are review-local row identifiers, not new toolkit artifact types.

| ID | Instrument/document and kind | Jurisdiction | Trigger and supporting facts | Applicability and unresolved classification | Version, effective/application dates | Exact official source | Follow-up |
|---|---|---|---|---|---|---|---|

Retain excluded candidates with reasons when their omission could affect the conclusion. Preserve `Potentially applicable` or `Unknown` when facts or legal text are unavailable. A regulation can have different dates for different provisions; record which version governs the review and planned deployment. Verify amendments as enacted, rather than treating proposals or announcements as operative law. Check national transposition for directives. Check exclusions and interactions among instruments before recommending duplicate or conflicting controls.

Standards are not automatically binding. Record whether a standard is voluntary, incorporated in law, contractual, required by internal policy, or unresolved. A catalog entry or harmonization listing does not expose its licensed clauses. Record exact edition and access limits; never infer compliance with unread content.

## Source ledger

For every processed source record: source ID; path/document ID and link; title; issuer; source kind; version; modification date if available (otherwise unavailable); retrieval date; and computed SHA-256 for every local file processed. Include architecture and internal policies, not only laws. Keep source modification, retrieval, entry-into-force and application dates distinct. Verify archive hashes against processed files where available and flag mismatches. An unchanged hash establishes reproducibility, not authenticity, currency or applicability.

Use indexes/registers to discover candidate documents; read relevant provisions before citing obligations. Prefer official promulgated text and documented amendments; note the legal status of consolidated text. Search only public regulatory terms on external services, never private paths or policy content. Record translations, uncertain OCR, unavailable pages and conflicts. Do not silently resolve unreadable labels or diagram connections.

## Requirement-to-evidence matrix

| Requirement ID / source provision | Applicability basis | Expected control or outcome | Architecture element and artifact/version/section | Implementation/test evidence | Result | Gap / recommendation ID |
|---|---|---|---|---|---|---|

Use `Evidence supports requirement`, `Partial evidence`, `Gap`, `Not verifiable`, or `Not applicable`. `Gap` needs affirmative evidence of a mismatch with a supported applicable requirement; it is not a legal verdict. `Not applicable` needs a reason and source facts. Unresolved applicability cannot produce a confirmed compliance result. Report tested implementation separately from stated design; no percentage score or overall certification follows from document coverage.

## Recommendations

For each recommendation include:

- Review-local ID, priority and explained impact; state whether it addresses an observed gap, missing evidence, conditional obligation, or optional improvement.
- Requirement text in concise paraphrase, exact article/paragraph/annex or policy section, official link and source-ledger ID. Cite a readable internal document reference for internal requirements; do not invent a public URL.
- Why it applies, supporting facts, uncertainty, and affected architecture elements with exact artifact/section references.
- Practical change or evidence request, alternatives where useful, verification/acceptance criteria, dependencies, and proposed ADR/task links when a decision is required. Label proposals as proposals; leave nonexistent links as `To create`.
- Owner only if evidenced; otherwise `Unassigned`, with a suggested reviewer role explicitly labeled as a suggestion. Record due dates only when sourced or label a proposed target.

Finish with assumptions, risks (including stale legal sources and incomplete architecture), privacy/security implications, policy conflicts, open questions, and decisions requiring accountable legal/compliance/domain review. An approved internal exception is evidence of that exception only; it cannot waive statutory obligations. Review completion must never imply stakeholder approval.
