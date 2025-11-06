---
title: Spec-Kit & Spec-Driven Development
doc-type: guide
module: GitHub Copilot Context
order: 7
tags:
  - spec-kit
  - spec-driven-development
  - context-engineering
  - copilot

marp: true
theme: default
paginate: true
layout: default

header: Spec-Kit & Spec-Driven Development
footer: "© Context Engineering Workshop"
---

# Spec-Kit & Spec-Driven Development

**Transform how you build software** by flipping the traditional development model on its head.

Spec-Kit is an open-source toolkit that helps you use **specifications as executable artifacts** rather than just documentation scaffolding.

---

## What is Spec-Driven Development?

Traditional development flow:
```
Requirements → Code → (Specifications discarded)
```

Spec-Driven Development flow:
```
Requirements → Specifications → Implementations → Working Code
```

**Key insight**: Specifications become the *primary artifact* that generates implementations, not the other way around.

---

## The Problem Spec-Kit Solves

### "Vibe Coding" vs. Intentional Development

**Vibe Coding** (Traditional):
- ❌ Write code first, clarify requirements as you go
- ❌ Tests written after implementation
- ❌ Inconsistent quality across features
- ❌ Specifications treated as documentation burden

**Spec-Driven** (Spec-Kit):
- ✅ Define specifications first, generate code
- ✅ Tests derived from specifications
- ✅ Consistent quality and architecture
- ✅ Specifications drive implementation

---

## What is GitHub Spec-Kit?

A toolkit that enables **specification-first development** with AI coding agents.

**Core Components:**
- `specify` CLI - Initialize and manage spec-driven projects
- Slash commands - Interactive workflow steps (e.g., `/speckit.specify`)
- Project artifacts - Constitution, specifications, plans, tasks
- Multi-agent support - Works with GitHub Copilot, Claude Code, Cursor, Windsurf, and more

**Open Source**: https://github.com/github/spec-kit

---

## The Spec-Driven Workflow

A five-step structured process with an AI coding agent:

### Step 1: Establish Principles
**Command**: `/speckit.constitution`
- Define project governing principles
- Set code quality standards
- Establish testing requirements
- Document architectural decisions

*Result*: `.specify/memory/constitution.md`

---

## The Spec-Driven Workflow (continued)

### Step 2: Create Specifications
**Command**: `/speckit.specify`
- Describe what you want to build
- Focus on **what** and **why**, not technology
- Include user stories and requirements
- Define success criteria

*Result*: `.specify/artifacts/specification.md`

**Tip**: Be explicit. The AI uses this as the primary guide.

---

## The Spec-Driven Workflow (continued)

### Step 3: Create Technical Plan
**Command**: `/speckit.plan`
- Specify your tech stack
- Define architecture choices
- Provide constraints and requirements
- Document infrastructure decisions

*Result*: `.specify/artifacts/plan.md`

---

## The Spec-Driven Workflow (continued)

### Step 4: Generate Tasks
**Command**: `/speckit.tasks`
- Break down the plan into actionable tasks
- Create implementation sequence
- Identify dependencies
- Define acceptance criteria

*Result*: `.specify/artifacts/tasks.md`

---

## The Spec-Driven Workflow (continued)

### Step 5: Execute Implementation
**Command**: `/speckit.implement`
- Execute all tasks systematically
- Generate working code
- Follow the established architecture
- Maintain consistency with specifications

*Result*: Working implementation

---

## Spec-Kit CLI Installation

### Quick Start

```bash
# Install with uv (recommended)
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Initialize a new project
specify init my-project --ai copilot
```

### Verify Installation

```bash
# Check system requirements
specify check

# See if tools are installed
# This checks for: git, claude, gemini, code, cursor-agent, etc.
```

---

## Supported AI Agents

Spec-Kit works with **many AI coding assistants**:

✅ GitHub Copilot
✅ Claude Code
✅ Cursor
✅ Windsurf
✅ Gemini CLI
✅ Qwen Code
✅ opencode
✅ Amazon Q Developer

**Flexibility**: The process works regardless of your chosen agent.

---

## Slash Commands Reference

Once initialized, use these commands in your AI agent:

| Command | Purpose |
|---------|---------|
| `/speckit.constitution` | Create project principles |
| `/speckit.specify` | Define requirements |
| `/speckit.clarify` | Clarify underspecified areas |
| `/speckit.plan` | Create technical plan |
| `/speckit.analyze` | Check consistency |
| `/speckit.tasks` | Generate task list |
| `/speckit.implement` | Execute tasks |
| `/speckit.checklist` | Create quality checklist |

---

## Practical Example: Photo Album App

### Step 1: Constitution
```
/speckit.constitution
Create principles focused on code quality, 
accessibility, performance, and user experience.
```

### Step 2: Specification
```
/speckit.specify
Build an application that helps users organize 
photos into albums. Albums are grouped by date 
and can be reorganized by drag-and-drop. Within 
each album, photos display in a tile interface.
```

---

## Practical Example: Photo Album App (continued)

### Step 3: Technical Plan
```
/speckit.plan
Use Vite with minimal dependencies. Vanilla HTML, 
CSS, and JavaScript. Store metadata in local SQLite 
database. No external image uploads.
```

### Step 4: Generate Tasks
```
/speckit.tasks
```
*(System generates actionable task list)*

### Step 5: Implement
```
/speckit.implement
```
*(AI executes all tasks systematically)*

---

## How Spec-Kit Integrates with GitHub Copilot

### 1. Custom Instructions
Pair Spec-Kit with custom instructions in your repository to provide:
- Project constitution as context
- Specification documents for reference
- Architectural guidelines

### 2. Workspace Context
Use `@workspace` participant with Spec-Kit:
- Copilot understands specification artifacts
- References plan and architecture
- Maintains consistency across implementation

---

## How Spec-Kit Integrates with GitHub Copilot (continued)

### 3. Task-Based Development
Instead of asking for features ad-hoc:
- Specifications define the scope
- Tasks provide incremental steps
- Copilot follows structured workflow
- Reduces context switching

### 4. Multi-File Coordination
Spec-Kit helps Copilot understand:
- Inter-component dependencies
- Architectural boundaries
- How components fit together

---

## Spec-Kit & Context Engineering

### How Spec-Kit Applies Context Engineering Principles

**Structural Context**
- Constitutional principles structure all decisions
- Specifications define interfaces
- Plans establish architecture

**Memory Context**
- Saved artifacts become team knowledge base
- Constitution guides future decisions
- Specifications prevent scope creep

**Instructional Context**
- Clear step-by-step workflow
- Explicit constraints and goals
- Focused AI assistance

---

## Using Spec-Kit in This Workshop

### Exercise Application

Within the context engineering workshop, Spec-Kit demonstrates:

1. **Better Prompts Through Specs** (Exercise 1)
   - Specification is a well-structured prompt
   - Clear requirements reduce ambiguity

2. **Context Through Documentation** (Exercise 2)
   - Constitution provides project context
   - Plans provide architectural context
   - These guide all subsequent interactions

---

## Using Spec-Kit in This Workshop (continued)

3. **Test-Driven Context** (Exercise 3)
   - Tasks include test requirements
   - Tests validate specification compliance
   - Documentation becomes requirements

4. **Tools & Context** (Exercise 4)
   - Slash commands are specialized tools
   - Each tool takes structured input
   - Tools work together in sequence

---

## Development Phases with Spec-Kit

### Greenfield (0-to-1)
**Start from scratch** with high-level requirements
- Generate comprehensive specifications
- Plan full architecture
- Build production-ready from day one

### Creative Exploration
**Try multiple approaches** in parallel
- Different tech stacks
- Alternative architectures
- Competing designs

### Brownfield Enhancement
**Iteratively improve** existing systems
- Add new features
- Modernize legacy code
- Refactor and optimize

---

## Best Practices for Spec-Kit

### ✅ Do

- **Start with clear requirements** - Specification quality determines output quality
- **Include principles** - Constitution prevents inconsistency
- **Break tasks into steps** - Smaller tasks = more reliable implementation
- **Version control specs** - Track how specifications evolve
- **Use parallel exploration** - Try multiple technical approaches
- **Document decisions** - Plan explains why, not just what

### ❌ Don't

- **Skip the constitution** - Principles prevent tech debt
- **Rush the specification** - Vague specs → vague code
- **Ignore the plan** - Without architecture, you get chaotic code
- **Mix concerns** - Keep specification separate from technical plan

---

## Project Structure with Spec-Kit

```
my-project/
├── .specify/
│   ├── memory/
│   │   └── constitution.md      # Project principles
│   └── artifacts/
│       ├── specification.md     # What to build
│       ├── plan.md             # Technical architecture
│       ├── tasks.md            # Implementation steps
│       └── analysis.md         # Consistency checks
├── src/                         # Generated code
├── tests/                       # Specification-driven tests
├── docs/                        # Generated documentation
└── .github/
    └── prompts/                 # Custom prompts for Copilot
```

---

## Getting Started with Spec-Kit Today

### Immediate Steps

1. **Install Specify CLI**
   ```bash
   uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
   ```

2. **Initialize a test project**
   ```bash
   specify init my-spec-project --ai copilot
   ```

3. **Open in your AI agent** (GitHub Copilot, Claude Code, etc.)

4. **Start with constitution**
   ```
   /speckit.constitution
   ```

5. **Create your first specification**
   ```
   /speckit.specify
   ```

---

## Common Patterns for Spec-Kit

### Pattern 1: Feature Development
Specification → Plan → Tasks → Implementation

Ideal for: New features in established codebases

### Pattern 2: New Project
Constitution → Specification → Plan → Tasks → Implementation

Ideal for: Greenfield projects with team standards

### Pattern 3: Code Modernization
Analysis → Updated Plan → Migration Tasks → Implementation

Ideal for: Modernizing legacy systems

---

## Advanced: Optional Commands

### `/speckit.clarify`
Ask Copilot to identify ambiguities in specifications before planning.

```
/speckit.clarify
Which parts of the specification are underspecified?
What additional details would help the implementation?
```

### `/speckit.analyze`
Check consistency between specification, plan, and tasks.

```
/speckit.analyze
Are the tasks aligned with the specification?
Does the plan support all requirements?
```

### `/speckit.checklist`
Create quality validation checklist.

```
/speckit.checklist
Create a checklist for testing this specification.
```

---

## Key Differences: Spec-Kit vs Traditional Development

| Aspect | Traditional | Spec-Kit |
|--------|-------------|----------|
| **Starting Point** | Write code | Write specification |
| **Requirements** | Implicit in code | Explicit in artifacts |
| **Architecture** | Emerges over time | Planned upfront |
| **Quality** | Varies by developer | Consistent via constitution |
| **Testing** | After code | Derived from spec |
| **Scalability** | Manual coordination | Structured workflow |

---

## Spec-Kit Within Context Engineering

### The Context Engineering Stack

```
Context Engineering (How to communicate with AI)
    ↓
Prompt Engineering (Basic techniques)
    ↓
Advanced Prompts (Chains, reasoning)
    ↓
Tools & Participants (Custom prompts, agents)
    ↓
Spec-Kit (Specification-first development)
```

**Spec-Kit is the ultimate application** of context engineering principles to development workflows.

---

## Summary: Spec-Kit Key Takeaways

**Spec-Kit transforms development by:**

1. **Prioritizing specifications** over ad-hoc coding
2. **Providing structured workflow** with slash commands
3. **Enabling consistent quality** through constitutional principles
4. **Supporting multiple AI agents** (Copilot, Claude, Cursor, etc.)
5. **Creating reusable artifacts** (specs, plans, tasks)
6. **Reducing context switching** through systematic workflow

**Result**: Faster, more consistent, higher-quality software development.

---

## Resources

**Official Documentation:**
- [GitHub Spec-Kit Repository](https://github.com/github/spec-kit)
- [Spec-Driven Development Methodology](https://github.com/github/spec-kit/blob/main/spec-driven.md)
- [Specify CLI Documentation](https://github.com/github/spec-kit)

**Try It Now:**
```bash
specify init my-first-spec-project --ai copilot
```

**Next Steps:**
- Create a specification for a feature you're building
- Establish principles for your team
- Use Spec-Kit with GitHub Copilot in your next project

---

## Questions?

**Key Concept to Remember:**

> Specifications are not documentation you create *after* coding. They are the **primary artifact** that *drives* implementation.

Spec-Kit makes this practical through an AI-native workflow.

---

## Exercise: Spec-Kit in Action

**Try this now:**

1. Initialize a Spec-Kit project
   ```bash
   specify init my-app --ai copilot
   ```

2. Run the constitution command
   ```
   /speckit.constitution
   ```

3. Create a specification for a small feature
   ```
   /speckit.specify
   [Describe what you want to build]
   ```

4. Create a technical plan
   ```
   /speckit.plan
   [Describe your tech stack]
   ```

5. Generate tasks
   ```
   /speckit.tasks
   ```

**Observe** how the structured approach produces better results than ad-hoc prompts!