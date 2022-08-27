function getTwoFactorialDivision(numOne, numTwo){
    let factorial = x => {
        let n = 1;
        for (let i = 2; i <= x; i++) {
            n *= i;
        }
        return n;
    }

    let result = factorial(numOne) / factorial(numTwo);
    console.log(result.toFixed(2));
}

getTwoFactorialDivision(5, 2);