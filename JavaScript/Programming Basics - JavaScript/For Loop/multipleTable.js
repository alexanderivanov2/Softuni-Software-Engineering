function getNumAndMultiplyFrom1To10(input){
    let num = Number(input[0]);
    for (let i = 1; i <= 10; i++){
        console.log(`${i} * ${num} = ${i * num}`);
    }
}


getNumAndMultiplyFrom1To10(['5']);