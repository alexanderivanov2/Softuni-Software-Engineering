function calculator(numOne, numTwo, operator) {
    let result;
    let add = (a, b) => a + b;
    let subtract = (a, b) => a - b;
    let multiply = (a, b) => a * b;
    let divide = (a, b) => a / b;

    if (operator === 'add') {
        result = add(numOne, numTwo);
    } else if (operator === 'subtract') {
        result = subtract(numOne, numTwo);
    } else if (operator === 'multiply') {
        result = multiply(numOne, numTwo);
    } else if (operator === 'divide') {
        result = divide(numOne, numTwo);
    }

    console.log(result);
}

calculator(26, 58, 'add');