# Product of array excluding self

Given an integer array nums, return an array output where output[i] is the
product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)

O(n) time without using the division operation?

## Active recall

- Pattern: prefix product + suffix product.
- Do not use division.
- First pass stores product of everything to the left.
- Second pass walks right-to-left and multiplies by product of everything to the right.
- Time: O(n). Extra space: O(1) excluding output.

## Example 1

Input: nums = [1,2,4,6]

Output: [48,24,12,8]

## Example 2

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]

```python
# Brute Force
def solution(nums: List[int]) -> List[int]:
    ans: list[int] = []

    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]

        ans.append(product)

    return ans

print(solution([1, 2, 4, 6]))
print(solution([-1, 0, 1, 2, 3]))

```

```python
# Prefix array solution
def solution(nums: List[int]) -> List[int]:
    # Output create the memory and store all as 1
    res = [1] * (len(nums))

    # Prefix calculation
    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]

    postfix = 1

    # Postfix calculation 
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


print(solution([1, 2, 4, 6]))
print(solution([-1, 0, 1, 2, 3]))

```


```cpp 
class Solution {
public:
    vector<int> productExceptSelf(const vector<int>& nums) {
        vector<int> output(nums.size(), 1);

        // Calculate the prefix products
        for(int i(1); i< nums.size(); i++)
        {
            output[i] =  output[i-1] * nums[i-1];
        }

        // Calculate suffix products
        // right to left here as we got the most out of
        // bound suffix at 1
        int suffix = 1;
        for(int j = static_cast<int>(nums.size()) - 1; j >= 0; j--)
        {
            output[j] *= suffix; // use right-only product before including nums[j]
            suffix *= nums[j];
        }

        return output;
    }
};

```

Session learning: the prefix/suffix algorithm was correct; the missing function name was the mistake. Recall the full signature `vector<int> productExceptSelf(const vector<int>& nums)` and `public:` for a judge-facing `Solution` class. Prefix pass starts at 1; suffix pass starts at `n - 1`. This uses O(n) time and O(1) extra space excluding output. Assume prefix/suffix products fit the chosen integer type.
