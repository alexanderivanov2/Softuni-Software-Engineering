function reverseArray(n, arr){
    let startIndex = n - 1;
    let newArr = [];
    for (let i = startIndex; i >= 0; i--){
        newArr.push(arr[i]);
    }
    console.log(newArr.join(' '));
}

reverseArray(3, [10, 20, 30, 40, 50]);
reverseArray(4, [-1, 20, 99, 5]);
reverseArray(2, [66, 43, 75, 89, 47]);