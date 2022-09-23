function calcDiagonalSums(arr) {
    function calcMainDiagonal(arr) {
        let sum = 0;
        for (let i = 0; i < arr.length; i+=1) {
            sum += arr[i][i];
        }
        return sum;
    }

    function calcSecondaryDiagonal(arr) {
        let sum = 0;
        
        for (let i=0; i < arr.length; i+=1) {
            let secondIndex = arr[i].length - i - 1;
            sum += arr[i][secondIndex];
        }
        return sum;
    }

    let mainDiagonal = calcMainDiagonal(arr);
    let secondaryDiagonal = calcSecondaryDiagonal(arr);
    console.log(mainDiagonal + ' ' + secondaryDiagonal);
}

calcDiagonalSums([[20, 40],
    [10, 60]])