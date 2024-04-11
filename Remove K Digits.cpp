class Solution 
{
public:
    string removeKdigits(string num, int k) 
    {
        stack<char>s;
        for(int i = 0; i < num.size(); i++)
        {
            while(k && !s.empty() && s.top() > num[i])
            {
                s.pop();
                k--;
            }
            s.push(num[i]);
        }
        while(k--)
        {
            s.pop();
        }

        string res;
        while(!s.empty())
        {
            res += s.top();
            s.pop();
        }
        reverse(res.begin(), res.end());
        size_t pos = res.find_first_not_of("0");
        res = (pos == std::string::npos) ? "0" : res.substr(pos);
        return res;
    }
};