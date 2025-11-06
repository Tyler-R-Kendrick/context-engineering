# Install and Configure MCP Servers

## Task Objective
Enable Model Context Protocol (MCP) servers so Copilot and other agents can securely access sanctioned tools, datasets, and documentation during conversations.

## Context Engineering Problems Addressed
- Agents repeatedly ask for the same context because external tools are not connected.
- Responses rely on hallucinations when assistants cannot reach authoritative systems.
- Inconsistent developer experience when teammates manage different local scripts and credentials.
- Security risks from improvising CLI access without centrally managed policies.

## How to Execute
1. **Review available servers**: determine which official MCP servers (e.g., Microsoft Docs, Context7, GitHub, Playwright, Serena) map to your workflows.
2. **Install prerequisites**: ensure language runtimes (`node`, `python`, `uv`, etc.) and server binaries are available, following each server’s installation guide.
3. **Configure `.vscode/mcp.json`**: define server commands, arguments, environment variables, and descriptions so Copilot can auto-discover the tooling.
4. **Authenticate securely**: store API tokens or credentials using recommended secret managers and document rotation procedures.
5. **Test integration**: restart Copilot Chat, verify the servers appear in the `@` menu, and issue trial prompts that exercise each tool.
6. **Document usage rules**: explain when to invoke each server, expected latency, and fallback plans if the server is offline.
7. **Update prompts**: refresh existing prompts to ensure effective tool selection from the registered MCPs.

## Further Reading
- [MCP overview and architecture](../slides/github-copilot-context/mcp.md)
- [Layered context strategies](../slides/github-copilot-context/mcp.md#layer-your-context)
- [Troubleshooting guide](../slides/github-copilot-context/mcp.md#troubleshooting-mcp-configuration)
