function solve(text) {
    text = text.split(' ');
    for (let word of text) {
        if (word[0] === '#' && word.length > 1){
            console.log(word.slice(1));
        }
    }
}

solve('Nowadays everyone uses # to tag a #special word in #socialMedia');