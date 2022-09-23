function rotateArrayToRight(arr, sep) {
    for (let i = 0; i < sep; i += 1){
        arr.unshift(arr.pop());
    }
    console.log(arr.join(' '));
}

rotateArrayToRight(['1', 
'2', 
'3', 
'4'], 
2)

rotateArrayToRight(['Banana', 
'Orange', 
'Coconut', 
'Apple'], 
15);