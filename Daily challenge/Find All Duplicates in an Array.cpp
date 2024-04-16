class Solution 
{
public:
    vector<int> findDuplicates(vector<int>& nums) 
    {
        vector<int>dup;
        vector<int>freq(100000,0);
        for(int i = 0; i < nums.size(); i++)
        {
            if(freq[nums[i]] != 0)
            {
                dup.push_back(nums[i]);
            }
            else
            {
                freq[nums[i]]++;
            }
        }
        return dup;
    }
};