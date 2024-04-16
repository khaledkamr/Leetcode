class Solution 
{
public:
    int maxDepth(string s) 
    {
       int curr = 0;
       int Max = 0;
       for(int i = 0; i < s.size(); i++)
       {
           if(s[i] == '(')
           {
              curr++;
              Max = max(Max, curr);
           }
           else if(s[i] == ')')
           {
               if(curr > 0)
               {
                  curr--;
               }
               else
               {
                  return -1;
               }
           }
       }
       if(curr != 0)
       {
        return -1;
       }
       return Max;
    }
};