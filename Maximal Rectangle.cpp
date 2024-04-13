class Solution 
{
public:
    int LargestArea(int n, vector<int>& rowHistogram)
    {
        int area = 0;
        for (int i = 0; i < n; i++) 
        {
            int breadth = 1;
            area = max(area, rowHistogram[i] * breadth);

            for (int j = i - 1; j >= 0; j--) 
            {
                if (rowHistogram[j] >= rowHistogram[i]) 
                {
                    breadth++;
                } 
                else 
                {
                    break;
                }
            }

            for (int j = i + 1; j < n; j++) 
            {
                if (rowHistogram[j] >= rowHistogram[i]) 
                {
                    breadth++;
                } 
                else 
                {
                    break;
                }
            }
            area = max(area, rowHistogram[i] * breadth);
        }
        return area;
    }
    int maximalRectangle(vector<vector<char>>& matrix) 
    {
        int area = 0;
        vector<int> rowHistogram(matrix[0].size(), 0);
        
        for(int i = 0; i < matrix.size(); i++)
        {
            for(int j = 0; j < matrix[0].size(); j++)
            {
                if(matrix[i][j] == '1')
                {
                    rowHistogram[j]++;
                }
                else
                {
                    rowHistogram[j] = 0;
                }
            }
            area = max(area, LargestArea(matrix[0].size(), rowHistogram));
        }
        return area;
    }
};
auto init = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 'c';
}();