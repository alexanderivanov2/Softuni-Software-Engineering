function smallestOfThreeNumbers(num1, num2, num3) {
    let getSmallNum = (a, b) => a < b ? a : b;
    let result = getSmallNum(getSmallNum(num1, num2), num3);

    console.log(result);
}


smallestOfThreeNumbers(2,
    5,
    3);
smallestOfThreeNumbers(600,
    342,
    123);
smallestOfThreeNumbers(25,
    21,
    4);
smallestOfThreeNumbers(2,
    2,
    2);