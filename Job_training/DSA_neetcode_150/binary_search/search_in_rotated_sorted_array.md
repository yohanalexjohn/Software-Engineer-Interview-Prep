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
- Use inclusive boundaries: `left = 0`, `right = nums.size() - 1`,
  `while (left <= right)`.
- Check `mid` first. If found, return it.
- If `nums[left] <= nums[mid]`, the left half is sorted. Keep it only if
  `nums[left] <= target && target < nums[mid]`; otherwise discard it.
- Otherwise the right half is sorted. Keep it only if
  `nums[mid] < target && target <= nums[right]`; otherwise discard it.
- Time: O(log n). Space: O(1).
- Common mistake: do not return `-1` early before deciding which half can be
  discarded.

Recall prompt:

- Which half is sorted?
- Is the target inside that sorted half?

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

## October 1 weak point

Today's errors were mainly reversed inequalities and boundary logic. Say the range aloud before writing it: left sorted -> `nums[left] <= target && target < nums[mid]`; right sorted -> `nums[mid] < target && target <= nums[right]`. Use `left <= right` and return immediately on a match. These O(log n) rules assume distinct values; duplicates can hide which half is sorted.
