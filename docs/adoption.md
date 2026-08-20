# Adopt the toolkit

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
```

## Project configuration

Copy `profiles/project-profile.example.yaml` to `architecture/toolkit-profile.yaml`. Adapt project name, artifact paths, governance frameworks, approval authorities, and task-management conventions. Do not put secrets, personal records, tokens, or sensitive endpoints in the profile.

The target repository's `AGENTS.md` remains authoritative for commands, branching, worktrees, validation, deployment, and organization-specific safeguards.

## Customization boundary

Prefer profiles and repository instructions over forked skills. Fork a core skill only when the workflow contract itself differs. This keeps improvements portable between Jurisdigta, AGEL, and other projects.

## Upgrade

Compare complete skill directories, review contract changes, rerun the target repository's checks, and validate the adopted skills with Codex `skill-creator`. Do not overwrite local customizations without reviewing them.

Run `python scripts/validate_architecture.py architecture` in the adopting project to detect duplicate identifiers, invalid lifecycle states, unknown artifact references, broken relative links, and a missing traceability index.

## Future plugin

Plugin packaging should add discovery metadata around these unchanged source skills. It should not embed organization secrets or make a domain profile mandatory for unrelated projects.
