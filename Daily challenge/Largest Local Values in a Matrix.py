class Solution:
    def findMax(self, grid, x, y) -> int:
        maxElement = 0
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                maxElement = max(maxElement, grid[i][j])
        return maxElement

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                maxElement = self.findMax(grid, i, j)
                maxLocal[i][j] = maxElement
        return maxLocal
