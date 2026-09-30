# Longest Subarray with Equal Zeroes and Ones

## Prompt

Given a binary array, return the longest contiguous subarray length containing equal numbers of 0 and 1.

## Approach

Treat 1 as +1 and 0 as -1. Store the first index of every prefix balance; a repeated balance gives a zero net balance between those indices.

## Key invariant

`firstSeen[balance]` always retains the earliest index, maximising the later distance. `firstSeen[0] = -1` represents the empty prefix before index 0.

## Complexity

O(n) expected time, O(n) space with a hash map.

## Common mistakes

- Do not overwrite the first index when the balance repeats.
- This map stores indices; [[../sliding_window/sub_array_sum_equals_k|Subarray Sum Equals K]] stores prefix frequencies to count matches.
- Length is `i - firstIndex`, with no extra +1.

```cpp
#include <algorithm>
#include <unordered_map>
#include <vector>

int longestEqualZeroOne(const std::vector<int>& nums)
{
    std::unordered_map<int, int> firstSeen{{0, -1}}; // empty prefix
    int balance = 0;
    int result = 0;
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        balance += nums[i] == 1 ? 1 : -1;
        auto it = firstSeen.find(balance);
        if (it != firstSeen.end())
            result = std::max(result, i - it->second);
        else
            firstSeen[balance] = i; // preserve earliest occurrence
    }
    return result;
}
```

## Active recall

Why -1 for balance zero? Why earliest index rather than frequency or latest index?
