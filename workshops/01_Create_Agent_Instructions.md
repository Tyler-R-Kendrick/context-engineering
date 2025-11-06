# Create Agent Instructions

## Task Objective
Create an `AGENTS.md` in the root directory that thoroughly explains how AI coding assistants and new contributors should operate within the repository.

## Context Engineering Problems Addressed
- Repeatedly re-teaching assistants and teammates the project structure and conventions.
- Context drift when refresh triggers, retrieval priorities, or tool boundaries are undocumented.
- Accidental exposure to untrusted code or data sources due to missing security guidance.
- Slow onboarding because critical setup steps are scattered across chat transcripts.

## How to Execute

1. **Audit the repository**: list build commands, test workflows, coding standards, deployment steps, and critical directories.
2. **Define retrieval guidance**: document which folders, files, and external systems provide authoritative context, plus exclusions to avoid noise or secrets.
3. **Describe workflows**: capture branch strategy, review expectations, commit hygiene, and communication protocols the agent should follow.
4. **Specify tool use**: provide clear instructions for how and when the agent should invoke internal tools.
5. **Set validation and safety rules**: include diff review requirements, security checks, and expected handoff formatting for generated changes.
6. **Publish and test**: add the file to the repo, then ask Copilot to summarize it to ensure the instructions are understood as intended.
7. **Iterate**: capture strong and weak examples, refine reasoning scaffolds, and add guardrails until the guidance reliably produces the desired output.

## Further Reading
- [Deep dive: Agent instructions](../slides/github-copilot-context/agents_instructions.md)
- [Implementation guidance](../slides/github-copilot-context/custom_agents.md#designing-reliable-instructions)
