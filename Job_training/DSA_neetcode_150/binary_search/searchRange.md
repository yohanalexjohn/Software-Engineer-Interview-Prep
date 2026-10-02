# Search Range

You’re given a sorted array and a target value. Return the first and last position of that target.

```cpp 
nums = [5,7,7,8,8,10]
target = 8

[3,4]
```

## Active recall

- Pattern: sorted array + first/last occurrence.
- Use two biased binary searches.
- First occurrence: when target is found, save `mid` and move `right = mid - 1`.
- Last occurrence: when target is found, save `mid` and move `left = mid + 1`.
- Common mistake: do not stop at the first match; keep searching toward the biased side.

```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first{-1};
        int last{-1};

        // Find first occurrence
        int left{0};
        int right{static_cast<int>(nums.size()) - 1};

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                first = mid;
                right = mid - 1;   // keep searching left
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        // Find last occurrence
        left = 0;
        right = static_cast<int>(nums.size()) - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                last = mid;
                left = mid + 1;    // keep searching right
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        return {first, last};
    }
};
```

## Boundary discipline

- Inclusive candidate interval `[left, right]` requires `left <= right`; a single remaining element still needs checking.
- On equality, save result before biasing left (`right = mid - 1`) or right (`left = mid + 1`). Ordinary comparisons remain `nums[mid] < target` -> move left up; otherwise move right down.
- Two searches are O(log n) time, O(1) extra space. Check absent target, one element, and target repeated at either edge.
