# Top K Frequent Elements 

Given an integer array `nums` and an integer `k`, return _the_ `k` _most frequent elements_. You may return the answer in **any order**.

**Example 1:**

**Input:** nums = [1,1,1,2,2,3], k = 2
**Output:** [1,2]

**Example 2:**

**Input:** nums = [1], k = 1
**Output:** [1]

**Constraints:**

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Solution

```python
def solution(data: List[int], k: int) -> List[int]:
    new_element = []
    repeating_element_count = {}

    if len(data) == 1:
        new_element.append(data[0])
        return new_element

    for i in range(len(data)):
        repeating_element_count[data[i]] = (
            (repeating_element_count[data[i]] + 1)
            if data[i] in repeating_element_count.keys()
            else 1
        )

    repeating_element_count = dict(
        sorted(repeating_element_count.items(), key=lambda item: item[1], reverse=True)
    )

    new_element = list(repeating_element_count.keys())

    return (data[:k]) if not new_element else new_element[:k]


print(solution([1, 1, 1, 2, 2, 2, 3], 2))
print(solution([1], 1))
print(solution([3, 0, 1, 0], 1))
print(solution([1, 2], 2))
print(
    solution(
        [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6,
            7,
            7,
            8,
            2,
            3,
            1,
            1,
            1,
            10,
            11,
            5,
            6,
            2,
            4,
            7,
            8,
            5,
            6,
        ],
        10,
    )
)
```
