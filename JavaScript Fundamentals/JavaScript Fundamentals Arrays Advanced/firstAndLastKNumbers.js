function printFirstAndLastElements (arr) {
    let numOfElements = arr.shift();
    let firstElements = arr.slice(0, numOfElements);
    let lastElements = arr.slice(numOfElements * -1);
    console.log(`${firstElements.join(' ')}\n${lastElements.join(' ')}`);
}

printFirstAndLastElements([2, 
    7, 8, 9]);
printFirstAndLastElements([3,
    6, 7, 8, 9]);