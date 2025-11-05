---
theme: default
highlighter: shiki
lineNumbers: true
transition: slide-left
---

# Advanced Context Engineering

Beyond prompt engineering fundamentals

---

# External Slides: RAG & Context Techniques

<v-clicks>

**Deep Dive References:**

| Topic | External Slide | Focus |
|-------|----------------|-------|
| RAG Fundamentals | [RAG Techniques](prompt-engineering/04.3_Prompt_Engineering_Techniques.RAG.md) | Retrieval-Augmented Generation |
| Parameter Optimization | [Parameter Tuning](prompt-engineering/04.4_Prompt_Engineering_Techniques.Parameter_Tuning.md) | Temperature, sampling, context length |
| Testing Strategies | [Testing and Evaluation](prompt-engineering/07_Testing_and_Evaluation_Strategies.md) | Metrics and benchmarking |

</v-clicks>

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