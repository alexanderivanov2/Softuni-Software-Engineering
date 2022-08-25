function printTriangle(inputRows) {
    let rows = inputRows;
    for (let i = 1; i <= rows; i++){
        let rowString = '';
        for (let j = 1; j <= i; j++){
            rowString += `${i} `;
        }
        console.log(rowString);
    }
}


printTriangle(6);