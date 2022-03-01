function sumNumbers(input){
    let firstSum = Number(input[0]);
    let secondSum = 0;
    let i = 1;
    while (secondSum < firstSum){
        secondSum += Number(input[i]);
        i++;
    }
    console.log(secondSum);
}


sumNumbers(["20",
"1",
"2",
"3",
"4",
"5",
"6"]);