---
title: Chat Participants
doc-type: guide
module: GitHub Copilot Context
order: 2
tags:
  - chat-participants
  - context-engineering
  - copilot

marp: true
theme: default
paginate: true
layout: default

header: Chat Participants for GitHub Copilot
footer: "© Context Engineering Workshop"
---

# Chat Participants

Chat participants are like **domain experts** who have a specialty that they can help you with.

You can specify a chat participant by typing `@` in the chat prompt box, followed by a chat participant name.

To see all available chat participants, type `@` in the chat prompt box.

---

## Built-in Chat Participants

GitHub Copilot provides several built-in chat participants that specialize in different aspects of development:

- **@workspace** - Project-aware assistance
- **@github** - GitHub platform workflows
- **@vscode** - IDE and editor features
- **@terminal** - Command-line and shell tasks

---

## @workspace Participant

The workspace participant has broad knowledge of your codebase and can:

- Answer questions about your project structure
- Suggest context-aware implementations
- Provide assistance based on your code

**Use this when:** You want Copilot to consider your entire project context.

---

## @github Participant

The GitHub participant helps with GitHub-specific workflows:

- Creating issues and pull requests
- Managing workflows and automation
- Accessing GitHub documentation
- Navigating repository features

**Use this when:** You need assistance with GitHub platform tasks.

---

## @vscode Participant

The VS Code participant specializes in:

- Visual Studio Code functionality
- Extension management and setup
- IDE settings and configuration
- Development environment help

**Use this when:** You need assistance with your development environment or editor.

---

## @terminal Participant

The Terminal participant helps with:

- Terminal and command-line tasks
- Shell script development
- Command suggestions for your OS
- System-level operations

**Use this when:** You need help with shell commands or scripting.

---

## Applying Chat Participants in This Workshop

Chat participants demonstrate **context engineering** principles:

1. **Specificity through Participants** - Choosing the right participant (e.g., @workspace vs general) shows how specific context improves assistance quality

2. **Targeted Context** - Each participant brings focused expertise, mirroring our workshop principle: better context = better results

3. **Tool Integration** - Combine participants with variables (#), custom instructions, and spaces for comprehensive context

4. **Hands-on Learning** - Experiment with different participants to see their impact on response quality

---

## Using Chat Participants Effectively

### Best Practices

- **Be explicit** - Type @ to select the appropriate participant rather than relying on general chat

- **Combine with other tools** - Use participants with chat variables (#), custom instructions, and workspace context

- **Experiment systematically** - Try different participants for the same query to understand their strengths

- **Learn from patterns** - Note which participants provide the best assistance for different task types

---

## Summary

Chat participants are a core **context engineering** tool in GitHub Copilot.

By choosing the right participant, you:
- Provide specific, targeted context
- Improve response quality and relevance
- Demonstrate context engineering principles
- Enhance your AI-assisted development workflow