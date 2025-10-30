# Workshop Exercise 4: Tools and Context Engineering

## Objective
Learn to use various tools and techniques to enhance context for better code generation and AI assistance.

## Duration
30 minutes

## Instructions

Explore different tools and patterns that provide context to GitHub Copilot.

---

## Part 1: Type System as Context

### Exercise 4.1: Type Definitions

**Scenario:** Create a task management system with strong typing.

```typescript
// Step 1: Define types to establish context
// TODO: Create type definitions for:
// - TaskStatus (enum or union type)
// - TaskPriority (enum or union type)
// - Task interface
// - TaskFilter interface

// Your types here:




// Step 2: Implement functions - Copilot will use type context
// TODO: Implement createTask, filterTasks, updateTaskStatus
```

**Example Answer:**
```typescript
// Step 1: Define comprehensive types
type TaskStatus = 'todo' | 'in_progress' | 'blocked' | 'completed';
type TaskPriority = 'low' | 'medium' | 'high' | 'urgent';

interface Task {
  id: string;
  title: string;
  description: string;
  status: TaskStatus;
  priority: TaskPriority;
  assignee?: string;
  createdAt: Date;
  updatedAt: Date;
  dueDate?: Date;
  tags: string[];
}

interface TaskFilter {
  status?: TaskStatus[];
  priority?: TaskPriority[];
  assignee?: string;
  tags?: string[];
  dueBefore?: Date;
}

// Step 2: Implementation - guided by types
function createTask(
  title: string,
  description: string,
  priority: TaskPriority = 'medium'
): Task {
  return {
    id: crypto.randomUUID(),
    title,
    description,
    status: 'todo',
    priority,
    createdAt: new Date(),
    updatedAt: new Date(),
    tags: []
  };
}

function filterTasks(tasks: Task[], filter: TaskFilter): Task[] {
  return tasks.filter(task => {
    if (filter.status && !filter.status.includes(task.status)) {
      return false;
    }
    if (filter.priority && !filter.priority.includes(task.priority)) {
      return false;
    }
    if (filter.assignee && task.assignee !== filter.assignee) {
      return false;
    }
    if (filter.tags && !filter.tags.some(tag => task.tags.includes(tag))) {
      return false;
    }
    if (filter.dueBefore && task.dueDate && task.dueDate > filter.dueBefore) {
      return false;
    }
    return true;
  });
}
```

---

## Part 2: Documentation as Context

### Exercise 4.2: API Documentation

**Scenario:** Document an API to provide context for implementation.

```markdown
<!-- Create API documentation first -->
<!-- TODO: Document the following: -->
<!-- - Endpoint path and method -->
<!-- - Request/response schemas -->
<!-- - Authentication requirements -->
<!-- - Error responses -->
<!-- - Example requests/responses -->

## API Documentation

### [Your API Name]

[Write documentation here]
```

**Example Answer:**
```markdown
## API Documentation

### Create User

Creates a new user account.

**Endpoint:** `POST /api/v1/users`

**Authentication:** Required (API Key in header)

**Headers:**
```
Authorization: Bearer {api_key}
Content-Type: application/json
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "role": "user",
  "preferences": {
    "notifications": true,
    "theme": "dark"
  }
}
```

**Validation Rules:**
- `email`: Required, valid email format, unique
- `name`: Required, 2-100 characters
- `role`: Optional, defaults to "user", must be "user" or "admin"
- `preferences`: Optional object

**Success Response (201):**
```json
{
  "success": true,
  "data": {
    "id": "usr_123abc",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "user",
    "createdAt": "2024-01-15T10:30:00Z"
  }
}
```

**Error Responses:**

400 Bad Request:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "fields": ["email"]
  }
}
```

409 Conflict:
```json
{
  "success": false,
  "error": {
    "code": "EMAIL_EXISTS",
    "message": "Email already registered"
  }
}
```

**Rate Limits:** 100 requests per minute per API key

**Example cURL:**
```bash
curl -X POST https://api.example.com/api/v1/users \
  -H "Authorization: Bearer your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","name":"John Doe"}'
```

---

## Part 3: Pattern Files

### Exercise 4.3: Create a Context File

**Scenario:** Create a project context file that Copilot can reference.

```markdown
<!-- Create .copilot-context.md or similar -->
<!-- TODO: Document: -->
<!-- - Tech stack -->
<!-- - Coding standards -->
<!-- - Common patterns -->
<!-- - Dependencies -->
<!-- - Architecture decisions -->

# Project Context

[Write your context file here]
```

**Example Answer:**
```markdown
# Project Context

## Tech Stack
- **Runtime:** Node.js 20.x LTS
- **Language:** TypeScript 5.x (strict mode enabled)
- **Framework:** Express.js 4.x
- **Database:** PostgreSQL 15
- **ORM:** Prisma 5.x
- **Testing:** Jest + Supertest
- **API:** RESTful with OpenAPI 3.0 specs

## Architecture Patterns

### Layered Architecture
```
Controller -> Service -> Repository -> Database
```
- Controllers handle HTTP, no business logic
- Services contain business logic
- Repositories handle data access
- Always use dependency injection

### Error Handling
```typescript
// Use custom error classes
throw new ValidationError('Invalid input', { field: 'email' });

// Catch and transform in middleware
app.use(errorHandler);
```

## Coding Standards

### TypeScript
- Always use strict mode
- Explicit return types on functions
- No `any` type (use `unknown` if needed)
- Interface for objects, type for unions/primitives
- Use optional chaining and nullish coalescing

### Async/Await
- Never use callbacks
- Always use try/catch with async
- Return promises from async functions
- Use Promise.all for parallel operations

### Naming Conventions
- camelCase for variables and functions
- PascalCase for classes and interfaces
- UPPER_SNAKE_CASE for constants
- Prefix interfaces with 'I' only for generic types

### Comments
- Use JSDoc for public APIs
- Explain WHY, not WHAT
- Update comments when code changes

## Database Patterns

### Queries
- Use Prisma client, never raw SQL
- Always use transactions for multi-step operations
- Include error handling for unique constraints
- Use proper indexes (defined in schema)

### Migrations
- Named descriptively: `YYYYMMDD_add_user_email_index`
- Never modify existing migrations
- Always test rollback

## Testing Requirements

### Unit Tests
- Minimum 80% coverage
- Test file naming: `*.test.ts`
- Mock external dependencies
- Use factories for test data

### Integration Tests
- Test API endpoints end-to-end
- Use test database (automatic cleanup)
- Include authentication tests

## Security Requirements

### Authentication
- JWT tokens with 24-hour expiration
- Refresh tokens stored in httpOnly cookies
- Password hashing with bcrypt (12 rounds)
- Rate limiting on auth endpoints

### Input Validation
- Validate all user input
- Use Joi schemas for complex validation
- Sanitize HTML content
- Parameterized queries only

## Common Utilities

### Error Response Format
```typescript
{
  success: false,
  error: {
    code: 'ERROR_CODE',
    message: 'User-friendly message',
    details?: object
  }
}
```

### Success Response Format
```typescript
{
  success: true,
  data: any,
  meta?: {
    page: number,
    total: number
  }
}
```

## Dependencies

### Avoid Adding
- Lodash (use native JS instead)
- Moment.js (use date-fns or native)
- Request (deprecated, use native fetch)

### Preferred
- date-fns for date manipulation
- zod for runtime validation
- winston for logging
```

---

## Part 4: Configuration Files

### Exercise 4.4: ESLint and Prettier

**Task:** Configure linting rules that establish coding standards.

```json
// .eslintrc.json
// TODO: Configure rules that enforce:
// - No console.log in production
// - Prefer const over let
// - Async/await over promises
// - Explicit return types
// - No unused variables

{
  "rules": {
    // Your rules here
  }
}
```

**Example Answer:**
```json
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-requiring-type-checking",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "project": "./tsconfig.json"
  },
  "rules": {
    "no-console": ["error", { "allow": ["warn", "error"] }],
    "prefer-const": "error",
    "prefer-promise-reject-errors": "error",
    "require-await": "error",
    "@typescript-eslint/explicit-function-return-type": "error",
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/no-unused-vars": ["error", {
      "argsIgnorePattern": "^_"
    }],
    "@typescript-eslint/explicit-module-boundary-types": "error",
    "@typescript-eslint/no-floating-promises": "error",
    "no-return-await": "off",
    "@typescript-eslint/return-await": "error"
  }
}
```

---

## Part 5: Practical Application

### Exercise 4.5: Combine All Tools

**Challenge:** Create a complete feature using all context tools.

**Feature:** User profile management endpoint

**Steps:**

1. **Create types** (TypeScript interfaces)
2. **Write API documentation**
3. **Add context comments**
4. **Write tests first**
5. **Configure validation rules**
6. **Implement with Copilot's help**

**Your Work:**

```typescript
// Step 1: Types
// [Your types here]


// Step 2: API docs in comments
/**
 * [Your API documentation]
 */


// Step 3: Tests
// [Your tests here]


// Step 4: Implementation
// [Your implementation here]
```

---

## Reflection

### What Worked Well?

1. ___________________________________________________________

2. ___________________________________________________________

3. ___________________________________________________________

### What Could Be Improved?

1. ___________________________________________________________

2. ___________________________________________________________

### Most Valuable Tool/Technique?

___________________________________________________________

---

## Key Takeaways

1. ___________________________________________________________

2. ___________________________________________________________

3. ___________________________________________________________

4. ___________________________________________________________

## Next Steps

- Create context files for your project
- Establish team coding standards
- Document common patterns
- Share tools with your team
- Continue practicing!
