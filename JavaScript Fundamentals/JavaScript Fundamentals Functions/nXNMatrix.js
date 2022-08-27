function createSquareMatrixN(num) {
    let row = new Array(num).fill(num);
    
    for (let i = 0; i < num; i++) {
        console.log(row.join(' '));
    }
}

createSquareMatrixN(3);
createSquareMatrixN(7);