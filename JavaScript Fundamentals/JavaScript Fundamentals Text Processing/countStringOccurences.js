function solve(text, word) {
    let arr = text.split(' ');
    let count = 0;
    for (let el of arr) {
        if (el === word) {
           count += 1;
        }
    }
    console.log(count)
}

solve('This is a word and it also is a sentence',
'is');