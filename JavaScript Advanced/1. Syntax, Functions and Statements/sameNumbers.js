function checkNumberContainsSameNums(num) {
    num = String(num);
    let n = num[0];
    let result = true;
    let sum = Number(n);
    
    for (let i = 1; i < num.length; i++) {
        if (num[i] !== n) {
            result = false;
        }
        sum += Number(num[i]);
    }

    console.log(result);
    console.log(sum);
}

checkNumberContainsSameNums(2222222);
checkNumberContainsSameNums(1234);