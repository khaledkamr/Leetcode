class Solution 
{
public:
    int lengthOfLastWord(string s) 
    {
        int size = 0;
        bool flag = false;
        int L = s.length() - 1;
        for(int i = L; i >= 0; i--)
        {
            if(s[i] != ' ')
            {
                flag = true;
                size++;
            }
            else if(flag)
            {
                break;
            }
        }
        return size;
    }
};