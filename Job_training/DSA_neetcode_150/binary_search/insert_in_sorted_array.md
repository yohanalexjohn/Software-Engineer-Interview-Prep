# Insert in Sorted Array

## Active recall

- Pattern: lower-bound binary search.
- Goal: return the first index where `nums[index] >= target`.
- Use `right = nums.size()` as an exclusive boundary so insertion at the end can
  return `nums.size()`.
- Time: O(log n). Space: O(1).
- Common mistake: using `right = nums.size() - 1` and `while (left < right)` can
  miss the insert-at-end case.

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

```cpp
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left{0};
        int right{static_cast<int>(nums.size())};

        while (left < right) {
            int middle = left + (right - left)/2;

            if (nums[middle] >= target) {
                right = middle;
            }
            else {
                left = middle + 1;
            }
        }

        return left;
    }
};
```
