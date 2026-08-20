# Architecture Artifact Contract

Use stable identifiers and repository-relative links. Map paths through `architecture/toolkit-profile.yaml` when a project overrides the defaults.

| Artifact | Identifier | Default path | Lifecycle |
|---|---|---|---|
| Use case | `UC-NNN` | `architecture/use-cases/UC-NNN-<slug>.md` | Draft, Reviewed, Approved, Retired |
| Business Decision Record | `BDR-NNN` | `architecture/business-decisions/BDR-NNN-<slug>.md` | Proposed, Accepted, Rejected, Superseded |
| Architecture Design Document | `ADD-NNN` | `architecture/design/ADD-NNN-<slug>.md` | Draft, In Review, Approved, Superseded |
| C4 view | `<system>-<state>-<view>` | `architecture/diagrams/<system>/` | Conceptual, Current, Transition, Target |
| Decision | `ADR-NNN` | `architecture/decisions/ADR-NNN-<slug>.md` | Proposed, Accepted, Rejected, Deprecated, Superseded |
| Task specification | repository-defined | repository-defined | Draft, Ready, In Progress, In Review, Done |
| Conformance review | `ACR-NNN` | `architecture/reviews/ACR-NNN-<slug>.md` | Draft, Complete |

Each persistent artifact must include status, date, scope, upstream and downstream links, evidence and uncertainty labels, applicable governance controls, and unresolved questions with owners when known. Never renumber an existing artifact.
