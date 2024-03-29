/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countSubarrays = function(nums, k) 
{
    const n = nums.length;
    let max = Math.max(...nums);
    let start = 0;
    let count = 0;

    for(let i = 0; i < n; i++)
    {
        if(nums[i] === max)
        {
            k--;
        }
        while(k == 0)
        {
            if(nums[start] == max)
            {
                k++;
            }
            start++;
        }
        count += start;
    }
    return count;
};