# Number of Islands

You’re given a 2D grid of '1's (land) and '0's (water). Return the number of separate islands.
An island is formed by connecting adjacent land cells horizontally or vertically.

```cpp
Example:
grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]

Output = 3
```

```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int islands {0};

        for(int row{0}; row < grid.size(); row++){
            for(int col{0}; col < grid[row].size(); col++){

                if(grid[row][col] == "1"){
                    islands++;
                    dfs(grid, row, col); // clear the boundaries
                }

        }

        return islands;
    }

private:
    void dfs(vector<vector<char>>& grid, int row, int col)
    {
        // Check boundaries
        if (row < 0 ||
            col < 0 ||
            row >= grid.size() ||
            col >= grid[0].size())
        {
            return;
        }

        // Water or already visited
        if (grid[row][col] == '0')
        {
            return;
        }

        // Mark current land as visited
        grid[row][col] = '0';

        // Explore four neighbours
        dfs(grid, row + 1, col); // down
        dfs(grid, row - 1, col); // up
        dfs(grid, row, col + 1); // right
        dfs(grid, row, col - 1); // left
    }
};

```

```Plain text
Outer scan:
find new island

DFS:
clear/mark all horizontally + vertically connected land

Outer scan resumes:
skip all cleared cells
find next new island
```
