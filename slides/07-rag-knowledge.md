---
theme: default
highlighter: shiki
lineNumbers: true
transition: slide-left
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