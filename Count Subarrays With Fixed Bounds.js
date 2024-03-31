/**
 * @param {number[]} nums
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
var countSubarrays = function(nums, minK, maxK) 
{
    const n = nums.length;
    let left = -1;
    let maxi = -1, mini = -1;
    let count = 0;

    for(let i = 0; i < n; i++)
    {
        if(nums[i] < minK || nums[i] > maxK)
        {
            left = i;
        }
        if(nums[i] == minK)
        {
            mini = i;
        }
        if(nums[i] == maxK)
        {
            maxi = i;
        }
        count += Math.max(0 , Math.min(maxi, mini) - left);
    }
    return count;
};