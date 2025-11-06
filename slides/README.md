# Context Engineering Slides

This folder contains the presentation slides for "Context Engineering for GitHub Copilot" broken down into manageable sections.

## Slide Organization

| File | Content | Slides | External References |
|------|---------|--------|-------------------|
| [00-title.md](00-title.md) | Title and introduction | 1-2 | - |
| [01-problem-statement.md](01-problem-statement.md) | Problem statement & core failure modes (lead section) | 3-22 | - |
| [02-introduction.md](02-introduction.md) | What is Context Engineering | 23-32 | - |
| [03-prompt-engineering.md](03-prompt-engineering.md) | Prompt Engineering Fundamentals | 33-75 | **🔗 [Workshop](prompt-engineering/)** (9 modules, 3hrs) |
| [04-implementation.md](04-implementation.md) | Implementation Patterns | 76-100 | - |
| [05-summary.md](05-summary.md) | Summary and Best Practices | 101-120 | **🔗 [Best Practices & Safety](prompt-engineering/)** (Modules 6, 8) |

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