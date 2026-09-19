# Move Zeroes

## Active recall

- Pattern: read/write pointer.
- Algorithm: `read` scans every value; `write` marks where the next non-zero should go.
- Copy or swap non-zero values forward, then fill the rest with zero if using copy.
- Time: O(n). Space: O(1).
- Common mistake: preserving order matters; do not sort.

Given an integer array nums, move all 0s to the end while keeping the relative order of the non-zero elements.
Do it in-place.

```cpp
Example:
nums = [0,1,0,3,12]

output = [1,3,12,0,0]
```

```cpp
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int prev_index {0};

        for(int i {0}; i < nums.size(); i++)
        {
            if(nums[i] != 0){
                nums[prev_index] = nums[i];
                prev_index++;
            }
        }

        for (prev_index; prev_index < nums.size(); prev_index++)
        {
            nums[prev_index] = 0;
        }
    }
};

```
