# Remove duplicates

## Active recall

- Pattern: sorted array + read/write pointer.
- `read` scans every value.
- `write` marks where the next unique value should be copied.
- Return `write`, because it is the length of the unique prefix.
- Time: O(n). Extra space: O(1).

```cpp 
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int write{1};

        for (int read{1}; read < nums.size(); read++) {
            if (nums[read] != nums[read - 1]) {
                nums[write] = nums[read];
                write++;
            }
        }

        return write;
    }
};
```
