# Install and Configure Spec-Kit

## Task Objective
Adopt GitHub Spec-Kit so specifications, plans, and tasks become first-class artifacts that guide Copilot-assisted implementation and reviews.

## Context Engineering Problems Addressed
- Teams “vibe code” without aligned requirements, causing inconsistent solutions.
- Architectural decisions drift because specs and code changes reside in separate silos.
- Difficult to audit decisions when prompts and plans are not version controlled.
- AI-generated code lacks traceability to the original business or technical need.

## How to Execute
1. **Install the CLI**: run `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git` (or the preferred package manager) and confirm `specify --help` works.
2. **Initialize the project**: execute `specify init <project-name> --ai copilot` inside the repository to scaffold `.specify/` configuration.
3. **Capture constitutions and specs**: use `/speckit.constitution` to define values, `/speckit.specify` to write detailed requirements, and commit the outputs.
4. **Plan and task**: generate implementation plans (`/speckit.plan`) and actionable tasks (`/speckit.tasks`) that Copilot can follow during coding sessions.
5. **Integrate with review**: run `/speckit.analyze` or `specify check` to verify code changes remain aligned with the documented plan before merging.
6. **Maintain cadence**: assign owners to refresh specs after major releases and record deltas in the repository history.

## Further Reading
- [Official Link](https://github.com/github/spec-kit)
- [Spec-driven workflow](../slides/github-copilot-context/spec-kit.md#the-spec-driven-workflow)
- [CLI installation & commands](../slides/github-copilot-context/spec-kit.md#spec-kit-cli-installation)
- [Context integration scenarios](../slides/github-copilot-context/spec-kit.md#spec-kit--context-engineering)
