# Architecture compliance review

Invoke `$compliance-review` for any sector and jurisdiction. The skill first clarifies business purpose, location, dates, AI and data roles, and architecture evidence. It explicitly asks for an internal compliance folder or document register, then presents candidate obligations before assessing requirements against architecture. It can review a proposed design or an implementation; it reports the evidence level separately.

The review returns an applicability register, source ledger, requirement-to-evidence matrix, and prioritized recommendations with explanations, provision links, concrete actions and verification criteria. Unknown applicability and unavailable evidence stay visible. Laws, standards, guidance, contracts and internal policies retain their distinct authority.

Research uses supplied documents and official sources by default. Request supplied-sources-only review when needed; the skill records currency limitations. No source upload is authorized by invoking the skill. Source documents remain read-only. Review reports are saved only when requested; reusable intake parameters are saved locally by default unless the user opts out.

For healthcare AI in CZ/SK, supply the optional [discovery profile](../profiles/healthcare-cz-sk-compliance.example.md), your architecture paths, and your regulation index if available. The skill asks for missing internal policy sources during intake; the author of the toolkit does not need those documents to install or use the skill.

## Repeat runs

After initial intake, the skill saves settings per system/review scope in `architecture/compliance/<scope-slug>.parameters.json` (or a configured local path). The next invocation shows the previous parameters and asks **Continue with these parameters, or change any of them?** Choosing reuse skips the original questionnaire; choosing changes revisits only affected details.

Say `Run again using the previous parameters` to continue without that question, or `Run again, but only for SK` to apply a specific change. Ambiguous system selection is clarified before reuse. Unknown values remain visible, and no-persistence requests are honored.

Each run refreshes evidence and legal-source currency within the chosen research mode. Settings reuse does not reuse previous compliance conclusions or approvals. The assessment date advances to the current date unless a fixed historical date was explicitly requested. Prior reports remain intact.

## Example

> Use $compliance-review to evaluate our synthetic architecture in architecture/design/. Ask missing business and jurisdiction questions first, list candidate obligations, ask for our internal compliance folder, then explain recommendations with links to the relevant provisions. Save the review locally when complete.

Persistent reviews use an unused `ACR-NNN-compliance-<slug>.md` in the configured review directory, with `Draft` or `Complete` status. This preserves the existing artifact validator contract; completion means review completion, never approval or certification. Link the idea/BDR/use case/ADD/C4/ADR/task and conformance evidence wherever supplied. Material architectural choices need a proposed ADR; a review does not silently change accepted decisions.

## Assumptions, risks and open questions

- Sector and jurisdiction examples are discovery aids, not legal classification or exhaustive inventories.
- Archived documents can be stale; effective dates and future deployment dates require provision-level research.
- Design documents cannot prove implementation or operational controls. Missing evidence does not establish a violation.
- Policy scope, owners, classifications and approvals require evidence. Unavailable licensed standards remain gaps.
- Private documents must stay within authorized processing boundaries. External searches use public regulatory terms only.
- Who owns the review, which policy versions govern, and which expert decisions remain necessary are answered per project.

See [ADR-002](../architecture/decisions/ADR-002-evidence-led-compliance-review.md) for the proposed architectural choice and [source evidence](compliance-skill-source-evidence.json) for authoring provenance.
