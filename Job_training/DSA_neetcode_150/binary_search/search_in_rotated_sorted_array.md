# Search in Rotated Sorted Array

Given a rotated sorted array nums with unique values and an integer target,
return the index of target. If it is not present, return -1.

```cpp 
nums = [4,5,6,7,0,1,2]
target = 0

Output = 4

nums = [4,5,6,7,0,1,2]
target = 3

Output = -1
```

## Active recall

- Pattern: rotated sorted array still has one sorted half.
- Check `mid` first.
- If left half is sorted, decide whether target lies inside `[nums[left], nums[mid])`.
- Otherwise the right half is sorted, decide whether target lies inside `(nums[mid], nums[right]]`.
- Common mistake: do not return `-1` early before deciding which half can be discarded.

```cpp 
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left (0);
        int right (nums.size() -1);

        while (left <= right){
            int middle = left + (right - left)/2;

            if (nums[middle] == target){
                return middle;
            }

            // Left is sorted
            if(nums[left] <= nums[middle]){

                if((nums[left] <= target) &&
                    (target < nums[middle])){
                    right = middle - 1;
                }
                else{
                    left = middle + 1;
                }
            }
            // right is sorted
            else{
                if((nums[right] >= target) && 
                   (target > nums[middle])){
                    left = middle + 1;
                }
                else{
                    right = middle - 1;
                }
            }
        }

        return -1;
    }
};
```
