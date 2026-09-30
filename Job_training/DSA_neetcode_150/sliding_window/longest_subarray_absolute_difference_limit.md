# Longest Continuous Subarray Within Absolute-Difference Limit

## Recognition clue

Need the longest window where `max(window) - min(window) <= limit`.

## Core idea

Store indices in two monotonic deques:

- `maxDeque` is decreasing by value, so its front is the window maximum.
- `minDeque` is increasing by value, so its front is the window minimum.
- Pop from each back while the new value makes that candidate useless.
- While `nums[maxDeque.front()] - nums[minDeque.front()] > limit`, move
  `left` and remove a deque front only when its index is leaving the window.

```cpp
int longestSubarray(const std::vector<int>& nums, int limit)
{
    std::deque<int> maxDeque;
    std::deque<int> minDeque;
    int left = 0;
    int best = 0;

    for (int right = 0; right < static_cast<int>(nums.size()); ++right)
    {
        while (!maxDeque.empty() && nums[maxDeque.back()] < nums[right])
            maxDeque.pop_back(); // back: discard dominated max candidates
        while (!minDeque.empty() && nums[minDeque.back()] > nums[right])
            minDeque.pop_back(); // back: discard dominated min candidates

        maxDeque.push_back(right);
        minDeque.push_back(right);

        while (static_cast<long long>(nums[maxDeque.front()]) -
               nums[minDeque.front()] > limit) // > is the invalid boundary
        {
            if (maxDeque.front() == left) maxDeque.pop_front();
            if (minDeque.front() == left) minDeque.pop_front();
            ++left;
        }
        best = std::max(best, right - left + 1);
    }
    return best;
}
```

## Recall

- Front = current answer candidate; back = maintenance/removal of dominated
  candidates.
- Store indices, not only values, so expired elements can be removed.
- Each index enters and leaves each deque at most once: O(n) time, O(n) space.

## Common mistakes from this session

- `deque` uses `front()`/`back()`, not `top()` (that belongs to a stack/heap).
- Write the comparison operator `> limit` and call `nums.size()` with parentheses.
- Declare the global result (`best` here) outside the loop; update after shrinking and return it.
- Remove a front only if `front() == left`; monotonic maintenance removes from the back.
- Input assumption: `limit >= 0`. Cast before subtracting to avoid signed overflow for extreme integer values.
