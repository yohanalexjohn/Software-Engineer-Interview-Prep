# Array Algorithms

## Slow and Fast Pointer Concept — Two Pointer Algorithm

### Core Idea
Use two indices/pointers that move through the same array at different speeds or under different conditions.

### Common Pattern

- `fast` scans through the array.
- `slow` tracks the position where useful/valid data should be placed or where a second comparison should happen.
- Often allows an in-place solution with `O(1)` extra space.

### Example — Remove Elements / Move Valid Values
```cpp
int slow = 0;

for (int fast = 0; fast < nums.size(); ++fast)
{
    if (nums[fast] meets_condition)
    {
        nums[slow] = nums[fast];
        slow++;
    }
}
```

### Recognition Clues
- Array is sorted.
- Need to modify an array in place.
- Remove/move duplicates.
- Compare elements from opposite ends.
- Need `O(1)` extra space.

### Variations

#### Same Direction
```text
slow ->
fast ---->
```

Used for:
- removing duplicates
- filtering values
- compacting arrays

#### Opposite Directions
```text
left ----> <---- right
```

Used for:
- palindrome
- 3Sum
- Container With Most Water
- sorted pair problems

### Complexity
Usually:

```text
Time:  O(n)
Space: O(1)
```

---

# Prefix / Suffix Products and Prefix Sums

## Prefix Sum

### Core Idea
Store or maintain the cumulative sum of everything before or up to the current position.

Example:

```text
nums   = [1, 2, 3, 4]

prefix = [1, 3, 6, 10]
```

So:

```text
prefix[i] = nums[0] + ... + nums[i]
```

Useful when repeatedly asking for sums over ranges.

### Range Formula

For a range:

```text
left ... right
```

the sum can be calculated using:

```text
prefix[right] - prefix[left - 1]
```

instead of summing the range again.

---

## Prefix Sum + Hash Map

Used in:

### Subarray Sum Equals K

Maintain:

```cpp
currentSum += nums[i];
```

If an earlier prefix satisfies:

```text
previousPrefix = currentSum - k
```

then:

```text
currentSum - previousPrefix = k
```

so a valid subarray exists.

Store:

```cpp
unordered_map<int, int> prefixCount;
prefixCount[0] = 1;
```

### Recognition Clues
- contiguous subarray
- need number of subarrays matching a sum
- negative numbers mean normal sliding window may not work
- repeated range-sum calculations

### Complexity

```text
Time:  O(n) average
Space: O(n)
```

---

## Prefix / Suffix Product

Used in:

### Product of Array Except Self

For every index:

```text
answer[i]
=
product of everything left of i
×
product of everything right of i
```

Example:

```text
nums = [1, 2, 3, 4]
```

Prefix products:

```text
[1, 1, 2, 6]
```

Suffix is maintained as a running variable:

```cpp
int suffix = 1;
```

Then:

```cpp
output[i] *= suffix;
suffix *= nums[i];
```

### Key Insight

The current element is naturally excluded because we only multiply:

```text
everything before it
×
everything after it
```

### Complexity

```text
Time:  O(n)
Space: O(1) extra, excluding output
```

---

# Sliding Window — Fixed Size

## Core Idea

Maintain a window of exactly `k` elements.

Instead of recalculating the whole window each time:

1. Add the new incoming element.
2. Remove the element leaving the window.

Example:

```text
[1,2,3,4,5]
window size = 3
```

Windows:

```text
[1,2,3]
  [2,3,4]
    [3,4,5]
```

### Typical Structure

```cpp
int windowSum = 0;

for (int i = 0; i < nums.size(); ++i)
{
    windowSum += nums[i];

    if (i >= k)
    {
        windowSum -= nums[i - k];
    }

    if (i >= k - 1)
    {
        // process current window
    }
}
```

### Recognition Clues
- contiguous subarray
- exact window size `k`
- maximum/minimum/average over every group of `k`
- repeated recalculation can be avoided

### Complexity

```text
Time:  O(n)
Space: O(1)
```

---

# Sliding Window — Variable Size

## Core Idea

Use:

```cpp
left
right
```

`right` expands the window.

`left` shrinks the window when some condition becomes invalid.

General structure:

```cpp
int left = 0;

for (int right = 0; right < nums.size(); ++right)
{
    // add nums[right] to window

    while (window is invalid)
    {
        // remove nums[left]
        left++;
    }

    // process valid window
}
```

---

## Example — Longest Substring Without Repeating Characters

Maintain an `unordered_set<char>` containing the current window.

```cpp
while (seen.find(s[right]) != seen.end())
{
    seen.erase(s[left]);
    left++;
}

seen.insert(s[right]);
```

Window length:

```cpp
right - left + 1
```

### Recognition Clues
- longest/shortest contiguous section
- condition must remain valid
- substring/subarray
- "without repeating"
- "at most..."
- "minimum window..."
- window can expand and shrink

### Important Complexity Point

A `for` loop containing a `while` does not automatically mean `O(n²)`.

If:

```text
right only moves forward
left only moves forward
```

each element is visited only a constant number of times.

Therefore:

```text
Time: O(n)
```

---

# Kadane's Algorithm

## Core Idea

Find the maximum-sum contiguous subarray in one pass.

At each index ask:

> Is it better to extend the previous subarray or start a new subarray here?

```cpp
currentSum = std::max(
    nums[i],
    currentSum + nums[i]
);
```

Then maintain the best result seen anywhere:

```cpp
maxSum = std::max(maxSum, currentSum);
```

### Implementation

```cpp
int currentSum = nums[0];
int maxSum = nums[0];

for (int i = 1; i < nums.size(); ++i)
{
    currentSum =
        std::max(nums[i], currentSum + nums[i]);

    maxSum =
        std::max(maxSum, currentSum);
}
```

### Meaning of Variables

```text
currentSum
=
best subarray sum ending exactly at this index

maxSum
=
best subarray sum found anywhere so far
```

### Important Edge Case

Do not initialise:

```cpp
int maxSum = 0;
```

because the array may contain only negative values.

Example:

```text
[-5,-2,-7]
```

Correct answer:

```text
-2
```

So initialise from:

```cpp
nums[0]
```

### Complexity

```text
Time:  O(n)
Space: O(1)
```

---

# Maximum Product Subarray

Similar idea to Kadane, but multiplication introduces an important difference:

> A negative minimum can become the new maximum after multiplying by another negative number.

Therefore track both:

```cpp
maxProduct
minProduct
```

At each position compare:

```cpp
current
oldMax * current
oldMin * current
```

Example:

```cpp
int oldMax = maxProduct;
int oldMin = minProduct;

maxProduct = std::max({
    nums[i],
    oldMax * nums[i],
    oldMin * nums[i]
});

minProduct = std::min({
    nums[i],
    oldMax * nums[i],
    oldMin * nums[i]
});

result = std::max(result, maxProduct);
```

### Why Compare Against `nums[i]`?

Because sometimes continuing the previous subarray is worse than starting a new subarray at the current element.

### Why Save `oldMax` / `oldMin`?

Both new values must be calculated from the previous iteration's state.

Updating one first and then using it for the other mixes old and new state.

### Complexity

```text
Time:  O(n)
Space: O(1)
```

---

# Quick Recognition Guide

```text
Sorted + pair/triplet?
→ Two pointers

Longest/shortest contiguous region with condition?
→ Sliding window

Exact window size?
→ Fixed sliding window

Range/subarray sums?
→ Prefix sum

Number of subarrays with sum K?
→ Prefix sum + hash map

Everything except current position?
→ Prefix/suffix

Maximum contiguous sum?
→ Kadane

Maximum contiguous product?
→ Track current min + max

Modify sorted array in place?
→ Slow/fast pointers

Search sorted structure faster than O(n)?
→ Binary search
```

