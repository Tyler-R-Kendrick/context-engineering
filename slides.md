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

# Advanced Context Engineering

Beyond prompt engineering fundamentals

---

# Context Optimization Strategies

<v-clicks>

Moving beyond basic prompts to **systematic context management**:

1. 🎯 **Token Optimization**: Reduce costs and improve response quality
2. 📊 **Knowledge Modeling**: Structure information for better retrieval
3. 🔧 **Tool Integration**: Extend AI capabilities with external functions
4. 🔄 **Context Reduction**: Maintain relevant information across long conversations

</v-clicks>

<v-click>

> "Effective context engineering isn't just about what you say—it's about managing what the AI remembers and accesses."

</v-click>

---

# Token Optimization: Chat Reducers

Manage conversation context to stay within token limits

<v-clicks>

### The Problem
- LLMs have token limits (4K, 8K, 128K tokens)
- Long conversations exceed limits
- Costs scale with tokens used

### Solution: Context Reduction Strategies

1. **Sliding Window**: Keep only recent N messages
2. **Summarization**: Compress old context into summaries
3. **Selective Retention**: Keep important messages, discard routine ones
4. **Role-Based Filtering**: Retain system/assistant messages, compress user messages

</v-clicks>

---

# Implementing Chat Reducers

```typescript
interface Message {
  role: 'system' | 'user' | 'assistant';
  content: string;
  tokens: number;
  important?: boolean;
}

class ChatReducer {
  constructor(private maxTokens: number = 4000) {}
  
  reduce(messages: Message[]): Message[] {
    let totalTokens = messages.reduce((sum, m) => sum + m.tokens, 0);
    
    if (totalTokens <= this.maxTokens) {
      return messages;
    }
    
    // Strategy 1: Keep system message and recent messages
    const system = messages.filter(m => m.role === 'system');
    const important = messages.filter(m => m.important);
    const recent = messages.slice(-10);
    
    // Strategy 2: Summarize middle messages
    const middle = messages.slice(1, -10);
    const summary = this.summarize(middle);
    
    return [
      ...system,
      summary,
      ...important.filter(m => !recent.includes(m)),
      ...recent
    ];
  }
  
  private summarize(messages: Message[]): Message {
    // Call LLM to create concise summary
    return {
      role: 'system',
      content: 'Summary of previous conversation: [key points]',
      tokens: 100
    };
  }
}
```

---

# Token-Efficient Summarization Patterns

<v-clicks>

### Progressive Summarization
```
Original (1000 tokens) → Summary (250 tokens) → 
Key Points (50 tokens) → Single Sentence (10 tokens)
```

### Hierarchical Compression
```typescript
// Level 1: Full detail (recent messages)
"User asked about authentication. Explained JWT tokens, 
 refresh tokens, and security best practices. User 
 implemented solution successfully."

// Level 2: Key facts (medium history)
"Discussed: JWT auth implementation, security best practices"

// Level 3: Minimal context (old history)
"Auth: JWT"
```

### Selective Detail Retention
- **Code blocks**: Keep in full
- **Definitions**: Compress to key terms
- **Examples**: Keep one, reference others
- **Explanations**: Extract key points only

</v-clicks>

---

# Knowledge Modeling for RAG

Retrieval-Augmented Generation beyond vector search

---

# RAG Architecture Patterns

<v-clicks>

### Traditional RAG (Vector Similarity)
```
Query → Embed → Search Vectors → Retrieve → Context + Query → LLM
```
**Limitation**: Semantic similarity doesn't always mean relevance

### Advanced RAG Strategies

1. **Graph-Based RAG**: Model relationships between entities
2. **Hybrid Search**: Combine keyword, semantic, and graph
3. **Structured Content**: Use metadata and schemas
4. **Multi-Stage Retrieval**: Filter → Rank → Rerank

</v-clicks>

---

# Graph-Based Knowledge Modeling

```typescript
interface KnowledgeNode {
  id: string;
  type: 'concept' | 'document' | 'entity' | 'code';
  content: string;
  metadata: Record<string, any>;
}

interface KnowledgeEdge {
  from: string;
  to: string;
  type: 'references' | 'implements' | 'depends_on' | 'related_to';
  weight: number;
}

class KnowledgeGraph {
  private nodes: Map<string, KnowledgeNode> = new Map();
  private edges: KnowledgeEdge[] = [];
  
  // Find related content by traversing relationships
  findRelated(nodeId: string, depth: number = 2): KnowledgeNode[] {
    const visited = new Set<string>();
    const result: KnowledgeNode[] = [];
    
    const traverse = (id: string, currentDepth: number) => {
      if (currentDepth > depth || visited.has(id)) return;
      visited.add(id);
      
      const node = this.nodes.get(id);
      if (node) result.push(node);
      
      // Follow edges to connected nodes
      this.edges
        .filter(e => e.from === id || e.to === id)
        .forEach(e => {
          const nextId = e.from === id ? e.to : e.from;
          traverse(nextId, currentDepth + 1);
        });
    };
    
    traverse(nodeId, 0);
    return result;
  }
}
```

---

# Hybrid RAG Implementation

```typescript
interface SearchResult {
  content: string;
  score: number;
  source: 'vector' | 'keyword' | 'graph';
}

class HybridRAG {
  async search(query: string): Promise<string[]> {
    // 1. Vector similarity search
    const vectorResults = await this.vectorSearch(query);
    
    // 2. Keyword/BM25 search
    const keywordResults = await this.keywordSearch(query);
    
    // 3. Graph traversal from query entities
    const entities = await this.extractEntities(query);
    const graphResults = await this.graphSearch(entities);
    
    // 4. Fusion: Combine and re-rank results
    const combined = this.fuseResults([
      ...vectorResults,
      ...keywordResults,
      ...graphResults
    ]);
    
    // 5. Rerank based on query intent
    const reranked = await this.rerank(query, combined);
    
    // 6. Select top-k with diversity
    return this.diversitySelect(reranked, 5);
  }
  
  private fuseResults(results: SearchResult[]): SearchResult[] {
    // Reciprocal Rank Fusion (RRF)
    const scores = new Map<string, number>();
    
    results.forEach((result, rank) => {
      const current = scores.get(result.content) || 0;
      scores.set(result.content, current + 1 / (rank + 60));
    });
    
    return Array.from(scores.entries())
      .sort((a, b) => b[1] - a[1])
      .map(([content, score]) => ({
        content,
        score,
        source: 'hybrid'
      }));
  }
}
```

---

# Structured Content Aggregation

Beyond embeddings: Use document structure

```typescript
interface DocumentChunk {
  content: string;
  metadata: {
    source: string;
    section: string;
    headings: string[];  // Hierarchical context
    codeLanguage?: string;
    timestamp?: Date;
    author?: string;
  };
}

class StructuredRetrieval {
  // Retrieve with structural context
  async retrieveWithContext(
    query: string, 
    filters: {
      sections?: string[];
      codeLanguage?: string;
      dateRange?: [Date, Date];
    }
  ): Promise<string> {
    const chunks = await this.search(query, filters);
    
    // Group by document and section
    const grouped = this.groupByStructure(chunks);
    
    // Build hierarchical context
    return this.buildContext(grouped);
  }
  
  private buildContext(grouped: Map<string, DocumentChunk[]>): string {
    let context = '';
    
    for (const [source, chunks] of grouped) {
      context += `\n## From: ${source}\n`;
      
      // Include heading hierarchy
      const sections = new Set(chunks.map(c => c.metadata.section));
      sections.forEach(section => {
        context += `\n### ${section}\n`;
        const sectionChunks = chunks.filter(
          c => c.metadata.section === section
        );
        context += sectionChunks.map(c => c.content).join('\n\n');
      });
    }
    
    return context;
  }
}
```

---

# Tool Use for Context Optimization

Extend AI capabilities with external tools

---

# Function Calling for Dynamic Context

```typescript
interface Tool {
  name: string;
  description: string;
  parameters: {
    type: 'object';
    properties: Record<string, {
      type: string;
      description: string;
    }>;
    required: string[];
  };
}

const tools: Tool[] = [
  {
    name: 'search_codebase',
    description: 'Search the codebase for specific patterns or implementations',
    parameters: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'The search query or pattern to find'
        },
        fileTypes: {
          type: 'array',
          description: 'File extensions to search in (e.g., [".ts", ".js"])'
        }
      },
      required: ['query']
    }
  },
  {
    name: 'get_api_docs',
    description: 'Retrieve documentation for a specific API or library',
    parameters: {
      type: 'object',
      properties: {
        libraryName: {
          type: 'string',
          description: 'Name of the library (e.g., "express", "react")'
        },
        method: {
          type: 'string',
          description: 'Specific method or function to document'
        }
      },
      required: ['libraryName']
    }
  },
  {
    name: 'execute_code',
    description: 'Run code snippets and return results for validation',
    parameters: {
      type: 'object',
      properties: {
        code: {
          type: 'string',
          description: 'Code to execute'
        },
        language: {
          type: 'string',
          description: 'Programming language (python, javascript, etc.)'
        }
      },
      required: ['code', 'language']
    }
  }
];
```

---

# Tool-Augmented Context Pipeline

```typescript
class ToolAugmentedContext {
  async processQuery(query: string): Promise<string> {
    // 1. Analyze query to determine needed tools
    const neededTools = await this.analyzeQueryForTools(query);
    
    // 2. Execute tools in parallel
    const toolResults = await Promise.all(
      neededTools.map(tool => this.executeTool(tool))
    );
    
    // 3. Synthesize tool outputs into context
    const augmentedContext = this.synthesizeContext(
      query,
      toolResults
    );
    
    // 4. Add to conversation with proper formatting
    return this.formatToolContext(augmentedContext);
  }
  
  private formatToolContext(results: ToolResult[]): string {
    let context = '## Available Context from Tools:\n\n';
    
    for (const result of results) {
      context += `### ${result.toolName}\n`;
      context += `${result.summary}\n\n`;
      
      if (result.codeSnippets) {
        context += '```' + result.language + '\n';
        context += result.codeSnippets.slice(0, 3).join('\n\n');
        context += '\n```\n\n';
      }
      
      if (result.references) {
        context += `References: ${result.references.join(', ')}\n\n`;
      }
    }
    
    return context;
  }
}
```

---

# Context Caching Strategies

Reduce redundant token usage

<v-clicks>

### Prompt Caching
```typescript
// Cache static system prompts and context
const cachedSystemPrompt = cache.get('system-prompt-v1') || {
  role: 'system',
  content: 'You are an expert software engineer...',
  cache: true  // Provider-specific caching
};

// Reuse across multiple requests
const responses = await Promise.all(
  queries.map(q => llm.chat([
    cachedSystemPrompt,  // Cached, not re-tokenized
    { role: 'user', content: q }
  ]))
);
```

### Semantic Caching
```typescript
// Cache by semantic similarity, not exact match
const semanticCache = new SemanticCache();

const query = "How do I implement authentication?";
const similar = await semanticCache.find(query, threshold: 0.95);

if (similar) {
  return similar.response;  // Return cached response
} else {
  const response = await llm.chat(query);
  await semanticCache.store(query, response);
  return response;
}
```

</v-clicks>

---

# Context Window Management

Strategic use of available context space

```typescript
interface ContextBudget {
  systemPrompt: number;      // Fixed overhead
  conversationHistory: number; // Sliding window
  retrievedContext: number;   // RAG results
  toolOutputs: number;        // Function results
  responseReserve: number;    // Space for output
}

class ContextWindowManager {
  private maxTokens: number = 8000;
  
  allocate(budget: Partial<ContextBudget>): ContextBudget {
    const defaults = {
      systemPrompt: 500,
      responseReserve: 1500,
    };
    
    const allocated = { ...defaults, ...budget };
    
    // Calculate remaining space
    const used = allocated.systemPrompt + allocated.responseReserve;
    const remaining = this.maxTokens - used;
    
    // Distribute remaining tokens
    const parts = [
      'conversationHistory',
      'retrievedContext', 
      'toolOutputs'
    ].filter(k => !(k in allocated));
    
    const perPart = Math.floor(remaining / parts.length);
    parts.forEach(part => {
      allocated[part] = perPart;
    });
    
    return allocated as ContextBudget;
  }
  
  fit(content: string[], budget: number): string[] {
    let tokens = 0;
    const result: string[] = [];
    
    for (const item of content) {
      const itemTokens = this.estimateTokens(item);
      if (tokens + itemTokens > budget) break;
      result.push(item);
      tokens += itemTokens;
    }
    
    return result;
  }
}
```

---

# Best Practices for Advanced Context Engineering

<v-clicks>

### Token Optimization
- ✅ Use chat reducers for long conversations
- ✅ Implement progressive summarization
- ✅ Cache static content
- ✅ Monitor and optimize token usage

### Knowledge Retrieval
- ✅ Use hybrid search (vector + keyword + graph)
- ✅ Preserve document structure
- ✅ Implement multi-stage retrieval and reranking
- ✅ Consider relationships, not just similarity

### Tool Integration
- ✅ Provide clear tool descriptions
- ✅ Use tools to fetch just-in-time context
- ✅ Validate tool outputs before adding to context
- ✅ Format tool results consistently

### Context Management
- ✅ Budget context window strategically
- ✅ Prioritize recent and important information
- ✅ Use structured formats for better parsing
- ✅ Test with real token limits

</v-clicks>

---

# Workshop: Context Engineering Fundamentals

A comprehensive deep-dive into context engineering for GitHub Copilot

---

# Why Context Engineering Exists

Understanding the fundamental problem

<v-clicks>

### The Expectation Gap
- **Copilot's default context is shallow and local**
- Cannot infer architecture, intent, or cross-file logic
- Limited to visible code in the current file

### Common Failure Modes

1. **Context Starvation**: Too little information → vague, incorrect suggestions
2. **Context Overload**: Too much noise → degraded performance, high costs
3. **Context Misalignment**: Wrong data → irrelevant or misleading outputs

</v-clicks>

<v-click>

**Goal**: Engineer context flow to deliver high-signal information in the right order for consistent, accurate generations.

</v-click>

---

# What Is Context Engineering

The discipline of managing AI context systematically

<v-clicks>

### Definition
**Context Engineering** is the discipline of selecting, structuring, and ordering data fed to LLMs for optimal reasoning and output quality.

### Distinction from Prompt Engineering
- **Prompt Engineering**: How you phrase requests (the question)
- **Context Engineering**: What information you provide (the knowledge base)

### Core Principles
1. **Intent Clarity**: Make objectives explicit and unambiguous
2. **Efficient Token Use**: Maximize signal-to-noise ratio
3. **Deliberate Sequencing**: Order matters for attention and recall

</v-clicks>

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

---

# Core Problems Addressed

Context engineering solves critical LLM limitations

---

# Problem 1: Limited Attention Window

<v-clicks>

**Challenge**: Context must be prioritized because attention capacity is finite

- Most models: 4K-128K tokens
- Attention degrades with distance
- Not all tokens are equally important

**Solution**: Strategic prioritization and compression
```typescript
// HIGH PRIORITY: Recent conversation, current file
// MEDIUM PRIORITY: Related files, recent changes
// LOW PRIORITY: Distant history, peripheral docs
```

</v-clicks>

---

# Problem 2: Unreliable Retrieval

<v-clicks>

**Challenge**: Inaccurate or noisy fetches degrade grounding

- Vector search returns semantically similar but contextually wrong results
- Keyword search misses semantic relationships
- No ranking by relevance or recency

**Solution**: Hybrid retrieval with validation
```typescript
const results = await hybridSearch(query, {
  vector: { weight: 0.5, threshold: 0.85 },
  keyword: { weight: 0.3 },
  graph: { weight: 0.2, maxDepth: 2 },
  validate: (result) => isRelevant(result, currentContext)
});
```

</v-clicks>

---

# Problem 3: Sensitivity to Ordering

<v-clicks>

**Challenge**: Token placement affects recall strength

**Research Finding** (Anthropic):
- Information at the beginning: Better initial grounding
- Information in the middle: Often "lost" or forgotten
- Information at the end: Stronger immediate recall

**Solution**: Strategic placement
```typescript
// CRITICAL INFO AT START
const systemContext = "Primary objective: Implement secure auth...";

// SUPPORTING DETAILS IN MIDDLE
const references = loadReferences();

// KEY REMINDERS AT END
const finalContext = "REMEMBER: Validate all inputs, use bcrypt...";
```

</v-clicks>

---

# Problem 4: Forgetfulness

<v-clicks>

**Challenge**: Important content decays mid-sequence without reinforcement

Long contexts cause the model to "forget" earlier information

**Solution**: Interspersed repetition
```typescript
// Initial mention
"Use async/await for all database operations"

// ... 500 tokens of other context ...

// Reinforce key point
"REMINDER: All database calls must use async/await"

// ... more context ...

// Final reinforcement
"CRITICAL: async/await pattern required (see above)"
```

</v-clicks>

---

# Problem 5: Context Rot

<v-clicks>

**Challenge**: Outdated or irrelevant context remains cached or reused, leading to stale generations

- Code changes but cached context doesn't update
- Dependencies evolve but context references old versions
- Project decisions change but AI continues with old assumptions

**Solution**: Context freshness tracking
```typescript
interface ContextBlock {
  content: string;
  timestamp: Date;
  ttl: number;  // Time to live in seconds
  dependencies: string[];  // Files this context depends on
}

class ContextManager {
  isStale(block: ContextBlock): boolean {
    const age = Date.now() - block.timestamp.getTime();
    if (age > block.ttl * 1000) return true;
    
    // Check if dependencies changed
    return block.dependencies.some(dep => 
      fileWasModified(dep, block.timestamp)
    );
  }
  
  refresh(block: ContextBlock): ContextBlock {
    return {
      ...block,
      content: regenerateContext(block),
      timestamp: new Date()
    };
  }
}
```

</v-clicks>

---

# Problem 6: Content Poisoning

<v-clicks>

**Challenge**: Malicious or low-quality input data biases future completions or retrievals

- Compromised dependencies introduce malicious patterns
- Poor-quality code examples in training set
- User-provided context with hidden instructions
- Embedded prompts that hijack behavior

**Solution**: Input validation and sanitization
```typescript
class ContextValidator {
  validate(content: string): ValidationResult {
    const issues: string[] = [];
    
    // Check for prompt injection attempts
    if (/ignore (previous|above) instructions/i.test(content)) {
      issues.push('Potential prompt injection detected');
    }
    
    // Check for suspicious patterns
    if (containsSuspiciousCode(content)) {
      issues.push('Suspicious code patterns detected');
    }
    
    // Verify source authenticity
    if (!isFromTrustedSource(content)) {
      issues.push('Untrusted source');
    }
    
    return {
      isValid: issues.length === 0,
      issues,
      sanitized: sanitizeContent(content)
    };
  }
}
```

</v-clicks>

---

# Problem 7: Output Variance

<v-clicks>

**Challenge**: Inconsistent behavior due to unstandardized context delivery

- Same query, different results based on context order
- Unpredictable quality across sessions
- Difficulty reproducing issues

**Solution**: Standardized context templates
```typescript
interface StandardContext {
  systemPrompt: string;
  taskDescription: string;
  constraints: string[];
  examples: Example[];
  currentState: CodeContext;
  history: ConversationSummary;
}

function buildContext(input: UserInput): StandardContext {
  return {
    systemPrompt: SYSTEM_PROMPT_V1,  // Versioned
    taskDescription: extractTask(input),
    constraints: loadProjectConstraints(),
    examples: findRelevantExamples(input, maxCount: 3),
    currentState: captureCodeContext(),
    history: summarizeHistory(maxTokens: 500)
  };
}
```

</v-clicks>

---

# Context Pipeline Design

A systematic approach to context management

<v-clicks>

### Stage 1: Ingestion
Gather all candidate sources (code, specs, notes, history)

### Stage 2: Filtering
Remove redundant, irrelevant, or unsafe material to prevent poisoning

### Stage 3: Summarization
Condense large sections to preserve key information

### Stage 4: Packing
Arrange segments to emphasize importance and flow

### Stage 5: Injection
Deliver packed context through prompts, memory slots, or retrieval layers

### Stage 6: Evaluation
Continuously measure output quality and context freshness to detect rot

</v-clicks>

---

# Pipeline Stage 1: Ingestion

```typescript
class ContextIngestion {
  async gather(task: Task): Promise<RawContext[]> {
    const sources: RawContext[] = [];
    
    // Current workspace
    sources.push({
      type: 'workspace',
      content: await this.getCurrentFiles(),
      priority: 'high'
    });
    
    // Project documentation
    sources.push({
      type: 'docs',
      content: await this.loadDocs(['README.md', 'ARCHITECTURE.md']),
      priority: 'medium'
    });
    
    // Conversation history
    sources.push({
      type: 'history',
      content: await this.getRecentHistory(limit: 20),
      priority: 'medium'
    });
    
    // Vector search results
    sources.push({
      type: 'retrieved',
      content: await this.semanticSearch(task.description),
      priority: 'low'
    });
    
    return sources;
  }
}
```

---

# Pipeline Stage 2: Filtering

```typescript
class ContextFilter {
  filter(contexts: RawContext[]): FilteredContext[] {
    return contexts
      .map(ctx => this.validate(ctx))
      .filter(ctx => ctx.isValid)
      .map(ctx => this.removeNoise(ctx))
      .filter(ctx => this.isRelevant(ctx))
      .map(ctx => this.deduplicate(ctx));
  }
  
  private validate(ctx: RawContext): ValidatedContext {
    // Check for poisoning attempts
    if (this.containsMaliciousPatterns(ctx.content)) {
      return { ...ctx, isValid: false, reason: 'potential_poisoning' };
    }
    
    // Verify source trust
    if (!this.isTrustedSource(ctx.source)) {
      return { ...ctx, isValid: false, reason: 'untrusted_source' };
    }
    
    // Check freshness
    if (this.isStale(ctx)) {
      return { ...ctx, isValid: false, reason: 'context_rot' };
    }
    
    return { ...ctx, isValid: true };
  }
  
  private removeNoise(ctx: ValidatedContext): FilteredContext {
    // Remove comments, logs, debug statements
    const cleaned = ctx.content
      .replace(/\/\/ TODO:.*/g, '')
      .replace(/console\.log\(.*\);?/g, '')
      .replace(/debugger;?/g, '');
    
    return { ...ctx, content: cleaned };
  }
}
```

---

# Pipeline Stage 3: Summarization

```typescript
class ContextSummarizer {
  async summarize(
    contexts: FilteredContext[], 
    maxTokens: number
  ): Promise<SummarizedContext[]> {
    const results: SummarizedContext[] = [];
    
    for (const ctx of contexts) {
      const tokenCount = this.estimateTokens(ctx.content);
      
      if (tokenCount <= maxTokens) {
        // Keep as-is
        results.push({ ...ctx, summarized: false });
      } else {
        // Apply progressive summarization
        const summary = await this.progressiveSummarize(
          ctx.content,
          targetTokens: maxTokens,
          levels: ['detailed', 'moderate', 'brief']
        );
        
        results.push({
          ...ctx,
          content: summary,
          summarized: true,
          originalTokens: tokenCount,
          finalTokens: this.estimateTokens(summary)
        });
      }
    }
    
    return results;
  }
  
  private async progressiveSummarize(
    content: string,
    targetTokens: number,
    levels: string[]
  ): Promise<string> {
    let current = content;
    
    for (const level of levels) {
      const tokens = this.estimateTokens(current);
      if (tokens <= targetTokens) break;
      
      current = await this.llm.summarize(current, {
        style: level,
        maxTokens: Math.floor(targetTokens * 1.1)
      });
    }
    
    return current;
  }
}
```

---

# Pipeline Stage 4: Packing

```typescript
class ContextPacker {
  pack(contexts: SummarizedContext[]): PackedContext {
    // Sort by priority and recency
    const sorted = this.prioritize(contexts);
    
    // Group by type
    const grouped = this.groupByType(sorted);
    
    // Apply ordering strategy (edges + repetition)
    const ordered = this.applyOrderingStrategy(grouped);
    
    // Add structural markers
    return this.addStructure(ordered);
  }
  
  private applyOrderingStrategy(
    grouped: GroupedContext
  ): OrderedContext[] {
    const result: OrderedContext[] = [];
    
    // 1. Start with high-priority system context
    result.push(...this.formatSection('SYSTEM', grouped.system));
    
    // 2. Add critical task information
    result.push(...this.formatSection('TASK', grouped.task));
    
    // 3. Insert key constraints (will repeat later)
    const constraints = grouped.constraints;
    result.push(...this.formatSection('CONSTRAINTS', constraints));
    
    // 4. Add supporting context (code, docs, etc.)
    result.push(...this.formatSection('CONTEXT', grouped.supporting));
    
    // 5. Repeat critical constraints
    result.push(...this.formatSection('REMINDER', constraints));
    
    // 6. Add examples
    result.push(...this.formatSection('EXAMPLES', grouped.examples));
    
    // 7. Final reminder of key points
    result.push(...this.formatSection('KEY_POINTS', 
      this.extractKeyPoints(constraints)
    ));
    
    return result;
  }
}
```

---

# Pipeline Stage 5: Injection

```typescript
class ContextInjector {
  inject(packed: PackedContext, target: 'chat' | 'completion'): Message[] {
    if (target === 'chat') {
      return this.injectAsChat(packed);
    } else {
      return this.injectAsCompletion(packed);
    }
  }
  
  private injectAsChat(packed: PackedContext): Message[] {
    const messages: Message[] = [];
    
    // System message with core context
    messages.push({
      role: 'system',
      content: packed.sections
        .filter(s => s.type === 'SYSTEM')
        .map(s => s.content)
        .join('\n\n')
    });
    
    // Add structured context as assistant message
    messages.push({
      role: 'assistant',
      content: 'I understand the context. Here\'s what I know:\n\n' +
        packed.sections
          .filter(s => s.type === 'CONTEXT')
          .map(s => `- ${s.content}`)
          .join('\n')
    });
    
    // User task at the end (strong recency)
    messages.push({
      role: 'user',
      content: packed.sections
        .filter(s => s.type === 'TASK')
        .map(s => s.content)
        .join('\n\n')
    });
    
    return messages;
  }
}
```

---

# Pipeline Stage 6: Evaluation

```typescript
class ContextEvaluator {
  async evaluate(
    context: PackedContext,
    output: string,
    expectedOutcome?: string
  ): Promise<EvaluationResult> {
    return {
      accuracy: await this.measureAccuracy(output, expectedOutcome),
      quality: await this.measureQuality(output),
      efficiency: this.measureEfficiency(context),
      stability: await this.measureStability(context, output),
      freshness: this.checkFreshness(context)
    };
  }
  
  private measureEfficiency(context: PackedContext): number {
    const totalTokens = context.sections.reduce(
      (sum, s) => sum + this.estimateTokens(s.content), 0
    );
    
    const usefulTokens = context.sections
      .filter(s => s.priority === 'high')
      .reduce((sum, s) => sum + this.estimateTokens(s.content), 0);
    
    return usefulTokens / totalTokens;
  }
  
  private checkFreshness(context: PackedContext): FreshnessReport {
    const stale = context.sections.filter(s => {
      const age = Date.now() - s.timestamp.getTime();
      return age > s.ttl * 1000;
    });
    
    return {
      totalSections: context.sections.length,
      staleSections: stale.length,
      needsRefresh: stale.map(s => s.id),
      freshnessScore: 1 - (stale.length / context.sections.length)
    };
  }
}
```

---

# Ordering and Repetition (Anthropic Findings)

Research-backed strategies for context placement

---

# Lost-in-the-Middle Mitigation

<v-clicks>

**Research Finding**: Models struggle to recall information from the middle of long contexts

### Strategy: Edge Placement
```typescript
function arrangeContext(items: ContextItem[]): string {
  const critical = items.filter(i => i.priority === 'critical');
  const supporting = items.filter(i => i.priority === 'supporting');
  const supplementary = items.filter(i => i.priority === 'supplementary');
  
  return [
    '=== CRITICAL INFORMATION (START) ===',
    ...critical,
    '',
    '=== SUPPORTING DETAILS ===',
    ...supporting,
    ...supplementary,
    '',
    '=== CRITICAL REMINDERS (END) ===',
    ...critical.map(c => `REMINDER: ${c}`)
  ].join('\n\n');
}
```

**Result**: 30-40% improvement in recall for critical information

</v-clicks>

---

# Interspersed Repetition

<v-clicks>

**Research Finding**: Periodic repetition refreshes attention and prevents decay

### Strategy: Spaced Repetition
```typescript
class RepetitionManager {
  insertRepetitions(
    content: string[], 
    keyPoints: string[]
  ): string[] {
    const result: string[] = [];
    const interval = Math.floor(content.length / (keyPoints.length + 1));
    
    let pointIndex = 0;
    for (let i = 0; i < content.length; i++) {
      result.push(content[i]);
      
      // Insert reminder at intervals
      if ((i + 1) % interval === 0 && pointIndex < keyPoints.length) {
        result.push(`\n🔔 REMINDER: ${keyPoints[pointIndex]}\n`);
        pointIndex++;
      }
    }
    
    // Final reminder
    result.push('\n⚠️ KEY REQUIREMENTS:');
    result.push(...keyPoints.map(p => `  - ${p}`));
    
    return result;
  }
}
```

**Frequency**: Every 200-300 tokens for critical constraints

</v-clicks>

---

# Hierarchical Ordering

<v-clicks>

**Strategy**: Use structured layering—summary, details, reminder—to maintain focus

```typescript
interface HierarchicalContext {
  summary: string;      // High-level overview (50-100 tokens)
  details: Section[];   // In-depth information (500-1000 tokens)
  reminder: string;     // Key takeaways (50-100 tokens)
}

function buildHierarchy(topic: string, data: any): HierarchicalContext {
  return {
    summary: `
## ${topic} Overview
${generateSummary(data, maxTokens: 100)}
    `,
    details: data.sections.map(s => ({
      heading: s.title,
      content: s.content,
      examples: s.examples
    })),
    reminder: `
## Key Points to Remember
${extractKeyPoints(data).map(p => `- ${p}`).join('\n')}
    `
  };
}
```

**Pattern**: Summary → Detailed Context → Reminder

</v-clicks>

---

# Refresh Cycles

<v-clicks>

**Strategy**: Periodically replace or regenerate context blocks to counteract context rot

```typescript
class ContextRefreshManager {
  private refreshSchedule: Map<string, RefreshPolicy> = new Map();
  
  scheduleRefresh(contextId: string, policy: RefreshPolicy) {
    this.refreshSchedule.set(contextId, policy);
  }
  
  async runRefreshCycle() {
    for (const [id, policy] of this.refreshSchedule) {
      const context = await this.getContext(id);
      
      if (this.shouldRefresh(context, policy)) {
        await this.refresh(context, policy.strategy);
      }
    }
  }
  
  private shouldRefresh(
    context: ContextBlock, 
    policy: RefreshPolicy
  ): boolean {
    // Time-based refresh
    const age = Date.now() - context.lastRefresh.getTime();
    if (age > policy.maxAge) return true;
    
    // Change-based refresh
    if (policy.watchFiles) {
      const changed = policy.watchFiles.some(f => 
        this.fileChanged(f, context.lastRefresh)
      );
      if (changed) return true;
    }
    
    // Quality-based refresh
    if (context.qualityScore < policy.minQuality) return true;
    
    return false;
  }
}
```

**Policies**: Time-based, event-based, quality-based

</v-clicks>

---

# Evaluation & Metrics

Measuring context engineering effectiveness

---

# Metric 1: Accuracy

<v-clicks>

**Definition**: Reduction in factual or logical errors

```typescript
interface AccuracyMetrics {
  factualCorrectness: number;    // 0-1, verified facts
  logicalCoherence: number;       // 0-1, reasoning validity
  specCompliance: number;         // 0-1, meets requirements
  errorRate: number;              // Count of mistakes
}

async function measureAccuracy(
  output: string,
  groundTruth: string,
  specs: Specification[]
): Promise<AccuracyMetrics> {
  // Extract facts from output
  const outputFacts = await extractFacts(output);
  const truthFacts = await extractFacts(groundTruth);
  
  const factualCorrectness = outputFacts.filter(f => 
    truthFacts.some(t => semanticallySimilar(f, t))
  ).length / truthFacts.length;
  
  // Check logical consistency
  const logicalCoherence = await checkLogic(output);
  
  // Verify spec compliance
  const specCompliance = specs.filter(s => 
    meetsSpecification(output, s)
  ).length / specs.length;
  
  return {
    factualCorrectness,
    logicalCoherence,
    specCompliance,
    errorRate: countErrors(output)
  };
}
```

</v-clicks>

---

# Metric 2: Quality

<v-clicks>

**Definition**: Alignment between output and target objectives

```typescript
interface QualityMetrics {
  codeQuality: number;         // Style, maintainability
  completeness: number;        // All requirements addressed
  usability: number;           // Practical utility
  consistency: number;         // Matches project patterns
}

function measureQuality(
  output: string,
  project: ProjectContext
): QualityMetrics {
  return {
    codeQuality: analyzeCodeQuality(output, {
      complexity: true,
      maintainability: true,
      testability: true
    }),
    completeness: checkCompleteness(output, project.requirements),
    usability: assessUsability(output, project.userStories),
    consistency: measureConsistency(output, project.codebase)
  };
}
```

**Target**: > 0.85 on all dimensions

</v-clicks>

---

# Metric 3: Efficiency

<v-clicks>

**Definition**: Useful tokens per total tokens processed

```typescript
interface EfficiencyMetrics {
  tokenUtilization: number;     // Useful / Total tokens
  retrievalPrecision: number;   // Relevant / Retrieved items
  compressionRatio: number;     // Original / Compressed size
  costPerTask: number;          // $ spent per completion
}

function measureEfficiency(
  context: PackedContext,
  output: string
): EfficiencyMetrics {
  const totalTokens = countTokens(context);
  const usefulTokens = identifyUsefulTokens(context, output);
  
  return {
    tokenUtilization: usefulTokens / totalTokens,
    retrievalPrecision: calculatePrecision(context.retrieved),
    compressionRatio: context.originalSize / context.packedSize,
    costPerTask: estimateCost(totalTokens)
  };
}
```

**Goal**: Maximize useful tokens, minimize cost

</v-clicks>

---

# Metric 4: Stability

<v-clicks>

**Definition**: Reduced drift across repeated runs

```typescript
interface StabilityMetrics {
  outputVariance: number;       // Consistency across runs
  deterministicScore: number;   // Same input → same output
  robustness: number;           // Handles edge cases
}

async function measureStability(
  context: PackedContext,
  runs: number = 10
): Promise<StabilityMetrics> {
  const outputs: string[] = [];
  
  // Run multiple times with same context
  for (let i = 0; i < runs; i++) {
    const output = await generateWithContext(context);
    outputs.push(output);
  }
  
  // Calculate similarity between outputs
  const similarities = pairwiseSimilarity(outputs);
  const avgSimilarity = mean(similarities);
  
  return {
    outputVariance: 1 - avgSimilarity,
    deterministicScore: avgSimilarity,
    robustness: await testEdgeCases(context)
  };
}
```

**Target**: > 0.90 similarity across runs

</v-clicks>

---

# Metric 5: Freshness

<v-clicks>

**Definition**: Absence of stale, outdated, or poisoned context in recent outputs

```typescript
interface FreshnessMetrics {
  contextAge: number;              // Average age in hours
  staleRatio: number;              // Stale / Total blocks
  updateFrequency: number;         // Updates per day
  poisoningDetections: number;     // Caught attempts
}

function measureFreshness(
  context: PackedContext
): FreshnessMetrics {
  const now = Date.now();
  const ages = context.sections.map(s => 
    (now - s.timestamp.getTime()) / (1000 * 60 * 60)
  );
  
  const stale = context.sections.filter(s => 
    this.isStale(s)
  );
  
  return {
    contextAge: mean(ages),
    staleRatio: stale.length / context.sections.length,
    updateFrequency: context.refreshHistory.length / 7,
    poisoningDetections: context.validationLog.filter(
      l => l.type === 'poisoning_attempt'
    ).length
  };
}
```

**Alert**: If staleRatio > 0.2, trigger refresh cycle

</v-clicks>

---

# Practical Exercise

Hands-on context engineering with Copilot

---

# Exercise Setup

<v-clicks>

**Objective**: Compare baseline vs. engineered context for a real coding task

**Task**: Implement a caching layer for an API client

**Steps**:
1. Baseline run with minimal context
2. Enhanced run with full context engineering
3. Measure and compare results

**Duration**: 30 minutes

**Tools Needed**:
- VS Code with GitHub Copilot
- Git repository with sample code
- Evaluation script

</v-clicks>

---

# Exercise Part 1: Baseline

<v-clicks>

```typescript
// Minimal context - just the function signature
async function cacheApiResponse(key: string, fetcher: () => Promise<any>) {
  // Let Copilot complete this
}
```

**Copilot's likely output**: Basic in-memory cache, no expiration, no error handling

**Common issues**:
- No TTL management
- No cache invalidation
- Memory leaks from unbounded cache
- No handling of failed fetches
- Missing type safety

</v-clicks>

---

# Exercise Part 2: Enhanced Context

<v-clicks>

```typescript
// CONTEXT: API Caching Layer
// PROJECT: High-traffic REST API with rate limits
// REQUIREMENTS:
// - Redis-backed cache with 5-minute TTL
// - Graceful degradation if Redis unavailable
// - Automatic retry with exponential backoff
// - Type-safe keys and values
// - Metrics logging for cache hits/misses

// EXISTING PATTERNS: See RedisClient.ts for connection handling
// SIMILAR: UserCache.ts implements related pattern
// CONSTRAINTS:
// - Must not exceed 100MB Redis memory
// - Must handle concurrent requests safely
// - Must log all cache operations

interface CacheConfig {
  ttl: number;           // seconds
  maxSize: number;       // bytes
  retryAttempts: number;
}

// CRITICAL: Handle Redis connection failures gracefully
async function cacheApiResponse<T>(
  key: string, 
  fetcher: () => Promise<T>,
  config: CacheConfig
): Promise<T> {
  // Enhanced implementation with full context
}
```

</v-clicks>

---

# Exercise Part 3: Measurement

<v-clicks>

### Evaluation Criteria

**Accuracy**:
- ✅ Implements TTL correctly
- ✅ Handles Redis failures
- ✅ Includes retry logic
- ✅ Type-safe implementation

**Quality**:
- ✅ Follows project patterns
- ✅ Comprehensive error handling
- ✅ Proper logging
- ✅ Memory-safe

**Efficiency**:
- Baseline: ~150 tokens → 20% useful
- Enhanced: ~400 tokens → 75% useful
- Net improvement: 3.75x better signal

</v-clicks>

---

# Exercise Results Example

<v-clicks>

| Metric | Baseline | Enhanced | Improvement |
|--------|----------|----------|-------------|
| Accuracy | 45% | 92% | +104% |
| Quality Score | 3.2/10 | 8.7/10 | +172% |
| Token Efficiency | 22% | 76% | +245% |
| Edit Distance | 387 chars | 42 chars | -89% |
| Time to Working Code | 18 min | 4 min | -78% |

**Key Insight**: Small increase in context size (2.7x) yields massive quality improvement (2.7x accuracy, 9x fewer edits)

</v-clicks>

---

# Implementation Patterns for Copilot

Practical techniques for GitHub Copilot

---

# Pattern 1: Chat Commands

<v-clicks>

**Use Copilot's built-in scope tags to focus retrieval**

```typescript
// In Copilot Chat:

// Focus on specific file
#file:UserRepository.ts How does this handle transactions?

// Search entire codebase
#codebase Find all authentication implementations

// Reference documentation
#docs @microsoft/azure-functions How do I configure bindings?

// Use workspace context
#workspace Show me all API endpoints
```

**Benefits**:
- Targeted retrieval reduces noise
- Explicit scoping prevents context drift
- Combines multiple context sources

</v-clicks>

---

# Pattern 2: Spec Kit Artifacts

<v-clicks>

**Embed structured specification files to convey intent**

```markdown
<!-- spec.md -->
# Feature: User Authentication

## Overview
Implement JWT-based authentication with refresh tokens

## Requirements
- [ ] Support RS256 signing algorithm
- [ ] 15-minute access token expiration
- [ ] 7-day refresh token expiration
- [ ] Secure HttpOnly cookies
- [ ] CSRF protection

## Constraints
- Must work with existing UserRepository
- Must maintain backward compatibility with v1 API
- Must pass OWASP security standards

## Acceptance Criteria
- All security tests pass
- Performance: < 50ms token generation
- Zero user session loss during deployment
```

**Usage**: Reference `#file:spec.md` in Copilot prompts

</v-clicks>

---

# Pattern 3: Copilot Spaces

<v-clicks>

**Centralize shared context across contributors**

**What to include in Spaces**:
- Repository README and documentation
- Active issues and PRs
- Design documents and ADRs (Architecture Decision Records)
- Common questions and answers

**Benefits**:
- Consistent context across team
- Reduces repetitive explanations
- Captures institutional knowledge
- Prevents context poisoning from external sources

**Setup**:
```bash
# Create a Space for your project
# Add repositories: main repo, docs repo, examples repo
# Add key documentation files
# Invite team members
```

</v-clicks>

---

# Pattern 4: MCP Servers (Model Context Protocol)

<v-clicks>

**Extend Copilot with real-time, dynamic context**

### Use Cases

1. **Fetch Live Data**
```typescript
// MCP server for library updates
const libInfo = await mcp.getLibraryInfo('react');
// Returns: Latest version, breaking changes, migration guide
```

2. **Query Vector Indexes**
```typescript
// Semantic search on large codebase
const similar = await mcp.semanticSearch(
  'authentication middleware',
  { repo: 'company/backend', maxResults: 5 }
);
```

3. **Real-Time Grounding**
```typescript
// Check API status and docs
const apiStatus = await mcp.getApiStatus('stripe-payments');
// Returns: Status, rate limits, recent changes
```

</v-clicks>

---

# Pattern 5: agents.md Configuration

<v-clicks>

**Define context management rules for AI agents**

```markdown
<!-- .github/agents.md -->
# Agent Context Configuration

## Context Refresh Triggers
- On file save in `src/` directory
- On dependency updates in package.json
- On PR reviews containing "update context"
- Every 24 hours for cached documentation

## Retrieval Rules
- Always include: package.json, tsconfig.json, README.md
- Include on demand: Test files related to current file
- Exclude: node_modules/, dist/, .git/

## Poisoning Prevention
- Validate all external code samples
- Reject context from untrusted sources
- Sanitize user-provided examples
- Flag suspicious patterns: eval(), exec(), prompt injection

## Context Priorities
1. Current file and direct imports (HIGH)
2. Recent conversation history (HIGH)
3. Project documentation (MEDIUM)
4. Similar code from codebase (MEDIUM)
5. External references (LOW)

## Refresh Policy
- TTL: 1 hour for code context
- TTL: 24 hours for documentation
- TTL: 7 days for external references
```

</v-clicks>

---

# Summary: Context Engineering Loop

The operational cycle for sustained quality

<v-clicks>

### The Loop

1. **Select** relevant context sources
2. **Filter** for quality and safety (prevent poisoning)
3. **Order** strategically (edges + repetition)
4. **Repeat** key constraints (combat forgetfulness)
5. **Evaluate** output quality and context freshness
6. **Refresh** stale or outdated blocks (prevent rot)
7. **Protect** against malicious input (validation)

### Without Engineering
- Shallow, decaying context
- Potential poisoning risks
- Inconsistent output quality
- High edit burden

### With Engineering
- Fresh, relevant context
- Protected from corruption
- Stable, high-quality output
- Minimal manual fixes

</v-clicks>

---

# Key Takeaways

<v-clicks>

### Context Engineering Is Essential
- **Default context is insufficient** for complex tasks
- **Strategic engineering** multiplies effectiveness
- **Small context improvements** yield large quality gains

### Core Challenges Solved
- ✅ Limited attention through prioritization
- ✅ Context rot through refresh cycles
- ✅ Content poisoning through validation
- ✅ Forgetfulness through repetition
- ✅ Variance through standardization

### Practical Implementation
- Use Copilot's native tools (#file, #codebase, Spaces)
- Implement MCP servers for dynamic context
- Create spec.md and agents.md for structure
- Monitor metrics and adjust continuously

</v-clicks>

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
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [Pinecone Vector Database Docs](https://docs.pinecone.io/)

🛠️ **Practice Tools:**
- Polyglot Notebooks (included in /notebooks)
- Prompty Files (included in /prompty)
- Workshop Exercises (included in /workshops)

🎯 **Next Steps:**
- Complete all workshop exercises
- Experiment with different patterns
- Implement RAG with hybrid search
- Build chat reducers for your applications
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
