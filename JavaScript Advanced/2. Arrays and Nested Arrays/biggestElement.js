function returnBiggestValueInNestedArray(arr) {
    let biggestValue = Number.MIN_SAFE_INTEGER;

    for (let el of arr) {
        let sortEl = el.sort((a,b) => b - a)[0];
        if (biggestValue < sortEl) {
            biggestValue = sortEl;
        }
    }

    return biggestValue;
}

console.log(returnBiggestValueInNestedArray([[20, 50, 10],
    [8, 33, 145]]))
console.log(returnBiggestValueInNestedArray([[3, 5, 7, 12],
    [-1, 4, 33, 2],
    [8, 3, 0, 4]]));