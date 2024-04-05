class Solution 
{
public:
    string makeGood(string s) 
    {
        string res;

        for(int i = 0; i < s.size(); i++)
        {
            if(res != "" && abs(s[i] - res[res.size() - 1]) == 32)
            {
                res.pop_back();
            }
            else
            {
                res.push_back(s[i]);
            }
        }
        return res;
    }
};