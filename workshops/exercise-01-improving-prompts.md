# Workshop Exercise 1: Improving Vague Prompts

## Objective
Learn to transform vague prompts into specific, actionable ones that produce better results.

## Duration
15 minutes

## Instructions

For each vague prompt below, rewrite it to be specific and include:
1. Clear purpose/goal
2. Input/output specifications
3. Constraints or requirements
4. Expected behavior
5. Edge cases to handle

---

### Exercise 1.1: Basic Function

**Vague Prompt:**
```
Create a sorting function
```

**Your Improved Prompt:**
```
[Write your improved prompt here]




```

**Example Answer:**
```
Create a TypeScript function named 'sortUsers' that:
- Accepts an array of User objects (with id, name, email, createdAt properties)
- Returns a new array sorted by the 'name' property (ascending, case-insensitive)
- Handles null/undefined names by placing them at the end
- Does not mutate the original array
- Includes TypeScript type annotations
- Handles empty arrays gracefully
```

---

### Exercise 1.2: API Endpoint

**Vague Prompt:**
```
Build an API for users
```

**Your Improved Prompt:**
```
[Write your improved prompt here]




```

**Example Answer:**
```
Create a RESTful API endpoint for user management:
- Endpoint: POST /api/users
- Framework: Express.js with TypeScript
- Request body: { email: string, name: string, role: 'admin' | 'user' }
- Response: { success: boolean, user: User, message: string }
- Validation: Email must be valid format, name must be 2-50 chars
- Error handling: Return 400 for validation errors, 409 for duplicate email
- Database: Use PostgreSQL with parameterized queries
- Include middleware for request validation
- Add rate limiting (100 requests/minute)
```

---

### Exercise 1.3: Data Processing

**Vague Prompt:**
```
Process the data
```

**Your Improved Prompt:**
```
[Write your improved prompt here]




```

**Example Answer:**
```
Create a Python function to process sales data:
- Input: List of sale dictionaries with keys: date, amount, product_id, customer_id
- Output: Dictionary with daily totals, grouped by product
- Filter: Only include sales from the last 30 days
- Handle: Missing data (use 0 for amount), invalid dates (skip record)
- Performance: Must handle 100K+ records efficiently
- Return format: { 'product_id': { 'date': total_amount } }
- Use pandas for efficient processing
- Include error logging for skipped records
```

---

### Exercise 1.4: Refactoring Task

**Vague Prompt:**
```
Make this code better
```

**Your Improved Prompt:**
```
[Write your improved prompt here]




```

**Example Answer:**
```
Refactor this authentication function with these goals:
- Replace callback pattern with async/await
- Add input validation using Joi or similar
- Extract database logic to separate repository layer
- Improve error messages to be user-friendly
- Add logging for security events (failed attempts)
- Maintain backward compatibility with existing API
- Add JSDoc comments
- Follow Airbnb JavaScript style guide
- Must not change the function signature
```

---

## Self-Assessment

Rate your improved prompts on these criteria (1-5):
- [ ] Specificity: Clear and unambiguous?
- [ ] Completeness: All necessary information included?
- [ ] Constraints: Requirements and limitations defined?
- [ ] Context: Enough background provided?
- [ ] Actionable: Can be implemented directly?

## Key Takeaways

Write down 3 key learnings from this exercise:

1. ___________________________________________________________

2. ___________________________________________________________

3. ___________________________________________________________

## Next Steps

- Apply these techniques to your actual work prompts
- Compare results of vague vs. specific prompts
- Share examples with your team
- Move on to Workshop Exercise 2
