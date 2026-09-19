# 2 SUM

Given an array of integers, find two numbers such that they add up to a
specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2. Please note that your
returned answers (both index1 and index2) are not zero-based.

## Active recall

- Pattern: hash lookup for complement.
- Store value -> index.
- For each number, check `target - nums[i]` before inserting the current value.
- Contains Duplicate is simpler: use a set and return true when a value is seen again.
- `find()` is useful when I need the stored value. `count()` is enough for existence.

```python
def twoSum(nums, target):
    # Create a dictionary to store the number and its index
    num_dict = {}
    # Loop to get the index and the value all at one go 
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num
        # Check if the complement is already in the dictionary
        if complement in num_dict:
             # Return the indices in a 1-based manner
             return num_dict[complement] + 1, i + 1
        # Store the current number and its index in the dictionary
        num_dict[num] = i
    # If no solution is found, return None or raise an exception
    return None

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)

print(result)  # Output: (1, 2)
```

The key algorithm to remember here is `target - x` this gives the resulting
value we need to search for that exists in the dictionary.

If it doesn't we store it to the hash map or dictionary.


```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int>seen;
        
        int complement(0);

        for(int i(0); i < nums.size(); i++)
        {
            complement = target - nums[i];

            if(seen.find(complement) != seen.end())
            {
                return {seen[complement], i};
            }

            seen[nums[i]] = i;
        }
        return {};
    }
};
```

```cpp

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen;

        for(int i(0); i < nums.size(); i++)
        {
            if(seen.find(nums[i]) != seen.end())
            {
                return true;
            }
            seen.insert(nums[i]); 
        }

        return false;
    }
};
```
