# Two sum input array is sorted

Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they
add up to a given target number target and index1 < index2. Note that index1
and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

## Example 1

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]

Explanation: The sum of 1 and 2 is 3. Since we are assuming a
1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

```python
from typing import DefaultDict, List


def solution(numbers: List[int], target: int) -> List[int]:
    """
    The algorithm behind this is using the two pointer we 
    can traverse through the entire list in one go with 
    a single sweep

    To do this if the added sum of the indexes in start 
    and end is greater than the target we just have to 
    reduce the end index to reduce the sum

    If the added sum now or before was lesser than the 
    target we can increase the start index which has the 
    lease value by one to add the sum and return its indexes
    """
    start: int = 0
    end: int = len(numbers) - 1

    while start < end:
        if (numbers[start] + numbers[end]) < target:
            start += 1

        elif (numbers[start] + numbers[end]) > target:
            end -= 1

        else:
            return list([start + 1, end + 1])

    return [0]


print(solution([1, 2, 3, 4], 3))
```
