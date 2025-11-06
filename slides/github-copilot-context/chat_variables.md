---
title: Chat Variables
doc-type: guide
module: GitHub Copilot Context
order: 3
tags:
  - chat-variables
  - context-engineering
  - copilot

marp: true
theme: default
paginate: true
layout: default

header: Chat Variables for GitHub Copilot
footer: "© Context Engineering Workshop"
---

# Chat Variables

Chat variables are **placeholders** that reference specific context from your IDE and codebase.

You can include chat variables by typing `#` in the chat prompt box, followed by a variable name.

Chat variables automatically provide Copilot with the right context for your question.

---

## What Are Chat Variables?

Chat variables are **dynamic references** to code and project context:

- **Automatic context** - Pull specific files, selections, or project information
- **Precise targeting** - Reference exactly what you want Copilot to consider
- **Reusable** - Use the same variables across multiple prompts
- **IDE-aware** - Access information from your current editor state

---

## Built-in Chat Variables

Common chat variables available in most IDEs:

### **#file**
Reference a specific file in your project by name

```
#file:gameReducer.js
```

### **#selection**
Include the currently selected code in the editor

```
#selection
```

---

## Built-in Chat Variables (continued)

### **#editor**
Reference the active file currently open in the editor

```
#editor
```

### **#codebase**
Search your entire project for relevant code context

```
#codebase
```

### **#git**
Access git history and commit information

```
#git
```

---

## Chat Variables by IDE

Different IDEs support specific variables:

### VS Code
- `#file` - Specific file by name
- `#selection` - Selected code
- `#editor` - Active file
- `#codebase` - Full project search
- `#git` - Git history

### Visual Studio
- `#file` - Specific file
- `#solution` - Solution context

### JetBrains IDEs
- File references via **reference system**

---

## Practical Examples

### Example 1: Understanding a relationship
```
#file:gameReducer.js #file:gameInit.js how are these files related?
```

### Example 2: Debugging with context
```
#selection what's wrong with this code?
```

### Example 3: Codebase-wide search
```
#codebase how are notifications scheduled?
```

### Example 4: Git context
```
#git what changed in this recent commit?
```

---

## Applying Chat Variables in This Workshop

Chat variables demonstrate **context engineering** principles:

1. **Specificity** - Using `#file` instead of describing code manually is more precise

2. **Efficiency** - Variables automatically capture current context instead of manual copying

3. **Completeness** - Combine variables with participants (@) and custom instructions for comprehensive context

4. **Accuracy** - Reference exactly what you need, reducing ambiguity

---

## Chat Variables vs. Manual Context

### Without Variables (vague)
> "I have two files that work together, can you explain their relationship?"

### With Variables (precise)
> "#file:gameReducer.js #file:gameInit.js how are these files related?"

**Key insight**: Variables provide exact context that Copilot can reliably access.

---

## Best Practices

- **Use #selection for code snippets** - More reliable than describing code
- **Reference with #file for specific files** - Better than file paths in text
- **Combine #codebase for patterns** - Discover code patterns systematically
- **Layer variables together** - Use multiple variables for rich context: `#file:X #file:Y #selection`

---

## Summary

Chat variables are a **powerful context engineering tool**:

- Provide precise, targeted context to Copilot
- Reduce ambiguity compared to manual descriptions
- Work seamlessly with chat participants and custom instructions
- Enable systematic exploration of your codebase

**Practice**: Try using `#file` and `#selection` in your next Copilot query!
