function solve(words, text) {
    words = words.split(", ");
    
    for (let el of words) {
        censored = '*'.repeat(el.length);
        text = text.replace(censored, el);
    }
    console.log(text);
}


solve('great',
'softuni is ***** place for learning new programming languages');

solve('great, learning',
'softuni is ***** place for ******** new programming languages');