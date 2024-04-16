class Solution 
{
public:
    int findDuplicate(vector<int>& nums) 
    {
        long long dup;
        vector<int>freq(100000,0);
        sort(nums.begin(),nums.end());
        for(auto num:nums)
        {
            if(freq[num] != 0)
            {
                dup = num;
                break;
            }
            else
            {
                freq[num]++;
            }
        }
        return dup;
    }
};