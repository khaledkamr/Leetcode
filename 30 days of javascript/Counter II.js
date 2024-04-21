
var createCounter = function(init) 
{
    let x = init;
    return {
        increment: () =>  ++x,
        decrement: () => --x,
        reset: () => x = init,
    }    
};

