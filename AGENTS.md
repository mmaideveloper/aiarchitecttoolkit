# AI Architect working rules

## Data handling

- Use only synthetic, public, anonymized or explicitly approved data.
- Do not process patient-identifiable information during the toolkit pilot.
- Treat SharePoint and UNC sources as read-only.
- Do not rename, modify or delete source documents or diagrams.
- Do not upload source material to an external service unless the active
  task explicitly permits it.

## Evidence and traceability

- For every source, report:
  - source path or document identifier,
  - modification date when available,
  - SHA-256 when a local file is processed.
- Separate observed facts from architectural inference.
- Mark uncertain OCR text explicitly.
- Never silently invent an unreadable label or diagram connection.

## Output

- Store generated artifacts only in the local workspace.
- Use Mermaid or PlantUML for editable architecture diagrams.
- Create an ADR for important architectural choices.
- Include assumptions, risks, security considerations and open questions.

# Repository instructions

- Keep every skill project-neutral. Put organization-specific policy in `profiles/` examples.
- Preserve traceability from idea and business decision through use case, ADD, C4, ADR, task, and conformance review.
- Never infer stakeholder approval, regulatory classification, data classification, or ownership.
- Treat privacy, security, safety, accessibility, and applicable regulation as configurable governance concerns.
- Do not include real personal data, health data, credentials, secrets, or sensitive endpoints in examples.
- Update documentation and `examples/minimal_demo.py` when the repository contract changes.
- Validate every changed skill with the Codex `skill-creator` validator.
- Plugin packaging is out of scope until explicitly requested.
