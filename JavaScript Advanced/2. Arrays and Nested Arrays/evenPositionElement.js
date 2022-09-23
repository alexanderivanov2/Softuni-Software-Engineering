function printEvenPositionsInArray (arr) {
    let strEvenElements = '';
    
    for (let i = 0; i < arr.length; i+= 1){
        if (i % 2 === 0) {
            strEvenElements += arr[i] + ' ';
        }
    }

    console.log(strEvenElements.trimEnd());
}

printEvenPositionsInArray(['20', '30', '40', '50', '60']);