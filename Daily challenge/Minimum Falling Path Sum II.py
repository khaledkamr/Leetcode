class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = grid[0] 

        for i in range(1, n):
            next_dp = [float('inf')] * n
            for col in range(m):
                for prev_col in range(m):
                    if prev_col != col:
                        next_dp[col] = min(next_dp[col], grid[i][col] + dp[prev_col])
            dp = next_dp
        return min(dp)