---
theme: default
layout: intro
highlighter: shiki
lineNumbers: true
transition: slide-left
---

## Categories of Context

Five types of context that influence AI behavior

<v-switch>

<template v-slot:1>

### 1. Instructional Context
Directives, goals, constraints, and acceptance criteria
```yaml
goal: Implement user authentication with JWT
constraints:
  - Must support refresh tokens
  - 15min expiry
acceptance:
  - Pass all security tests
  - Handle edge cases
```

<!--
Start with the most direct form of context - explicit instructions. Instructions should emphasize  clear goals and constraints that help AI systems understand exactly what you want.
-->

</template>

<template v-slot:2>

### 2. Environmental Context
Active code, related modules, tests, and documentation
```yaml
related:
  - UserRepository.ts
  - AuthService.ts
tests:
  - file: auth.test.ts
    lines: 45-67
docs:
  - docs/authentication.md
```

<!-- 
Environmental context provides the surrounding landscape. Related files, test references, and documentation helps AI systems understand the codebase patterns and existing implementations. This context prevents hallucinations and ensures consistency.
-->

</template>

<template v-slot:3>

### 3. Memory Context
Condensed history from previous interactions
```yaml
previousSession:
  - Discussed JWT structure
  - Decided on RS256
userPreference:
  - Functional style
  - Comprehensive error handling
```

<!-- 
Memory context builds continuity across conversations. Storing the historical context of an ongoing interaction helps to steer generations towards a more correct trajectory with real-time learning strategies.
-->

</template>

<template v-slot:4>

### 4. Retrieved Context
Dynamically fetched references or embeddings from external knowledge (RAG)
```yaml
retrievedFromCodebase:
  - similarPattern: auth pattern in AdminAuth.ts
retrievedFromDatabase:
  - relatedNodes: graph nodes associated with a user identity.
retrievedFromDocs:
  - guide: OAuth2 integration guide
```

<!-- 
Retrieved context represents dynamic, on-demand information pulled from search engines, vector databases, or other knowledge stores. This scales context beyond what you manually provide and enables AI to find and apply similar patterns from the broader scope of knoweledge relevant for your domain.
-->

</template>

<template v-slot:5>

### 5. Structural Context
Layout, ordering, and repetition patterns that shape model attention
```yaml
keyRequirement:
  description: Must validate email format
  priority: repeated
critical:
  description: Handle network timeouts gracefully
reminder:
  description: Use existing error codes from ErrorCodes.ts
```

<!--
Structural context uses formatting, ordering, and repetition to guide model attention.
HOW you present information matters as much as WHAT you present.
Repeated items, keywords in caps, and logical ordering all influence which details the model prioritizes in its reasoning.
-->

</template>

</v-switch>

<!--
Each of these categories can be optimized through modification of the RAW context. To better understand the value proposition of **context** engineering over **prompt** engineering, we'll first show explain where context gets included for github copilot.

Instructional context provides clear goals, constraints, and acceptance criteria for assisted task completion. Constraints could be positive examples - or negative examples. These instruction sets provide the initial frame that guides reasoning trajectories for the rest of the context.

Environmental context uses related files and content out of the initial scope of the prompt being sent by the user. In copilot, this could mean your entire codebase.

If memory is integrated into your system, you can pull summarized chat history to maintain reasoning trajectories that you previously cultivated. This allows for real-time in-context learning when you use history to guide reasoning trajectories.

Context can be retrieved from external sources with RAG patterns to pull in relevant context outside of your codebase. 

Structural context is an increasing area of study. Because of issues inherent to long context llms (like context rot and lost-in-the-middle problems), we are learning techniques to focus attention on content we don't want the llm to "forget".
-->
