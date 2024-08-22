# Max Water Container

You are given an integer array heights where heights[i] represents the height
of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of
water a container can store.

## Example 1

Input: height = [1,7,2,5,4,7,3,6]

Output: 36

## Example 2

Input: height = [2,2,2]

Output: 4

```python
# Brute force
def solution(heights: List[int]) -> int:
    volume = 0
    start = 0

    if heights == []:
        return 0

    end = len(heights) - 1

    while start < end:
        max_height = min(heights[start], heights[end])
        max_width = end - start

        volume = max(volume, max_height * max_width)

        if heights[start] < heights[end]:
            start += 1

        else:
            end -= 1

    return volume


print(solution([1, 7, 2, 5, 4, 7, 3, 6]))
print(solution([2, 2, 2]))
print(solution([]))
print(solution([0]))
```

