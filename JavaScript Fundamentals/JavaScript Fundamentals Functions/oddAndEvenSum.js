function oddEvenSums(num) {
    let isEven = x => x % 2 === 0;
    let strNum = String(num);
    let evenSum = 0;
    let oddSum = 0;

    for (let digit of strNum){
        let n = Number(digit);
        
        if (isEven(n)) {
            evenSum += n;
        } else {
            oddSum += n;
        }
    }

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}

oddEvenSums(1000435);