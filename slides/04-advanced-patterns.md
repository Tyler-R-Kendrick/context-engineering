---
theme: default
highlighter: shiki
lineNumbers: true
transition: slide-left
---

# Advanced Patterns

Taking context engineering to the next level

---

# External Slides: Advanced Techniques

<v-clicks>

**Deep Dive References:**

| Technique | External Slide |
|-----------|----------------|
| Reasoning Techniques | [CoT, ToT, Self-Consistency](prompt-engineering/04.2_Prompt_Engineering_Techniques.Reasoning_Techniques.md) |
| Parameter Tuning | [Temperature, Top-p, Sampling](prompt-engineering/04.4_Prompt_Engineering_Techniques.Parameter_Tuning.md) |
| Constrained Decoding | [Output Formatting & Control](prompt-engineering/04.5_Prompt_Engineering_Techniques.Constrained_Decoding.md) |
| RAG Integration | [Retrieval-Augmented Generation](prompt-engineering/04.3_Prompt_Engineering_Techniques.RAG.md) |

</v-clicks>

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