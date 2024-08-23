# Trapping Rain Water

You are given an array non-negative integers heights which represent an
elevation map. Each value heights[i] represents the height of a bar, which has
a width of 1.

Return the maximum area of water that can be trapped between the bars.

## Example 1

Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9

```python
def solution(height: List[int]) -> int:
    if height == []:
        return 0

    # Two start and end pointer
    start = 0
    end = len(height) - 1

    ans = 0

    # Need to calculate max heights of the left and right locations
    # in order to determine how much water can be filled
    max_start = height[start]
    max_end = height[end]

    while start < end:
        if max_start < max_end:
            # Increment the left pointer
            # once we know what the current max left height
            # is we can subtract that from the current position
            # to determine how much water can be filled
            start += 1
            max_start = max(max_start, height[start])
            ans += max_start - height[start]
        else:
            # Same as above
            end -= 1
            max_end = max(max_end, height[end])
            ans += max_end - height[end]

    return ans


print(solution([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
```
