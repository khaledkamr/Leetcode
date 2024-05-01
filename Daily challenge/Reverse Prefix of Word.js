
var reversePrefix = function(word, ch) 
{
    let rev = word;
    for (let i = 0; i < word.length; ++i) 
    {
        if (word[i] === ch) 
        {
            rev = word.slice(0, i + 1).split('').reverse().join('') + word.slice(i + 1);
            break;
        }
    }
    return rev;    
};