# Longest Subarray Sum at Most K

## Prompt

For non-negative `nums` and `k >= 0`, return the longest contiguous subarray length with sum <= k; return 0 if no non-empty window qualifies.

## Approach

Add right, then shrink while sum > k, then maximise the valid length.

## Key invariant

After shrinking, the current sum is <= k. Non-negative values make expansion/shrinking monotonic.

## Complexity

O(n) time, O(1) extra space: each index enters and leaves once.

## Common mistakes

- Negatives invalidate this simple sliding-window argument.
- Use `max` for longest; shortest >= target uses `min` and records before shrinking a valid window.
- Keep window sum separate from the global result; exactly k is valid.

```cpp
#include <algorithm>
#include <vector>

int longestSubarraySumAtMostK(const std::vector<int>& nums, long long k)
{
    int left = 0;
    int result = 0;
    long long currentSum = 0;
    for (int right = 0; right < static_cast<int>(nums.size()); ++right) {
        currentSum += nums[right]; // add before checking validity
        while (currentSum > k) {
            currentSum -= nums[left];
            ++left;
        }
        result = std::max(result, right - left + 1);
    }
    return result;
}
```

## Active recall

Why do non-negative values make this O(n) window valid? Which boundary is invalid? Compare [[shortest_contiguous_subarray]].
