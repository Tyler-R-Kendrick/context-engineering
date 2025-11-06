---
title: Copilot Spaces
doc-type: guide
module: GitHub Copilot Context
order: 5
tags:
  - copilot-spaces
  - context-engineering
  - shared-context
  - microservices

marp: true
theme: default
paginate: true
layout: default

header: Copilot Spaces for GitHub Copilot
footer: "© Context Engineering Workshop"
---

# Copilot Spaces

Centralized context for distributed teams and microservices architectures

---

## What is a Copilot Space?

A **Copilot Space** is a collaborative container that centralizes shared context and documentation for GitHub Copilot.

Key characteristics:
- **Persistent context** that persists across conversations and team members
- **Shared knowledge base** accessible to all participants
- **Organized resources** including documentation, code references, and decisions
- **Team alignment** ensuring consistent context across contributors

**Think of it as:** A dedicated knowledge hub for AI-assisted development

---

## The Problem: Context Loss in Microservices

When large monolithic repositories are refactored into microservices:

### Context Fragmentation
- Each microservice repository becomes isolated
- Institutional knowledge is scattered across multiple repos
- Team members lack holistic project understanding
- New developers must search multiple sources for context

### Integration Challenges
- Understanding how services interact becomes difficult
- Shared patterns and standards are unclear
- Cross-service consistency is hard to maintain
- AI assistants see only individual service context

### Knowledge Decay
- Common decisions and rationale are forgotten
- Design patterns diverge across services
- Architecture documentation becomes stale
- Why decisions were made is lost over time

---

## Copilot Spaces as a Solution

Copilot Spaces bridge the context gap in microservices architectures by:

1. **Centralizing Knowledge**
   - Single source of truth for project context
   - Unified documentation across all services
   - Shared architectural decisions and patterns

2. **Maintaining Context Continuity**
   - Team context persists across conversations
   - Consistent assistance regardless of individual service
   - Collective institutional memory

3. **Improving AI Assistance**
   - Copilot understands full system architecture
   - Service relationships and dependencies are clear
   - Consistency rules and patterns are explicit

---

## What to Include in a Copilot Space

### Essential Documentation

#### 1. Architecture Overview
```markdown
# System Architecture

## Services Overview
- **Auth Service**: User authentication and JWT tokens
- **API Service**: Main REST API for client applications  
- **Data Service**: Database access and caching layer
- **Notification Service**: Email and push notifications

## Service Interactions
[Diagram or detailed description of how services communicate]

## Technology Stack
- Runtime: Node.js 20.x LTS
- Language: TypeScript 5.x
- API: REST with OpenAPI 3.0
```

#### 2. Shared Patterns and Standards
```markdown
# Development Standards

## Coding Conventions
- Use async/await (no callbacks)
- Error handling with try/catch blocks
- Comprehensive input validation
- TypeScript strict mode enabled

## API Design Patterns
- RESTful endpoints
- Standardized error responses
- JWT authentication on all endpoints
```

#### 3. Design Decisions and ADRs
```markdown
# Architecture Decision Records (ADRs)

## ADR-001: Microservices Over Monolith
- **Decision**: Refactor monolithic application into microservices
- **Rationale**: Scalability, independent deployment, team autonomy
- **Consequences**: Distributed system complexity, eventual consistency

## ADR-002: TypeScript for All Services
- **Decision**: Use TypeScript across all service implementations
- **Rationale**: Type safety, developer experience, consistency
```

---

## Setting Up a Copilot Space

### Step 1: Create the Space
- Navigate to GitHub and create a new Copilot Space
- Name it descriptively (e.g., "MyApp Architecture")
- Invite relevant team members

### Step 2: Add Repositories
```
Repositories to include:
- Main project documentation repository
- Each microservice repository
- Shared libraries and utilities repository
- Example/template repository
```

### Step 3: Add Key Documentation Files
- `README.md` - Project overview
- `ARCHITECTURE.md` - System design and service interactions
- `STANDARDS.md` - Coding and API standards
- `CONTRIBUTING.md` - How to contribute
- Design decision records (ADRs)

### Step 4: Configure Context Rules
- Set which files should always be included
- Define search priorities for documentation
- Configure refresh triggers for stale context

---

## Real-World Example: E-Commerce Platform

### Scenario
An e-commerce company refactored from a monolithic application into four microservices:
- **User Service**: Account and profile management
- **Product Service**: Catalog and inventory
- **Order Service**: Order processing and tracking
- **Payment Service**: Payment processing and reconciliation

### Problem Without Copilot Spaces
- Developers working on Payment Service don't understand User Service schema
- Inconsistent error handling across services
- Duplicate code because patterns are unknown
- New developers spend days understanding the system

### Solution With Copilot Spaces
- All developers see the same architecture overview
- Shared error handling patterns are documented
- Payment Service developers understand User Service contracts
- New developers are productive on day one

### Space Contents
```
Space: E-Commerce Platform
├── Architecture Overview
│   ├── Service Dependencies Diagram
│   └── API Contract Documentation
├── Shared Standards
│   ├── Error Response Format
│   ├── Authentication Flow
│   └── Logging Standards
├── Decision Records
│   ├── Why we chose async messaging
│   └── JWT vs OAuth2 decision
└── Common Questions
    ├── How do services communicate?
    ├── Where is user data stored?
    └── What's the payment retry strategy?
```

---

## Best Practices for Copilot Spaces

### 1. Keep Documentation Current
- Update architecture docs when services change
- Archive outdated decisions
- Review and refresh quarterly
- Link from code to relevant documentation

### 2. Make Documentation Discoverable
```
Well-organized hierarchy:
- Start with overview (5 min read)
- Link to detailed guides
- Cross-reference related topics
- Include search-friendly keywords
```

### 3. Capture Institutional Knowledge
- Document why decisions were made, not just what
- Include trade-offs and alternatives considered
- Record common gotchas and solutions
- Document known limitations and workarounds

### 4. Combine With Other Context Tools
- Use @workspace participant to access Space context
- Reference specific files with #file tags
- Create custom instructions that reference the Space
- Link Spaces to workflow automation

### 5. Manage Context Quality
- Regularly audit Space contents for accuracy
- Remove conflicting or duplicate information
- Test that AI gets correct answers from Space context
- Update when team processes or standards change

---

## Applying Copilot Spaces in This Workshop

Copilot Spaces demonstrate core **context engineering** principles:

1. **Structural Context**
   - How you organize information matters
   - Clear hierarchies guide AI attention
   - Centralized context prevents fragmentation

2. **Preventing Context Rot**
   - Persistent context remains accurate
   - Team alignment prevents drift
   - Documented decisions preserve rationale

3. **Scalable Context**
   - Context scales with team size
   - New members inherit institutional knowledge
   - Context persists across conversations

4. **Multi-Source Integration**
   - Combine Spaces with chat variables (#)
   - Integrate with custom instructions
   - Use with MCP servers for dynamic data

---

## Common Pitfalls to Avoid

### ❌ Don't: Create Static Spaces
**Problem:** Information becomes outdated and misleading
**Solution:** Establish a review schedule (monthly/quarterly)

### ❌ Don't: Over-Document
**Problem:** Too much information overwhelms AI and humans
**Solution:** Prioritize critical information; link to details

### ❌ Don't: Ignore Consistency
**Problem:** Conflicting information pollutes AI responses
**Solution:** Treat Space as source of truth; audit regularly

### ❌ Don't: Isolate From Other Tools
**Problem:** Spaces work in isolation rather than together
**Solution:** Integrate with @workspace, #file, custom instructions

---

## Summary

Copilot Spaces are essential for **context engineering** at scale:

✅ **Centralize** project knowledge in one place
✅ **Align** teams through shared context
✅ **Scale** context as your organization grows
✅ **Persist** institutional knowledge across conversations
✅ **Integrate** with other Copilot context tools

### Key Takeaways

For organizations with microservices architectures:
- Create a Space early, even with incomplete information
- Treat it as a living document, not a static artifact
- Connect it to your other context engineering practices
- Measure impact through team alignment and productivity

### Next Steps

1. Evaluate your current documentation organization
2. Identify critical information scattered across repos
3. Create a pilot Copilot Space for your team
4. Gather feedback and iterate
5. Expand to organization-wide knowledge hub
