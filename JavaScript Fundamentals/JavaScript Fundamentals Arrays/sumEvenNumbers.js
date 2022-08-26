function sumEvenNumbers(arr){
    let sum = 0;
    for(let num of arr){
        num = Number(num);
        if (num % 2 === 0){
            sum += num;
        }
    }
    console.log(sum);
}

sumEvenNumbers(['1','2','3','4','5','6']);