/**
 * @param {string} s
 * @return {string}
 */
var makeGood = function(s) 
{
    let res = "";
    for (let i = 0; i < s.length; i++) 
    {
        if (res && Math.abs(s.charCodeAt(i) - res.charCodeAt(res.length - 1)) === 32) 
        {
            res = res.slice(0, -1);
        } 
        else 
        {
            res += s[i];
        }
    }
    return res;
};