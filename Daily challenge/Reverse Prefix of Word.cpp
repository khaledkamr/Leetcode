class Solution {
public:
    string reversePrefix(string word, char ch) 
    {
        string rev = word;
        for (int i = 0; i < word.length(); ++i) {
            if (word[i] == ch) {
                rev = word.substr(0, i + 1);
                std::reverse(rev.begin(), rev.end());
                rev += word.substr(i + 1);
                break;
            }
        }
        return rev;    
    }
};