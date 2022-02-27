function smartLilly(input){
    let age = Number(input[0]);
    let priceForWashingMachine = Number(input[1]);
    let priceForOneToy = Number(input[2]);
    let moneyForEvenBirthday = 0;
    let toys = 0;
    let savings = 0;
    for (let i = 1; i <= age; i++){
        if (i % 2 != 0){
            toys += 1;
        } else {
            moneyForEvenBirthday += 10;
            savings += moneyForEvenBirthday - 1;
        }
    }
    savings += toys * priceForOneToy;
    if (savings >= priceForWashingMachine){
        console.log(`Yes! ${(savings-priceForWashingMachine).toFixed(2)}`);
    } else {
        console.log(`No! ${(priceForWashingMachine-savings).toFixed(2)}`);
    }
}


smartLilly(["10",
"170.00",
"6"]);

smartLilly(["21",
"1570.98",
"3"]);