# Max Sub Array

Given an integer array **nums**, find the contiguous subarray with the largest 
sum and return that sum

```text 
nums = [-2,1,-3,4,-1,2,1,-5,4]

Output = 6

```

```text
Use Kadanes Algorithm

At each element is it better to extend the previous subarray 
or start a new subarray from the current position 
```

```cpp 

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        //  use nums[0] in case of any negative numbers
        int currentSum (nums[0]);
        int maxSum(nums[0]);

        for (int num : nums)
        {
            currentSum = std::max(num, currentSum + num );
            maxSum = std::max(maxSum, currentSum );
        }

        return maxSum;

    }
};
```
