class Solution 
{
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) 
    {
        int n = nums.size();
        int left = -1;
        int minI = -1, maxI = -1;
        long long count = 0;

        for(int i = 0; i < n; i++)
        {
            if(nums[i] < minK || nums[i] > maxK)
            {
                left = i;
            }
            if(nums[i] == minK)
            {
                minI = i;
            }
            if(nums[i] == maxK)
            {
                maxI = i;
            }
            count += max(0 , min(maxI, minI) - left);
        }
        return count;
    }
};