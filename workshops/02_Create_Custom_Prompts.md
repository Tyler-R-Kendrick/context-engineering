# Create Custom Prompts

## Task Objective
Design reusable Copilot Chat prompts (`.prompt.md` files) that standardize how your team requests common tasks, ensuring consistent outcomes across contributors.

## Context Engineering Problems Addressed
- Drift caused by ad-hoc, one-off prompts that omit critical constraints or success criteria.
- Lost institutional knowledge when effective prompt wording lives only in past chats.
- Poor reproducibility when teams cannot reference the prompt that produced a change.
- Reusable context to be selectively included.

## How to Execute
1. **Inventory high-value workflows**: list repetitive requests such as research, planning, scaffolding, code reviews, documentation updates, migrations, or test generation.
2. **Draft prompt templates**: create `.github/prompts/<name>.prompt.md` with frontmatter (mode, description, author) and structured sections for context, instructions, tone, and success checks.
3. **Parameterize inputs**: use `${input:variable:help-text}` placeholders so teammates can supply repo-specific details without modifying the template.
4. **Embed guardrails**: note required validation, tooling commands, or reference docs the assistant must consult before responding.
5. **Version and test**: commit the prompt, trigger it via Copilot slash commands (e.g., `/review-pr`), and iterate based on the assistant’s behavior.
6. **Document usage**: link each prompt from `README.md` or `CONTRIBUTING.md` to help contributors discover and adopt it.

## Further Reading
- [Official Prompt File Reference Docs](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Prompt templates overview](../slides/github-copilot-context/custom_prompts.md)
- [Prompt engineering techniques](../slides/prompt-engineering/04_Prompt_Engineering_Techniques.md)
