function getIncreasingNumbersFromArray(arr) {
    let resultArr = [];

    for (let el of arr) {
        if (resultArr.length == 0) {
            resultArr.push(el);
        } else if (el >= resultArr[resultArr.length - 1]) {
            resultArr.push(el);
        }
    }
    return resultArr
}

console.log(getIncreasingNumbersFromArray([1, 
    3, 
    8, 
    4, 
    10, 
    12, 
    3, 
    2, 
    24]))
console.log(getIncreasingNumbersFromArray([1, 
    2, 
    3,
    4]))
console.log(getIncreasingNumbersFromArray([20, 
    3, 
    2, 
    15,
    6, 
    1]));