---
theme: default
highlighter: shiki
lineNumbers: true
transition: slide-left
---

# Agent Instructions

Two complementary standards for context management

---

# Two Complementary Standards

GitHub Copilot works with two context management approaches

| Aspect | agents.md | copilot-instructions.md |
|--------|-----------|------------------------|
| **Standard** | OpenAI emerging standard | GitHub Copilot specific |
| **Location** | Repository root | Repository root or `.github/` |
| **Audience** | Any AI agent/tool in workflow | GitHub Copilot specifically |

---

# AGENTS.MD

> Think of AGENTS.md as a README for agents: a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project.

---

# Getting Started with AGENTS.MD

## Step 1: Add AGENTS.md
Create an AGENTS.md file at the root of the repository. Most coding agents can scaffold one if you ask.

## Step 2: Cover What Matters
Add sections that help agents work effectively:

<v-clicks>

- Project overview
- Build and test commands
- Code style guidelines
- Testing instructions
- Security considerations

</v-clicks>

---

# AGENTS.MD for Advanced Setups

## Step 3: Add Extra Instructions
Include anything you'd tell a new teammate:

<v-clicks>

- Commit message guidelines
- Pull request conventions
- Security gotchas
- Large datasets
- Deployment steps

</v-clicks>

---

# AGENTS.MD in Monorepos

## Step 4: Use Nested AGENTS.md Files

Place an AGENTS.md inside each package for subproject-specific instructions.

Agents automatically read the nearest file in the directory tree:
- ✅ The closest one takes precedence
- ✅ Every subproject ships tailored instructions
- 📊 Example: OpenAI repo has 88 AGENTS.md files

---

# Custom Instructions for GitHub Copilot

Tailor chat responses to your team's workflow

GitHub Copilot can provide chat responses tailored to:
- How your team works
- The tools you use
- The specifics of your project

Instead of repeatedly adding context to queries, create a file that automatically provides this information.

---

# Setting Up Custom Instructions

## Prerequisites

<v-clicks>

1. A custom instructions file (see next slide)
2. "Use Instruction Files" (VS Code) or "Enable custom instructions" (Visual Studio) enabled in settings
   - ✅ Enabled by default in VS Code
   - ❌ Disabled by default in Visual Studio

</v-clicks>

---

# Creating a Custom Instructions File

## File Location & Format

Create `.github/copilot-instructions.md` in your repository:

```bash
.github/
└── copilot-instructions.md
```

<v-clicks>

### Guidelines

- Use Markdown format for natural language instructions
- Whitespace between instructions is ignored
- Write as a single paragraph, one per line, or separated for legibility
- Instructions are available to Copilot but not displayed in chat
- Enables higher quality, context-aware responses

</v-clicks>
