---
background: https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80
theme: default
layout: cover
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

<!-- Include all slide sections -->
<script setup>
import { ref } from 'vue'
</script>


# Context Engineering for GitHub Copilot

The art of crafting context for AI assistants

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<!--
Welcome everyone! We're diving into something that's becoming increasingly critical as we work with AI - a new emerging field called context engineering **context engineering**.

What is this and how does it apply? 
Well, AI assistants like GitHub Copilot are powerful, but only as good as the instructions and context we give them. A 30% improvement in how you frame a problem can feel like a 10x improvement in the results. Conversely, poor context framing can feel like a net negative productivity loss.

By the end of today, we hope that you'll have a repeatable framework for getting consistently better results from AI - whether you're writing code, reviewing code, or building systems that leverage AI.
-->

---
src: slides/00-title.md
---

---
src: slides/01-introduction.md
---

---
src: slides/02-problem-statement.md
---

---
src: slides/03-prompt-engineering.md
---

---
src: slides/04-implementation.md
---

---
src: slides/05-summary.md
---