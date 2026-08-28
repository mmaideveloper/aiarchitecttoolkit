# AI Architect Toolkit

A reusable set of Codex skills for software architects, with a focus on AI architecture. It turns stakeholder needs into traceable business and architecture documentation and implementation-ready tasks.

## Lifecycle

```text
Idea -> optional Business Decision Record -> Use case
     -> Architecture Design Document -> necessary C4 views and ADRs
     -> Implementation-ready task -> Implementation -> Conformance review
                                             |-> Security review
                                             |-> Azure review (when applicable)
                                             `-> AI solution final review
```

The C4 capability supports system context, container, component, dynamic, deployment, integration, and regulated-data-flow views. Each artifact remains evidence-backed. The toolkit distinguishes confirmed facts, assumptions, items to verify, and unknowns; it never invents approvals.

## Skills

| Skill | Output |
|---|---|
| `idea-task` | Validated idea draft |
| `generate-use-case` | `UC-NNN` |
| `generate-bdr` | `BDR-NNN` business decision record |
| `generate-add` | `ADD-NNN` architecture design |
| `generate-c4` | Source, rendering, and evidence for a C4 view |
| `generate-adr` | `ADR-NNN` architecture decision record |
| `prepare-task` | Implementation-ready task specification |
| `review-architecture-conformance` | `ACR-NNN` or an in-chat review |
| `security-review` | Threat-and-control security assessment |
| `azure-review` | Azure architecture and operational-readiness assessment |
| `ai-solution-final-review` | Final AI readiness recommendation and evidence ledger |
| `architecture-change` | End-to-end coordination and traceability |

## Use in another repository

Copy the required complete folders from `skills/` into `<project>/skills/`, or copy all folders for the complete lifecycle. Do not copy only `SKILL.md`; assets, references, and agent metadata are part of each skill.

1. Add project rules to the target repository's `AGENTS.md`.
2. Copy `profiles/project-profile.example.yaml` to `architecture/toolkit-profile.yaml` and adapt it.
3. Keep organization-specific requirements in the profile or `AGENTS.md`, not in the core skills.
4. Invoke `$architecture-change` for the complete workflow or a focused skill for one artifact.

Examples for Jurisdigta, AGEL, and a project-neutral healthcare configuration are under `profiles/`. Document-type instructions can be selected through a profile and live under `profiles/instructions/`. They contain no secrets or environment-specific identifiers.

See `docs/lifecycle.md` for gates and traceability, and `docs/adoption.md` for project adoption and customization boundaries. Project-specific adoption guides are available for [AGEL](docs/adoption-agel.md) and [Jurisdigta](docs/adoption-jurisdigta.md).

## Validate

```powershell
python examples/minimal_demo.py
```

For Codex schema validation, run `quick_validate.py` from the installed `skill-creator` skill against every directory under `skills/`.

Validate a project's architecture identifiers, lifecycle states, artifact references, and relative links with:

```powershell
python scripts/validate_architecture.py <project>/architecture
```

### Validate and render a project use case in GitHub Actions

The `Validate use case and create PDF` workflow supports manual dispatch and
reusable `workflow_call`. It accepts `project_name` and `UC-NNN`, resolves the
project repository and `profiles/<project_name>/profile.yaml`, validates the
matching project use case with the selected rules, evaluates readiness, renders
linked Mermaid diagrams, and creates a verified PDF.

Run it from **Actions > Validate use case and create PDF > Run workflow**. The
Select `agel` or `jurisdigta`; the default use case is `UC-001`. JurisDigta's
repository is configured in its profile. AGEL requires `source_repository`
until its GitHub repository is configured. The workflow uploads the PDF, JSON report,
Markdown summary, and rendered diagrams. Its final gate fails when checklist or
readiness blockers remain, while preserving the reports for review.

Identifier scans and required reviewers are selected by the project profile.
Static validation does not replace privacy, clinical, legal, security, data, or
architecture review.

## Packaging status

This repository is intentionally a source project, not yet a Codex plugin. A later release can add `.codex-plugin/plugin.json` and marketplace metadata without changing the skill contracts.
