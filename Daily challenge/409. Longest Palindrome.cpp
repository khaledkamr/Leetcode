class Solution 
{
public:
    int longestPalindrome(string s) 
    {
        int palindrome = 0;
        unordered_set<char> hash_map;

        for(int i = 0; i < s.size(); i++)
        {
            if(hash_map.find(s[i]) != hash_map.end())
            {
                hash_map.erase(s[i]);
                palindrome += 2;
            }
            else
            {
                hash_map.insert(s[i]);
            }
        }
        palindrome += (s.size() > palindrome)? 1 : 0;
        
        return palindrome;
    }
};