function sumFirstAndLastElementOfArr(arr) {
    firstElement = Number(arr.shift());
    lastElemnt = Number(arr.pop());
    console.log(firstElement + lastElemnt);
}

sumFirstAndLastElementOfArr(['25', '35', '45', '55']);