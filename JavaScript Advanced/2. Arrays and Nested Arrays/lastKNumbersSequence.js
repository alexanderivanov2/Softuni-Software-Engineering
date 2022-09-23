function printSequence(n, k) {
    let reducer = (a, b) => a + b;
    
    let arr = [1];
    for (let i = 1; i < n; i+= 1) {
        let statIndex = i - k < 0 ? 0 : i - k;
        let n = arr.slice(statIndex, i).reduce(reducer);
        arr.push(n);
    }

    return arr;
}

printSequence(6, 3);
printSequence(8, 2);