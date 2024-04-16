/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) 
{
    let n = height.length;
    let left = height[0];
    let right = height[n - 1];
    let res = 0;
    let i = 0;
    let j = n - 1;
    while (i < j) 
    {
        if (left <= right) 
        {
            res += left - height[i];
            i++;
            left = Math.max(left, height[i]);
        } 
        else 
        {
            res += right - height[j];
            j--;
            right = Math.max(right, height[j]);
        }
    }
    return res;    
};