# Find Minimum in Rotated Sorted Array

You’re given a sorted array that has been rotated an unknown number of times.

```c++
Example:
[3,4,5,1,2]
The minimum is:
1

Another example:
[4,5,6,7,0,1,2]

Output:
0
```

since its sorted a binary search will make it faster to extract less time than o(n)

## Active recall

- Pattern: rotated sorted array, no target.
- Compare `nums[mid]` with `nums[right]`.
- If `nums[mid] > nums[right]`, minimum is to the right, so `left = mid + 1`.
- Otherwise `mid` may be the minimum, so keep it with `right = mid`.
- Common mistake: do not use `right = mid - 1` here because `mid` might be the answer.

```cpp 
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
    
        while (left < right)
        {
            int middle = left + (right - left) / 2;

            if (nums[middle] > nums[right])
            {
                left = middle + 1;
            }
            else{
                right = middle; // not middle - 1 as middle might be the minimum
            }
        }

        return nums[left];
    }
};
```
