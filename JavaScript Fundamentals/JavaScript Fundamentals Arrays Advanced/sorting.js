function sorting(arr) {
    arr.sort((a, b) => b - a);
    let resultArr = [];
    let i = 0;

    while(arr.length > 0) {
        if (i % 2 === 0) {
            resultArr.push(arr.shift());
        } else {
            resultArr.push(arr.pop());
        }
        i++;
    }
    console.log(resultArr.join(' '));
}


sorting([1, 21, 3, 52, 69, 63, 31, 2, 94]);
sorting([34, 2, 32, 45, 690, 6, 32, 7, 19, 47]);