function processOddPositions(arr) {
    let result = arr
    .filter((x, index) => index % 2 != 0)
    .map((x) => x * 2)
    .reverse()
    return result.join(' ')
}

processOddPositions([10, 15, 20, 25]);
processOddPositions([3, 0, 10, 4, 7, 3]);