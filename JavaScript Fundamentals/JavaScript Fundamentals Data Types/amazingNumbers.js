function amazingNumbers(number){
    let num = String(number);
    let sum = 0;
    let amazing = false;
    for (let i = 0; i < num.length; i++){
        sum += Number(num[i]);
    }
    let sumString = String(sum);
    for (let i = 0; i < sumString.length; i++){
        if (sumString[i] === '9'){
            amazing = true;
        }
    }
    if (amazing === true){
        console.log(`${num} Amazing? True`);
    } else {
        console.log(`${num} Amazing? False`);
    }
}

amazingNumbers(1233);
amazingNumbers(999);