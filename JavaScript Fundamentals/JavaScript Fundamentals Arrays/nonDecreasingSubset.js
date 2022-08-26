function nonDecreasingSubset(arr) {
    let biggestNum = arr[0];
    let arrSubset = [arr[0]];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] >= biggestNum){
            arrSubset.push(arr[i]);
            biggestNum = arr[i];
        }
    }
    console.log(arrSubset.join(' '));
}

nonDecreasingSubset([ 1, 3, 8, 4, 10, 12, 3, 2, 24]);