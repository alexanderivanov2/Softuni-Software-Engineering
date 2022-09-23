function printSmallestTwoNumbersOfArray(arr) {
    let newArr = arr.sort((a, b) => a - b);

    console.log(newArr[0] + ' ' + newArr[1]);
}

printSmallestTwoNumbersOfArray([30, 15, 50, 5]);