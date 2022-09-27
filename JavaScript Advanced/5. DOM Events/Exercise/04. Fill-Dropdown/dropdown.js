function addItem() {
    let selectElement = document.getElementById('menu');
    let inputTextElement = document.getElementById('newItemText');
    let inputValueElement = document.getElementById('newItemValue');
    let createOptionElement = document.createElement('option');

    createOptionElement.textContent = inputTextElement.value;
    createOptionElement.value = inputValueElement.value;
    selectElement.appendChild(createOptionElement);
    
    inputTextElement.value = '';
    inputValueElement.value = '';
}