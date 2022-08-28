function getLastKNumbersSequence(n, k) {
    let arr = [1];
    for (let i = 1; i < n; i++) {
        startIndex = i - k < 0 ? 0 : i - k;
        let newArrElement = (arr.slice(Math.abs(startIndex), i));
        let sum = 0;
        for (let el of newArrElement) {
            sum += el;
        }
        arr.push(sum);
    }
    console.log(arr.join(' '));
}

getLastKNumbersSequence(6, 3);
getLastKNumbersSequence(8, 2);