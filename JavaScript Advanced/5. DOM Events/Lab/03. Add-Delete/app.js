function addItem() {
    let ulElements = document.getElementById('items');
    let inputElement = document.getElementById('newItemText');
    

    let createLiElement = document.createElement('li');
    createLiElement.textContent = inputElement.value;
    inputElement.value = '';
    let createAElement = document.createElement('a');
    
    createAElement.textContent = '[Delete]';
    createAElement.href = '#'; 
    // can addEventListener here for 'a' element!
    createLiElement.appendChild(createAElement);
    ulElements.appendChild(createLiElement);

    let aElements = document.querySelectorAll('a');
    aElements = Array.from(aElements);
    aElements.forEach(el => {
        el.addEventListener('click', (e) =>{
            let currentElement = e.currentTarget;
            currentElement.parentNode.remove();
        });
    });
}