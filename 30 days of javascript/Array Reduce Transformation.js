
var reduce = function(nums, fn, init) 
{
    if(nums.length == 0)
    {
        return init;
    }
    return nums.reduce(fn, init);
};