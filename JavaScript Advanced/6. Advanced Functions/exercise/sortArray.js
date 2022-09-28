function sortArr(arr, order) {
    let command = order == 'asc' ? (a, b) => a - b : (a, b) => b - a; 
    let sortedArr = arr.sort(command);

    return sortedArr;
}

console.log(sortArr([14, 7, 17, 6, 8], 'asc'));
console.log(sortArr([14, 7, 17, 6, 8], 'desc'));