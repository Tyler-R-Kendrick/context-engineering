---
theme: default
background: https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Context Engineering for GitHub Copilot
  
  Learn how to effectively engineer context to get the most out of GitHub Copilot.
  
  Focus on prompt engineering patterns and tools for better AI assistance.
drawings:
  persist: false
transition: slide-left
title: Context Engineering for GitHub Copilot
mdc: true
---

# Context Engineering for GitHub Copilot

Master the art of providing context to AI assistants

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: default
---

# What is Context Engineering?

Context Engineering is the practice of **structuring and organizing information** to help AI assistants understand your needs and provide better results.

<v-clicks>

- 🎯 **Clear Intent**: Express what you want to achieve
- 📚 **Relevant Information**: Provide necessary background and constraints  
- 🔧 **Proper Format**: Structure requests for optimal understanding
- 🔄 **Iterative Refinement**: Improve context based on results

</v-clicks>

<br>
<br>

<v-click>

> "The quality of AI assistance is directly proportional to the quality of context provided."

</v-click>

---
layout: two-cols
---

# Why Context Matters

::right::

<v-clicks>

## Without Good Context
```
"Make this better"
```
- Vague and ambiguous
- Unclear goals
- Poor results

## With Good Context
```
"Refactor this authentication function 
to use async/await pattern, maintain 
backward compatibility, and add error 
handling for network timeouts"
```
- Specific and clear
- Defined constraints
- Better outcomes

</v-clicks>

---

# Prompt Engineering Fundamentals

The foundation of effective context engineering

---

# Pattern 1: Be Specific and Clear

<v-clicks>

❌ **Vague**: "Write a function"

✅ **Specific**: "Write a TypeScript function that validates email addresses using regex, returns a boolean, and includes JSDoc comments"

</v-clicks>

<v-click>

```typescript
/**
 * Validates an email address using regex pattern
 * @param email - The email address to validate
 * @returns True if email is valid, false otherwise
 */
function validateEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}
```

</v-click>

---

# Pattern 2: Provide Examples

Examples help establish patterns and expectations

<v-clicks>

**Prompt with examples:**
```
// Create a similar function for phone validation
// Example: validateEmail returns boolean for email validity
// Pattern: validate{Type} with consistent return types
```

**Result:** More consistent with your codebase patterns

</v-clicks>

---

# Pattern 3: Specify Constraints

Define limitations, requirements, and standards

<v-clicks>

```
Requirements:
- Must work with Node.js 18+
- Use only standard library (no external dependencies)
- Handle edge cases (null, undefined, empty strings)
- Include unit tests
- Follow existing code style conventions
```

</v-clicks>

---

# Pattern 4: Break Down Complex Tasks

Divide large problems into smaller, manageable pieces

<v-clicks>

Instead of: "Build a complete authentication system"

Break down into:
1. "Create user model with email and password fields"
2. "Implement password hashing function using bcrypt"
3. "Create login endpoint that verifies credentials"
4. "Add JWT token generation for authenticated users"
5. "Implement token verification middleware"

</v-clicks>

---

# Pattern 5: Use Role-Based Prompts

Frame your request by setting the AI's role or perspective

<v-clicks>

```
"As a senior security engineer, review this authentication 
code for potential vulnerabilities"

"As a code reviewer focused on performance, suggest 
optimizations for this data processing function"

"As a documentation specialist, write clear API docs 
for this REST endpoint"
```

</v-clicks>

---

# Interactive Exercise 1: Prompt Engineering

Let's practice writing better prompts!

---

# Exercise 1.1: Improve This Prompt

**Bad Prompt:**
```
Make a function for users
```

<v-click>

**Your Task:** Rewrite this to include:
- Specific functionality
- Input/output types
- Constraints or requirements
- Any relevant context

</v-click>

<v-click>

**Possible Answer:**
```
Create a TypeScript function named 'getUserById' that:
- Accepts a numeric user ID as parameter
- Returns a Promise<User | null>
- Queries the database using our existing connection pool
- Handles errors gracefully with try/catch
- Includes JSDoc comments
```

</v-click>

---

# Exercise 1.2: Add Context

**Initial Prompt:**
```
Optimize this loop
```

<v-click>

**Your Task:** Add context about:
- What kind of optimization (speed, memory, readability)?
- What are the constraints?
- What data volume are we dealing with?

</v-click>

<v-click>

**Better Prompt:**
```
Optimize this loop for processing 1 million records:
- Priority: Reduce memory usage (currently causing OOM errors)
- Must maintain existing output format
- Can use Node.js streams or async iterators
- Performance target: <10GB memory usage
```

</v-click>

---

# Tools for Context Engineering

Enhance your workflow with these tools

---

# Tool 1: Code Comments as Context

Strategic comments provide context to Copilot

```typescript
// TODO: Implement caching layer for frequently accessed user data
// Requirements:
// - Use Redis for cache storage
// - 5 minute TTL for cache entries
// - Fall back to database if cache miss
// - Handle Redis connection errors gracefully
async function getUserData(userId: string) {
  // Implementation will go here
}
```

---

# Tool 2: Type Definitions

TypeScript types provide strong context signals

```typescript
interface UserPreferences {
  theme: 'light' | 'dark';
  notifications: {
    email: boolean;
    push: boolean;
    sms: boolean;
  };
  language: string;
}

// Copilot now understands the expected structure
function updatePreferences(userId: string, prefs: UserPreferences) {
  // Better suggestions based on type information
}
```

---

# Tool 3: Test Cases as Specifications

Write tests first to define expected behavior

```typescript
describe('calculateDiscount', () => {
  it('should apply 10% discount for orders over $100', () => {
    expect(calculateDiscount(150)).toBe(135);
  });
  
  it('should apply 20% discount for orders over $500', () => {
    expect(calculateDiscount(600)).toBe(480);
  });
  
  it('should not apply discount for orders under $100', () => {
    expect(calculateDiscount(50)).toBe(50);
  });
});

// Now implement the function - Copilot has full context
```

---

# Tool 4: Documentation Files

Keep context in markdown files for reference

```markdown
# API Design Guidelines

## Authentication
- All endpoints require JWT token in Authorization header
- Tokens expire after 24 hours
- Use refresh tokens for extended sessions

## Error Handling
- Return standardized error objects
- Include error codes and user-friendly messages
- Log errors with correlation IDs

## Response Format
- Always return JSON
- Use camelCase for field names
- Include metadata (timestamp, version)
```

---

# Tool 5: .promptyignore and Context Files

Create context configuration files

`.copilot-context.md`:
```markdown
# Project Context

## Tech Stack
- Node.js 20.x
- TypeScript 5.x
- Express.js for API
- PostgreSQL database

## Coding Standards
- Use async/await (no callbacks)
- Error handling with try/catch
- Always validate input
- Write tests for new features
```

---

# Interactive Exercise 2: Using Tools

Practice using context engineering tools

---

# Exercise 2.1: Type-Driven Development

**Task:** Create types first, then implement

```typescript
// Define these types to provide context:
type TaskStatus = // TODO: What statuses should a task have?
type Priority = // TODO: What priority levels?

interface Task {
  // TODO: What properties does a task need?
}

// Now implement:
function createTask(data: Partial<Task>): Task {
  // Copilot will suggest based on types
}
```

---

# Exercise 2.2: Test-First Context

**Task:** Write tests, then implement

```typescript
describe('formatCurrency', () => {
  // TODO: Write test cases that define the behavior:
  // - Handle positive numbers
  // - Handle negative numbers  
  // - Handle different currencies (USD, EUR, JPY)
  // - Handle decimal places
});

// Then implement formatCurrency with full context
```

---

# Advanced Patterns

Taking context engineering to the next level

---

# Pattern: Contextual Chaining

Build context progressively through related prompts

<v-clicks>

1. "Create a User model with id, email, and name"
2. "Add validation methods to the User model"
3. "Create a UserRepository class with CRUD operations"
4. "Add transaction support to UserRepository"

Each step builds on previous context!

</v-clicks>

---

# Pattern: Reference Examples

Point to existing code as reference

```typescript
// Similar to how we handle ProductRepository.findById()
// Follow the same error handling pattern
// Use the same database connection approach
async function findUserById(id: string): Promise<User | null> {
  // Implementation
}
```

---

# Pattern: Negative Constraints

Specify what NOT to do

```typescript
// Requirements:
// - DO NOT use var, only const/let
// - DO NOT use any type
// - DO NOT add new dependencies
// - DO NOT modify the existing API contract
function refactorLegacyCode() {
  // Implementation
}
```

---

# Pattern: Progressive Enhancement

Start simple, then add complexity

<v-clicks>

1. "Create basic user authentication"
2. "Add password reset functionality"  
3. "Add two-factor authentication"
4. "Add OAuth provider support"
5. "Add rate limiting for security"

</v-clicks>

---

# Workshop: Real-World Scenarios

Apply what you've learned!

---

# Workshop Scenario 1: API Endpoint

**Challenge:** Create a RESTful API endpoint

**Context to provide:**
- HTTP method and route
- Request/response schemas
- Validation requirements
- Error handling needs
- Authentication/authorization
- Database operations

**Time:** 10 minutes

---

# Workshop Scenario 2: Data Processing

**Challenge:** Process and transform large datasets

**Context to provide:**
- Input data format
- Output requirements
- Performance constraints
- Memory limitations
- Error handling strategy

**Time:** 10 minutes

---

# Workshop Scenario 3: Refactoring

**Challenge:** Refactor legacy code

**Context to provide:**
- Current issues/problems
- Desired improvements
- Constraints (backward compatibility)
- Testing requirements
- Code style guidelines

**Time:** 10 minutes

---

# Best Practices Summary

Key takeaways for effective context engineering

<v-clicks>

✅ **Be Specific**: Clarity beats brevity
✅ **Provide Examples**: Show patterns you want
✅ **Define Constraints**: Set clear boundaries
✅ **Use Types**: Let the type system help
✅ **Write Tests First**: Define behavior upfront
✅ **Iterate**: Refine context based on results
✅ **Document**: Keep context accessible
✅ **Break Down**: Smaller tasks, better results

</v-clicks>

---

# Common Anti-Patterns

What NOT to do

<v-clicks>

❌ Too vague: "Make it better"
❌ Too complex: Trying to do everything at once
❌ No context: Expecting Copilot to read your mind
❌ Wrong scope: Asking for entire applications
❌ Ignoring results: Not iterating based on output
❌ No validation: Accepting suggestions blindly

</v-clicks>

---

# Resources and Next Steps

Continue your learning journey

<v-clicks>

📚 **Further Reading:**
- GitHub Copilot Documentation
- Prompt Engineering Guide
- Context Engineering Patterns

🛠️ **Practice Tools:**
- Polyglot Notebooks (included in /notebooks)
- Prompty Files (included in /prompty)
- Workshop Exercises (included in /workshops)

🎯 **Next Steps:**
- Complete all workshop exercises
- Experiment with different patterns
- Share your learnings with the team

</v-clicks>

---
layout: center
class: text-center
---

# Thank You!

Questions and Discussion

[GitHub Repository](https://github.com/Tyler-R-Kendrick/context-engineering)

<div class="pt-12">
  <span class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Happy Context Engineering! 🚀
  </span>
</div>
