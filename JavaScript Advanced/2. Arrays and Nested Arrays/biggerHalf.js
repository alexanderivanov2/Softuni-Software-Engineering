function returnBiggerHalf (arr) {
    let sortArr = arr.sort((a, b) => b - a);
    let endIndex = Math.ceil(arr.length / 2);
    let finalArr = sortArr.slice(0, endIndex).sort((a, b) => a - b);
    return finalArr
}

console.log(returnBiggerHalf([4, 7, 2, 5]));
console.log(returnBiggerHalf([3, 19, 14, 7, 2, 19, 6]));