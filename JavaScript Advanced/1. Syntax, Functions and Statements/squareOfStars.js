function printSquareOfStars(n) {
    let result = '* '.repeat(n);
    result.trimEnd;
    for (let i = 0; i < n; i+= 1) {
        console.log(result);
    }
}

printSquareOfStars(1);
printSquareOfStars(2);
printSquareOfStars(5);
printSquareOfStars(7);