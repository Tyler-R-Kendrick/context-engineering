---
title: "Anatomy of an Effective Prompt"
doc-type: content
module: "01 - Prompt Engineering"
order: 3
tags:
  - prompts
  - sdk

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

<!-- _class: 'title-slide' -->
<!-- _paginate: skip -->

# Anatomy of an Effective Prompt

## Prerequisites
- Complete the Types of Prompts module.

## Learning Objectives
- Describe required and optional components of an effective prompt.

---

## Key Concepts
- Core Task
- System Instructions
- Examples
- Contextual Information

Effective prompts are structured with deliberate components that enhance clarity, ensure context, and guide the language model toward the desired response. Below is a breakdown of the key elements:

<!--
Speaker Notes:
Think of a prompt like a well-written specification. It has required elements and optional elements that make it more robust.

This slide is the most important conceptual framework in the entire workshop. If people remember nothing else, they should remember: Core Task + System Instructions + Examples.

Analogy: "If the model is a waiter at a restaurant, the Core Task is your order, System Instructions set the tone of service, Examples show them how you want it presented."
-->



---

### Core Task (Required)
The core task is the critical anchor of any prompt and must be both clear and specific. This involves:

- Clearly defined instructions or questions
- Eliminating ambiguity by stating exactly what needs to be accomplished
- Using direct language to focus the model's attention

**Example:**

> Summarize the main points from the following article.

<!--
Speaker Notes:
This is the foundation. Everything else supports this.
Without a clear core task, all the other components don't matter.
Pro tip: If you're struggling to define your core task, you're not ready to ask the model yet. Step back and think about what you really need.
-->

---

### System Instructions
Use this section to:

- Define the style, tone, or persona (e.g., "Respond as a technical expert")
- Impose constraints (e.g., "Limit your answer to three sentences" or "Avoid jargon")
- Clarify the expected format of output

**Example:**

> You are a friendly customer support agent. Answer in a helpful and concise manner.

<!--
Speaker Notes:
System instructions are like setting up the environment before the work begins.
They're optional, but they often dramatically improve results.
Use them when you want consistency in style or tone.
Real-world example: "You are a code reviewer focused on performance and security. Review this code and highlight any issues."
-->

---

### Examples
Demonstrate desired input-output relationships with examples to:

- Set expectations for style, structure, or reasoning
- Clarify edge cases or ambiguous requests

**Format:**

```
Input: [Sample input]
Output: [Expected output]
```

**Example:**

```
Input: What is the capital of France?
Output: Paris
```

---

### Contextual Information
Provide relevant background or reference data, such as:

- Definitions, reference documents, or data tables
- Context that grounds the response or clarifies assumptions

**Example:**

> Based on the attached project brief document, summarize the deliverables.

---

## Roles in Prompting
Understand the distinct responsibilities in prompt-driven workflows:

- **User:** Initiates the request, specifying tasks and providing necessary background or constraints.
- **Tool:** (If present) Applies prioritized instructions, policies, or constraints, often before passing to the assistant.
- **Assistant:** Generates the response, following the instructions, adapting to examples provided, and respecting any constraints.

---

## Tips

- Be explicit with required tasks.
- Layer optional components for increased accuracy.
- Use examples to reduce ambiguity.
- Specify roles and expectations as needed.
