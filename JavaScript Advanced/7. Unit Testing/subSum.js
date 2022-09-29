function solve(arr, startIndex, endIndex) {
    if (!Array.isArray(arr)) {
        return NaN;
    } 

    startIndex = startIndex < 0 ? 0 : startIndex;
    endIndex = endIndex > arr.length ? arr.length  : endIndex + 1;

    let slicedArr = arr.slice(startIndex, endIndex);
    let sum = slicedArr.reduce((a, b) => a + b, 0);

    if (isNaN(sum)) {
        return NaN;
    }

    return sum;
}


console.log(solve([10, 20, 30, 40, 50, 60], 3, 300));
console.log(solve([1.1, 2.2, 3.3, 4.4, 5.5], -3, 1))
console.log(solve([], 1, 2));
console.log(solve({}, 1, 2));
console.log(solve([10, 'twenty', 30, 40], 0, 2));
console.log(solve('text', 0, 2));