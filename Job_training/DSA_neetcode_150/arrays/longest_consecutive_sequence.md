# Longest Consecutive Sequence

Given an array of integers nums, return the length of the longest consecutive
sequence of elements.

A consecutive sequence is a sequence of elements in which each element is
exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

## Example 1

Input: nums = [2,20,4,10,3,4,5]

Output: 4

Explanation: The longest consecutive sequence is [2, 3, 4, 5].

## Example 2

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7

```python

# Brute Force
def solution(nums: List[int]) -> int:
    # Sort the list first
    nums.sort()
    # A list to store the ordered Consecutive
    # numbered list
    ans = []
    compare_before_delete = []

    # Initalise the order
    # probably dont have to do any of this
    # if the list is [] just return 0
    prev = nums[0] if nums != [] else 0

    if nums != []:
        ans.append(nums[0])

    for num in nums:
        # If the difference between the order
        # is 1 then it is the next ordered number
        if (num - prev) == 1:
            ans.append(num)

        # To be used to clear and pop the first element 
        # which is a repeat
        if len(ans) >= 2:
            # Checking if the newly added difference list
            # is in order with the full sequence
            # if not delete the list but first store the 
            # copy of the current list and return 
            # the biggest length that is of order
            if (ans[len(ans) - 1] - ans[len(ans) - 2]) != 1:
                temp = ans[len(ans) - 1]
                if len(compare_before_delete) < len(ans):
                    compare_before_delete = ans.copy()
                    compare_before_delete.pop(len(compare_before_delete) - 1)
                ans.clear()
                ans.append(prev)
                ans.append(temp)

        prev = num

    return (
        len(ans)
        if len(ans) > len(compare_before_delete)
        else len(compare_before_delete)
    )


print(solution([2, 20, 4, 10, 3, 4, 5]))
print(solution([0, 3, 2, 5, 4, 6, 1, 1]))
print(solution([]))
print(solution([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
print(solution([100, 4, 200, 1, 3, 2]))
print(
    solution([4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -
             8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3])
)
```

```python
# Optimal o[n]
def solution(nums: List[int]) -> int:
    # sets will order the list for you and cannot have multiple
    # occurance
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest


print(solution([2, 20, 4, 10, 3, 4, 5]))
print(solution([0, 3, 2, 5, 4, 6, 1, 1]))
print(solution([]))
print(solution([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
print(solution([100, 4, 200, 1, 3, 2]))
print(
    solution([4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -
             8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3])
)

```

