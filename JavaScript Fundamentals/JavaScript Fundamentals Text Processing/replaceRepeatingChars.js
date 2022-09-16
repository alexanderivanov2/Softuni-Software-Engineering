function solve(sequence) {
    let noRepeat = sequence[0];
    for (let i = 1; i < sequence.length; i+=1){
        if (sequence[i] !== sequence[i - 1]) {
            noRepeat += sequence[i];
        }
    }
    console.log(noRepeat);
}

solve('aaaaabbbbbcdddeeeedssaa');