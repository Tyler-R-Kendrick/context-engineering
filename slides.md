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

# Prompt Engineering with Semantic Kernel

A framework approach to AI application development

---

# What is Semantic Kernel?

<v-clicks>

**Semantic Kernel** is an open-source SDK that enables you to build AI agents and integrate Large Language Models (LLMs) into your applications.

Key Features:
- 🔧 **Multi-Language Support**: C#, Python, Java
- 🧩 **Plugin Architecture**: Extensible and modular
- 🔄 **Prompt Templates**: Reusable, parameterized prompts
- 🤖 **Agentic Patterns**: Built-in support for AI agents
- 🔌 **Connector System**: Works with multiple AI services

</v-clicks>

<v-click>

> Semantic Kernel makes prompt engineering systematic and scalable

</v-click>

---

# Prompt Template Engines

Semantic Kernel supports multiple template formats

<v-clicks>

### 1. **YAML Format**
```yaml
name: SummarizeText
description: Summarizes input text
template: |
  Summarize the following in {{$maxWords}} words:
  {{$input}}
```

### 2. **Handlebars Templates**
```handlebars
{{#if userRole}}
  As a {{userRole}}, please {{task}}
{{else}}
  Please {{task}}
{{/if}}
```

### 3. **Prompty Format**
```yaml
---
name: CodeReview
model: gpt-4
---
system:
Review this {{language}} code for {{focus}}
```

</v-clicks>

---

# Zero-Shot, One-Shot, Few-Shot Patterns

Different approaches to prompt engineering

---

# Zero-Shot Prompting

Ask the model without any examples

```csharp
var kernel = builder.Build();

var prompt = """
Translate the following English text to French:
"Hello, how are you today?"
""";

var result = await kernel.InvokePromptAsync(prompt);
Console.WriteLine(result);
```

<v-click>

**Best for:**
- Simple, well-defined tasks
- Models with strong general knowledge
- Quick prototyping

</v-click>

---

# One-Shot Prompting

Provide a single example to guide the model

```csharp
var prompt = """
Convert product descriptions to JSON format.

Example:
Input: "Red cotton t-shirt, size M, $19.99"
Output: {"color": "red", "material": "cotton", "type": "t-shirt", "size": "M", "price": 19.99}

Now convert:
Input: "Blue denim jeans, size 32, $49.99"
Output:
""";

var result = await kernel.InvokePromptAsync(prompt);
```

<v-click>

**Best for:**
- Specific formats or patterns
- Consistency in output structure
- Reducing ambiguity

</v-click>

---

# Few-Shot Prompting

Multiple examples for better pattern recognition

```python
from semantic_kernel import Kernel

prompt = """
Classify customer feedback sentiment and extract key topics.

Examples:
Feedback: "Great product, fast shipping!"
Sentiment: Positive | Topics: product quality, delivery speed

Feedback: "Item arrived damaged, poor packaging"
Sentiment: Negative | Topics: product condition, packaging

Feedback: "Average quality, expected better for the price"
Sentiment: Neutral | Topics: value, quality expectations

Now classify:
Feedback: "Excellent customer service, resolved my issue quickly"
"""

result = await kernel.invoke_prompt_async(prompt)
```

---

# Few-Shot: When to Use

<v-clicks>

**Advantages:**
- ✅ Better pattern learning
- ✅ More consistent outputs
- ✅ Handles complex transformations
- ✅ Reduces need for fine-tuning

**Considerations:**
- ⚠️ Longer prompts (more tokens)
- ⚠️ Choose diverse, representative examples
- ⚠️ Balance: too few = inconsistent, too many = expensive

**Rule of Thumb:** Start with 3-5 examples

</v-clicks>

---

# Semantic Kernel: Kernel Builder Pattern

Creating and configuring kernels

```csharp
using Microsoft.SemanticKernel;

// Create kernel with builder pattern
var builder = Kernel.CreateBuilder();

// Add AI service
builder.AddAzureOpenAIChatCompletion(
    deploymentName: "gpt-4",
    endpoint: "https://your-resource.openai.azure.com",
    apiKey: "your-api-key"
);

// Add plugins
builder.Plugins.AddFromType<TimePlugin>();
builder.Plugins.AddFromType<MathPlugin>();

// Build the kernel
var kernel = builder.Build();
```

<v-click>

**Key Concept:** The kernel orchestrates AI services, plugins, and prompts

</v-click>

---

# Semantic Functions vs Native Functions

Two ways to extend the kernel

<v-clicks>

### **Semantic Functions** (Prompt-based)
```csharp
var summarize = kernel.CreateFunctionFromPrompt("""
Summarize the following text in {{$maxWords}} words:
{{$input}}
""");

var result = await kernel.InvokeAsync(summarize, 
    new() { ["input"] = longText, ["maxWords"] = "50" });
```

### **Native Functions** (Code-based)
```csharp
public class TextPlugin
{
    [KernelFunction]
    public int CountWords(string text) 
        => text.Split(' ', StringSplitOptions.RemoveEmptyEntries).Length;
}
```

</v-clicks>

---

# Chaining Functions Together

Compose complex workflows

```csharp
// Define prompts
var translate = kernel.CreateFunctionFromPrompt(
    "Translate to {{$language}}: {{$input}}");

var summarize = kernel.CreateFunctionFromPrompt(
    "Summarize in 2 sentences: {{$input}}");

// Chain execution
var input = "Long English article text...";

// Step 1: Translate
var translated = await kernel.InvokeAsync(translate,
    new() { ["input"] = input, ["language"] = "Spanish" });

// Step 2: Summarize translated text
var summary = await kernel.InvokeAsync(summarize,
    new() { ["input"] = translated.ToString() });

Console.WriteLine(summary);
```

---

# Automatic Function Calling

Let the LLM decide when to use tools

```csharp
// Define functions
public class WeatherPlugin
{
    [KernelFunction, Description("Get current weather for a city")]
    public string GetWeather(string city) 
        => $"Weather in {city}: 72°F, Sunny";
}

// Add to kernel
builder.Plugins.AddFromType<WeatherPlugin>();

// Enable auto-function calling
var settings = new OpenAIPromptExecutionSettings
{
    ToolCallBehavior = ToolCallBehavior.AutoInvokeKernelFunctions
};

// LLM will automatically call WeatherPlugin when needed
var result = await kernel.InvokePromptAsync(
    "What's the weather in Seattle and should I bring an umbrella?",
    new(settings)
);
```

---

# Prompt Engineering with Agents

Semantic Kernel's agentic patterns

```csharp
#pragma warning disable SKEXP0110

// Create an agent
var agent = new ChatCompletionAgent
{
    Name = "ResearchAssistant",
    Instructions = """
        You are a helpful research assistant.
        Use available tools to find accurate information.
        Always cite your sources.
        """,
    Kernel = kernel
};

// Agent conversation
var chat = new AgentGroupChat();

await chat.AddChatMessageAsync(
    new ChatMessageContent(AuthorRole.User, 
        "What are the latest developments in quantum computing?")
);

await foreach (var message in chat.InvokeAsync(agent))
{
    Console.WriteLine($"{message.AuthorName}: {message.Content}");
}
```

---

# Multi-Agent Patterns

Agents working together

<v-clicks>

**Use Cases:**
- 🎭 **Role-based collaboration**: Different agents with specialized roles
- 🔄 **Iterative refinement**: One agent drafts, another reviews
- 🗳️ **Consensus building**: Multiple agents vote on solutions
- 🎯 **Divide and conquer**: Break complex tasks across agents

**Example Pattern:**
```
Researcher Agent → Drafter Agent → Reviewer Agent → Final Output
```

</v-clicks>

---

# Memory and Context Management

Keeping conversation context

```csharp
using Microsoft.SemanticKernel.Memory;

// Add memory to kernel
var memoryBuilder = new MemoryBuilder();
memoryBuilder.WithAzureOpenAITextEmbeddingGeneration(/*...*/);
var memory = memoryBuilder.Build();

// Save context
await memory.SaveInformationAsync(
    collection: "conversation",
    id: "user-pref-001",
    text: "User prefers concise responses"
);

// Retrieve relevant context
var relevantMemories = memory.SearchAsync(
    collection: "conversation",
    query: "How should I format my response?",
    limit: 3
);

// Use context in prompt
var context = string.Join("\n", relevantMemories);
var prompt = $"""
    Context: {context}
    
    User question: {{$input}}
    """;
```

---

# Prompt Template Best Practices

Tips for effective Semantic Kernel prompts

<v-clicks>

1. **Use Clear Variable Names**
   ```
   Good: {{$userRole}}, {{$targetLanguage}}
   Bad: {{$x}}, {{$temp}}
   ```

2. **Provide Descriptions**
   ```csharp
   [KernelFunction, Description("Translates text to target language")]
   ```

3. **Validate Inputs**
   ```csharp
   if (string.IsNullOrEmpty(input))
       throw new ArgumentException("Input cannot be empty");
   ```

4. **Version Your Prompts**
   - Save prompt templates in source control
   - Track changes and performance

</v-clicks>

---

# RAG Pattern with Semantic Kernel

Retrieval-Augmented Generation

```csharp
// 1. Index your documents
await memory.SaveInformationAsync(
    collection: "docs",
    id: "doc-001",
    text: "Your documentation content..."
);

// 2. Search for relevant context
var query = "How do I configure authentication?";
var relevantDocs = await memory.SearchAsync(
    collection: "docs",
    query: query,
    limit: 3
);

// 3. Augment prompt with retrieved context
var prompt = $"""
    Based on the following documentation:
    {string.Join("\n\n", relevantDocs)}
    
    Answer this question: {query}
    """;

var answer = await kernel.InvokePromptAsync(prompt);
```

---

# Semantic Kernel: Integration Points

Where SK fits in your application

<v-clicks>

- 🌐 **Web APIs**: Build AI-powered endpoints
- 💬 **Chatbots**: Conversational interfaces
- 🔧 **Automation**: Intelligent workflows
- 📊 **Data Processing**: Extract, transform, analyze
- 🧪 **Testing**: Generate test data and scenarios
- 📝 **Content Generation**: Documents, summaries, translations

**Key Advantage:** Same code works with multiple AI providers

</v-clicks>

---

# From GitHub Copilot to Semantic Kernel

How they complement each other

<div class="grid grid-cols-2 gap-4">

<div>

### GitHub Copilot
- 💻 Development-time assistance
- 🎯 Code completion
- 📝 Comment-driven generation
- 🔄 Interactive coding

**Best for:** Writing code faster

</div>

<div>

### Semantic Kernel
- 🏗️ Runtime AI integration
- 🔌 Application-level AI features
- 📦 Productionized AI
- 🤖 Agent orchestration

**Best for:** Building AI applications

</div>

</div>

<v-click>

**Use Together:** Use Copilot to write your SK code faster! 🚀

</v-click>

---

# Hands-On: Try Semantic Kernel

Getting started resources

<v-clicks>

📦 **Installation:**
```bash
# .NET
dotnet add package Microsoft.SemanticKernel

# Python
pip install semantic-kernel

# Java
// Maven coordinates in docs
```

📚 **Learning Resources:**
- [GitHub: microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)
- [Documentation](https://learn.microsoft.com/semantic-kernel)
- [Sample Applications](https://github.com/microsoft/semantic-kernel/tree/main/samples)
- [Community Discord](https://aka.ms/SKDiscord)

🎯 **Next Steps:**
- Check out `/dotnet/notebooks` from learn-sk repo
- Try the samples and patterns
- Build a simple AI agent

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
