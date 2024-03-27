/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) 
{
    let n = nums.length;
    let count = 0;

    for(let i = 0; i < n; i++)
    {
        let pro = 1;
        for(let j = i; j < n; j++)
        {
            pro *= nums[j];
            if(pro >= k)
            {
                break;
            }
            count++;
        }
    }
    return count;
};