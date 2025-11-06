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

---

# Constraint 1: Limited Attention Window

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

# Constraint 2: Unreliable Retrieval

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

# Constraint 3: Sensitivity to Ordering

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

# Constraint 4: Context Rot

<v-clicks>

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

</v-clicks>

---

# Constraint 5: Content Poisoning

<v-clicks>

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

# Pipeline Implementation Example

```typescript
class ContextPipeline {
  async process(task: Task): Promise<PackedContext> {
    // Stage 1: Ingestion
    const rawContexts = await this.ingestion.gather(task);
    
    // Stage 2: Filtering
    const filteredContexts = this.filter.process(rawContexts);
    
    // Stage 3: Summarization
    const summarizedContexts = await this.summarizer.process(
      filteredContexts, 
      maxTokens: 2000
    );
    
    // Stage 4: Packing
    const packedContext = this.packer.arrange(summarizedContexts);
    
    // Stage 5: Injection happens in client code
    // Stage 6: Evaluation happens post-generation
    
    return packedContext;
  }
}
```

---

# Lost-in-the-Middle Mitigation

Research-backed strategies for context placement

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
