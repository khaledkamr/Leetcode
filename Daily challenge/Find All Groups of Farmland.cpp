class Solution 
{
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) 
    {
        int rows = land.size();
        int cols = land[0].size();
        vector<vector<int>> farmlands;

        for (int i = 0; i < rows; ++i) 
        {
            for (int j = 0; j < cols; ++j) 
            {
                if (land[i][j] == 1 && 
                   (i == 0 || land[i - 1][j] == 0) && 
                   (j == 0 || land[i][j - 1] == 0)) 
                   {
                    int bottom_row = i;
                    int right_col = j;

                    while (bottom_row + 1 < rows && land[bottom_row + 1][j] == 1) 
                    {
                        bottom_row++;
                    }
                    while (right_col + 1 < cols && land[i][right_col + 1] == 1) 
                    {
                        right_col++;
                    }
                    farmlands.push_back({i, j, bottom_row, right_col});
                }
            }
        }
        return farmlands;
    }
};