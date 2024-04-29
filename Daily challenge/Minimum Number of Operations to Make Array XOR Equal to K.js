
var minOperations = function(nums, k) 
{
    let finalXor = 0;
        for (let n of nums) 
        {
            finalXor = finalXor ^ n;
        }

        let count = 0;
        while (k || finalXor) 
        {
            if ((k % 2) !== (finalXor % 2)) 
            {
                count++;
            }
            k = Math.floor(k / 2);
            finalXor = Math.floor(finalXor / 2);
        }

        return count;   
};