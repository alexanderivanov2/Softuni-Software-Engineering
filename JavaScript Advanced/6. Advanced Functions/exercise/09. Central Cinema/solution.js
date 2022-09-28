function solve() {
    let buttonOnScreenElement = document.querySelector('#container button');
    let buttonClearElement = document.querySelector('#archive button');
    let onScreenUlElement = document.querySelector('#movies ul');
    let archiveUlElement = document.querySelector('#archive ul');

    buttonOnScreenElement.addEventListener('click', onScreen);
    buttonClearElement.addEventListener('click', clearArchive);
           
    function onScreen(event) {
        event.preventDefault();
        let nameElement = document.querySelector('#container input:nth-child(1)');
        let hallElement = document.querySelector('#container input:nth-child(2)');
        let priceElement = document.querySelector('#container input:nth-child(3)');
        
        if (nameElement.value && hallElement.value && priceElement.value && !isNaN(priceElement.value)) {
            // Create li and append to him span, strong
            let li = document.createElement('li');
            let span = document.createElement('span');
            span.textContent = nameElement.value;
            li.appendChild(span);
            let strong = document.createElement('strong');
            strong.textContent = `Hall: ${hallElement.value}`;
            li.appendChild(strong);
            // Create div and append to him strong, input
            let div = document.createElement('div');
            let divStrong = document.createElement('strong');
            divStrong.textContent = Number(priceElement.value).toFixed(2);
            div.appendChild(divStrong);
            let input = document.createElement('input');
            input.placeholder = 'Tickets Sold';
            div.appendChild(input);
            // Create Button add event listener to him and append it to div
            let button = document.createElement('button');
            button.textContent ='Archive';
            button.addEventListener('click', archive)
            div.appendChild(button);

            // append div to li;
            li.appendChild(div);
            onScreenUlElement.appendChild(li);

            // Clear Elements 
            nameElement.value = '';
            hallElement.value = '';
            priceElement.value = '';
        }
    }

    function archive(event) {
        let CurrentTargetLi = event.currentTarget.parentNode.parentNode;
        // Get Name, price ticket solds
        let currentTarget = event.currentTarget;
        let ticketsSold = currentTarget.previousSibling.value;
        let price = currentTarget.parentNode.children[0].textContent;
        let nameElement = currentTarget.parentNode.parentNode.children[0].textContent;
        // Check ticketsSold available
        if (ticketsSold.length > 0 && !isNaN(Number(ticketsSold))) {
            // add li element and li innerHTML content
            let liElement = document.createElement('li');
           
            let spanElement = document.createElement('span');
            spanElement.textContent = nameElement;
            liElement.appendChild(spanElement);
            
            let strongElement = document.createElement('strong');
            let totalSum = Number(ticketsSold) * Number(price);
            strongElement.textContent = `Total amount: ${totalSum.toFixed(2)}`;
            liElement.appendChild(strongElement);
           
            let buttonElement = document.createElement('button');
            buttonElement.textContent = 'Delete';
            buttonElement.addEventListener('click', deleteArchiveElement)
            liElement.appendChild(buttonElement);

            archiveUlElement.appendChild(liElement);
            onScreenUlElement.removeChild(CurrentTargetLi);
        }
    }

    function deleteArchiveElement(event) {
        let currentTargetElement = event.currentTarget.parentNode;
        archiveUlElement.removeChild(currentTargetElement);
    }

    function clearArchive() {
        while(archiveUlElement.firstChild) {
            archiveUlElement.removeChild(archiveUlElement.firstChild);
        }
    }
}