from typing import DefaultDict, List


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
    # Prefer seprate as the answers should be less than the
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
