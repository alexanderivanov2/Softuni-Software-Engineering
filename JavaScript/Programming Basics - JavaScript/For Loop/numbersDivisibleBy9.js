function getNumsDivisibleByNine (input) {
    let start = Number(input[0]);
    let end = Number(input[1]);
    let sum = 0;
    let intDivisibleByNine = [];
    for (let i = start; i <= end; i++) {
        if (i % 9 === 0) {
            sum += i;
            intDivisibleByNine.push(i);
        }
    }
    console.log(`The sum: ${sum}`);
    for (let i = 0; i < intDivisibleByNine.length; i++){
        console.log(intDivisibleByNine[i]);
    }
}

getNumsDivisibleByNine(['100', '200']);