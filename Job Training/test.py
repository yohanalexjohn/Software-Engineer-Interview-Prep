from typing import List


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
        sorted(repeating_element_count.items(),
               key=lambda item: item[1], reverse=True)
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
