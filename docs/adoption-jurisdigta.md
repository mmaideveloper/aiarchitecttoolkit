# Adopt the toolkit in Jurisdigta

Jurisdigta should own its architecture documents. Keep use cases, BDRs, ADDs, C4 sources, ADRs, tasks, and conformance evidence in the Jurisdigta repository so architecture history remains coupled to its code, GitHub issues, and reviewers.

## Repository layout

```text
Jurisdigta repository/
  .github/workflows/validate-use-case.yml
  architecture/
    toolkit-profile.yaml
    use-cases/
    business-decisions/
    designs/
    decisions/
    diagrams/
    traceability.md
```

Start `architecture/toolkit-profile.yaml` from this toolkit's `profiles/jurisdigta.example.yaml`. Confirm every governance setting in the project; listing GDPR or the EU AI Act in a profile does not prove applicability or compliance.

## Caller workflow

After this toolkit publishes a reusable workflow, add a small caller in Jurisdigta:

```yaml
name: Validate architecture use case

on:
  workflow_dispatch:
    inputs:
      use_case_id:
        description: Use-case identifier, for example UC-001
        required: true
        default: UC-001
        type: string

permissions:
  contents: read

jobs:
  validate:
    uses: mmaideveloper/aiarchitecttoolkit/.github/workflows/validate-use-case.yml@v1
    with:
      project_name: jurisdigta
      use_case_id: ${{ inputs.use_case_id }}
      toolkit_ref: v1
```

Use the same release tag or commit SHA in both the `uses` reference and `toolkit_ref`. The called workflow validates the JurisDigta caller repository; central manual execution resolves `mmaideveloper/aijurisdictionagents` from `profiles/jurisdigta/profile.yaml`.

## Jurisdigta validation boundary

The validator is profile-driven and applies:

- common checks for identifiers, metadata, traceability, links, deterministic requirements, risks, owners, and Mermaid rendering;
- JurisDigta owner, reviewer, identifier-scan, autonomy, oversight, and metric rules from its selected profile;
- no inferred legal approval, AI-risk classification, data classification, or regulatory applicability.

## Receiving toolkit updates

Do not duplicate toolkit scripts in Jurisdigta. Publish toolkit releases and let Dependabot, Renovate, or an equivalent scheduled process propose a pull request updating the release tag or pinned SHA. Jurisdigta tests and reviewers decide when the update enters the project.

Referencing `@main` causes each toolkit update to affect the next Jurisdigta workflow run automatically. Reserve that behavior for an explicitly accepted experimental channel, not a governed validation gate.

## Adoption checklist

- Verify GitHub permits Jurisdigta to call reusable workflows from `mmaideveloper/aiarchitecttoolkit`.
- Copy and review the Jurisdigta profile without adding secrets or personal/legal case data.
- Review the project validation rules before enforcing the gate.
- Add the caller workflow pinned to an approved toolkit release or SHA.
- Run it against a synthetic use case and inspect reports, diagrams, and failure behavior.
- Keep project approvals and accountable ownership in Jurisdigta.
