function printAlphabethicallNames(arr) {
    arr.sort((a, b) => a.localeCompare(b));
    let lineNumber = 1;
    arr.forEach(el => {
        console.log(`${lineNumber}.${el}`);
        lineNumber += 1;
    });
}

printAlphabethicallNames(["John", "Bob", "Christina", "Ema"]);