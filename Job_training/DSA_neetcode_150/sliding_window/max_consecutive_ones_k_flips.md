# Max Consecutive Ones with at Most K Flips

## Active recall

- Pattern: variable-size sliding window with a count of the expensive value.
- Expand `right` and increment `zeroCount` when `nums[right] == 0`.
- The window is invalid only when `zeroCount > k`; exactly `k` zeroes is valid.
- While invalid, remove `nums[left]` from the count and increment `left`.
- Then update `best = max(best, right - left + 1)`.
- Time O(n), space O(1).

```cpp
int longestOnes(const std::vector<int>& nums, int k)
{
    int left = 0;
    int zeroCount = 0;
    int best = 0;

    for (int right = 0; right < static_cast<int>(nums.size()); ++right)
    {
        if (nums[right] == 0) ++zeroCount; // add right before validating

        while (zeroCount > k)             // not >= k: k flips are allowed
        {
            if (nums[left] == 0) --zeroCount;
            ++left;
        }

        best = std::max(best, right - left + 1);
    }
    return best;
}
```

Common mistake from recall: checking validity before adding the right element,
or shrinking at `zeroCount >= k` and rejecting a valid window.
