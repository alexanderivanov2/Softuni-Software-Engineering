function solve() {
    let number = document.getElementById('input');
    let convertResult = document.getElementById('result');
    let selectedElement = document.getElementById('selectMenuTo');

    const binary = document.createElement('option');
    binary.setAttribute('value', 'binary');
    binary.textContent = 'Binary';

    const hexadecimal = document.createElement('option');
    hexadecimal.setAttribute('value', 'hexadecimal');
    hexadecimal.textContent = 'Hexadecimal';

    selectedElement.appendChild(binary);
    selectedElement.appendChild(hexadecimal);

    document.querySelector('button').addEventListener('click', (x) => {
        console.log(selectedElement.value);
        if (selectedElement.value == 'binary') {
            convertResult.value = Number(number.value).toString(2);
    
        } else if (selectedElement.value == 'hexadecimal') {
            convertResult.value = Number(number.value).toString(16).toUpperCase();
        } else {
            convertResult.value = '';
        }
    });

}