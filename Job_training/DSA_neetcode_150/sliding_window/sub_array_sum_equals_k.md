# Sub Array Sum Equals K

## Active recall

- Pattern: prefix sum + hash map of previous prefix counts.
- Algorithm: running sum is `prefix`. Need previous prefix `prefix - k`.
- Add `prefixCount[prefix - k]` to result, then increment `prefixCount[prefix]`.
- Start with `currentSum = 0` and `seen[0] = 1` (`seen` is named `prefixCount` below). Process from index 0; query `currentSum - k` before inserting the current prefix.
- Count exact-sum subarrays with prefix frequencies. Kadane instead maximises a subarray sum; it does not count matches.
- Time: O(n). Space: O(n).
- Common mistake: sliding window does not work with negative numbers; use prefix sums.

Given an integer array nums and an integer k, return the total number of 
continuous subarrays whose sum equals k.

```text 
nums = [1,1,1]
k = 2

Output = 2
```

```cpp 
class Solution {
public:
    // Brute force
    int subarraySum(vector<int>& nums, int k) {

        int output(0);

        // Growing sliding window
        for (int i(0); i < nums.size(); i++)
        {
            int runningSum(0);

            for(int j(i); j < nums.size(); j++)
            {
               runningSum +=  nums[j];

               if (runningSum == k)
               {
                    output++;
               }
            }
        }

        return output;
    }
};
```

```cpp 
class Solution {
public:
    // Prefix Sum 
    int subarraySum(const vector<int>& nums, int k)
    {
        std::unordered_map<int, int>prefixCount;
        int output (0);
        int currentSum (0); // empty prefix; process every element from index 0

        // Count for if the sums cancel out is still a
        // valid result hence default it to 1
        // We record one prefix sum of zero before the array begins. 
        // That allows a running sum equal to k to represent a valid 
        //  subarray starting at index 0.
        prefixCount[0] = 1;

        for(int num : nums)
        {
            currentSum += num;
            int prefixNeeded = currentSum - k; // previous prefix, not Kadane state

            if(prefixCount.find(prefixNeeded) != prefixCount.end())
            {
                output += prefixCount[prefixNeeded];
            }

            prefixCount[currentSum]++;
        }

        return output;
    }
};
```
