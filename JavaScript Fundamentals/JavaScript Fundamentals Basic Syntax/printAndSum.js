function sumLoopNumbers(startInput, endInput) {
    let start = startInput;
    let end = endInput;
    let result = 0;
    let resultString = '';
    for (let i = startInput; i <= endInput; i++) {
        result += i;
        resultString += `${i} `;
    }
    console.log(`${resultString}\nSum: ${result}`);
}

sumLoopNumbers(5, 10);
sumLoopNumbers(0, 26);
sumLoopNumbers(50, 60);
