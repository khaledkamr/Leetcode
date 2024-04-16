class Solution 
{
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) 
    {
        int count = 0;
        while(tickets[k])
        {
            for(int i = 0; i < tickets.size(); i++)
            {
                if(tickets[i] > 0)
                {
                    tickets[i]--;
                    count++;
                }
                if(tickets[k] == 0)
                {
                    return count;
                }
            }
        }
        return count;
    }
};