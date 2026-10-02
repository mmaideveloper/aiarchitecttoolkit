# Release notes

## 1.0.2 - 2026-10-02

This version identifies the complete 13-skill toolkit; it does not introduce plugin packaging.

- Add `compliance-review`: business/jurisdiction intake, internal compliance discovery, applicability registers, and architecture recommendations with source links.
- Save review parameters per scope and offer reuse or selective changes on later runs, while refreshing review evidence.
- Add a CZ/SK healthcare discovery example, traceable source evidence and review documentation.
- Include project-profiled architecture validation from the integrated development branch.

### Included skills

`idea-task`, `generate-bdr`, `generate-use-case`, `generate-add`, `generate-c4`, `generate-adr`, `prepare-task`, `review-architecture-conformance`, `security-review`, `azure-review`, `ai-solution-final-review`, `architecture-change`, `compliance-review`.

### Adoption

Copy complete skill folders from this release. Existing installations with the prior 12 toolkit skills need the new `compliance-review` folder, including its `agents/` and `references/` files. Preserve project-specific skills and configuration. The healthcare discovery example is optional and remains separate from the neutral skill.
