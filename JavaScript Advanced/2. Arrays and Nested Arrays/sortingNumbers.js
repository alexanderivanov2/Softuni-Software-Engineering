function sortingNumbers(arr) {
    arr.sort((a,b) => a - b);
    let resultArr = [];
    let endIndex = arr.length;
    for (let i = 0; i < endIndex; i += 1) {
        if (i % 2 == 0) {
            resultArr.push(arr.shift());
        } else {
            resultArr.push(arr.pop());
        }
    } 

    return resultArr
}

console.log(sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));