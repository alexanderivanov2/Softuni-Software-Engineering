function mathOperations(a, b, operator) {
    const mathAdd = (a, b) => a + b;
    const mathReduce = (a, b) => a - b;
    const mathMultiply = (a, b) => a * b;
    const mathDevide = (a, b) => a / b;
    const mathPiece = (a, b) => a % b;
    const mathPower = (a, b) => a ** b;
    
    switch (operator) {
        case '+': console.log(mathAdd(a, b)); break;
        case '-': console.log(mathReduce(a, b)); break;
        case '*': console.log(mathMultiply(a, b)); break;
        case '/': console.log(mathDevide(a, b)); break;
        case '%': console.log(mathPiece(a, b)); break;
        case '**': console.log(mathPower(a, b)); break;
    }
}

mathOperations(5, 6, '+');
mathOperations(3, 5.5, '*');