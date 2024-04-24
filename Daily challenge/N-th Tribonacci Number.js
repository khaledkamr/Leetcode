/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) 
{
    if (n === 0) return 0;
    else if (n === 1 || n === 2) return 1;
    let t0 = 0, t1 = 1, t2 = 1;
    
    while (n-- > 2) 
    {
        let temp = t2;
        t2 = t0 + t1 + t2;
        t0 = t1;
        t1 = temp;
    }
    
    return t2;
};