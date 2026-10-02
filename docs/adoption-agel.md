# Adopt the toolkit in AGEL

AGEL should own its architecture documents. Keep use cases, ADDs, C4 sources, ADRs, and review evidence in the AGEL repository so changes can be reviewed with the implementation and by the appropriate AGEL authorities.

## Repository layout

```text
AGEL repository/
  .github/workflows/validate-use-case.yml
  architecture/
    toolkit-profile.yaml
    use-cases/
    designs/
    decisions/
    diagrams/
    traceability.md
```

Start `architecture/toolkit-profile.yaml` from this toolkit's `profiles/agel.example.yaml`. Confirm artifact paths and governance settings locally; the example does not establish regulatory classification, data classification, ownership, or approval.

## Caller workflow

After this toolkit publishes a reusable workflow, add a small caller in AGEL:

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
      project_name: agel
      use_case_id: ${{ inputs.use_case_id }}
      toolkit_ref: v1
```

Use the same release tag or commit SHA in both the `uses` reference and `toolkit_ref`. The called workflow validates the AGEL caller repository with `profiles/agel/profile.yaml`. Central manual execution must supply `source_repository` until the AGEL GitHub repository is configured in that profile.

## AGEL validation boundary

Select a healthcare ruleset through the profile. It may require clinical ownership, clinical reviewer evidence, patient-identifier scanning, human oversight, and clinical-safety assessment. These checks are appropriate only when supported by AGEL policy and recorded evidence; the workflow must not infer approval or classification.

## Receiving toolkit updates

Do not reference `main` for governed validation. Publish toolkit releases and let Dependabot, Renovate, or an equivalent scheduled process propose a pull request that changes `@v1` or the pinned SHA. AGEL reviewers then see the validator change and its results before merging it.

For an experimental channel, AGEL may deliberately call `@main`; this applies toolkit changes immediately on the next run and sacrifices reproducibility.

## Adoption checklist

- Verify GitHub permits AGEL to call reusable workflows from `mmaideveloper/aiarchitecttoolkit`.
- Copy and review the AGEL profile; do not copy real patient data into it.
- Add the caller workflow pinned to an approved toolkit release or SHA.
- Run the use-case gate on a synthetic example and inspect all artifacts.
- Record responsible AGEL owners and approval evidence in AGEL, not in this toolkit.
