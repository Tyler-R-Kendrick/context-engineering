# Prompty Templates

This directory contains reusable prompt templates in the `.prompty` format. These templates provide structured, repeatable ways to request specific types of assistance from AI coding assistants.

## What are Prompty Files?

Prompty files are structured prompt templates that include:
- Clear role definitions for the AI
- Parameterized inputs for customization
- Consistent formatting
- Model configuration
- Sample values for testing

## Available Templates

### 1. `code-review.prompty`
Request code reviews with specific focus areas.

**Use Case:** Get targeted code reviews for security, performance, or quality.

**Key Parameters:**
- `code`: The code to review
- `focus`: What to focus on (security, performance, etc.)
- `language`: Programming language
- `framework`: Framework being used
- `standards`: Team coding standards

**Example Usage:**
```
focus: security
language: JavaScript
framework: Express.js
code: [your code here]
```

---

### 2. `implement-function.prompty`
Request implementation of functions with complete specifications.

**Use Case:** Generate well-documented, tested function implementations.

**Key Parameters:**
- `function_name`: Name of the function
- `purpose`: What the function should do
- `input_type`: Input parameter types
- `output_type`: Return type
- `requirements`: Functional requirements
- `constraints`: Limitations or rules
- `edge_cases`: Special cases to handle

**Example Usage:**
```
function_name: validateUserInput
purpose: Validate user registration data
input_type: { email: string, password: string, age: number }
output_type: { valid: boolean, errors: string[] }
requirements: Email must be unique, password min 8 chars, age 18+
```

---

### 3. `refactor-code.prompty`
Request code refactoring with specific goals and constraints.

**Use Case:** Improve existing code while maintaining functionality.

**Key Parameters:**
- `current_code`: Code to refactor
- `goals`: What to improve
- `current_issues`: Problems to fix
- `performance_requirements`: Performance targets
- `compatibility_constraints`: What must be maintained
- `maintain_1/2/3`: Things that must not change
- `improvement_1/2/3`: Specific improvements needed

**Example Usage:**
```
goals: Improve readability, reduce complexity
current_issues: Nested callbacks, no error handling
compatibility_constraints: Must maintain existing API
```

---

### 4. `generate-tests.prompty`
Generate comprehensive test suites for functions.

**Use Case:** Create thorough test coverage for code.

**Key Parameters:**
- `function_code`: The function to test
- `test_framework`: Testing framework to use
- `coverage_requirement_1/2/3`: Coverage goals
- `edge_cases`: Edge cases to test
- `error_conditions`: Error scenarios
- `existing_patterns`: Test patterns to follow

**Example Usage:**
```
test_framework: Jest
coverage_requirement_1: 100% branch coverage
edge_cases: null, undefined, empty strings
error_conditions: network failures, invalid input
```

---

## How to Use Prompty Files

### Method 1: Manual Template Usage

1. Open the `.prompty` file
2. Read the template structure
3. Replace placeholder values with your specific needs
4. Copy the complete prompt to your AI assistant

### Method 2: With Prompty Tools (if available)

```bash
# Install prompty CLI (example)
npm install -g prompty-cli

# Run a template
prompty run code-review.prompty --code="your code" --focus="security"
```

### Method 3: In VS Code with Prompty Extension

1. Install Prompty extension for VS Code
2. Open `.prompty` file
3. Fill in parameters in the sidebar
4. Execute the prompt directly

### Method 4: Integration with Scripts

```javascript
// Example: Load and use prompty template
const fs = require('fs');
const prompty = fs.readFileSync('./prompty/code-review.prompty', 'utf8');

// Parse and fill template with your values
const filledPrompt = fillTemplate(prompty, {
  code: myCode,
  focus: 'security',
  language: 'JavaScript'
});

// Send to AI assistant
const review = await aiAssistant.complete(filledPrompt);
```

## Creating Your Own Templates

### Template Structure

```yaml
---
name: Your Template Name
description: What this template does
authors:
  - Your Name
model:
  api: chat
  configuration:
    type: azure_openai
    azure_deployment: gpt-4
sample:
  param1: example value
  param2: example value
---
system:
[System prompt defining AI's role]

user:
[User prompt with {{placeholders}} for parameters]
```

### Best Practices

1. **Clear System Role**: Define what expertise the AI should have
2. **Structured Prompts**: Organize information logically
3. **Parameterization**: Use `{{variable}}` for customizable parts
4. **Sample Values**: Include examples in the sample section
5. **Comprehensive Instructions**: Cover all requirements clearly
6. **Expected Output**: Describe what format response should have

### Example: Creating a New Template

```yaml
---
name: Database Query Optimization
description: Template for optimizing SQL queries
authors:
  - Your Team
model:
  api: chat
  configuration:
    type: azure_openai
    azure_deployment: gpt-4
sample:
  query: SELECT * FROM users WHERE status = 'active'
  database: PostgreSQL
  issues: Slow performance on large tables
---
system:
You are a database optimization expert with deep knowledge of {{database}} performance tuning.

user:
Optimize the following SQL query:

```sql
{{query}}
```

Current Issues:
{{issues}}

Database: {{database}}
Table Size: {{table_size}}
Current Execution Time: {{current_time}}
Target Execution Time: {{target_time}}

Please provide:
1. Optimized query
2. Explanation of changes
3. Index recommendations
4. Execution plan analysis
5. Additional optimization suggestions
```

## Tips for Effective Prompty Usage

### 1. Be Specific with Parameters
```yaml
# ❌ Vague
focus: make it better

# ✅ Specific  
focus: performance optimization, specifically reduce memory usage and improve loop efficiency
```

### 2. Provide Context
```yaml
# Include relevant context parameters
framework: Express.js 4.x
coding_standards: Airbnb JavaScript Style Guide
team_patterns: Use async/await, no callbacks
```

### 3. Define Success Criteria
```yaml
requirements: |
  - Function must complete in <100ms
  - Handle up to 10,000 items
  - Memory usage under 50MB
  - No external dependencies
```

### 4. Specify Constraints
```yaml
constraints: |
  - Must maintain backward compatibility
  - Cannot change public API
  - Must work with Node.js 16+
  - No breaking changes
```

## Common Use Cases

### Daily Development
- Code reviews before committing
- Function implementation with full specs
- Test generation for new features
- Refactoring legacy code

### Code Quality
- Security audits
- Performance optimization
- Code consistency improvements
- Documentation generation

### Learning & Onboarding
- Understanding unfamiliar code
- Learning best practices
- Getting implementation examples
- Code explanation requests

## Integration Examples

### With CI/CD
```yaml
# .github/workflows/code-review.yml
- name: AI Code Review
  run: |
    prompty run ./prompty/code-review.prompty \
      --code="$(git diff HEAD^)" \
      --focus="security,performance"
```

### With Git Hooks
```bash
# pre-commit hook
#!/bin/bash
prompty run ./prompty/code-review.prompty \
  --code="$(git diff --cached)" \
  --focus="code-quality"
```

### With Development Scripts
```javascript
// review-changes.js
const { execSync } = require('child_process');
const diff = execSync('git diff HEAD').toString();

const result = runPrompty('code-review.prompty', {
  code: diff,
  focus: 'all',
  standards: loadTeamStandards()
});

console.log(result);
```

## Resources

- [Prompty Format Specification](https://github.com/microsoft/prompty)
- Workshop exercises in `/workshops` directory
- Interactive notebooks in `/notebooks` directory
- Main presentation in `slides.md`

## Contributing

Have a useful template? Share it!

1. Create a new `.prompty` file
2. Follow the structure guidelines
3. Include sample values
4. Add documentation here
5. Submit a pull request

---

**Pro Tip:** Start with these templates and customize them for your team's specific needs. Save team-specific versions in your project repository!
