from typing import DefaultDict, List


def solution(nums: List[int]) -> int:
    nums.sort()
    ans = []
    compare_before_delete = []
    prev = nums[0] if nums != [] else 0

    if nums != []:
        ans.append(nums[0])

    for num in nums:
        if (num - prev) == 1:
            ans.append(num)

        if len(ans) >= 2:
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
