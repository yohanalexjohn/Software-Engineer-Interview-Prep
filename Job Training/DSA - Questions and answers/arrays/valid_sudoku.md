# Valid Sudoku

You are given a  9 x 9 Sudoku board board. A Sudoku board is valid if the
following rules are followed:

1. Each row must contain the digits 1-9 without duplicates.
2. Each column must contain the digits 1-9 without duplicates.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
   without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

## Example 1

Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true

## Example 2

Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false

[!> [!NOTE]
> ] Algorithm Logic

The algorithm here is to just check if the given box is a valid box or not.

To do this just pass through and check if we have seen a repeat of the value in
the box or not.

For the sub-box the algorithm used here is to abstract out the index of the big
box to 3 big row and column boxes as in a sudoku puzzle. This sets the
mini_box_values key values and within that are able to identify what the sub
values are within that sub group and check for repeated values

```python
from typing import DefaultDict, List


def solution(board: List[List[str]]) -> bool:
    # Check for repeats by checking if the value
    # already exists in the dictionary
    row_values = DefaultDict(set)
    column_values = DefaultDict(set)
    # The mini box will have a subset of row_values
    # and column_values. We iterate through this
    # set in r // 3 and c / /3(floor division because the size
    # of the Sudoku box is 9 and equal parts is 3)
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
```
