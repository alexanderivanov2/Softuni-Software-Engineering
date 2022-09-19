function aggregateElements(arrOfNums) {
    let sumResult = 0;
    let sumResultDivide = 0;
    let sumString = '';

    for (let i of arrOfNums) {
        sumResult += i;
        sumResultDivide += 1 / i;
        sumString += i;
    }

    console.log(sumResult);
    console.log(sumResultDivide);
    console.log(sumString);    
}

aggregateElements([1, 2, 3]);
aggregateElements([2, 4, 8, 16]);