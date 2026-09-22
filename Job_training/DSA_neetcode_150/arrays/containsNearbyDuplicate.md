# Contains Nearby Duplicate

You’re given an integer array nums.
Return true if there exists any pair of indices i != j such that:

```text 
nums[i] == nums[j]
and:
abs(i - j) <= k
Otherwise return false.
Example:
nums = [1,2,3,1]
k = 3

output = true
because the two 1s are 3 indices apart.
Another:
nums = [1,2,3,1,2,3]
k = 2

output = false
```

```cpp
nums = [1, 2, 1, 1]
k = 1
At index 2:
2 - 0 = 2 > 1
so that pair is invalid.
But then at index 3:
3 - 2 = 1
```

```cpp 

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {

        std::unordered_map<int, int>seen;

        for(int i(0); i < nums.size(); i++)
        {
            if(seen.count(nums[i])){

                int diff = i - seen[nums[i]];

                if(diff <= k) return true;

            }
            seen[nums[i]] = i;
        }

        return false;
    }
};
```

O\[n\] complexity
O\[n\] space 

