function equalSums(arr) {
    if (arr.length === 1){
        console.log(0);
    } else if (arr.length === 2){
        console.log('no');
    } else {
        let index = 1;

        while (index < arr.length - 1){
            let sumLeft = 0;
            let sumRight = 0;

            for (let i = 0; i < index; i++){
                sumLeft += arr[i];
            }

            for (let i = index + 1; i < arr.length; i++){
                sumRight += arr[i];
            }
            
            if (sumLeft === sumRight){
                console.log(index);
                return;
            }
            index += 1;
        }

        console.log('no');
    }
}

equalSums([1, 2, 3, 3]);
equalSums([1, 2]);
equalSums([1]);
equalSums([1, 2, 3]);
equalSums([10, 5, 5, 99, 3, 4, 2, 5, 1, 1, 4]);