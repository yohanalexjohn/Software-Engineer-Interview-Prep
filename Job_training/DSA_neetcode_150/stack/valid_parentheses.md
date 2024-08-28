# Valid Parentheses

You are given a string s consisting of the following characters: `'('`, `')'`, `'{'`,
`'}'`, `'['` and `']'`.

The input string s is valid if and only if:

- Every open bracket is closed by the same type of close bracket.
- Open brackets are closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

## Example 1

```text
Input: s = "[]"

Output: true

```

## Example 2

```text

Input: s = "([{}])"

Output: true

```

## Example 3

```text
Input: s = "[(])"

Output: false
```

## Solution

```python
def solution(s: str) -> bool:
    # Map the closing brackets to the opening
    # use closing instead of opening to determine
    # when to pop
    bracket_map = {"}": "{", ")": "(", "]": "["}

    stack = []

    for bracket in s:
        if bracket in bracket_map:
            top_element = stack.pop() if stack else "#"

            # If the bracket is a closing bracket and
            # if the popped element does not match the
            # opening of the bracket it is not the top_element
            # that should have popped
            if bracket_map[bracket] != top_element:
                return False

        else:
            # Append the opening bracket to the top of the
            # stack
            stack.append(bracket)

    return not stack


print(solution("[]"))
print(solution("([{}])"))
print(solution("["))
print(solution("[(])"))
print(solution("{[]}"))
```
