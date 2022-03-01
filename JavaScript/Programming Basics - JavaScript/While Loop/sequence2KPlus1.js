function sequenceNum(input){
    let endNum = Number(input[0]);
    let currentNum = 1;
    while(currentNum <= endNum){
        console.log(currentNum);
        currentNum = currentNum * 2 + 1;       
    }
}


sequenceNum(['17']);