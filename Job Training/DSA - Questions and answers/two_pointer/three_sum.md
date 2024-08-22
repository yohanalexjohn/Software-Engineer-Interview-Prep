# 3 sum

Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k]
== 0.

Notice that the solution set must not contain duplicate triplets.

## Example 1

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

### Explanation 1

nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0+ 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2]. Notice that the order of the
output and the order of the triplets does not matter.

## Example 2

Input: nums = [0,1,1]
Output: []

### Explanation 2

The only possible triplet does not sum up to 0.

## Example 3

Input: nums = [0,0,0]
Output: [/[0,0,0]]

### Explanation 3

The only possible triplet sums up to 0.

```python
# Brute Force
def solution(nums: List[int]) -> List[List[int]]:
    ans = []
    temp = []

    # Sort the input list
    nums.sort()

    # If the input list has no data return empty
    if nums == []:
        return ans

    # Algorithm:
    # For each increment of the number list. We use
    # two pointers start and end to check if there is
    # a valid match of the sum to get to 0
    for i in range(len(nums)):
        # if the sorted number list has no numbers in
        # the negative list then exit with an empty list
        if nums[i] > 0:
            break

        # Remove the repeated iterative index as the
        # answer will be similar to the ones before
        if (i > 0) and (nums[i - 1] == nums[i]):
            continue

        # Start and Stop pointers
        start = i + 1
        end = len(nums) - 1

        # For the value nums[i]. Find the rest of the numbers
        # by using two pointer algorithm if the sum is greater
        # than 0 reduce the end index and vice - versa.
        # Increment start and decrement end if there is a match
        while start < end:
            if (nums[i] + nums[start] + nums[end]) > 0:
                end -= 1

            elif (nums[i] + nums[start] + nums[end]) < 0:
                start += 1

            else:
                ans.append([nums[i], nums[start], nums[end]])

                start += 1
                end -= 1

                continue

    # Remove duplicate answers from the list
    # Prefer separate as the answers should be less than the
    # calculation
    for i in range(len(ans)):
        if (i > 0) and (ans[i - 1] == ans[i]):
            continue
        else:
            temp.append(ans[i])

    ans.clear()
    ans = temp.copy()

    return ans


print(solution([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
print(solution([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
print(solution([-2, 0, 0, 2, 2]))
print(solution([-1, 0, 1, 2, -1, -4]))
print(solution([0, 0, 0]))
print(solution([0, 1, 1]))
```

```python
# Similar to Brute force but cleaner
def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if a > 0:
            break

        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res
```
