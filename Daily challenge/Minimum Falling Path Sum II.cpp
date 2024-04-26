class Solution 
{
public:
    int minFallingPathSum(vector<vector<int>>& grid) 
    {
        int n = grid.size();
        int m = grid[0].size();
        vector<int> dp = grid[0];

        for(int i = 1; i < n; i++)
        {
            vector<int> next_dp(m, INT_MAX);
            for(int j = 0; j < m; j++)
            {
                for(int prev = 0; prev < m; prev++)
                {
                    if(prev != j)
                    {
                        next_dp[j] = min(next_dp[j], grid[i][j] + dp[prev]);
                    }
                }
            }
            dp = next_dp;
        }
        return *min_element(dp.begin(), dp.end());
    }
};