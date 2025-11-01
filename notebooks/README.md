# Interactive Notebooks

This directory contains polyglot notebooks that provide interactive, executable examples of context engineering techniques. These notebooks can be run in VS Code with the Polyglot Notebooks extension.

## 📚 Available Notebooks

### 1. Prompt Engineering Basics
**File:** `01-prompt-engineering-basics.ipynb`

**Duration:** 30-45 minutes

**Description:** Foundational concepts of prompt engineering with executable examples.

**Topics Covered:**
- Vague vs. specific prompts (with examples)
- Providing context through comments
- Using type definitions as context
- Test-driven context
- Practical exercises

**Languages Used:**
- C#
- JavaScript/TypeScript
- Python

**Key Takeaways:**
- How to write specific, actionable prompts
- The importance of context in code generation
- Using tests to define behavior
- Handling edge cases explicitly

---

### 2. Advanced Prompt Patterns
**File:** `02-advanced-prompt-patterns.ipynb`

**Duration:** 45-60 minutes

**Description:** Advanced techniques for crafting effective prompts and building context progressively.

**Topics Covered:**
- Role-based prompting (security expert, performance engineer, etc.)
- Contextual chaining (building on previous code)
- Example-driven development
- Constraint specification (what NOT to do)
- Multi-language context
- Incremental refinement

**Languages Used:**
- C#
- JavaScript/TypeScript
- Python

**Key Takeaways:**
- How to set AI perspective for specialized results
- Building complex features progressively
- Maintaining consistency across languages
- Combining multiple patterns for complex scenarios

---

## 🚀 Getting Started

### Prerequisites

1. **VS Code** - Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. **Polyglot Notebooks Extension** - Install from VS Code marketplace
   ```
   code --install-extension ms-dotnettools.dotnet-interactive-vscode
   ```
3. **.NET SDK 8.0+** - Required for polyglot notebooks runtime
   - Download from [dotnet.microsoft.com](https://dotnet.microsoft.com/download)

### Optional but Recommended

- **GitHub Copilot** - For trying techniques as you learn
- **Python 3.8+** - For Python code cells
- **Node.js 18+** - For JavaScript code cells

### Opening Notebooks

1. Open VS Code
2. Open the `context-engineering` folder
3. Navigate to `notebooks/` directory
4. Click on a `.ipynb` file
5. VS Code will open it in notebook mode
6. Select the `.NET Interactive` kernel when prompted

### Running Code Cells

- **Run Single Cell:** Click the ▶️ button on the left of the cell
- **Run All Cells:** Use the "Run All" button in the toolbar
- **Run Cell and Below:** Right-click → "Run Cell and Below"
- **Keyboard Shortcut:** `Shift+Enter` to run current cell and move to next

## 💡 How to Use These Notebooks

### Learning Mode

1. **Read Through First:** Understand concepts before running code
2. **Run Examples:** Execute cells to see results
3. **Experiment:** Modify code and re-run to explore
4. **Complete Exercises:** Fill in TODOs and test your understanding
5. **Reflect:** Consider the key takeaways

### Practice Mode

1. **Create Your Own Cells:** Add new code cells for experimentation
2. **Try Variations:** Change prompts and compare results
3. **Apply to Real Code:** Use techniques on your actual projects
4. **Document Learnings:** Add markdown cells with your insights

### Reference Mode

1. **Quick Lookup:** Find patterns you need
2. **Copy Templates:** Use examples as starting points
3. **Team Sharing:** Run through with teammates

## 🎯 Learning Path

### Recommended Order

```
1. Start with 01-prompt-engineering-basics.ipynb
   ↓
2. Complete the practice exercises in the notebook
   ↓
3. Move to 02-advanced-prompt-patterns.ipynb
   ↓
4. Try the complex scenario at the end
   ↓
5. Apply techniques to real projects
   ↓
6. Return for reference as needed
```

### Time Investment

- **First Pass:** 90-120 minutes for both notebooks
- **Practice Exercises:** 30-60 minutes additional
- **Real Project Application:** Ongoing

## 📝 Notebook Structure

Each notebook follows this pattern:

```
1. Introduction & Objectives
   ↓
2. Concept Explanation (Markdown)
   ↓
3. Code Example (Executable)
   ↓
4. Variations & Edge Cases
   ↓
5. Practice Exercise (Your Turn)
   ↓
6. Key Takeaways
```

## 🛠️ Tips for Success

### Getting the Most Out of Notebooks

✅ **Do:**
- Run every code cell to see output
- Modify examples to test understanding
- Complete all practice exercises
- Take notes in markdown cells
- Share discoveries with your team
- Return for reference

❌ **Don't:**
- Just read without running code
- Skip practice exercises
- Rush through content
- Work only in isolation
- Forget to experiment

### Troubleshooting

**Notebook won't open?**
- Ensure Polyglot Notebooks extension is installed
- Check that .NET SDK 8.0+ is installed
- Restart VS Code

**Code cell won't run?**
- Select the correct kernel (.NET Interactive)
- Check for syntax errors in the cell
- Restart the kernel: Command Palette → "Polyglot Notebook: Restart Notebook"

**Missing output?**
- Look for error messages in the cell output
- Check that previous cells have been run (some cells depend on earlier ones)
- Clear all outputs and run from top

**Python/JavaScript cells not working?**
- Ensure Python 3.8+ is installed and in PATH
- Ensure Node.js 18+ is installed
- Restart the kernel after installing language runtimes

## 🎓 Learning Objectives

By completing these notebooks, you will be able to:

### After Notebook 1 (Basics)
- [ ] Distinguish between vague and specific prompts
- [ ] Write clear, actionable prompts with complete context
- [ ] Use comments to guide code generation
- [ ] Leverage type systems for better suggestions
- [ ] Apply test-driven context techniques
- [ ] Handle edge cases explicitly

### After Notebook 2 (Advanced)
- [ ] Use role-based prompting effectively
- [ ] Build complex features through contextual chaining
- [ ] Follow example-driven development patterns
- [ ] Specify both requirements and constraints
- [ ] Maintain consistency across multiple languages
- [ ] Refine code incrementally
- [ ] Combine multiple patterns for complex scenarios

## 🔄 Extending the Notebooks

### Add Your Own Examples

```python
# Add a new code cell
# Example: Your own prompt engineering scenario
def my_custom_example():
    """
    Try your own context engineering technique here.
    Document what you're trying to achieve.
    """
    pass
```

### Create Custom Notebooks

1. Copy an existing notebook as a template
2. Modify cells to cover your specific needs
3. Add your team's patterns and examples
4. Share with colleagues

## 🤝 Contributing

Found an error or have an improvement?

1. Open an issue describing the problem/suggestion
2. Submit a pull request with fixes
3. Share additional examples that helped you

## 📚 Additional Resources

### Related Materials
- **Workshops:** `/workshops` directory for hands-on exercises
- **Prompty Templates:** `/prompty` directory for reusable prompts
- **Presentation:** `slides.md` for teaching concepts

### External Resources
- [Polyglot Notebooks Documentation](https://github.com/dotnet/interactive)
- [VS Code Notebook Documentation](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)

## 💬 Feedback

- What examples were most helpful?
- What concepts need more explanation?
- What additional patterns should be covered?

Share your feedback through issues or pull requests!

---

**Ready to dive in?** Open `01-prompt-engineering-basics.ipynb` and start your context engineering journey! 🚀
