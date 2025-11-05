---
theme: default
highlighter: shiki
lineNumbers: true
transition: slide-left
---

# Prompt Engineering Fundamentals

The foundation of effective context engineering

---

---
src: ./prompt-engineering/01_Introduction_to_Prompt_Engineering.md
---

---
src: ./prompt-engineering/02_Types_of_Prompts.md
---

---
src: ./prompt-engineering/03_Anatomy_of_an_Effective_Prompt.md
---

---
src: ./prompt-engineering/04_Prompt_Engineering_Techniques.md
---

---
src: ./prompt-engineering/04.1_Prompt_Engineering_Techniques.Basic_Techniques.md
---

---
src: ./prompt-engineering/04.2_Prompt_Engineering_Techniques.Reasoning_Techniques.md
---

---
src: ./prompt-engineering/04.3_Prompt_Engineering_Techniques.RAG.md
---

---
src: ./prompt-engineering/04.4_Prompt_Engineering_Techniques.Parameter_Tuning.md
---

---
src: ./prompt-engineering/04.5_Prompt_Engineering_Techniques.Constrained_Decoding.md
---

---
src: ./prompt-engineering/05_Practical_Use_Cases_and_Examples.md
---

---
src: ./prompt-engineering/06_Best_Practices_for_Effective_Prompts.md
---

---
src: ./prompt-engineering/07_Testing_and_Evaluation_Strategies.md
---

---
src: ./prompt-engineering/08_Safety_Ethics_and_Fallback_Responses.md
---

---
src: ./prompt-engineering/09_Resources_for_Further_Learning.md
---

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

# Quick Reference: Key Patterns

These patterns are expanded in the external slides above

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