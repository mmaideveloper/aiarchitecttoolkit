# Adopt the toolkit

## Recommended multi-project model

Keep architecture documents in the repository of the project they govern. Keep reusable skills, validators, schemas, project profiles, project-scoped instructions, and reusable GitHub workflows in this toolkit. Each project should contain only its local profile overrides and a small caller workflow pinned to a toolkit release tag or commit SHA.

`project_name` resolves exactly to `profiles/<project_name>/profile.yaml`. That profile identifies the source repository, project `AGENTS.md`, document-specific Markdown instructions, artifact paths, governance settings, and validation rules. Unknown project names fail; there is no fallback profile. The target repository's root `AGENTS.md` remains authoritative.

See the project guides for [AGEL](adoption-agel.md) and [Jurisdigta](adoption-jurisdigta.md), and the proposed rationale in [ADR-001](../architecture/decisions/ADR-001-consume-toolkit-through-versioned-reusable-workflows.md).

This replaces copying as the target operating model. The copy model below remains a temporary option until the reusable workflow and release process are implemented.

## Copy model

Until plugin packaging is added, copy complete skill directories into a repository-visible `skills/` directory or the user's Codex skill directory. Keep each directory intact so its `agents/`, `assets/`, and `references/` remain available.

Recommended full set:

```text
skills/
  idea-task/
  architecture-change/
  generate-use-case/
  generate-bdr/
  generate-add/
  generate-c4/
  generate-adr/
  prepare-task/
  review-architecture-conformance/
  security-review/
  azure-review/
  ai-solution-final-review/
```

## Project configuration

Copy `profiles/project-profile.example.yaml` to `architecture/toolkit-profile.yaml`. Adapt project name, artifact paths, governance frameworks, approval authorities, and task-management conventions. Do not put secrets, personal records, tokens, or sensitive endpoints in the profile.

Profiles may configure document-type guidance under `document_instructions`. Project-selected toolkit profile paths are toolkit-relative; local target profiles use target-repository-relative paths. They are loaded only by the corresponding authoring skill. A missing configured instruction is an error, not an instruction to continue without the domain safeguards.

```yaml
document_instructions:
  use_case: profiles/instructions/healthcare-use-case.md
  business_design: null
  architecture_design: null
  decision: null
  conformance_review: null
```

The target repository's `AGENTS.md` remains authoritative for commands, branching, worktrees, validation, deployment, and organization-specific safeguards.

## Customization boundary

Prefer profiles and repository instructions over forked skills. Fork a core skill only when the workflow contract itself differs. This keeps improvements portable between Jurisdigta, AGEL, and other projects.

## Upgrade

Compare complete skill directories, review contract changes, rerun the target repository's checks, and validate the adopted skills with Codex `skill-creator`. Do not overwrite local customizations without reviewing them.

Run `python scripts/validate_architecture.py architecture` in the adopting project to detect duplicate identifiers, invalid lifecycle states, unknown artifact references, broken relative links, and a missing traceability index.

## Future plugin

Plugin packaging should add discovery metadata around these unchanged source skills. It should not embed organization secrets or make a domain profile mandatory for unrelated projects.
