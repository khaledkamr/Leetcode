
var findMaxK = function(nums) 
{
    nums.sort((a, b) => b - a);
    for (let n of nums) 
    {
        if (n > 0 && nums.includes(-n)) 
        {
            return n;
        }
    }
    return -1;    
};