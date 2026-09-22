# Longest Valid Parentheses

## Active recall

- Pattern: stack of indices.
- Push sentinel `-1` before scanning.
- Push index for `'('`.
- For `')'`, pop once.
- If the stack becomes empty, push the current index as the new invalid
  boundary.
- Otherwise, current valid length is `i - stack.top()`.
- Time: O(n). Space: O(n).
- Common mistake: storing only characters. The length calculation needs
  indices and the sentinel boundary.

```Text
You’re given a string s containing only '(' and ')'.
Return the length of the longest valid parentheses substring.

Examples:
s = "(()"
output = 2
because:
"()"
Another:
s = ")()())"
output = 4
because:
"()()"
```

```cpp 
class Solution {
public:
    int longestValidParentheses(string s) {
        std::stack<int> indices;

        // Base index before a valid substring starts
        indices.push(-1);

        int maxLength{0};

        for (int i{0}; i < s.size(); i++) {

            if (s[i] == '(') {
                indices.push(i);
            }
            else {
                indices.pop();

                // No matching '(' available
                if (indices.empty()) {
                    indices.push(i);
                }
                else {
                    maxLength = std::max(
                        maxLength,
                        i - indices.top()
                    );
                }
            }
        }

        return maxLength;
    }
};
```

s = "()"
Start:
stack = [-1]
At index 0, '(':
[-1, 0]
At index 1, ')':
pop 0
stack = [-1]
