---
title: Custom Agents
doc-type: guide
module: GitHub Copilot Context
order: 7
tags:
  - custom-agents
  - context-engineering
  - specialized-expertise
  - agent-customization

marp: true
theme: default
paginate: true
layout: default

header: Custom Agents for GitHub Copilot
footer: "© Context Engineering Workshop"
---

# Custom Agents

Custom agents are specialized AI assistants with tailored expertise for specific development tasks and workflows.

---

## What is a Custom Agent?

A **custom agent** is a specialized version of GitHub Copilot configured with:

- **Tailored expertise** for specific development roles or tasks
- **Custom instructions** that define the agent's behavior and approach
- **Persistent personality** that maintains consistent assistance patterns
- **Domain focus** that narrows scope to particular areas

**Think of it as:** Hiring a specialist instead of a generalist

---

## Why Custom Agents Matter

### The Problem: One-Size-Fits-All Assistance

Default Copilot provides broad, general assistance but lacks specialization:

- **Context fatigue** - Generic responses to domain-specific problems
- **Tone mismatch** - Formal writing help vs. casual coding assistance
- **Process incompatibility** - Generic suggestions don't match team workflows
- **Expertise gaps** - Generalist responses miss domain patterns

### The Solution: Custom Agents

Custom agents solve these problems through specialization:

```
Generic Copilot          vs.    Custom Agent
├─ General advice              ├─ Specialized knowledge
├─ Default tone                ├─ Consistent personality
├─ One-size-fits-all           ├─ Tailored approach
└─ No process knowledge        └─ Workflow-aware
```

---

## Key Components of Custom Agents

### 1. Custom Instructions
Define how the agent thinks and responds:

```markdown
# Example: "Security-First Architect" Agent

You are an expert security architect. When reviewing code:

- Always consider security implications first
- Suggest security patterns (OWASP Top 10)
- Ask about threat models and data flows
- Recommend security testing strategies
- Point out potential vulnerabilities
```

### 2. Task Specialization
Focus on specific development tasks:

- **Code reviewers** - Focus on quality, performance, security
- **Documentation specialists** - Emphasize clarity and examples
- **Test architects** - Design comprehensive test coverage
- **Refactoring experts** - Improve code structure and performance
- **Onboarding guides** - Explain concepts to newcomers

### 3. Context Anchoring
Ground the agent in your project:

- Reference your coding standards
- Link to architecture decisions
- Mention technology stack
- Include team processes
- Reference common patterns

---

## Common Custom Agent Examples

### 1. Code Review Agent

**Purpose:** Thorough and constructive code reviews

```
Specialties:
✓ Performance optimization
✓ Security vulnerabilities
✓ Design pattern alignment
✓ Test coverage analysis
✓ Documentation completeness

Tone: Constructive, educational, specific
```

### 2. Documentation Agent

**Purpose:** Clear, comprehensive documentation

```
Specialties:
✓ Technical explanations
✓ API documentation
✓ User guides and tutorials
✓ Architecture diagrams
✓ Code examples

Tone: Clear, beginner-friendly, example-rich
```

### 3. Test Architecture Agent

**Purpose:** Comprehensive testing strategies

```
Specialties:
✓ Unit test design
✓ Integration test coverage
✓ End-to-end test scenarios
✓ Mock and fixture strategy
✓ Edge case identification

Tone: Thorough, systematic, quality-focused
```

### 4. Onboarding Agent

**Purpose:** Help new team members understand the codebase

```
Specialties:
✓ Explain project structure
✓ Walk through key files
✓ Describe team patterns
✓ Suggest learning paths
✓ Answer fundamental questions

Tone: Patient, encouraging, pedagogical
```

### 5. Refactoring Agent

**Purpose:** Improve code structure and maintainability

```
Specialties:
✓ Identify code smells
✓ Suggest refactoring patterns
✓ Improve readability
✓ Reduce complexity
✓ Maintain backward compatibility

Tone: Pragmatic, incremental, thoughtful
```

---

## Creating a Custom Agent

### Step 1: Define the Specialization

Identify a specific role or task:

```
Questions to ask:
- What problem does this agent solve?
- Who will use this agent?
- What are their key tasks?
- What domain expertise is needed?
- What tone should it have?
```

### Step 2: Write Custom Instructions

Create clear, specific guidance:

```markdown
# System Prompt

You are a [ROLE] specializing in [DOMAIN].

Your approach:
- [Guideline 1]
- [Guideline 2]
- [Guideline 3]

When helping, always consider:
- [Context element 1]
- [Context element 2]

Preferred format for responses:
- [Format guideline]
```

### Step 3: Test and Iterate

Validate the agent's behavior:

```
Test checklist:
□ Agent maintains consistent personality
□ Responses align with specialization
□ Tone is appropriate and consistent
□ Examples are relevant and helpful
□ Output format matches expectations
```

### Step 4: Document Usage

Share agent guidelines with team:

```markdown
# Usage Guidelines

## When to use this agent:
- Task 1
- Task 2

## What to provide:
- Context 1
- Context 2

## Expected output:
- Result 1
- Result 2
```

---

## Real-World Example: Documentation Agent

### Scenario
A team struggling with API documentation quality and consistency across services.

### The Problem
```
Current state:
- Inconsistent format across services
- Missing examples
- Outdated parameter descriptions
- No generated documentation
- Hard to onboard new developers
```

### Custom Agent Solution

```markdown
# Documentation Specialist Agent

You are an expert technical writer who creates
clear, comprehensive API documentation.

Your approach:
1. Start with overview, then details
2. Include practical code examples
3. Document all parameters with types
4. Note common gotchas
5. Suggest related endpoints

Always include:
- Purpose and use cases
- Request/response examples
- Error scenarios
- Performance considerations
- Links to related resources

Format: Markdown with consistent structure
```

### Results
- Consistent documentation format
- All APIs documented with examples
- Reduced onboarding time
- Better service integration understanding

---

## Applying Custom Agents in This Workshop

Custom agents demonstrate core **context engineering** principles:

### 1. Targeted Context Through Specialization
```
Generic Copilot → Sees all code equally
Custom Agent    → Focuses on relevant patterns
```

### 2. Context Persistence
- Agent personality persists across conversations
- Consistent approach to familiar patterns
- Team knowledge encoded in agent instructions

### 3. Process Integration
- Agents embody team standards and practices
- Workflows become automated through specialization
- Knowledge transfer through agent behavior

### 4. Scalable Expertise
- Expertise available to entire team
- No single expert bottleneck
- Consistent assistance regardless of who uses it

---

## Best Practices for Custom Agents

### 1. Be Specific and Clear

**❌ Vague:**
```
You are a helpful coding assistant.
```

**✅ Specific:**
```
You are an expert in TypeScript performance optimization.
When reviewing code, identify bottlenecks and suggest
specific optimizations using profiling data when available.
```

### 2. Anchor to Your Context

**❌ Generic:**
```
Consider best practices when reviewing code.
```

**✅ Context-Aware:**
```
Our stack: TypeScript, React 18, Node.js 20.
Review against our documented patterns in STANDARDS.md.
Reference our shared component library.
```

### 3. Define Expected Tone and Format

**❌ Undefined:**
```
Help with code reviews.
```

**✅ Defined:**
```
Provide constructive feedback in 3-4 points.
Use encouraging language while being specific.
Format: bullet points with brief explanations.
End with actionable suggestions.
```

### 4. Include Examples

**❌ Without examples:**
```
Suggest refactoring improvements.
```

**✅ With examples:**
```
When suggesting refactoring:
- Show the original code
- Show the improved version
- Explain the benefits
Example: Convert callback to async/await, explain readability gain
```

### 5. Test Thoroughly

- Try edge cases
- Validate tone consistency
- Check context integration
- Gather team feedback
- Iterate based on results

---

## Combining Custom Agents With Other Tools

### Custom Agents + Chat Participants

```
"@workspace, using custom Documentation Agent,
explain this API endpoint"

Result: Specialized documentation explanation
with full project context
```

### Custom Agents + Chat Variables

```
"#architecture.md Custom Code Review Agent,
review this implementation"

Result: Review against documented architecture
with consistent tone and focus
```

### Custom Agents + Custom Instructions

```
Agent instructions set tone and specialty
Repository instructions add context and standards
Combined: Specialized expertise + local context
```

### Custom Agents + Copilot Spaces

```
Agent uses Space as knowledge base
Space provides consistent context
Result: Specialized agent with team knowledge
```

---

## Common Pitfalls to Avoid

### ❌ Don't: Create Too Many Agents

**Problem:** Team gets confused, can't remember which to use
**Solution:** Create agents for distinct, frequently-needed roles

### ❌ Don't: Make Instructions Too Long

**Problem:** Agent loses focus, instructions compete with each other
**Solution:** Keep core instructions concise, link to documentation

### ❌ Don't: Forget to Test

**Problem:** Agent behaves inconsistently or ignores specialization
**Solution:** Validate with real tasks before team adoption

### ❌ Don't: Leave Agents Static

**Problem:** As standards change, agents become outdated
**Solution:** Review and update instructions quarterly

### ❌ Don't: Ignore Feedback

**Problem:** Team stops using agents that don't match their needs
**Solution:** Gather feedback and iterate regularly

---

## Summary

Custom agents are specialized AI assistants that bring **context engineering** to life:

✅ **Specialize** expertise for specific tasks
✅ **Persist** consistent approach across conversations
✅ **Integrate** with your team's workflows and standards
✅ **Scale** expertise to your entire team
✅ **Evolve** with your team's growing knowledge

### Key Takeaways

1. **Specialization matters** - Focused agents provide better assistance than generalists
2. **Context is key** - Ground agents in your project, standards, and processes
3. **Testing is essential** - Validate agent behavior before team adoption
4. **Integration is powerful** - Combine with other Copilot context tools
5. **Maintenance is ongoing** - Keep agents updated as team and standards evolve

### Next Steps

1. Identify your first custom agent need (e.g., code review, documentation)
2. Draft custom instructions based on this specialization
3. Test with your team on real tasks
4. Gather feedback and iterate
5. Expand to additional agents based on team needs

### Real Impact

Custom agents transform Copilot from generic assistant into **specialized team member**:
- Consistent approach to common tasks
- Reduced cognitive load on team
- Faster onboarding of new developers
- Elevated code and documentation quality