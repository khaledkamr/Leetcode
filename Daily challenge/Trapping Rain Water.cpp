class Solution 
{
public:
    int trap(vector<int>& height) 
    {
        int n = height.size();
        int left = height[0], right = height[n - 1];
        int res = 0;
        for(int i = 0, j = n - 1; i < j;)
        {
            if(left <= right)
            {
                res += left - height[i];
                i++;
                left = max(left, height[i]);
            }
            else
            {
                res += right - height[j];
                j--;
                right = max(right, height[j]);
            }
        }
        return res;
    }
};