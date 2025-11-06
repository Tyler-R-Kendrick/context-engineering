# Set Up Copilot Spaces (optional)

## Task Objective
Create a Copilot Space that aggregates critical repositories, documentation, and context variables so every assistant interaction starts with rich, shared knowledge.

## Context Engineering Problems Addressed
- Context fragmentation across services or teams slows decision-making and increases hallucinations.
- Documentation rot occurs when canonical references live outside version control or lack owners.
- AI assistants miss cross-repo dependencies when the workspace scope is too narrow.

## How to Execute
1. **Create the Space**: in GitHub, open Spaces, create a new space, and invite the relevant collaborators.
2. **Attach context sources**: link primary repositories, architecture docs, ADRs, dashboards, and knowledge bases that need to be discoverable.
3. **Organize structure**: add sections or boards for service maps, decision logs, reusable prompts, agent instructions, and escalation paths.
4. **Layer context in chats**: combine Spaces with chat participants (`@workspace`), variables (`#prod-deploy`), MCP servers, and custom prompts to deliver targeted instructions.
5. **Abstract semantic extensions**: provide abstract overridable instructions to be shared in a more reusable way; then allow the individual repos to provide the implementation of those generalized instructions.

## Further Reading
- [Copilot Spaces overview](../slides/github-copilot-context/copilot_spaces.md)
- [Preventing context rot](../slides/github-copilot-context/copilot_spaces.md#applying-copilot-spaces-in-this-workshop)
- [Best practices & pitfalls](../slides/github-copilot-context/copilot_spaces.md#best-practices-for-copilot-spaces)
