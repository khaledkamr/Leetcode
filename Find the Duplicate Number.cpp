class Solution 
{
public:
    int findDuplicate(vector<int>& nums) 
    {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int dub;

        for(int i = 0; i < n-1; i++)
        {
            if(nums[i] == nums[i+1])
            {
                dub = nums[i];
                break;
            }
        }
        return dub;
    }
};