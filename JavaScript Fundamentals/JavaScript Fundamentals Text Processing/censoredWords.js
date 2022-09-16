function solve(text, replaceWord) {
    let censored = '*'.repeat(replaceWord.length)

    while (text.includes(replaceWord)) {
        text = text.replace(replaceWord, censored);
    }
    
    console.log(text);
}

solve('A small sentence with some words', 'small');