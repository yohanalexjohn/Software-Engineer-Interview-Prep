# Product of array excluding self

Given an integer array nums, return an array output where output[i] is the
product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)

O(n) time without using the division operation?

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
