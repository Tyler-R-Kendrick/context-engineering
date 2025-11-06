---
theme: title
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

The art of crafting context for AI assistants

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<!--
Welcome everyone! Over the next few hours, we're diving into something that's becoming increasingly critical as we work with AI: **context engineering**.

Here's the reality: AI assistants like GitHub Copilot are incredibly powerful, but only as good as the instructions and context we give them. A 30% improvement in how you frame a problem can feel like a 10x improvement in the results.

By the end of today, we hope that you'll have a repeatable framework for getting consistently better results from AI - whether you're writing code, reviewing code, or building systems that leverage AI.

-->

---
layout: default
---

# Context & Prompt Engineering

> "The quality of AI assistance is directly proportional to the quality of context provided."

<v-click>

> "Prompt Engineering asks what should a user write; Context Engineering asks what should a model read."

</v-click>

<!--

You might have heard of "prompt engineering" - and yes, that's related. But there's an important distinction we're going to explore today.

**Prompt engineering** asks: "What should the *user* write to get a good result?" - with an understanding of how llms behave and reason.

**Context engineering** asks: "What should the *model* read to understand what the user actually wants?"

That might sound like the same thing, but it's a fundamental shift in perspective. And this shift changes everything about how we get the most value from tools like GitHub Copilot.

Think about it this way: You can craft the perfect prompt, but if the model doesn't have the right context - the right background information, code examples, architectural patterns - you'll still get suboptimal results. Context is the invisible foundation that makes prompts actually work.

## What We're Covering Today

We'll break this down into three main areas:

1. **The Foundations** - We'll start with prompt engineering basics and patterns you can use immediately with any AI tool.
2. **Advanced Context Strategies** - Then, we'll take a look at how to apply these patterns to the entire context (with and without user guided prompt optimizations) - and, more specifically, how they apply to the GitHub Copilot ecosystem.
3. **Applied Context Engineering** - Finally, we will build our own local environment optimized for our own developer experience.

-->