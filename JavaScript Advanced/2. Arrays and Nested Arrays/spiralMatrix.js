function buildSpiralMatrix(row, col) {
    let spiralMatrix = [];
    for (let i = 0; i < row; i+=1) {
        let currRow = [];
        currRow.length = col;
        spiralMatrix.push(currRow);
    }

    let end = row * col;
    let start = 1;
    let spiralRowStart = 0;
    let spiralColStart = 0;
    let spiralRowEnd = row;
    let spiralColEnd = col;
    while(start <= end) {
        // Spiral Go Left Top Row
        for (let i = spiralColStart; i < spiralColEnd; i+=1) {
            spiralMatrix[spiralColStart][i] = start;
            start += 1;
        }
        spiralRowStart += 1;
        // Spiral Go Down End Column
        for (let i = spiralRowStart; i < spiralRowEnd; i+=1) {
            spiralMatrix[i][spiralColEnd - 1] = start;
            start += 1;
        }
        spiralColEnd -= 1;

        //  Spiral Go Left Row

        for (let i = spiralColEnd; i > spiralColStart; i -= 1) {
            spiralMatrix[spiralRowEnd - 1][i - 1] = start;
            start += 1
        }

        spiralRowEnd -= 1;


        // Spiral Go Up Start Column
        for (let i = spiralRowEnd; i > spiralRowStart; i-= 1) {
            spiralMatrix[i - 1][spiralColStart] = start;
            start += 1;
        }

        spiralColStart += 1;
    }
    for (let el of spiralMatrix) {
        console.log(el.join(' '));
    }
}

buildSpiralMatrix(5, 5);
console.log('-----')
buildSpiralMatrix(3, 3);