function characterSequence (input) {
    let sequence = input[0]
    let lastElement = sequence.length;
   
    for (let i = 0; i < lastElement; i++) {
        console.log(sequence[i]);
    }
}


characterSequence(['Hello JS']);