from typing import DefaultDict, List


def solution(heights: List[int]) -> int:
    volume = 0
    start = 0
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
