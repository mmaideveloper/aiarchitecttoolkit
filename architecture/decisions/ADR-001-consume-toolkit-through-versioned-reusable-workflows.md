# ADR-001: Keep project artifacts local and consume versioned toolkit workflows

## Record

- Status: Proposed
- Date: 2026-08-26
- Decision owner: Unknown
- Decision source: Not yet decided
- Supersedes: None
- Superseded by: None
- Related artifacts: [Adoption model](../../docs/adoption.md), [AGEL adoption](../../docs/adoption-agel.md), [Jurisdigta adoption](../../docs/adoption-jurisdigta.md)

## Context

The toolkit is intended to support at least AGEL and Jurisdigta. The current repository contains reusable skills, project-profile examples, validation scripts, and a manually dispatched use-case workflow. The project documents require their own repository history, review permissions, ownership, and project-specific governance. Copying toolkit logic into both projects would make fixes drift; storing both projects' architecture documents here would separate those documents from the code and reviewers they govern.

The present `validate_use_case.py` also contains clinical review and patient-identifier checks. It therefore cannot be treated as a project-neutral Jurisdigta gate until profile-driven validation is implemented.

## Scope and Non-goals

- In scope: ownership of architecture documents, reuse of toolkit skills and CI, update propagation, version selection, and project-specific configuration.
- Out of scope: plugin packaging, inferred approval, migration of existing project documents, and making the current clinical validator project-neutral.

## Decision Drivers

| Driver | Priority | Source/confidence |
|---|---|---|
| Architecture artifacts must be reviewed beside the implementation they govern | High | Repository working rules; confirmed |
| Toolkit fixes should not be manually copied into every consumer | High | User request; confirmed |
| Updates must be reproducible and reviewable | High | GitHub workflow supply-chain practice; architectural inference |
| AGEL and Jurisdigta governance must remain distinct | High | `profiles/agel.example.yaml` and `profiles/jurisdigta.example.yaml`; confirmed |
| Source repositories remain independently operable | Medium | Architectural inference |

## Options Considered

### Option A: Store both projects' architecture documents in this toolkit repository

- Description: Centralize documents, profiles, validators, and execution here.
- Advantages: One documentation location and one workflow.
- Disadvantages/risks: Reviews and changes are detached from project code; repository permissions and release history are coupled; cross-repository validation requires fetching project state; ownership becomes unclear.
- Driver assessment: Weak fit for traceability and project-local governance.

### Option B: Copy toolkit files into each project

- Description: Copy skills, scripts, and workflows into AGEL and Jurisdigta.
- Advantages: Simple initial setup; each project is self-contained.
- Disadvantages/risks: Copies drift, fixes require repeated merges, and local edits make upgrades difficult.
- Driver assessment: Acceptable for an experiment, weak for maintained reuse.

### Option C: Keep documents in each project and call a versioned reusable workflow here

- Description: Each project owns its `architecture/` documents and profile. This repository publishes reusable workflows and toolkit releases. Consumer workflows call a tag or commit SHA and pass the project profile.
- Advantages: Project-local traceability and permissions; shared validation implementation; explicit, reviewable upgrades; rollback to a known toolkit version.
- Disadvantages/risks: Requires a reusable-workflow interface, project-neutral/profile-aware validation, release tags, and dependency-update automation.
- Driver assessment: Best fit across all high-priority drivers.

## Decision

Propose Option C.

AGEL and Jurisdigta keep architecture artifacts and `architecture/toolkit-profile.yaml` in their own repositories. This toolkit owns reusable skills, schemas, scripts, and reusable GitHub workflows. Each consumer uses a small local caller workflow pinned to a toolkit release tag or, for stronger immutability, a commit SHA.

Updates do not silently enter consumers. A dependency-update bot or scheduled pull request advances the pinned toolkit reference, runs validation, and leaves acceptance to the project's reviewers. Referencing `main` is allowed only for an explicitly accepted experimental channel because any toolkit commit would immediately change consumer CI behavior.

Use-case validation reads the selected project profile. Common checks remain in validator code; required owners, reviewer topics, identifier scans, autonomy, human oversight, and success-metric gates are selected from the AGEL or JurisDigta profile.

## Consequences

### Positive

- Architecture changes remain in the same review and history as the affected project.
- Shared improvements are released once and adopted through visible pull requests.
- Consumers can reproduce or roll back validation behavior.
- Organization- and domain-specific policy remains outside core skills.

### Negative and trade-offs

- The toolkit needs semantic releases and a backward-compatible workflow contract.
- Each project retains a small caller workflow and profile.
- Cross-repository private access and action allow-list settings must be configured.
- A profile-driven validator is required before one use-case gate serves both domains.

## Security, Privacy, Safety, and Compliance

- Security/trust impact: Third-party action versions and this toolkit should be pinned and reviewed; reusable workflows receive only the permissions declared by the caller and must request least privilege.
- GDPR/data-lifecycle impact: Documentation must contain only approved, anonymized, synthetic, or public data. Project documents remain under project-specific access and retention controls.
- EU AI Act/human-oversight impact: Applicability and required controls remain profile- and evidence-driven; they are not inferred by the shared workflow.
- Clinical/legal-risk impact: AGEL clinical gates and Jurisdigta legal-AI gates must be separate selectable rulesets with common baseline checks.
- Required review/approval: Toolkit maintainer and accountable architecture representatives for both projects; to obtain.

## Validation and Follow-up

| Action or validation | Owner | Due date | Tracking link |
|---|---|---|---|
| Make the workflow callable with `workflow_call` and define a stable input/output contract | Toolkit maintainer | 2026-08-26 | Implemented in `.github/workflows/validate-use-case.yml`; review required |
| Make validation profile-driven with common, AGEL, and Jurisdigta rulesets | Toolkit maintainer | 2026-08-26 | Implemented in project profiles and validator; review required |
| Publish the first semantic release and immutable commit reference | Unknown | Unknown | To create |
| Add caller workflows and automated update PRs in both projects | Project owners unknown | Unknown | To create |
| Record approval or rejection of this ADR | Decision owner unknown | Unknown | To create |

## Evidence and Uncertainty

| Claim/question | Source | State |
|---|---|---|
| The repository provides skills, profiles, scripts, and a manual validation workflow | `README.md`, modified 2026-08-26, SHA-256 `c4a51f971dc6d06263b99bb7f795f78945b6b54e1f50f0ff26e3890330c713e3`; `.github/workflows/validate-use-case.yml`, modified 2026-08-26, SHA-256 `dc5406ad568be9659ec219f2213d36a7bc97243338338e247dd46e69ec02b12d` | Confirmed |
| Current validation requires clinical ownership/review and scans patient identifiers | `scripts/architecture/validate_use_case.py`, modified 2026-08-26, SHA-256 `7ad19d05d60ac6f1205083d6aaef28fe86ace9836def1ba0468b503dd9886107` | Confirmed |
| AGEL and Jurisdigta have different governance profiles | `profiles/agel.example.yaml`, modified 2026-08-25, SHA-256 `2e433181646766ec2b711a40011a27c0fe9cd49932f7d8f04cfeb170f8e28ffe`; `profiles/jurisdigta.example.yaml`, modified 2026-08-26, SHA-256 `c3c13e3e21b54e4608d03219c8c249dcf1a672b7bd3ad8bd27982c5378b5ae21` | Confirmed |
| Toolkit and project repository visibility/action policy permit reusable workflow calls | Repository settings | To verify |
| Accountable owners approve the proposed model | No decision record supplied | Unknown |
| Toolkit repository constraints and validation obligations | `C:\Projects\aiarchitecttoolkit\AGENTS.md`, modified 2026-08-26, SHA-256 `57a831a319dc955004489e3e3d5410c11f552b11b57a4a4cf374b98029d0acc4` | Confirmed |
| AGEL repository instructions and actual use-case layout | `C:\Projects\___agel\AGENTS.md`, modified 2026-07-22, SHA-256 `7bf1b71b21c12558b98ddc379f01530042547b7974baf0d28e2db04bcf2a6cf7`; `C:\Projects\___agel\architecture\use-cases\UC‑001-retrieve-medical-guideline-evidence.md` (displayed with a non-breaking hyphen), modified 2026-08-24, SHA-256 `7cdb7d279b3bf18497bd7983e3044722d683bd624d2f056b03106c3dd8e29ad1` | Confirmed |
| JurisDigta repository identity, instructions, and profile | `C:\Projects\aijuristiction\aijurisdictionagents\AGENTS.md`, modified 2026-08-20, SHA-256 `aa00cce855275bc641dc7a3e41ff0c5798865f5bb76e9d008f979e2be9ad3970`; `C:\Projects\aijuristiction\aijurisdictionagents\architecture\toolkit-profile.yaml`, modified 2026-08-20, SHA-256 `74296c99fca45f999197fde90591237b55f21877b92e01a7b16b5c1cd3befe5c`; Git remote `https://github.com/mmaideveloper/aijurisdictionagents.git` observed 2026-08-26 | Confirmed |
| AGEL has a configured GitHub repository | Local workspace has no `.git`; `gh repo list mmaideveloper` observed 2026-08-26 and returned no AGEL-named repository | Unknown |
