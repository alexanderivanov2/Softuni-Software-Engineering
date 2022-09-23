function sumFirstAndLastElementOfArr(arr) {
    let sum = 0;

    if (arr.length === 1) {
        sum += Number(arr[0]);
    } else {
        sum += Number(arr[0]) + Number(arr[arr.length-1]);
    }

    return sum;
}

console.log(sumFirstAndLastElementOfArr(['20', '30', '40']));