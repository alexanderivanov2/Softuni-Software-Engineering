function arrayRotation(arr, rotate) {
    for (let i = 0; i < rotate; i++){
        arr.push(arr.shift(0));
    }
    console.log(arr.join(' '));
}

arrayRotation([51, 47, 32, 61, 21], 2);
arrayRotation([2, 4, 15, 31], 5);