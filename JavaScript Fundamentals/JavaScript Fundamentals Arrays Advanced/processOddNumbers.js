function getAndDoubleOddIndex(arr) {
    let result = arr
    .filter((x, i) => i % 2 !== 0)
    .map(x => x * 2)
    .reverse();
    console.log(result.join(' '));
}

getAndDoubleOddIndex([10, 15, 20, 25])
getAndDoubleOddIndex([2, 0, 10, 4, 7, 3]);