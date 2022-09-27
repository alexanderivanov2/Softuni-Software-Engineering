function solve() {
    // Get Textareas
    let textareaElements = document.querySelectorAll('textarea');
    let textareaInputElement = textareaElements[0];
    let textareaOutputElement = textareaElements[1];
    // Get Buttons
    let buttonElements = document.querySelectorAll('button');
    let buttonGenerate = buttonElements[0];
    let buttonBuy = buttonElements[1];
    // Get Table Body 
    let tableBodyElement = document.querySelector('tbody')

    // EventListener for Generate Button
    buttonGenerate.addEventListener('click', (e) => {
        let textareaObjects = JSON.parse(textareaInputElement.value);
        for (let obj of textareaObjects) {
            // Create Table Row
            let createTr = document.createElement('tr');
            // Create and append Table Columns
            let createTd = document.createElement('td');
            let createImg = document.createElement('img');
            createImg.src = obj.img;
            createTd.appendChild(createImg);
            createTr.appendChild(createTd);
            // New Table column
            createTd = document.createElement('td');
            let createP = document.createElement('p');
            createP.textContent = obj.name;
            createTd.appendChild(createP);
            createTr.appendChild(createTd);
            // New Table Column
            createTd = document.createElement('td');
            createP = document.createElement('p')
            createP.textContent = obj.price;
            createTd.appendChild(createP);
            createTr.appendChild(createTd);
            // New Table Column
            createTd = document.createElement('td');
            createP = document.createElement('p')
            createP.textContent = obj.decFactor;
            createTd.appendChild(createP);
            createTr.appendChild(createTd);
            // Create and Add input checkbox
            createTd = document.createElement('td');
            createInput = document.createElement('input');
            createInput.type = 'checkbox';
            createTd.appendChild(createInput);
            createTr.appendChild(createTd);

            tableBodyElement.appendChild(createTr);
        }

        // Event Listener for Buy Button
        buttonBuy.addEventListener('click', (e) => {
            let inputElements = document.querySelectorAll('input[type="checkbox"]');
            let decorationFactorTotal = 0;
            let totalPrice = 0;
            let products = [];
         
            for (let inputEl of inputElements) {
                if (inputEl.checked) {
                    let td = inputEl.parentNode.previousSibling;
                    let decorationFactor = td.firstChild;
                    
                    td = td.previousSibling;
                    let price = td.firstChild;
        
                    td = td.previousSibling;
                    let name = td.firstChild;
                
                    products.push(name.textContent);
                    totalPrice += Number(price.textContent);
                    decorationFactorTotal += Number(decorationFactor.textContent);
                }
            }

            let avgDecFactor = decorationFactorTotal / products.length; 

            textareaOutputElement.value += `Bought furniture: ${products.join(', ')}\n`;
            textareaOutputElement.value += `Total price: ${totalPrice.toFixed(2)}\n`;
            textareaOutputElement.value += `Average decoration factor: ${avgDecFactor}`;
        });

    });
}