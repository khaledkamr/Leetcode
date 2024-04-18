class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        perimeter = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if (j > 0 and grid[i][j - 1] != 1) or j == 0:
                        perimeter += 1
                    if (i > 0 and grid[i - 1][j] != 1) or i == 0:
                        perimeter += 1
                    if (j < m - 1 and grid[i][j + 1] != 1) or j == m - 1:
                        perimeter += 1
                    if (i < n - 1 and grid[i + 1][j] != 1) or i == n - 1:
                        perimeter += 1
        return perimeter