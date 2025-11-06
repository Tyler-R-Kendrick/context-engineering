# Create Custom Agents (Optional)

## Task Objective
Define specialized Copilot Custom Agents (or instruction files for other IDEs) that encode expert behavior for critical domains such as security reviews, documentation, or performance tuning.

> NOTE! Custom Agents are in preview and are only available with Preview version of VS Code.

## Context Engineering Problems Addressed
- Generic assistants ignore domain-specific standards, creating rework for subject-matter experts.
- Knowledge silos form when tacit expertise is not captured in persistent agent instructions.
- Important guardrails (e.g., secure coding checks) get skipped when the base assistant lacks specialized context.
- Team outputs vary in tone and format, making code review and documentation harder to maintain.

## How to Execute
1. **Select high-impact roles**: identify workflows needing consistent expert judgment (e.g., API design, compliance, translations).
2. **Gather expertise**: interview domain owners to capture heuristics, reference materials, and mandatory checklists.
3. **Write the agent profile**: document objectives, required inputs, boundaries, tone, and escalation rules so the agent acts predictably.
4. **Embed reference links**: point to architecture docs, style guides, or MCP-enabled tools the agent should consult.
5. **Pilot and refine**: run the agent on sample tasks, collect feedback from maintainers, and update instructions quarterly or after major changes.

## Further Reading
- [Custom agent patterns](../slides/github-copilot-context/custom_agents.md)
- [Agent instruction checklist](../slides/github-copilot-context/agents_instructions.md#agent-instruction-checklist)
- [Advanced theory recap](../slides/01-problem-statement.md)
