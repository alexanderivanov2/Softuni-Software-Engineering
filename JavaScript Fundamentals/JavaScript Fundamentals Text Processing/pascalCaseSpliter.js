function solve(sequence) {

    let arr = [];
    let text = sequence[0];
    for (let i = 1; i < sequence.length; i++) {
        if (sequence[i] === sequence[i].toUpperCase()){
            arr.push(text);
            text = sequence[i];
        } else {
            text += sequence[i];
        }
    }

    arr.push(text);
    console.log(arr.join(', '));
}

solve('SplitMeIfYouCanHaHaYouCantOrYouCan');