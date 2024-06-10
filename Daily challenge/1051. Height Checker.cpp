class Solution 
{
public:
    int heightChecker(vector<int>& heights) 
    {
        int notMatch = 0;
        vector<int> ex = heights;
        sort(heights.begin(), heights.end());
        for(int i = 0; i < heights.size(); i++)
        {
            if(heights[i] != ex[i])
            {
                notMatch++;
            }
        }
    return notMatch;
    }
};