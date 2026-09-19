# Max Average Sub array 1

## Active recall

- Pattern: fixed-size sliding window.
- Algorithm: sum the first `k` values, then slide by adding the new right value and subtracting the old left value.
- Track the maximum window sum, then divide by `k`.
- Time: O(n). Space: O(1).
- Common mistake: recomputing each window sum from scratch makes it O(n * k).

Given an integer array nums and an integer k, find the contiguous subarray of length exactly k with the maximum average, and return that average.

```text
Example:

nums = [1,12,-5,-6,50,3]
k = 4
Output:
12.75

because the best length-4 subarray is:
[12,-5,-6,50]

sum = 51
average = 51 / 4 = 12.75
```

```cpp 
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int currentSum{0};

        // Build the first window
        for (int i{0}; i < k; ++i) {
            currentSum += nums[i];
        }

        int maxSum{currentSum};

        // Rolling window remove old sum and add new sum
        for (int right{k}; right < nums.size(); right++) {
            currentSum += nums[right];
            currentSum -= nums[right - k];

            maxSum = std::max(maxSum, currentSum);
        }

        return static_cast<double>(maxSum) / k;
    }
};
```

Build the fixed window first and then rolling 
