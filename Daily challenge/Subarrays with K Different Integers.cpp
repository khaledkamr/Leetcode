class Solution 
{
public:
    int atMost(vector<int>& nums, int k)
    {
        int n = nums.size();
        unordered_map<int, int>freq;
        int start = 0;
        int count = 0;

        for(int i = 0; i < n; i++)
        {
            freq[nums[i]]++;
            while(freq.size() > k)
            {
                freq[nums[start]]--;
                if(freq[nums[start]] == 0)
                {
                    freq.erase(nums[start]);
                }
                start++;
            }
            count += (i - start + 1);
        }
        return count;
    }
    int subarraysWithKDistinct(vector<int>& nums, int k) 
    {
        return atMost(nums, k ) - atMost(nums, k-1);
    }
};