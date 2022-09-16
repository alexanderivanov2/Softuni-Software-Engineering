function solve(word, start, end) {
    start = Number(start);
    end = Number(end);
    console.log(word.substring(start, end + start));
}

solve('ASentence', 1, 8);