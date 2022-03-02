function sumOfTwoNums(input){
    let start = Number(input[0]);
    let end = Number(input[1]);
    let result = Number(input[2]);
    let counter = 0;
    for (let i = start; i <= end; i++){
        for (let j = start; j <= end; j++){
            counter += 1
            if (i + j === result){
                console.log(`Combination N:${counter} (${i} + ${j} = ${i + j})`);
                return;
            }
        }
    }
    console.log(`${counter} combinations - neither equals ${result}`);
}


sumOfTwoNums(["88",
"888",
"1000"]);