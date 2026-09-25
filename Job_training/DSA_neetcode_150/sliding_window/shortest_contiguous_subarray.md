# Shortest Contiguous Sub array

## Active recall

- Pattern: variable-size sliding window over positive integers.
- Algorithm: expand `right`, add to `currentSum`, then while
  `currentSum >= target`, record the shortest length and shrink from `left`.
- Sentinel: initialise `minLength = nums.size() + 1`; return `0` if unchanged.
- Time: O(n). Space: O(1).
- Common mistake: this relies on positive values. With negatives, shrinking
  no longer has monotonic behaviour.

Recall prompt:

- Why can I shrink while the sum is still valid?
- What does the sentinel prove at the end?

You’re given an array of integers nums.
Return the length of the shortest contiguous subarray whose sum is at least target.
If none exists, return 0.

```text
Example:
nums = [2,3,1,2,4,3]
target = 7

output = 2
because:
[4,3]
has sum 7.
```

```cpp 
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left{0};
        int currentSum{0};

        // Record to Max First
        int minLength{static_cast<int>(nums.size()) + 1};

        for (int right{0}; right < nums.size(); right++) {

            // Grow window
            currentSum += nums[right];

            // Shrink while window is still valid
            while (currentSum >= target) {

                minLength = std::min(
                    minLength,
                    right - left + 1
                );

                currentSum -= nums[left];
                left++;
            }
        }

        return minLength == nums.size() + 1
            ? 0
            : minLength;
    }
};
```
