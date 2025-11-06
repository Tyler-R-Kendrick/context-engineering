---
title: Custom Prompts
doc-type: guide
module: GitHub Copilot Context
order: 6
tags:
  - custom-prompts
  - prompt-files
  - slash-commands
  - context-engineering
  - copilot

marp: true
theme: default
paginate: true
layout: default

header: Custom Prompts for GitHub Copilot
footer: "© Context Engineering Workshop"
---

# Custom Prompts

**Custom prompts are reusable slash commands** that you create and save in your repository.

They enable **precise, repeatable assistance** tailored to your team's needs and workflows.

---

## What Are Custom Prompts?

Custom prompts are saved in your repository as **prompt files** (`.prompt.md` files).

They define **reusable slash commands** that you invoke in Copilot Chat.

### Key Characteristics

- **Reusable** - Create once, use everywhere in your team
- **Versionable** - Store in `.github/prompts/` alongside your code
- **Context-aware** - Use inputs and placeholders for dynamic behavior
- **Team-standardized** - Enforce consistent workflows and output quality

---

## How Prompt Files Work

Prompt files have a simple structure:

1. **Frontmatter** - Metadata including `mode` and `description`
2. **Prompt content** - Your instructions and any input placeholders

When saved as `filename.prompt.md`, they become slash commands: `/filename`

---

## Anatomy of a Prompt File

```markdown
---
mode: 'agent'
description: 'What this prompt does'
---

Your instructions here.

Use placeholders for dynamic inputs:
${input:variable_name:Display text for user}
```

### Frontmatter Fields

- **`mode`** - Set to `'agent'` for Copilot to process it in agent mode
- **`description`** - Shown when users discover your prompt

---

## Creating Your First Prompt File

### Step 1: Create the file structure

Save your prompt in `.github/prompts/` folder:

```
.github/
└── prompts/
    └── explain-code.prompt.md
```

### Step 2: Write the prompt file

Create a simple code explanation prompt:

```markdown
---
mode: 'agent'
description: 'Generate clear code explanations with examples'
---

Explain the following code in a beginner-friendly way:

Code to explain: ${input:code:Paste your code here}
Target audience: ${input:audience:Who is this for?}

Please provide:
* Brief overview of what the code does
* Step-by-step breakdown of main parts
* Explanation of key concepts
* Simple example showing how it works
```

### Step 3: Invoke it

In VS Code Copilot Chat, type: `/explain-code`

Copilot will prompt you for the inputs and process the code.

---

## Example: Security Code Review Prompt

Create `security-review.prompt.md`:

```markdown
---
mode: 'agent'
description: 'Comprehensive security review of code'
---

Review this code for security vulnerabilities:

Code to review: ${input:code:Paste code here}

Check for:
* Input validation and sanitization
* Authentication/authorization issues
* Sensitive data exposure
* SQL injection or similar risks
* Third-party dependency vulnerabilities
* OWASP Top 10 compliance

Report each finding with:
1. Vulnerability description
2. Risk level (Critical/High/Medium/Low)
3. Recommended fix
4. Code example of the fix
```

**Usage:** Type `/security-review` in chat

---

## Example: Documentation Generator Prompt

Create `document-api.prompt.md`:

```markdown
---
mode: 'agent'
description: 'Generate comprehensive API documentation'
---

Create documentation for this API:

API code: ${input:api:Paste API code here}
API purpose: ${input:purpose:What does this API do?}

Generate:
* Function/endpoint descriptions
* Parameter documentation with types
* Return value specifications
* Usage examples
* Error handling documentation
* Rate limits and constraints
* Markdown-formatted output
```

**Usage:** Type `/document-api` in chat

---

## Input Placeholders

Format: `${input:variable_name:Display text}`

Copilot shows the display text and stores the user's input in a variable.

### Example with Multiple Inputs

```markdown
${input:filename:What is the filename?}
${input:purpose:What should this function do?}
${input:language:Programming language?}
```

Each becomes a separate prompt for the user.

---

## Custom Prompts in This Workshop

Custom prompts demonstrate **context engineering** principles:

### Structural Context
- **Defined format** - Consistent prompt structure ensures predictable output
- **Reusable templates** - Encode team standards once

### Memory Context
- **Captured workflows** - Save proven development patterns
- **Team knowledge** - Preserve best practices as code

### Instructional Context
- **Clear directives** - Detailed instructions guide Copilot's behavior
- **Constraints and goals** - Specify exactly what you need

---

## Best Practices for Custom Prompts

### ✅ Do

- **Be specific** - Detailed instructions produce better results
- **Include examples** - Show the format you want for output
- **Version control** - Keep prompts in your repository
- **Test thoroughly** - Refine prompts based on actual results
- **Document purpose** - Add comments explaining why the prompt exists
- **Use descriptive names** - `typescript-refactor.prompt.md` vs `prompt1.prompt.md`

### ❌ Don't

- **Keep it too simple** - Vague prompts produce vague results
- **Hardcode sensitive data** - Never include credentials or secrets
- **Create duplicate prompts** - Consolidate similar workflows
- **Forget to update** - Keep prompts synchronized with your standards

---

## Combining Prompts with Other Context Tools

Custom prompts work best layered with other context engineering tools:

### Prompt + Chat Variables

```
In Copilot Chat:
/security-review

Then provide:
#selection  (includes selected code in the review)
```

### Prompt + Chat Participants

```
/security-review

Answers from:
@workspace (uses project context)
```

### Prompt + Custom Instructions

Your repository's custom instructions provide **global context**, while prompt files handle **specific tasks**.

---

## Managing Prompt Files at Scale

### Repository Structure

```
.github/
└── prompts/
    ├── code-review.prompt.md
    ├── documentation.prompt.md
    ├── security-audit.prompt.md
    ├── test-generation.prompt.md
    └── README.md  (List and document all prompts)
```

### README in .github/prompts/

```markdown
# Available Custom Prompts

## Code Review Prompts
- `/code-review` - General code quality review
- `/security-review` - Security vulnerability assessment

## Documentation Prompts
- `/document-api` - Generate API documentation
- `/explain-code` - Explain code behavior

## Development Prompts
- `/generate-tests` - Create unit test cases
- `/refactor-function` - Improve code structure
```

---

## Discovering Available Prompts

### In VS Code

1. Open Copilot Chat
2. Type `/` to see all available slash commands
3. Your custom prompts appear alongside built-in commands
4. Descriptions help you choose the right one

### Sharing with Your Team

1. Commit prompt files to your repository
2. Document them in `.github/prompts/README.md`
3. Link to them in your team's development guide
4. Include examples of when to use each

---

## Summary

Custom prompts are **your gateway to context engineering at scale**:

- **Created once** - Save as reusable slash commands
- **Invoked anywhere** - Use in any Copilot Chat session
- **Team-standardized** - Ensure consistent workflows
- **Version controlled** - Evolve with your codebase
- **Discoverable** - Easy for teammates to find and use

**Key insight**: Custom prompts transform ad-hoc instructions into **reliable, repeatable tools** that scale across your team.

---

## Next Steps

- Create your first prompt file for a common workflow
- Document prompts in `.github/prompts/README.md`
- Combine with **chat participants** (@workspace, @github) for richer context
- Use alongside **custom instructions** for global behavior guidelines
- Apply prompts in your **team's development process**

**Resources:**
- [GitHub Docs: Your first prompt file](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file)
- [VS Code: Use prompt files](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Awesome Copilot: Community prompt examples](https://github.com/github/awesome-copilot/blob/main/README.prompts.md)