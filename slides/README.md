# Context Engineering Slides

This folder contains the presentation slides for "Context Engineering for GitHub Copilot" broken down into manageable sections.

## Slide Organization

| File | Content | Slides | External References |
|------|---------|--------|-------------------|
| [00-title.md](00-title.md) | Title and introduction | 1-2 | - |
| [01-introduction.md](01-introduction.md) | What is Context Engineering | 3-7 | - |
| [02-prompt-engineering.md](02-prompt-engineering.md) | Prompt Engineering Fundamentals | 8-20 | **🔗 [Workshop](prompt-engineering/)** (9 modules, 3hrs) |
| [03-tools.md](03-tools.md) | Tools for Context Engineering | 21-32 | - |
| [04-advanced-patterns.md](04-advanced-patterns.md) | Advanced Patterns | 33-40 | **🔗 [Advanced Techniques](prompt-engineering/)** (Reasoning, RAG, Parameters) |
| [05-workshop.md](05-workshop.md) | Workshop Scenarios | 41-49 | **🔗 [Practical Use Cases](prompt-engineering/05_Practical_Use_Cases_and_Examples.md)** |
| [06-context-optimization.md](06-context-optimization.md) | Context Optimization Strategies | 50-70 | **🔗 [RAG & Testing](prompt-engineering/)** (Modules 4.3, 7) |
| [07-rag-knowledge.md](07-rag-knowledge.md) | RAG and Knowledge Modeling | 71-85 | - |
| [08-implementation.md](08-implementation.md) | Implementation Patterns | 86-95 | - |
| [09-summary.md](09-summary.md) | Summary and Best Practices | 96-100 | **🔗 [Best Practices & Safety](prompt-engineering/)** (Modules 6, 8) |
| [10-advanced-theory.md](10-advanced-theory.md) | Advanced Theory and Core Problems | 101-120 | - |

## Usage

Each file can be used independently or combined for the full presentation. All files use the same slidev configuration and can be presented using:

```bash
npm run dev slides/[filename].md
```

## External Workshop Materials

### Learn-SK Prompt Engineering Workshop
A comprehensive 3-hour workshop with detailed techniques and enterprise focus:

📖 **[Complete Reference Guide](../LEARN_SK_REFERENCE.md)** - Detailed integration guide  
📂 **[Workshop Slides](prompt-engineering/)** - 9 modules covering all aspects of prompt engineering  
🎨 **[Supporting Assets](../styles/)** - Microsoft branding and styling

**Key External Modules:**
- Introduction & Types of Prompts (30min)
- Anatomy & Basic Techniques (30min) 
- Advanced Reasoning Techniques (45min)
- RAG & Parameter Optimization (35min)
- Practical Examples & Best Practices (50min)
- Safety, Ethics & Evaluation (40min)

## Slidev Configuration

The main configuration is maintained in the title slide (00-title.md) and can be inherited by other files.