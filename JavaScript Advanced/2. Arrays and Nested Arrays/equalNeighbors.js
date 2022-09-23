function getCountOfEqualNeighbors(arr){
    let count = 0;
    for (let r = 0; r < arr.length; r +=1 ) {
        for (let c = 0; c < arr[r].length; c += 1){
            let el = arr[r][c];
            if (r == arr.length - 1) {
                if (el === arr[r][c + 1]){
                    count += 1;
                }
            } else {
                if (el === arr[r + 1][c]) {
                    count += 1;
                }

                if (el === arr[r][c + 1]) {
                    count += 1;
                }
            }
        }
    }

    return count;
}

console.log(getCountOfEqualNeighbors([['2', '3', '4', '7', '0'],
['4', '0', '5', '3', '4'],
['2', '3', '5', '4', '2'],
['9', '8', '7', '5', '4']]));
console.log(getCountOfEqualNeighbors([['test', 'yes', 'yo', 'ho'],
['well', 'done', 'yo', '6'],
['not', 'done', 'yet', '5']]));