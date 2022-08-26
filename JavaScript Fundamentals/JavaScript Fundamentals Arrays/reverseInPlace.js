function reverseInPlace(arr){
    let middle = Math.floor(arr.length / 2);
    for (let i = 0; i < middle; i++){
        let change = arr.length - 1 - i;
        let temp = arr[i];
        arr[i] = arr[change];
        arr[change] = temp;
    }
    console.log(arr.join(' '));
}

reverseInPlace(['a', 'b', 'c', 'd', 'e']);
reverseInPlace(['abc', 'def', 'hig', 'klm', 'nop']);
reverseInPlace(['33', '123', '0', 'dd']);