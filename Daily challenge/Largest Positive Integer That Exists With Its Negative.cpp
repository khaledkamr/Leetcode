class Solution {
public:
    int findMaxK(vector<int>& nums) 
    {
        sort(nums.begin(), nums.end());
        reverse(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] > 0 && find(nums.begin(), nums.end(), -nums[i]) != nums.end()) 
            {
                return nums[i];
            }
        }
        return -1;
    }
};