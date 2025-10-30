# Workshop Exercise 3: Test-Driven Context

## Objective
Learn to use tests as context to drive better implementations and establish clear specifications.

## Duration
25 minutes

## Instructions

Write tests first to define behavior, then implement the function based on those tests.

---

### Exercise 3.1: Email Validation

**Your Task:** Write tests that define email validation behavior

```javascript
// Write your test cases here
describe('validateEmail', () => {
  // TODO: Add test cases that define:
  // - Valid email formats
  // - Invalid email formats  
  // - Edge cases
  // - Return value format
  
});

// Now implement based on tests
function validateEmail(email) {
  // Implementation guided by tests above
}
```

**Example Answer:**
```javascript
describe('validateEmail', () => {
  it('should return true for valid email addresses', () => {
    expect(validateEmail('user@example.com')).toBe(true);
    expect(validateEmail('test.user@company.co.uk')).toBe(true);
    expect(validateEmail('user+tag@domain.com')).toBe(true);
  });

  it('should return false for invalid email addresses', () => {
    expect(validateEmail('invalid')).toBe(false);
    expect(validateEmail('@example.com')).toBe(false);
    expect(validateEmail('user@')).toBe(false);
    expect(validateEmail('user @example.com')).toBe(false);
  });

  it('should handle edge cases', () => {
    expect(validateEmail('')).toBe(false);
    expect(validateEmail(null)).toBe(false);
    expect(validateEmail(undefined)).toBe(false);
  });
});

function validateEmail(email) {
  if (!email) return false;
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}
```

---

### Exercise 3.2: Shopping Cart Total

**Your Task:** Write tests for calculating shopping cart total with discounts

```python
# Write your test cases here
import pytest

# TODO: Define test cases for:
# - Basic total calculation
# - Applying percentage discounts
# - Applying fixed amount discounts
# - Handling empty cart
# - Multiple items
# - Maximum discount limits


def test_calculate_cart_total():
    # Your tests here
    pass


# Now implement based on tests
def calculate_cart_total(items, discount=None):
    """
    Calculate total price for shopping cart.
    Implementation guided by tests above.
    """
    pass
```

**Example Answer:**
```python
import pytest

def test_basic_total_calculation():
    items = [
        {'name': 'Item 1', 'price': 10.00, 'quantity': 2},
        {'name': 'Item 2', 'price': 15.00, 'quantity': 1}
    ]
    assert calculate_cart_total(items) == 35.00

def test_percentage_discount():
    items = [{'name': 'Item', 'price': 100.00, 'quantity': 1}]
    discount = {'type': 'percentage', 'value': 10}
    assert calculate_cart_total(items, discount) == 90.00

def test_fixed_discount():
    items = [{'name': 'Item', 'price': 100.00, 'quantity': 1}]
    discount = {'type': 'fixed', 'value': 15.00}
    assert calculate_cart_total(items, discount) == 85.00

def test_empty_cart():
    assert calculate_cart_total([]) == 0.00

def test_discount_cannot_exceed_total():
    items = [{'name': 'Item', 'price': 10.00, 'quantity': 1}]
    discount = {'type': 'fixed', 'value': 20.00}
    assert calculate_cart_total(items, discount) == 0.00

def calculate_cart_total(items, discount=None):
    if not items:
        return 0.00
    
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    
    if discount:
        if discount['type'] == 'percentage':
            discount_amount = subtotal * (discount['value'] / 100)
        else:  # fixed
            discount_amount = discount['value']
        
        subtotal = max(0, subtotal - discount_amount)
    
    return round(subtotal, 2)
```

---

### Exercise 3.3: Rate Limiter

**Your Task:** Write tests for a rate limiter that prevents too many requests

```typescript
// Write your test cases here
describe('RateLimiter', () => {
  // TODO: Define test cases for:
  // - Allowing requests within limit
  // - Blocking requests over limit
  // - Reset after time window
  // - Different limits per user
  // - Concurrent requests
  
});

// Now implement based on tests
class RateLimiter {
  // Implementation guided by tests above
}
```

**Example Answer:**
```typescript
describe('RateLimiter', () => {
  beforeEach(() => {
    // Reset for each test
  });

  it('should allow requests within limit', () => {
    const limiter = new RateLimiter({ max: 5, windowMs: 1000 });
    expect(limiter.tryRequest('user1')).toBe(true);
    expect(limiter.tryRequest('user1')).toBe(true);
    expect(limiter.tryRequest('user1')).toBe(true);
  });

  it('should block requests over limit', () => {
    const limiter = new RateLimiter({ max: 2, windowMs: 1000 });
    expect(limiter.tryRequest('user1')).toBe(true);
    expect(limiter.tryRequest('user1')).toBe(true);
    expect(limiter.tryRequest('user1')).toBe(false);
  });

  it('should reset after time window', async () => {
    const limiter = new RateLimiter({ max: 1, windowMs: 100 });
    expect(limiter.tryRequest('user1')).toBe(true);
    expect(limiter.tryRequest('user1')).toBe(false);
    
    await new Promise(resolve => setTimeout(resolve, 150));
    expect(limiter.tryRequest('user1')).toBe(true);
  });

  it('should track different users separately', () => {
    const limiter = new RateLimiter({ max: 1, windowMs: 1000 });
    expect(limiter.tryRequest('user1')).toBe(true);
    expect(limiter.tryRequest('user2')).toBe(true);
    expect(limiter.tryRequest('user1')).toBe(false);
  });
});

class RateLimiter {
  private requests: Map<string, number[]>;
  private max: number;
  private windowMs: number;

  constructor({ max, windowMs }: { max: number; windowMs: number }) {
    this.requests = new Map();
    this.max = max;
    this.windowMs = windowMs;
  }

  tryRequest(userId: string): boolean {
    const now = Date.now();
    const userRequests = this.requests.get(userId) || [];
    
    // Remove old requests outside window
    const validRequests = userRequests.filter(
      time => now - time < this.windowMs
    );
    
    if (validRequests.length >= this.max) {
      return false;
    }
    
    validRequests.push(now);
    this.requests.set(userId, validRequests);
    return true;
  }
}
```

---

### Exercise 3.4: Your Own Scenario

**Challenge:** Pick a function you need to implement in your project.

1. **Function Purpose:**
   ___________________________________________________________

2. **Write Tests First:**
```
[Your test code here]











```

3. **Implement Based on Tests:**
```
[Your implementation here]











```

4. **Run Tests and Iterate**

---

## Reflection Questions

1. How did writing tests first change your implementation approach?

___________________________________________________________

2. What edge cases did you discover while writing tests?

___________________________________________________________

3. Did tests help clarify ambiguous requirements?

___________________________________________________________

4. How did this compare to writing implementation first?

___________________________________________________________

---

## Test-Driven Context Best Practices

Check the practices you found valuable:

- [ ] Start with the happy path
- [ ] Add edge cases incrementally  
- [ ] Test error conditions
- [ ] Use descriptive test names
- [ ] One assertion per test (when possible)
- [ ] Test behavior, not implementation
- [ ] Include boundary value tests
- [ ] Test async behavior explicitly
- [ ] Mock external dependencies
- [ ] Other: _______________________

---

## Benefits Observed

List benefits you noticed from test-driven context:

1. ___________________________________________________________

2. ___________________________________________________________

3. ___________________________________________________________

---

## Key Takeaways

1. ___________________________________________________________

2. ___________________________________________________________

3. ___________________________________________________________

## Next Steps

- Apply TDD to your next feature
- Create test templates for common patterns
- Share successful test patterns with your team
- Move on to Workshop Exercise 4
