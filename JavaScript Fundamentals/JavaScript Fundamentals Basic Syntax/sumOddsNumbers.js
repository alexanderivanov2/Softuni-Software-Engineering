function solveOddNumbers(n) {
    let i = 1;
    let num = 1;
    let sum = 0;
    while (i <= n){
        console.log(num);
        sum += num;
        num += 2;
        i += 1;
    }
    console.log(`Sum: ${sum}`);
}

solveOddNumbers(5);