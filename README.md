# Context Engineering for GitHub Copilot

A comprehensive collection of context engineering patterns, practices, and interactive examples designed to help you master the art of working with GitHub Copilot and other AI coding assistants.

## 🎯 What is Context Engineering?

Context Engineering is the practice of structuring and organizing information to help AI assistants understand your needs and provide better results. This repository provides a complete learning path from fundamentals to advanced techniques, with a focus on **prompt engineering first, then tools**.

## 🚀 Quick Start

### View the Presentation

```bash
npm install
npm run dev
```

Then open your browser to view the Slidev presentation on context engineering.

### Explore Interactive Notebooks

Open the polyglot notebooks in VS Code with the Polyglot Notebooks extension:

1. `notebooks/01-prompt-engineering-basics.ipynb` - Core prompt engineering concepts
2. `notebooks/02-advanced-prompt-patterns.ipynb` - Advanced techniques and patterns

### Complete Workshop Exercises

Work through the progressive workshop exercises in the `workshops/` directory:

1. **Exercise 1**: Improving Vague Prompts (15 min)
2. **Exercise 2**: Context Through Comments (20 min)
3. **Exercise 3**: Test-Driven Context (25 min)
4. **Exercise 4**: Tools and Context Engineering (30 min)

See `workshops/README.md` for detailed instructions.

## 📚 Repository Structure

```
├── slides.md                    # Main Slidev presentation
├── notebooks/                   # Interactive polyglot notebooks
│   ├── 01-prompt-engineering-basics.ipynb
│   └── 02-advanced-prompt-patterns.ipynb
├── prompty/                     # Reusable prompt templates
│   ├── code-review.prompty
│   ├── implement-function.prompty
│   ├── refactor-code.prompty
│   └── generate-tests.prompty
└── workshops/                   # Hands-on exercises
    ├── README.md
    ├── exercise-01-improving-prompts.md
    ├── exercise-02-context-comments.md
    ├── exercise-03-test-driven-context.md
    └── exercise-04-tools-and-context.md
```

## 🎓 Learning Path

This repository is organized as a progressive learning experience:

### Phase 1: Prompt Engineering Fundamentals (Primary Focus)
- Understanding what makes a good prompt
- Being specific and clear
- Providing examples and context
- Specifying constraints
- Breaking down complex tasks
- Role-based prompting

**Resources:**
- Presentation slides (slides 1-25)
- Notebook: `01-prompt-engineering-basics.ipynb`
- Workshop: Exercise 1 & 2

### Phase 2: Advanced Prompt Patterns
- Contextual chaining
- Example-driven development
- Constraint specification
- Multi-language context
- Incremental refinement

**Resources:**
- Presentation slides (slides 26-40)
- Notebook: `02-advanced-prompt-patterns.ipynb`
- Workshop: Exercise 3

### Phase 3: Tools for Context Engineering (Secondary Focus)
- Type systems as context
- Documentation files
- Test-driven specifications
- Configuration files
- Pattern files

**Resources:**
- Presentation slides (slides 41-50)
- Prompty templates
- Workshop: Exercise 4

### Phase 4: Real-World Application
- Combining techniques
- Team standards
- Measuring impact
- Continuous improvement

**Resources:**
- Workshop scenarios
- Prompty templates for reuse

## 💡 Key Concepts

### Prompt Engineering Best Practices

✅ **Be Specific**: Clarity beats brevity
- Include input/output types
- Define expected behavior
- Specify constraints

✅ **Provide Examples**: Show the patterns you want
- Reference existing code
- Include test cases
- Show expected results

✅ **Use Structure**: Organize information clearly
- Type definitions
- Comments and documentation
- Consistent patterns

✅ **Iterate**: Refine based on results
- Review generated code
- Adjust prompts
- Build on successes

### Common Anti-Patterns

❌ Too vague: "Make it better"
❌ Too complex: Trying to do everything at once
❌ No context: Expecting mind reading
❌ Wrong scope: Asking for entire applications
❌ No validation: Accepting suggestions blindly

## 🛠️ Prerequisites

- **Node.js 18+** (for running Slidev presentation)
- **VS Code** (recommended editor)
- **Polyglot Notebooks Extension** (for interactive notebooks)
- **GitHub Copilot** or similar AI coding assistant (optional but recommended)
- Basic programming knowledge in any language

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Tyler-R-Kendrick/context-engineering.git
cd context-engineering

# Install dependencies
npm install

# Run the presentation
npm run dev

# Build static presentation
npm run build

# Export as PDF
npm run export
```

## 🎯 Use Cases

This material is perfect for:

- **Individual Developers**: Learn to work more effectively with AI assistants
- **Team Workshops**: Run a 90-120 minute workshop on context engineering
- **Onboarding**: Help new team members understand AI-assisted development
- **Conference Talks**: Use or adapt the presentation for speaking engagements
- **Training Programs**: Incorporate into developer training curricula

## 🤝 Contributing

Contributions are welcome! Whether it's:

- Additional workshop exercises
- New prompt patterns
- Improved examples
- Bug fixes
- Documentation improvements

Please feel free to open issues or submit pull requests.

## 📄 License

See LICENSE file for details.

## 🙏 Acknowledgments

This project draws on best practices from the AI-assisted development community and practical experience with GitHub Copilot.

## 📞 Support

- Open an issue for bugs or questions
- Check existing issues and discussions
- Share your success stories and learnings!

---

**Ready to become a context engineering expert?** Start with the presentation, work through the notebooks, complete the workshops, and apply these techniques to your daily coding!

🚀 **Happy Context Engineering!**
