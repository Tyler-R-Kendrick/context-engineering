# Workshop Exercise 2: Context Through Comments

## Objective
Learn to use comments effectively to provide context for GitHub Copilot and improve code generation quality.

## Duration
20 minutes

## Instructions

For each scenario, write contextual comments that will guide Copilot to generate the right implementation.

---

### Exercise 2.1: Authentication Function

**Scenario:** You need to implement a secure login function.

**Your Contextual Comments:**
```javascript
// [Write your comments here to guide implementation]






function authenticateUser(username, password) {
  // Implementation will be generated based on your comments
}
```

**Example Answer:**
```javascript
// User authentication function
// Requirements:
// - Validate input (username and password are not empty)
// - Query database using parameterized queries to prevent SQL injection
// - Compare password using bcrypt.compare() for timing-attack resistance
// - Return JWT token on success with 24-hour expiration
// - Return error object on failure: { success: false, message: string }
// - Log failed login attempts for security monitoring
// - Implement rate limiting check (max 5 attempts per 15 minutes)
// Dependencies: bcrypt, jsonwebtoken, database connection pool

async function authenticateUser(username, password) {
  // Implementation
}
```

---

### Exercise 2.2: Data Transformation

**Scenario:** Transform API response to frontend format.

**Your Contextual Comments:**
```python
# [Write your comments here to guide implementation]






def transform_user_response(api_data):
    # Implementation will be generated based on your comments
    pass
```

**Example Answer:**
```python
# Transform API response from backend format to frontend format
# Input: Dictionary from API with snake_case keys
#   {
#     'user_id': int,
#     'first_name': str,
#     'last_name': str,
#     'email_address': str,
#     'created_at': str (ISO format),
#     'is_active': bool
#   }
# Output: Dictionary with camelCase keys for frontend
#   {
#     'userId': int,
#     'fullName': str (combined first and last),
#     'email': str,
#     'createdAt': str (formatted as 'MMM DD, YYYY'),
#     'status': str ('active' or 'inactive')
#   }
# Handle: Missing fields (use empty string), invalid dates (use 'Unknown')
# No external libraries - use standard library only

def transform_user_response(api_data):
    # Implementation
    pass
```

---

### Exercise 2.3: Caching Layer

**Scenario:** Implement a caching mechanism with TTL.

**Your Contextual Comments:**
```typescript
// [Write your comments here to guide implementation]






class CacheManager {
  // Implementation will be generated based on your comments
}
```

**Example Answer:**
```typescript
// Redis-based cache manager with TTL support
// Features:
// - Store/retrieve key-value pairs with automatic expiration
// - TTL (Time To Live) configurable per key
// - Handle Redis connection errors gracefully (fallback to direct DB query)
// - Support serialization of objects to JSON
// - Implement cache warming for frequently accessed keys
// Methods needed:
// - get(key): Promise<any | null> - Returns null if expired or not found
// - set(key, value, ttlSeconds): Promise<void> - Store with TTL
// - delete(key): Promise<void> - Manual invalidation
// - clear(): Promise<void> - Clear all keys
// Configuration:
// - Redis host/port from environment variables
// - Default TTL: 300 seconds (5 minutes)
// - Max retry attempts: 3
// Error handling:
// - Log errors but don't throw (fail gracefully)
// - Return null on cache miss or error

class CacheManager {
  // Implementation
}
```

---

### Exercise 2.4: Validation Pipeline

**Scenario:** Create a validation pipeline for form data.

**Your Contextual Comments:**
```javascript
// [Write your comments here to guide implementation]






class ValidationPipeline {
  // Implementation will be generated based on your comments
}
```

**Example Answer:**
```javascript
// Composable validation pipeline for form data
// Pattern: Chain validators that each return { valid: boolean, errors: string[] }
// Usage:
//   const pipeline = new ValidationPipeline()
//     .addValidator(validateEmail)
//     .addValidator(validatePassword)
//     .run(formData);
// Features:
// - Support async validators (e.g., checking email uniqueness in DB)
// - Stop on first failure or collect all errors (configurable)
// - Custom error messages per validator
// - Support field-level and form-level validation
// Built-in validators to implement:
// - required(field): Check field exists and not empty
// - minLength(field, length): String minimum length
// - maxLength(field, length): String maximum length
// - pattern(field, regex): Match regex pattern
// - custom(field, fn): Custom validation function
// Return format:
//   { valid: boolean, errors: { field: string[] }, values: object }

class ValidationPipeline {
  // Implementation
}
```

---

## Practice Activity

Now try this with your own code:

1. Take a function you need to implement
2. Write detailed contextual comments first
3. Let Copilot generate the implementation
4. Review and refine
5. Compare with what you would have written without the comments

---

## Reflection Questions

1. How did detailed comments change the quality of generated code?

___________________________________________________________

2. What level of detail works best? Too much? Too little?

___________________________________________________________

3. What types of context are most valuable to include?

___________________________________________________________

4. Did you discover any patterns in effective comments?

___________________________________________________________

---

## Best Practices Discovered

List techniques that worked well:

- [ ] Specify input/output formats explicitly
- [ ] Mention error handling requirements
- [ ] Reference existing patterns in codebase
- [ ] Include performance constraints
- [ ] Specify dependencies to use (or avoid)
- [ ] List edge cases to handle
- [ ] Define return types clearly
- [ ] Other: _______________________

---

## Key Takeaways

1. ___________________________________________________________

2. ___________________________________________________________

3. ___________________________________________________________

## Next Steps

- Apply this technique to your next feature
- Create a template for common scenarios
- Move on to Workshop Exercise 3
