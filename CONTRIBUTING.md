# Contributing to Context Engineering

Thank you for your interest in contributing! This guide will help you get started.

## 🎯 Ways to Contribute

### 1. Report Issues
- Found a bug in an example?
- Unclear instructions?
- Broken links or formatting?

**Open an issue** with details about what's wrong and how to reproduce it.

### 2. Improve Documentation
- Fix typos or grammar
- Add clarifying examples
- Improve explanations
- Add translations

### 3. Add Examples
- New prompt patterns
- Additional workshop exercises
- More prompty templates
- Real-world case studies

### 4. Enhance Notebooks
- Additional code examples
- More language variations
- Practice exercises
- Interactive demonstrations

### 5. Share Experiences
- Success stories
- Lessons learned
- Team adoption strategies
- Measurement results

---

## 🚀 Getting Started

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/Tyler-R-Kendrick/context-engineering.git
cd context-engineering

# Install dependencies
npm install

# Test the presentation
npm run dev

# Install notebook requirements
# - VS Code
# - Polyglot Notebooks extension
# - .NET SDK 8.0+
```

### Making Changes

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a branch** for your changes
   ```bash
   git checkout -b feature/my-improvement
   ```
4. **Make your changes**
5. **Test your changes** (run presentation, validate notebooks)
6. **Commit with clear messages**
   ```bash
   git commit -m "Add example for role-based prompting"
   ```
7. **Push to your fork**
   ```bash
   git push origin feature/my-improvement
   ```
8. **Open a Pull Request**

---

## 📝 Contribution Guidelines

### Content Standards

#### Markdown Files
- Use clear, concise language
- Include code examples where relevant
- Add time estimates for exercises
- Provide learning objectives
- Include reflection questions

#### Code Examples
- Test all code examples
- Include comments explaining key concepts
- Show both before and after states
- Handle edge cases
- Follow language best practices

#### Prompty Templates
- Include complete metadata
- Provide sample values
- Add usage instructions
- Explain parameters clearly
- Show expected output format

#### Notebooks
- Use descriptive cell names
- Include markdown explanations
- Test all executable cells
- Provide practice exercises
- Add key takeaways

### Style Guide

#### Writing Style
- Use second person ("you") for instructions
- Active voice preferred
- Short paragraphs and sentences
- Bullet points for lists
- Clear headings and subheadings

#### Code Style
- Follow language-specific conventions
- Use meaningful variable names
- Add inline comments for complex logic
- Include error handling
- Show best practices

#### Formatting
- Use proper markdown syntax
- Include syntax highlighting for code blocks
- Add emojis for visual interest (but don't overdo it)
- Use tables for comparisons
- Include screenshots where helpful

### Example Structure

```markdown
# Title

Brief introduction explaining what this covers.

## Learning Objectives
- Objective 1
- Objective 2

## Concept Explanation

Clear explanation of the concept.

### Example

\`\`\`javascript
// Code example with comments
function example() {
  // Clear, working code
}
\`\`\`

## Practice Exercise

Your turn to try this concept!

## Key Takeaways

1. Key point 1
2. Key point 2

## Next Steps

What to do next.
```

---

## 🎯 Types of Contributions

### 🐛 Bug Fixes

**Examples:**
- Broken code examples
- Incorrect instructions
- Typos or formatting issues

**Process:**
1. Open issue describing the bug
2. Create branch: `fix/bug-description`
3. Fix the issue
4. Test thoroughly
5. Submit PR referencing issue

### ✨ New Features

**Examples:**
- New workshop exercises
- Additional prompt templates
- Extra notebook sections

**Process:**
1. Open issue proposing the feature
2. Discuss approach with maintainers
3. Create branch: `feature/feature-name`
4. Implement feature
5. Add documentation
6. Submit PR

### 📚 Documentation

**Examples:**
- Improved READMEs
- Better examples
- Clarified instructions

**Process:**
1. Create branch: `docs/what-youre-documenting`
2. Make improvements
3. Submit PR

### 🎨 Polish

**Examples:**
- Better slide layouts
- Improved notebook formatting
- Enhanced code examples

**Process:**
1. Create branch: `polish/area-of-improvement`
2. Make refinements
3. Submit PR

---

## ✅ Pull Request Checklist

Before submitting a PR, ensure:

- [ ] Code examples work and are tested
- [ ] New files have appropriate READMEs
- [ ] Markdown is properly formatted
- [ ] Links are valid
- [ ] Slides build successfully (`npm run build`)
- [ ] Notebooks open and run in VS Code
- [ ] Changes are documented
- [ ] Commit messages are clear
- [ ] Branch is up to date with main

---

## 🔍 Review Process

1. **Automated Checks**: Basic validation
2. **Maintainer Review**: Content and quality check
3. **Feedback**: May request changes
4. **Approval**: Once ready, PR is merged
5. **Recognition**: Contributors are acknowledged

---

## 🏆 Recognition

Contributors will be:
- Listed in PR acknowledgments
- Mentioned in release notes
- Added to contributors list (if desired)

---

## 💡 Ideas for Contributions

### Quick Wins (30 minutes or less)
- Fix typos in documentation
- Add code comments
- Improve example clarity
- Fix broken links

### Medium Projects (2-4 hours)
- Create new workshop exercise
- Add prompty template
- Enhance existing notebook
- Write blog post about usage

### Large Projects (8+ hours)
- New notebook topic
- Video tutorial series
- Translation to another language
- Additional presentation track

---

## 📋 Commit Message Format

Use clear, descriptive commit messages:

```
Add example for test-driven context in Python

- Added new code cells with pytest examples
- Included edge case handling
- Updated notebook README
```

**Format:**
```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

---

## 🤔 Questions?

- **General questions**: Open a discussion
- **Bug reports**: Open an issue
- **Feature ideas**: Open an issue for discussion first
- **Quick questions**: Comment on relevant issue/PR

---

## 📜 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information
- Other unprofessional conduct

### Enforcement

Violations may result in:
1. Warning
2. Temporary ban
3. Permanent ban

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project (see LICENSE file).

---

## 🙏 Thank You!

Every contribution, no matter how small, helps make this resource better for everyone. Thank you for taking the time to contribute!

---

**Ready to contribute?** Pick an area from the ideas above and get started! 🚀
