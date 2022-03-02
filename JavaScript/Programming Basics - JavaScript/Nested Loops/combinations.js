function combinations(input){
    let result = Number(input[0]);
    let numOfCombinations = 0;
    for (x1 = 0; x1 <= result; x1++){
        for (x2 = 0; x2 <= result; x2++){
            for (x3 = 0; x3 <= result; x3++){
                if (x1 + x2 + x3 === result){
                    numOfCombinations += 1;
                }
            }
        }
    }
    console.log(numOfCombinations);
}

combinations(['25']);