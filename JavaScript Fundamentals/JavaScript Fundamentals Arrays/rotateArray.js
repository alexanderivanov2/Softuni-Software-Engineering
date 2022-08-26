function rotateArray(inputArr) {
    let arr = inputArr.slice(0, inputArr.length - 1);
    let rotate = Number(inputArr[inputArr.length - 1]);
    for (let i = 0; i < rotate; i++){
        let el = arr.pop();
        arr.splice(0, 0, el);
    }
    console.log(arr.join(' '));
}

rotateArray(['1', '2', '3', '4', '2']);