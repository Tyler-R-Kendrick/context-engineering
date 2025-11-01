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
