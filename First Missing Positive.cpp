class Solution 
{
public:
    int firstMissingPositive(vector<int>& nums) 
    {
        int max = *max_element(nums.begin(), nums.end());
        unordered_map<int, bool> ex;

        for(int i = 0; i < nums.size(); i++)
        {
            ex[nums[i]] = true;
        }

        for(int i = 1; i < max; i++)
        {
            if(!ex[i])
            {
                return i; 
            }
        }

        if(max < 0)
        {
            return 1;
        }
        else
        {
            return max + 1;
        }
    }
};