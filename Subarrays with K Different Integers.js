/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var atMost = function(nums, k)
{
    const n = nums.length;
    let freq = new Map();
    let start = 0;
    let count = 0;

    for(let i = 0; i < n; i++)
    {
        freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);
        while(freq.size > k)
        {
            freq.set(nums[start], freq.get(nums[start]) - 1);
            if(freq.get(nums[start]) == 0)
            {
                freq.delete(nums[start]);
            }
            start++;
        }
        count += (i - start + 1);
    }
    return count;
}
var subarraysWithKDistinct = function(nums, k) 
{
    return atMost(nums, k) - atMost(nums, k-1);
};