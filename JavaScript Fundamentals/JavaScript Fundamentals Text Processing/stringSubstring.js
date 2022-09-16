function solve(word, text) {
    let textArr = text.split(' ');

    for (let w of textArr) {
        if (w.toLocaleLowerCase() === word.toLocaleLowerCase()) {
            console.log(word);
            return;
        }
    }
   
    console.log(`${word} not found!`);
}

solve('Javascript',
'JavaScript is the best programming language')