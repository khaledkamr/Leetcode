class Solution 
{
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) 
    {
        queue<int>qu;
        sort(deck.begin(), deck.end());
        reverse(deck.begin(), deck.end());

        for(int i = 0; i < deck.size(); i++)
        { 
            qu.push(qu.front());
            qu.pop();
            qu.push(deck[i]);
        }
        vector<int> res;
        int n = qu.size();
        for(int i = 0; i < n; i++)
        {
            res.insert(res.begin(), qu.front());
            qu.pop();
        }
        return res;
    }
};