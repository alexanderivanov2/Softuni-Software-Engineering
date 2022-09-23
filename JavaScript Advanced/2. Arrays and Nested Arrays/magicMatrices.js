function checkAllRowsSums(arr) {
    let neededSum = arr[0].reduce((a, b) => a + b);
    let isEqual = true;
    let endIndex = arr.length;

    for (let i = 0; i < endIndex; i += 1){
        let sum = arr[i].reduce((a, b) => a + b);
        if (sum != neededSum) {
            isEqual = false;
            break;
        }
        let rowSum = 0;
        for (let i2 = 0; i2 < endIndex; i2 += 1){
            rowSum += arr[i][i2];
        }
        if (neededSum != rowSum) {
            isEqual = false;
            break;
        }
    }
    console.log(isEqual);
}


checkAllRowsSums([[4, 5, 6],
    [6, 5, 4],
    [5, 5, 5]]);