function maxSequenceOfEqualElements(arr){
    let longestSeq = [arr[0]];
    let currSeq = [arr[0]];
    for (let i = 1; i < arr.length; i++) {
        if (currSeq.length === 0 || currSeq[0] === arr[i]) {
            currSeq.push(arr[i]);
        } 
        if (currSeq[0] !== arr[i] || i === arr.length - 1){
            if (currSeq.length > longestSeq.length){
                longestSeq = currSeq;
            }
            currSeq = [arr[i]];
        }
    }
    console.log(longestSeq.join(' '));
}

maxSequenceOfEqualElements([2, 1, 1, 2, 3, 3, 2, 2, 2, 1]);
maxSequenceOfEqualElements([1, 1, 1, 2, 3, 1, 3, 3]);
maxSequenceOfEqualElements([4, 4, 4, 4]);
maxSequenceOfEqualElements([0, 1, 1, 5, 2, 2, 6, 3, 3]);