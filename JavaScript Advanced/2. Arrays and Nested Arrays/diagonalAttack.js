function diagonalAttack(matrixString) {
    let matrix = []
    for (let r of matrixString) {
        matrix.push(r.split(' '));
    }

    let mainDiagonalSum = 0;
    let secondaryDiagonalSum = 0;
    
    for (let i = 0;  i < matrix.length; i += 1) {
        let i2 = matrix[i].length - i - 1;
        mainDiagonalSum += Number(matrix[i][i]);
        secondaryDiagonalSum += Number(matrix[i][i2]);
    }

    if (mainDiagonalSum === secondaryDiagonalSum) {
        let newMatrix = [];
        for (let r = 0; r < matrix.length; r += 1){
            newMatrix.push([]);
            for (let c = 0; c < matrix[r].length; c += 1) {
                let c2 = matrix[r].length - r - 1;
                if (c != r && c2 != c) {
                    newMatrix[r].push(mainDiagonalSum);
                } else {
                    newMatrix[r].push(Number(matrix[r][c]));
                }
            }
        }
        newMatrix.forEach(row => {
            console.log(row.join(' '));
        });
    } else {
        matrix.forEach(row => {
            console.log(row.join(' '));
        });
    }
}


diagonalAttack(['5 3 12 3 1',
'11 4 23 2 5',
'101 12 3 21 10',
'1 4 5 2 2',
'5 22 33 11 1']);