---
title: "Introduction to Prompt Engineering"
doc-type: intro
module: "01 - Prompt Engineering"
order: 1
tags:
  - prompts
  - sdk

marp: true
theme: default
paginate: true
layout: intro

header: Introduction to Prompt Engineering
footer: "© Microsoft Corporation. All rights reserved."
style: |
  @import '../styles/msft.css';

  section {
    overflow-y: scroll;
  }

---

## Summary

This module on prompt engineering is designed for developers working in enterprise environments who want to master prompt engineering for AI systems. By the end of this section, you will be able to:
- Define prompt engineering and explain its significance in enterprise AI applications.
- Identify the key components and types of prompts.
- Learn how to structure prompts for clarity, safety, and effectiveness.
- Optimize prompts using measurable rubrics - whilst explaining your approach.
- Understand how to leverage tools like Semantic Kernel, Microsoft.Extensions.AI, and Prompty for prompt development and evaluation.

Throughout the workshop, you will use Semantic Kernel and Prompty to design, test, and optimize prompts against measurable rubrics.

---

### Install the AI Toolkit VS Code Extension

To install the "[ms-windows-ai-studio.windows-ai-studio](vscode:extension/ms-windows-ai-studio.windows-ai-studio)" extension in VSCode using the CLI, follow these steps:

1. Open a terminal and run the following command to install the extension:

  ```bash
  code --install-extension ms-windows-ai-studio.windows-ai-studio
  ```

2. Ensure that the extension is successfully installed by running:

  ```bash
  code --list-extensions | grep ms-windows-ai-studio.windows-ai-studio
  ```

Alternatively, you can open this repository in a dev container and install the extension using the same command inside the container's terminal.
