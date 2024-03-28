class Solution 
{
public:
    int maxSubarrayLength(vector<int>& nums, int k) 
    {
        int n = nums.size();
        unordered_map<int, int>freq;
        int start = -1, end = 0;
        int res = INT_MIN;

        for(int i = 0; i < n; i++)
        {
            freq[nums[i]]++;
            while(freq[nums[i]] > k)
            {
                start++;
                freq[nums[start]]--;
            }
            if(end - start > res)
            {
                res = end - start;
            }
            end++;
        }
        return res;
    }
};