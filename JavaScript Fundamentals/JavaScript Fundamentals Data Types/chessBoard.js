function chessBoard(size){
    let color = 'black';
    console.log('<div class="chessboard">')
    
    for (let i = 1; i <= size; i++){
        console.log('  <div>');
        for (let j = 1; j <= size; j++){
            console.log(`    <span class="${color}"></span>`);
            color = color === 'black' ? 'white' : 'black';
        }
        if (size % 2 === 0){
            color = color === 'black' ? 'white' : 'black';
        }
        console.log('  </div>');
    }
    console.log('</div>')
}


chessBoard(6);