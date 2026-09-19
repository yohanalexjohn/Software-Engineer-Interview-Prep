# Maximum Product Sub Array

Given an integer array nums, find a contiguous non-empty subarray that has the 
largest product, and return the product.

```text
nums = [2,3,-2,4]
Output = 6

because [2,3] has product 6 

nums = [-2,0,-1]
Output = 0
```

## Active recall

- Pattern: Kadane-style running state, but track both max and min product.
- Negative values can flip min into max.
- Save `oldMin` and `oldMax` before updating either value.
- Compare against the current number so the subarray can restart.
- Time: O(n). Space: O(1).

```cpp 
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // To store the mini and max product 
        // so far allows us to determine the best 
        // result in a single pass
        int minProduct {nums[0]};
        int maxProduct {nums[0]};
        int result {nums[0]};

        for(int i(1); i < nums.size(); i++)
        {
            int oldMin = minProduct;
            int oldMax = maxProduct;

            minProduct = std::min({
                    nums[i], 
                    oldMin * nums[i],
                    oldMax * nums[i]
                });

            maxProduct = std::max({
                    nums[i], 
                    oldMin * nums[i],
                    oldMax * nums[i]
                });

            result = std::max(result, maxProduct);
        }

        return result;
    }
};
```

```text
things to remeber
algorithm , compares against the candidate products
against current position
current
oldMax * current
oldMin * current
```
