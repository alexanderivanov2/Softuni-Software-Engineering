function addItem() {
    let ulElement = document.getElementById('items');
    let inputTextElement = document.getElementById('newItemText');
    let newLiElement = document.createElement('li');

    newLiElement.textContent = inputTextElement.value;
    ulElement.appendChild(newLiElement);
    // clear input text element 
    inputTextElement.value = '';
}