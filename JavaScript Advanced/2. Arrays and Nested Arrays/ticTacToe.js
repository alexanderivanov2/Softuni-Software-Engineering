function ticTacToe(moves) {
    let board = [
    [false, false, false],
    [false, false, false],
    [false, false, false]];
    let move = 1;

    function checkForWin(board) {
        if ((board[0][0] === board[0][1] && board[0][1] === board[0][2])
        || (board[1][0] === board[1][1] && board[1][1] === board[1][2]) ||
        (board[2][0] === board[2][1] && board[2][1] === board[2][2])) {
            return true;
        }
        if ((board[0][0] === board[1][0] && board[1][0] === board[2][0])
        || (board[0][1] === board[1][1] && board[1][1] === board[2][1]) ||
        (board[0][2] === board[1][2] && board[1][2] === board[2][2])) {
            return true;
        }
        if ((board[0][0] === board[1][1] && board[1][1] === board[2][2])
        || (board[0][2] === board[1][1] && board[1][1] === board[2][0])) {
            return true;
        }
        return false;
    }

    let printBoard = function(board) {
        for (let el of board) {
            console.log(el.join('\t'));
        }
    }

    for (let el of moves) {
        let [y, x] = el.split(' ')
        y = Number(y);
        x = Number(x);
        if (board[y][x] != false){
            console.log("This place is already taken. Please choose another!");
            continue;
        }
        let player = move % 2 == 0 ? 'O' : 'X';
        board[y][x] = player;
        if (move > 4) {
            let isWin = checkForWin(board);
            if (isWin) {
                console.log(`Player ${player} wins!`);
                printBoard(board);
                return;
            }
        } 
        if (move == 9) {
            console.log("The game ended! Nobody wins :(");
            printBoard(board);
            return;
        }
        move += 1;
    }
}


ticTacToe(["0 1",
"0 0",
"0 2", 
"2 0",
"1 0",
"1 1",
"1 2",
"2 2",
"2 1",
"0 0"]);

ticTacToe(["0 0",
"0 0",
"1 1",
"0 1",
"1 2",
"0 2",
"2 2",
"1 2",
"2 2",
"2 1"]);

ticTacToe(["0 1",
"0 0",
"0 2",
"2 0",
"1 0",
"1 2",
"1 1",
"2 1",
"2 2",
"0 0"]);