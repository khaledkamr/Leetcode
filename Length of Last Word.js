/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) 
{
    let size = 0;
    let flag = false;
    const L = s.length - 1;

    for(let i = L; i >= 0; i--)
    {
        if(s[i] != " ")
        {
            flag = true;
            size++;
        }
        else if(flag) {break;}
    }
    return size;
};