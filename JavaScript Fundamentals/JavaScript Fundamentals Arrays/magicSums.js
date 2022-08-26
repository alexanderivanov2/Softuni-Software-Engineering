function getMagicSums(arr, magicSum){
    for (let i = 0; i < arr.length - 1; i++){
        let numOne = arr[i];
        for (let j = i + 1; j < arr.length; j++){
            if (numOne + arr[j] === magicSum){
                console.log(`${numOne} ${arr[j]}`);
            }
        }
    }
}


getMagicSums([1, 7, 6, 2, 19, 23],
    8);
getMagicSums([14, 20, 60, 13, 7, 19, 8],
    27);
getMagicSums([1, 2, 3, 4, 5, 6],
    6);