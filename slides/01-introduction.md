---
theme: default
highlighter: shiki
lineNumbers: true
transition: slide-left
---

# Why Context Matters

<div class="grid grid-cols-2 gap-4">

<div>

## Without Good Context
```
"Make this better"
```
- Vague and ambiguous
- Unclear goals
- Poor results

</div>

<div>

<v-clicks>

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

</div>

</div>

---

# Context Engineering Fundamentals

The foundation of effective context engineering

---

# Categories of Context

Five types of context that influence AI behavior

<v-clicks>

### 1. Instructional Context
Directives, goals, constraints, and acceptance criteria
```typescript
// GOAL: Implement user authentication with JWT
// CONSTRAINTS: Must support refresh tokens, 15min expiry
// ACCEPTANCE: Pass all security tests, handle edge cases
```

### 2. Environmental Context
Active code, related modules, tests, and documentation
```typescript
// Related: UserRepository.ts, AuthService.ts
// Tests: auth.test.ts (see line 45-67)
// Docs: docs/authentication.md
```

</v-clicks>

---

# Categories of Context (continued)

<v-clicks>

### 3. Memory Context
Condensed history from previous interactions
```typescript
// Previous session: Discussed JWT structure, decided on RS256
// User preference: Functional style, comprehensive error handling
```

### 4. Retrieved Context
Dynamically fetched references or embeddings from search/vector stores
```typescript
// Retrieved from codebase: Similar auth pattern in AdminAuth.ts
// Retrieved from docs: OAuth2 integration guide
```

### 5. Structural Context
Layout, ordering, and repetition patterns that shape model attention
```typescript
// KEY REQUIREMENT (repeated): Must validate email format
// CRITICAL: Handle network timeouts gracefully
// REMINDER: Use existing error codes from ErrorCodes.ts
```

</v-clicks>