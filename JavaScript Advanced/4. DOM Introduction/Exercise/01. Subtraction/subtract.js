function subtract() {
    let inputElement1 = document.getElementById('firstNumber');
    let inputElement2 = document.getElementById('secondNumber');
    let result = document.getElementById('result');
    result.textContent = Number(inputElement1.value) - Number(inputElement2.value);
}