class Solution:
    def outside(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return True
        return False

    def DFS(self, grid, i, j):
        if not self.outside(grid, i, j) and grid[i][j] == '1':
            grid[i][j] = 'v'
        else:
            return

        self.DFS(grid, i - 1, j)
        self.DFS(grid, i + 1, j)
        self.DFS(grid, i, j - 1)
        self.DFS(grid, i, j + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        lands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    lands += 1
                    self.DFS(grid, i, j)
                    
        return lands