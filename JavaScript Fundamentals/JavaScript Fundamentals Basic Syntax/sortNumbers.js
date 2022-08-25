function sort3Numbers(a, b, c){
    if (a >= b && b >= c){
        console.log(`${a}\n${b}\n${c}`);
    } else if (a >= c  && c >= b){
        console.log(`${a}\n${c}\n${b}`);
    } else if (b >= a && a >= c) {
        console.log(`${b}\n${a}\n${c}`);
    } else if (b >= c && c >= a) {
        console.log(`${b}\n${c}\n${a}`);
    } else if (c >= b && b >= a) {
        console.log(`${c}\n${b}\n${a}`);
    } else if (c >= a && a >= b) {
        console.log(`${c}\n${a}\n${b}`);
    }
}

sort3Numbers(2, 1, 3);
sort3Numbers(-2, 1, 3);
sort3Numbers(0, 0, 2);