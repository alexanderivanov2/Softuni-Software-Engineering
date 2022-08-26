function getTopIntegers(arr){
    let newArr = [];
    for (let i = 1; i < arr.length; i++){
        let num = arr[i];
        let bigger = true;
        for (let j = i + 1; j < arr.length; j++){
            if (num <= arr[j]){
                bigger = false;
                break;
            }
        }
        if (bigger){
            newArr.push(num);
        }
    }
    console.log(newArr.join(' '));
}

getTopIntegers([1, 4, 3, 2]);
getTopIntegers([14, 24, 3, 19, 15, 17]);
getTopIntegers([41, 41, 34, 20]);