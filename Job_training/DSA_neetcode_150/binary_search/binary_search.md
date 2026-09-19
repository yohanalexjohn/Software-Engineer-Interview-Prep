# Binary Search

## Active recall

- Pattern: sorted input, target lookup, eliminate half.
- Use `left <= right` when `mid` is discarded after each comparison.
- Midpoint: `left + (right - left) / 2`.
- If `nums[mid] == target`, return `mid`.
- If `nums[mid] > target`, move `right = mid - 1`.
- If `nums[mid] < target`, move `left = mid + 1`.

```cpp 
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left(0);
        int right(nums.size()-1);

        while(left <= right)
        {
            int middle = left + (right - left)/2;

            if(nums[middle] == target){
                return middle;
            }

            if (nums[middle] > target)
            {
                right = middle - 1;
            }

            if ( nums[middle] < target)
            {
                left = middle + 1;
            }
        }

        return -1;
    }
};
```
