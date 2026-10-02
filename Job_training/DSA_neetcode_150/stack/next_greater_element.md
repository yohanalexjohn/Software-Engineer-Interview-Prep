# Next Greater Element

## Prompt

For each position, return the first strictly greater value to its right; use -1 if absent. This is the non-circular, per-position version.

## Approach and invariant

- Same monotonic-stack family as [[daily_temperatures]]. Store unresolved indices.
- Stack values are non-increasing. A greater current value resolves smaller values on top.
- Compare `nums[i] > nums[waiting.top()]`; each index is pushed/popped at most once.
- Time O(n), extra space O(n).

## Common mistakes / Active recall

- Index vs value: `top()` is an index, not the value being compared.
- Output is `nums[i]`, the next greater VALUE; Daily Temperatures writes `i - index`, a DISTANCE.
- Strictly greater means `>`, not `>=`.

```cpp
#include <stack>
#include <vector>

std::vector<int> nextGreater(const std::vector<int>& nums) {
    std::vector<int> result(nums.size(), -1);
    std::stack<int> waiting;
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        // waiting.top() is an index: dereference before comparing.
        while (!waiting.empty() && nums[i] > nums[waiting.top()]) {
            int index = waiting.top();
            waiting.pop();
            result[index] = nums[i]; // VALUE, not i - index.
        }
        waiting.push(i);
    }
    return result;
}
```
