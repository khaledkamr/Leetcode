class Solution 
{
public:
    bool outside(vector<vector<char>>& grid, int i, int j)
    {
        if(i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size())
        {
            return true;
        }
        return false;
    }

    void DFS(vector<vector<char>>& grid, int i, int j)
    {
        if(!outside(grid, i, j) && grid[i][j] == '1')
        {
            grid[i][j] = 'v';
        }
        else return;

        DFS(grid, i-1, j);
        DFS(grid, i+1, j);
        DFS(grid, i, j-1);
        DFS(grid, i, j+1);
    }

    int numIslands(vector<vector<char>>& grid) 
    {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        int lands = 0;
        for(int i = 0; i < grid.size(); i++)
        {
            for(int j = 0; j < grid[0].size(); j++)
            {
                if(grid[i][j] == '1')
                {
                    lands++;
                    DFS(grid, i, j);        
                }
            }
        }
        return lands;
    }
};