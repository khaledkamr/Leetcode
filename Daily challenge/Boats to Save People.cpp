class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) 
    {
        int count = 0;
        sort(people.begin(), people.end());
        int start =0;
        int end = people.size() - 1;
        for(start, end; start <= end; end--)
        {
            if(people[start] + people[end] <= limit)
            {
                start++;
            }
            count++;
        }
        return count;
    }
};
