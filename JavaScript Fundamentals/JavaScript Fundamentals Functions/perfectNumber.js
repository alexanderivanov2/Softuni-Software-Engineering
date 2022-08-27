function isPerfectNumber(num) {
    let sum = 0;
    for (let i = 1; i <= num / 2; i++) {
        if (num % i === 0) {
            sum += i;
        }
    }

    if (sum === num && sum !== 0) {
        console.log('We have a perfect number!');
    } else {
        console.log("It's not so perfect.");
    }
}

isPerfectNumber(6);
isPerfectNumber(28);
isPerfectNumber(1236498);