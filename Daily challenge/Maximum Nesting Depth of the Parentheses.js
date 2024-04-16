/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) 
{
    let curr = 0;
    let Max = 0;
    for (let i = 0; i < s.length; i++) 
    {
        if (s[i] === '(') 
        {
            curr++;
            Max = Math.max(Max, curr);
        } else if (s[i] === ')') 
        {
            if (curr > 0) 
            {
                curr--;
            }
            else 
            {
                return -1;
            }
        }
    }
    if (curr !== 0) 
    {
        return -1;
    }
    return Max;
};