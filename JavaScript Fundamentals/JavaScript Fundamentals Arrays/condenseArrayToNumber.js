function condenseArrayToNumber(arr){
    let codensedArr = arr;
    while (codensedArr.length !== 1){
        let temp = [];
        for (let i = 0; i < codensedArr.length - 1; i++){
            let result = codensedArr[i] + codensedArr[i + 1];
            temp.push(result);
        }
        codensedArr = temp;
    }
    console.log(codensedArr[0]);
}


condenseArrayToNumber([2,10,3]);
condenseArrayToNumber([5,0,4,1,2]);
condenseArrayToNumber([1]);