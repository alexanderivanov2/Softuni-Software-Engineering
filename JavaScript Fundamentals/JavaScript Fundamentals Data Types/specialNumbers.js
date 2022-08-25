function specialNumbers(num) {
    for (let i = 1; i <= num; i++){
        let sum = 0;
        let strNum = String(i);
        for (let j = 0; j < strNum.length; j++) {
            sum += Number(strNum[j]);
        }
        if (sum === 5 || sum === 7 || sum === 11){
            console.log(`${i} -> True`);
        } else {
            console.log(`${i} -> False`)
        }
    }
}

specialNumbers(21);