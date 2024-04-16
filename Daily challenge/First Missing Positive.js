/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) 
{
    let n = nums.length;
    let mp = new Map();
    let maxI = Math.max(...nums, 0);

    for(let i = 0; i < n; i++)
    {
        mp.set(nums[i], true);
    }

    for(let i = 1; i < maxI; i++)
    {
        if(mp.has(i) == false)
        {
            return i;
        }
    }

    if(maxI < 0)
    {
        return 1;
    }
    else
    {
        return maxI + 1;
    }
};