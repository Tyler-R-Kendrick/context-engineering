---
title: "Types of Prompts"
doc-type: content
module: "01 - Prompt Engineering"
order: 2
tags:
  - prompts

marp: true
theme: default
paginate: true

header: Introduction to Prompt Engineering
footer: "© Microsoft Corporation. All rights reserved."
style: |
  @import '../styles/msft.css';

  section {
    overflow-y: scroll;
  }

---

## In-Context Learning Techniques

* Zero-shot
* Few-shot
* Multi-shot

--- 

### Zero-shot (Direct)

**Definition:** Provide the AI with a direct instruction—no examples are given.  
**Purpose:** Test the AI’s general capability to follow instructions.  
**Example:**
> Translate the following sentence to French: "Where is the library?"

**Use when:** You want a quick, straightforward answer or to test the model’s basic abilities.

--- 

### Few-shot and Multi-shot
**Definition:** Add one (few-shot) or several (multi-shot) examples in your prompt to guide the AI’s response.  
**Purpose:** Demonstrate the desired format, style, or logic with concrete examples.

**Few-shot Example:**
```
Q: What is the capital of France?
A: Paris
Q: What is the capital of Italy?
A: Rome
Q: What is the capital of Germany?
A:
```

**Multi-shot Example:** (More than two examples)
```
Translate the following:
English: Hello | French: Bonjour
English: Good morning | French: Bonjour
English: Good night | French:
```

**Use when:** The task requires specific output style or handling uncommon instructions.
