---
theme: default
highlighter: shiki
lineNumbers: true
transition: slide-left
---

# Problem Statement: Context Engineering Failure Modes

<v-clicks>

**Premise**: Even the best-crafted prompts collapse when the upstream context pipeline misallocates attention, retrieves noise, or recycles stale knowledge.

- Large language models inherit hard limits on attention, recall, and trust—without mitigation, they surface brittle or biased outputs.
- Engineering teams need a defensible strategy for what enters the window, how it is ordered, and how long it remains authoritative.
- Academic evaluation shows that failure to control these parameters drives the majority of hallucination and compliance regressions.

</v-clicks>

<!--
Now that we know where context gets pulled from, we need to consider the problems inherent in this space.

LLMs have several hard limits that bias their outputs.
So we need to identify those constraints if we are to design well engineered solutions for them.
-->

---

# Constraint 1: Limited Attention Window

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

<!--
With current llm architectures, recall and attention need to be attentuated - with degrading performance around the middle of the attention window.

Context must be structured and minimized to fit within these constraints.
-->

---

# Constraint 2: Unreliable Retrieval

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

<!--
A variety of retrieval techniques are available to model, index, and retrieve information from external sources - but they each come with their own host of issues.

VectorRAG has the problem of local vs global.
If you index a knoweledge base, user queries need to closely resemble the answers - otherwise, they will only pull back docs that are similar to the question - potentially reducing relevance.

GraphRAG is good at reasoning about relationships to information for finding more relevant groupings of info.
-->

---

# Constraint 3: Sensitivity to Ordering

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

<!--
Structure
-->

---

# Constraint 4: Context Rot

**Challenge**: Outdated or irrelevant context remains cached or reused

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
}
```

<!--
Context rot is a significant issue since llms have no concept of time. Because "freshness" of don't can't be reasoned about, techniques need to be implemented pull from sources that do effectively persist temporal data.
-->

---

# Constraint 5: Content Poisoning

**Challenge**: Malicious or low-quality input data biases future completions

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
    
    return {
      isValid: issues.length === 0,
      issues,
      sanitized: sanitizeContent(content)
    };
  }
}
```

---

# Context Pipeline Design

A systematic approach to context management

1. Ingestion
1. Filtering (sanitization)
1.

---

# Stage 1: Ingestion

Gather all candidate sources

- Code files and modules
- Specifications and requirements
- Notes and documentation
- Historical context and conversations

```typescript
const rawContexts = await this.ingestion.gather(task);
```

<!--
The first step to building relevant context should be around how you pull and persist knowledge.
Chunking strategies and different data modeling techniques can be used to enhance your ability to model knowledge for the relevant context.
-->

---

# Stage 2: Filtering

Remove redundant, irrelevant, or unsafe material to prevent poisoning

- Strip sensitive information
- Remove duplicates
- Eliminate noise
- Verify data integrity

```typescript
const filteredContexts = this.filter.process(rawContexts);
```

---

# Stage 3: Summarization

Condense large sections to preserve key information

```typescript
const summarizedContexts = await this.summarizer.process(
  filteredContexts, 
  { maxTokens: 2000 }
);
```

- Preserve essential details
- Reduce token overhead
- Maintain semantic meaning

---

# Stage 4: Packing

Arrange segments to emphasize importance and flow

```typescript
const packedContext = this.packer.arrange(summarizedContexts);
```

- Order by relevance
- Place critical info at boundaries
- Optimize for model attention

<!--
packing can reorder according to structure.
-->

# Stage 5: Evaluation

Continuously measure quality and freshness

```typescript
const quality = await this.evaluator.assess(output, context);
```

- Measure output quality
- Detect context staleness
- Identify degradation
- Trigger refresh cycles

---

# Lost-in-the-Middle Mitigation

Research-backed strategies for context placement

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

---

# Interspersed Repetition

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
