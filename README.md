# AI Architect Toolkit

A reusable set of Codex skills for software architects, with a focus on AI architecture. It turns stakeholder needs into traceable business and architecture documentation and implementation-ready tasks.

## Lifecycle

```text
Idea -> Use case -> Business Design Record -> Architecture Design Document
                                      |-> C4 views
                                      |-> Architecture Decision Records
     -> Implementation-ready task -> Implementation -> Conformance review
```

The C4 capability supports system context, container, component, dynamic, deployment, integration, and regulated-data-flow views. Each artifact remains evidence-backed. The toolkit distinguishes confirmed facts, assumptions, items to verify, and unknowns; it never invents approvals.

## Skills

| Skill | Output |
|---|---|
| `idea-task` | Validated idea draft |
| `generate-use-case` | `UC-NNN` |
| `generate-bdr` | `BDR-NNN` business requirements and design |
| `generate-add` | `ADD-NNN` architecture design |
| `generate-c4` | Source, rendering, and evidence for a C4 view |
| `generate-adr` | `ADR-NNN` architecture decision record |
| `prepare-task` | Implementation-ready task specification |
| `review-architecture-conformance` | `ACR-NNN` or an in-chat review |
| `architecture-change` | End-to-end coordination and traceability |

## Use in another repository

Copy the required complete folders from `skills/` into `<project>/skills/`, or copy all folders for the complete lifecycle. Do not copy only `SKILL.md`; assets, references, and agent metadata are part of each skill.

1. Add project rules to the target repository's `AGENTS.md`.
2. Copy `profiles/project-profile.example.yaml` to `architecture/toolkit-profile.yaml` and adapt it.
3. Keep organization-specific requirements in the profile or `AGENTS.md`, not in the core skills.
4. Invoke `$architecture-change` for the complete workflow or a focused skill for one artifact.

Examples for Jurisdigta and AGEL are under `profiles/`. They contain no secrets or environment-specific identifiers.

See `docs/lifecycle.md` for gates and traceability, and `docs/adoption.md` for project adoption and customization boundaries.

## Validate

```powershell
python examples/minimal_demo.py
```

For Codex schema validation, run `quick_validate.py` from the installed `skill-creator` skill against every directory under `skills/`.

## Packaging status

This repository is intentionally a source project, not yet a Codex plugin. A later release can add `.codex-plugin/plugin.json` and marketplace metadata without changing the skill contracts.
