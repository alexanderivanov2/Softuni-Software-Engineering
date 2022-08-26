function addAndSubtract(arr){
    let changeArr = [];
    let sumOldArr = 0;
    let sumNewArr = 0;
    for (let i = 0; i < arr.length; i++){
        sumOldArr += arr[i];
        if (arr[i] % 2 === 0){
            changeArr.push(arr[i] + i);
        } else {
            changeArr.push(arr[i] - i);
        }
        sumNewArr += changeArr[i];
    }
    console.log(changeArr);
    console.log(sumOldArr);
    console.log(sumNewArr);
}

addAndSubtract([5, 15, 23, 56, 35]);