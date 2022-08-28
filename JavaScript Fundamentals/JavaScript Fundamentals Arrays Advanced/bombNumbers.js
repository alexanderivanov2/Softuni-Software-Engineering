function bombNumbers (arr, bombArr) {
    let bombN = bombArr[0];
    let bombRange = bombArr[1];

    while(arr.includes(bombN)) {
        let index = arr.indexOf(bombN);
        let startSplice;
        let numDelete;

        if (index - bombRange < 0) {
            numDelete = index + bombRange + 1;
            startSplice = 0;
        } else {
            numDelete = bombRange * 2 + 1;
            startSplice = index - bombRange
        }
        arr.splice(startSplice, numDelete);
    }

    let sum = 0;
    arr.map(a => sum += a);
    console.log(sum);
}

bombNumbers([1, 7, 7, 1, 2, 3],
    [7, 1]);