---
title: Model Context Protocol (MCP)
doc-type: guide
module: GitHub Copilot Context
order: 7
tags:
  - mcp
  - model-context-protocol
  - copilot-extensions
  - context-engineering

marp: true
theme: default
paginate: true
layout: default

header: Model Context Protocol (MCP) for GitHub Copilot
footer: "© Context Engineering Workshop"
---

# Model Context Protocol (MCP)

**Extend GitHub Copilot's capabilities with custom tools and data sources**

MCP is the standardized way to provide **context and capabilities** that Copilot needs to assist you better.

---

## What is MCP?

Model Context Protocol (MCP) is an open standard that enables:

- **Tool Integration** - Connect custom tools and services
- **Data Access** - Provide Copilot access to your data sources
- **Capability Extension** - Add specialized functions tailored to your workflow
- **Standardized Communication** - Language-agnostic protocol for connecting tools

Think of MCP as **context engineering infrastructure** - it's how you architect context at the system level.

---

## Why MCP Matters for Context Engineering

Recall our core principle: **"Better context = Better results"**

MCP transforms this from a prompt-by-prompt concern into an **architectural practice**:

- **Persistent Context** - Tools and data are always available
- **Standardized Access** - Consistent way to expose capabilities
- **Reusable Infrastructure** - Build once, use everywhere
- **Team-Scale Solutions** - Share tools across your organization

---

## MCP in GitHub Copilot Workflow

```
┌─────────────────────────────────────────┐
│   Your Development Environment          │
│  ┌───────────────────────────────────┐  │
│  │  GitHub Copilot Chat              │  │
│  └────────────┬──────────────────────┘  │
│               │ Uses                     │
│  ┌────────────▼──────────────────────┐  │
│  │  MCP Configuration (.vscode/      │  │
│  │  mcp.json)                        │  │
│  └────────────┬──────────────────────┘  │
│               │ Manages                  │
│  ┌────────────▼──────────────────────┐  │
│  │  MCP Servers                      │  │
│  │  • Playwright (Browser tools)     │  │
│  │  • Context7 (Doc retrieval)       │  │
│  │  • MS Docs (Microsoft docs)       │  │
│  │  • GitHub (GitHub integration)    │  │
│  │  • Chrome DevTools                │  │
│  │  • Serena (Development toolkit)   │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

---

## MCP Servers Configured in This Workshop

Your `.vscode/mcp.json` file configures several servers:

### 1. **Playwright Server**
- **Purpose**: Browser automation and web interaction
- **Use Case**: Testing, web scraping, automated workflows
- **Context Benefit**: Copilot can help automate browser-based tasks

### 2. **Context7 Server**
- **Purpose**: Retrieve documentation from library databases
- **Use Case**: Look up official docs without manual searching
- **Context Benefit**: Copilot accesses the latest library documentation

### 3. **Microsoft Docs Server**
- **Purpose**: Access Microsoft and Azure documentation
- **Use Case**: Microsoft technology questions
- **Context Benefit**: Official, current Microsoft documentation context

---

## MCP Servers (Continued)

### 4. **GitHub Server**
- **Purpose**: GitHub platform integration
- **Use Case**: Repository operations, issue management, workflows
- **Context Benefit**: Copilot understands your GitHub context

### 5. **Chrome DevTools Server**
- **Purpose**: Browser developer tools integration
- **Use Case**: Performance analysis, debugging, DOM inspection
- **Context Benefit**: Deep inspection capabilities in Copilot interactions

### 6. **Serena Server**
- **Purpose**: Development toolkit and analysis
- **Use Case**: Code analysis, project insights
- **Context Benefit**: Project-aware capabilities for better assistance

---

## How MCP Applies to Context Engineering

### Structural Context
MCP provides **standardized structure** for context:
- Well-defined interfaces for tools
- Consistent communication patterns
- Predictable behavior across servers

### Memory Context
MCP creates **persistent, reusable context**:
- Tools stay configured once set up
- No need to repeat tool setup in every chat
- Team members share the same tools

### Instructional Context
MCP enables **capability documentation**:
- Tools describe what they can do
- Copilot knows capabilities without explicit instructions
- Better helps you leverage available tools

---

## Practical Example: Using MCP Servers

### Without MCP (Ad-hoc approach)
```
User: "Can you help me understand this web page?"
Copilot: "I can help, but I can't directly browse. 
         Tell me what you see..."
```

### With MCP (Integrated approach)
```
User: "Can you help me understand this web page?"
@Copilot + Playwright Server: Automatically visit the page,
                               analyze its structure,
                               provide detailed context
```

The difference: **MCP makes capabilities transparent and automatic**.

---

## Setting Up MCP Servers

MCP servers are configured in `.vscode/mcp.json`:

```json
{
  "servers": {
    "server-name": {
      "type": "stdio",  // or "http"
      "command": "npx",
      "args": ["@package/name@latest"]
    }
  }
}
```

**Key concepts:**
- **type**: How MCP communicates (stdio or HTTP)
- **command**: What executes the server
- **args**: Configuration passed to the server
- **env**: Environment variables for the server

---

## Creating Your Own MCP Server

MCP servers can be custom-built. Common patterns:

### Simple Tool Server
Expose domain-specific tools you use frequently:
- Code analysis tools
- Custom linters or validators
- Team-specific workflows

### Data Source Server
Provide access to internal systems:
- Your organization's documentation
- Internal APIs
- Project management systems

### Integration Server
Connect external services:
- CI/CD systems
- Deployment tools
- Monitoring dashboards

---

## Context Engineering Best Practices with MCP

### 1. **Choose Appropriate Servers**
Only enable servers you'll actually use. Too many servers = noise in context.

**Principle:** Reduce cognitive load by providing exactly what's needed.

### 2. **Understand Server Capabilities**
Know what each server can do so you can direct Copilot to use them.

**Principle:** Instructional context - help Copilot understand available tools.

### 3. **Combine with Other Context Strategies**
MCP works alongside custom prompts, chat participants, and variables.

**Principle:** Layered context - multiple strategies work together.

### 4. **Document for Your Team**
Create team standards about which MCP servers are available and when to use them.

**Principle:** Structural context - standardize how team members interact with Copilot.

---

## MCP vs Custom Prompts vs Chat Participants

| Aspect | MCP Servers | Custom Prompts | Chat Participants |
|--------|------------|---------------|--------------------|
| **Scope** | System-level | Task-level | Domain-level |
| **Persistence** | Always available | Invoked explicitly | Always available |
| **Reusability** | Across all chats | Specific workflows | Across all chats |
| **Context Type** | Capability context | Instructional context | Domain context |
| **Best For** | Tools & integrations | Specific workflows | Domain expertise |

---

## Layer Your Context

```
┌────────────────────────────────────────────────┐
│  Layer 4: MCP Servers (Capabilities)           │
│  └─ Tools, integrations, data access           │
├────────────────────────────────────────────────┤
│  Layer 3: Chat Participants (Domain Focus)     │
│  └─ @workspace, @github, etc.                  │
├────────────────────────────────────────────────┤
│  Layer 2: Custom Prompts (Workflow Templates)  │
│  └─ /command templates for repeated tasks      │
├────────────────────────────────────────────────┤
│  Layer 1: Individual Chat (Ad-hoc Context)     │
│  └─ Immediate prompts and selections           │
└────────────────────────────────────────────────┘

Each layer adds specific, targeted context
for increasingly complex assistance.
```

---

## Common MCP Patterns

### Pattern 1: Research & Documentation
**Servers**: Context7 + Microsoft Docs + GitHub
**Use Case**: Learning new libraries or APIs
**Benefit**: Copilot can fetch official documentation instantly

### Pattern 2: Browser-Based Tasks
**Servers**: Playwright + Chrome DevTools
**Use Case**: Automating web interactions
**Benefit**: Copilot can interact with web UIs

### Pattern 3: Development Workflows
**Servers**: GitHub + Serena + Chrome DevTools
**Use Case**: Managing development tasks end-to-end
**Benefit**: Copilot understands full project context

### Pattern 4: Multi-Tool Orchestration
**Servers**: All relevant servers
**Use Case**: Complex workflows requiring multiple tools
**Benefit**: Copilot can coordinate between systems

---

## Troubleshooting MCP Configuration

### Server Not Loading
- Verify `mcp.json` syntax is valid JSON
- Check command/args point to valid executables
- Review environment variables (especially API keys)

### Copilot Not Using Server
- Explicitly mention the server or tool in your prompt
- Use `@` for chat participants to surface available tools
- Check server logs for errors

### Performance Issues
- Too many servers can slow initialization
- Disable unused servers in `mcp.json`
- Monitor which servers are actually used

---

## Hands-On: Explore MCP Servers

Try this in Copilot Chat:

1. **Type `@`** - See available chat participants
2. **Mention a server in your prompt** - e.g., "Using Playwright..."
3. **Observe the capabilities** - What can each server do?
4. **Experiment with combinations** - Use multiple servers together
5. **Note what works** - Build your own patterns

**Key insight**: MCP visibility helps Copilot understand what's available.

---

## MCP and Team Context Engineering

### Standardize Context Infrastructure
Teams can define standard MCP configurations:
- Which servers every developer has
- Which servers for specific roles
- Security and access policies

### Share Server Configurations
`.vscode/mcp.json` can be version-controlled:
- New team members get the same setup
- Updates propagate across team
- Consistent experience for everyone

### Build Team-Specific Servers
Create MCP servers for team-specific needs:
- Internal documentation servers
- Team workflow integrations
- Custom analysis tools

---

## Summary

MCP is the **infrastructure layer** for context engineering:

- **Extends Copilot's capabilities** through standardized protocol
- **Provides persistent context** that survives across chats
- **Enables team-scale practices** through shared configurations
- **Complements prompts and participants** in layered context strategy

**Key Principle**: MCP transforms ad-hoc tools into **systematic, shared context infrastructure**.

---

## Next Steps

1. **Review `.vscode/mcp.json`** in this workshop repository
2. **Experiment with available servers** in Copilot Chat
3. **Identify workflows** that could benefit from MCP servers
4. **Create custom servers** for your team's specific needs
5. **Document and standardize** MCP configurations for your team

---

## Resources

- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Anthropic MCP Documentation](https://modelcontextprotocol.io/docs)
- [MCP Server Implementations](https://github.com/modelcontextprotocol/servers)
- [GitHub Copilot Extensions](https://docs.github.com/en/copilot/customization)
- [Building MCP Servers](https://modelcontextprotocol.io/docs/tools/building-servers)