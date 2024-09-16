## Logical Operators in Python

You can combine different conditions using logical operators.

- `A and B` Both conditions need to be true
- `C or D`  Only one condition needs to be true
- `not E`  The condition must be false

## Exercise

Update the code so that people age 45 to 55 (inclusive of both ages) ride for free. Use logical operators to check that the age is greater than or equal to 45, and it's also less than or equal to 55.

```python
age = int(input("Enter your age: "))

if age >= 45 and age <= 55:
    print("You ride for free!")
else:
    print("You need to pay for the ride.")
```
**Note:** 

The warning for simplification is just a suggestion. You can consider it and choose to simplify, or you can ignore it. In this lesson, I wanted to show you the `and`, `or`, and `not` logical operators. So I recommend keeping the original code in case you come back to this lesson for review.
