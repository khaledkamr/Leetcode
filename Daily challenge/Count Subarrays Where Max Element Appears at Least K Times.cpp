class Solution 
{
public:
    long long countSubarrays(vector<int>& nums, int k) 
    {
        int n  = nums.size();
        int start = 0;
        long long count = 0;
        int max = *max_element(nums.begin(),nums.end());

        for(int i = 0; i < n; i++)
        {
            if(nums[i] == max) {k--;}
            while(k == 0)
            {
                if(nums[start] == max) {k++;}
                start++;
            }
            count += start;
        }
        return count;
    }
};