---
theme: default
highlighter: shiki
lineNumbers: true
transition: slide-left
---

# Tools for Context Engineering

Enhance your workflow with these tools

---

# Tool 1: Code Comments as Context

Strategic comments provide context to Copilot

```typescript
// Implement caching layer for frequently accessed user data
// Requirements:
// - Use Redis for cache storage
// - 5 minute TTL for cache entries
// - Fall back to database if cache miss
// - Handle Redis connection errors gracefully
async function getUserData(userId: string): Promise<User> {
  const cacheKey = `user:${userId}`;
  
  try {
    // Try to get from cache first
    const cached = await redis.get(cacheKey);
    if (cached) {
      return JSON.parse(cached);
    }
  } catch (error) {
    console.error('Redis error:', error);
    // Fall through to database
  }
  
  // Cache miss or error - fetch from database
  const user = await database.users.findById(userId);
  
  // Store in cache with TTL
  try {
    await redis.setex(cacheKey, 300, JSON.stringify(user));
  } catch (error) {
    console.error('Failed to cache user:', error);
  }
  
  return user;
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
type TaskStatus = 'todo' | 'in_progress' | 'in_review' | 'completed' | 'blocked';
type Priority = 'low' | 'medium' | 'high' | 'urgent';

interface Task {
  id: string;
  title: string;
  description: string;
  status: TaskStatus;
  priority: Priority;
  assignee?: string;
  dueDate?: Date;
  tags: string[];
  createdAt: Date;
  updatedAt: Date;
}

// Now implement with full type context:
function createTask(data: Partial<Task>): Task {
  return {
    id: crypto.randomUUID(),
    title: data.title || 'Untitled Task',
    description: data.description || '',
    status: data.status || 'todo',
    priority: data.priority || 'medium',
    assignee: data.assignee,
    dueDate: data.dueDate,
    tags: data.tags || [],
    createdAt: new Date(),
    updatedAt: new Date(),
  };
}
```

---

# Exercise 2.2: Test-First Context

**Task:** Write tests, then implement

```typescript
describe('formatCurrency', () => {
  it('should format positive numbers with USD', () => {
    expect(formatCurrency(1234.56, 'USD')).toBe('$1,234.56');
  });
  
  it('should format negative numbers with USD', () => {
    expect(formatCurrency(-1234.56, 'USD')).toBe('-$1,234.56');
  });
  
  it('should handle EUR currency', () => {
    expect(formatCurrency(1234.56, 'EUR')).toBe('€1,234.56');
  });
  
  it('should handle JPY without decimals', () => {
    expect(formatCurrency(1234, 'JPY')).toBe('¥1,234');
  });
  
  it('should handle custom decimal places', () => {
    expect(formatCurrency(1234.5678, 'USD', 3)).toBe('$1,234.568');
  });
});

// Implementation based on test specifications:
function formatCurrency(
  amount: number, 
  currency: string, 
  decimals?: number
): string {
  const symbols = { USD: '$', EUR: '€', JPY: '¥' };
  const defaultDecimals = currency === 'JPY' ? 0 : 2;
  const precision = decimals ?? defaultDecimals;
  
  const formatted = Math.abs(amount).toLocaleString('en-US', {
    minimumFractionDigits: precision,
    maximumFractionDigits: precision
  });
  
  const symbol = symbols[currency] || currency;
  return amount < 0 ? `-${symbol}${formatted}` : `${symbol}${formatted}`;
}
```