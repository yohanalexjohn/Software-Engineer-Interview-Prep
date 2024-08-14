from typing import DefaultDict, List


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
