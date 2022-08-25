function biggestOf3Numbers(num1, num2, num3){
    let bigNum = 0;
    if (num1 >= num2){
        bigNum = num1;
    } else {
        bigNum = num2;
    }
    if (bigNum <= num3) {
        bigNum = num3;
    }
    console.log(bigNum);
}

biggestOf3Numbers(-2,
    7,
    3);

biggestOf3Numbers(130,
    5,
    99);