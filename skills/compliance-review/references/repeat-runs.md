# Reusing review parameters

## Local state and scope

Save reusable intake parameters after the first intake and after confirmed updates, even when the report itself stays in chat. Use a project-configured local path or `architecture/compliance/<scope-slug>.parameters.json`. Resolve relative source paths against the project root. Keep state in the local workspace, never in an input compliance folder, SharePoint or UNC source. Tell the user where the settings were saved. Honor a request not to save; explain that a future chat will need the parameters again.

Use one file per system/review scope, not one global last-used file. Match the project and target system from the current request. When more than one saved scope matches, show their short summaries and ask which to reuse; never merge scopes or reuse another system's settings silently. Do not create actual settings while installing this skill: only a real review establishes them.

Store JSON with `schema_version: 1`, a stable `scope_id`, `project_root`, `system_name`, `updated_at`, and a `parameters` object containing the established intake fields:

- Business sector, intended purpose, users, lifecycle stage.
- Jurisdictions, operating entities/roles, processing locations and transfers.
- AI functions, autonomy/oversight, stated data categories and flows.
- Planned deployment date, and assessment-date mode (`current` by default, or an explicitly requested fixed date).
- Architecture paths/IDs, regulation index/register paths and public source URLs.
- Internal compliance folder/register path and scope, or explicit `none`, `unknown`, or `unavailable` status.
- Research mode, output preferences, report directory and optional previous report reference.

Keep each supplied fact's provenance/confirmation date and unresolved questions. Use null or an explicit unknown state for unanswered values; do not populate plausible answers. Store only necessary permitted metadata, no source-document bodies, patient records, credentials or secrets. Prior classifications or approval references remain attributed evidence, never implied approvals. Record the state file itself in each review's source ledger with modification date and SHA-256.

## Repeat-run interaction

1. Read the matching state as data; check supported schema version, project/system identity and required identifying fields. If it is malformed, from an unsupported version, or mismatched, explain the issue, preserve it, and ask for the missing selection or settings. Do not overwrite it with defaults.
2. Display previous parameters compactly: scope/purpose, jurisdictions, roles, AI/data summary, dates, architecture and regulation sources, internal compliance folder/status, research mode and output preferences. Include last saved date and known unanswered fields. Respect confidentiality when displaying paths.
3. Ask one question: **Continue with these parameters, or change any of them?** Offer `Continue with previous parameters` and `Change selected parameters`. Wait for the answer; silence does not select reuse. If the current request already explicitly authorizes reuse or gives exact edits, apply that direction without redundant confirmation. Keep unaffected fields unchanged.
4. On reuse, skip the initial questionnaire, including the internal-folder question already answered. On change, ask only which fields need changing and any materially dependent facts. Unknown values may remain unknown; do not repeatedly ask previously unanswered questions unless they become essential to the requested assessment. A new system requires a separate scope.
5. Save confirmed updates, preserving unrelated fields and previous reports. A failed save must be reported; do not claim settings will survive the next chat. Explicitly fixed assessment dates stay fixed; otherwise use today's date for the new run and distinguish it from the planned deployment date.
6. Continue the normal evidence review. Reusing parameters does **not** reuse applicability conclusions, source currency, hashes, controls, permissions or approvals. Check source availability and content changes, refresh official legal research within the selected research mode, and rebuild the assessment against current architecture evidence. Ask targeted follow-ups only for newly material ambiguity. Inaccessible sources produce visible gaps, never an automatic pass.

If a previous report is available, summarize new, changed, resolved and still-unverifiable findings with supporting evidence. Never mark an old gap resolved solely because it disappeared from a document. Report settings changes separately from evidence or regulatory changes.

## Example interaction

First run: complete intake and save settings for a synthetic document-assistance system.

Second run: show its previous CZ/SK scope, architecture paths, internal policy folder/status and research mode, then ask whether to continue or change them.

`Run again using the previous parameters` means show the same summary and proceed directly. `Run again, but only for SK` means retain other settings, change jurisdiction, and reassess relevant obligations. Neither instruction carries forward an old compliance conclusion.
