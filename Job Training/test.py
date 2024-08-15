from typing import DefaultDict, List


def solution(board: List[List[str]]) -> bool:
    # Check for repeats by checking if the value
    # already exists in the dictionary
    row_values = DefaultDict(set)
    column_values = DefaultDict(set)
    # The mini box will have a subset of row_values
    # and column_values. We iterate through this
    # set in r // 3 and c / /3(floor division because the size
    # of the boz is 9 and equal parts is 3)
    mini_box_values = DefaultDict(set)

    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == ".":
                continue

            if (
                board[row][column] in row_values[row]
                or board[row][column] in column_values[column]
                or board[row][column] in mini_box_values[(row // 3), (column // 3)]
            ):
                return False

            column_values[column].add(board[row][column])
            row_values[row].add(board[row][column])
            mini_box_values[((row // 3), (column // 3))
                            ].add(board[row][column])

    return True


print(
    solution(
        [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)

print(
    solution(
        [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "1", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
