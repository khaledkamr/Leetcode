class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) 
    {
        sort(happiness.rbegin(), happiness.rend());
        long long sum = 0;
        for(int i = 0; k-- > 0; i++)
        {
            sum += happiness[i] - i > 0 ? happiness[i] - i : 0;
        }
        return sum;
    }
};