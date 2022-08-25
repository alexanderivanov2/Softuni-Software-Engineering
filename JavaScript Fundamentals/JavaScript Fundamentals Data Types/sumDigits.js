function sumDigit(num){
    let stringNum = String(num);
    let sum = 0;
    for (let i = 0; i < stringNum.length; i++){
        sum += Number(stringNum[i]);
    }
    console.log(sum);
};

sumDigit(245678);