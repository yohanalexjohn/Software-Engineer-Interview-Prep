# Flood Fill

## Prompt

Given an image, starting cell `(sr, sc)`, and `newColor`, recolour every four-directionally connected cell having the starting cell's original colour.

## Approach

Save `originalColor`. If it already equals `newColor`, return immediately. Otherwise DFS/BFS through cells with `originalColor`, recolouring as they are visited.

## Key invariant

A recoloured cell is also the visited marker, so it will not be processed again.

## Complexity

- Time: O(rows * cols) worst case.
- Space: O(rows * cols) worst case for DFS stack or BFS queue.

## Common mistakes

- Omitting the `originalColor == newColor` early return.
- Checking the cell value before checking bounds.
- Treating `0` as special instead of comparing with `originalColor`.

```cpp
void fill(vector<vector<int>>& image, int row, int col, int originalColor, int newColor)
{
    if (row < 0 || col < 0 ||
        row >= static_cast<int>(image.size()) ||
        col >= static_cast<int>(image[0].size()) ||
        image[row][col] != originalColor) return;

    image[row][col] = newColor;
    fill(image, row + 1, col, originalColor, newColor);
    fill(image, row - 1, col, originalColor, newColor);
    fill(image, row, col + 1, originalColor, newColor);
    fill(image, row, col - 1, originalColor, newColor);
}
```
