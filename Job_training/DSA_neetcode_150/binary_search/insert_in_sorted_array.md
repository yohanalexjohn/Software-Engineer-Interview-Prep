# Insert in Sorted Array

## Active recall

- Pattern: lower-bound binary search.
- Goal: return the first index where `nums[index] >= target`.
- Use `right = nums.size()` as an exclusive boundary so insertion at the end can
  return `nums.size()`.
- Inclusive variant: `left = 0`, `right = nums.size() - 1`,
  `while (left <= right)`, discard `mid`, and return `left` when not found.
- Time: O(log n). Space: O(1).
- Common mistake: mixing inclusive and exclusive boundaries. With inclusive
  search use `left <= right`; with exclusive search use `left < right`.

Recall prompt:

- When does `left` move?
- Why does returning `left` give the insert position?

You’re given a sorted array of integers nums and an integer target.
Return the index where target is found. If it is not found, return 
the index where it would be inserted to keep the array sorted.

```text
Example:
nums = [1,3,5,6]
target = 5

output = 2
Another:
nums = [1,3,5,6]
target = 2

output = 1
Another:
nums = [1,3,5,6]
target = 7

output = 4
```

