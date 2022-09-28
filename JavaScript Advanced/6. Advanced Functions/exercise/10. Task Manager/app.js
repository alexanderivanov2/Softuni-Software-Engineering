function solve() {
    // Add Task Elements
    let taskInputElement = document.querySelector('#task');
    let descTextareaElement = document.querySelector('#description');
    let dateInputElement = document.querySelector('#date');
    let buttonAddElement = document.querySelector('#add');

    buttonAddElement.addEventListener('click', addTask);

    // Open Section Div Element 
    let openSectionDiv = document.querySelector('section:nth-child(2) div:last-child');
    let inProgressDiv = document.querySelector('section:nth-child(3) div:last-child');
    let completeDiv = document.querySelector('section:last-child div:last-child');

    function addTask(event) {
        event.preventDefault();
        
        if (taskInputElement.value && descTextareaElement.value && dateInputElement.value) {
            // Create Article and append Heading
            let articleElement = document.createElement('article');
            let h3Element = document.createElement('h3');
            h3Element.textContent = taskInputElement.value;
            articleElement.appendChild(h3Element);
            // Add Paragraphs
            let pElementOne = document.createElement('p');
            let pElementTwo = document.createElement('p');
            pElementOne.textContent = `Description: ${descTextareaElement.value}`;
            articleElement.appendChild(pElementOne);
            pElementTwo.textContent = `Due Date: ${dateInputElement.value}`;
            articleElement.appendChild(pElementTwo);
            // Add div buttons
            let divElement = document.createElement('div');
            divElement.className = 'flex'
            let buttonStartElement = document.createElement('button');
            let buttonDeleteElement = document.createElement('button');

            buttonStartElement.className = 'green';
            buttonDeleteElement.className = 'red';
            
            buttonStartElement.textContent = 'Start';
            buttonDeleteElement.textContent = 'Delete';
            
            buttonStartElement.addEventListener('click', moveToInProgress);
            buttonDeleteElement.addEventListener('click', deleteArticle);
            
            divElement.appendChild(buttonStartElement);
            divElement.appendChild(buttonDeleteElement);
            
            articleElement.appendChild(divElement);
            // Add Article
            openSectionDiv.appendChild(articleElement);
            // Clear Add Task inputs
            taskInputElement.value = '';
            descTextareaElement.value = '';
            dateInputElement.value = '';
        }
    } 

    function moveToInProgress(event) {
        let currentTarget = event.currentTarget.parentNode.parentNode;
        let articleElement = document.createElement('article');

        articleElement.appendChild(currentTarget.querySelector('h3'));
        articleElement.appendChild(currentTarget.querySelector('p'));
        articleElement.appendChild(currentTarget.querySelector('p'));
        
        openSectionDiv.removeChild(currentTarget);

        // Add div buttons
        let divElement = document.createElement('div');
        divElement.className = 'flex'
        
        let buttonDeleteElement = document.createElement('button');
        let buttonFinishElement = document.createElement('button');

        buttonFinishElement.className = 'orange';
        buttonDeleteElement.className = 'red';

        buttonFinishElement.textContent = 'Finish';
        buttonDeleteElement.textContent = 'Delete';
            
        buttonFinishElement.addEventListener('click', moveToInComplete);
        buttonDeleteElement.addEventListener('click', deleteArticle);
        
        divElement.appendChild(buttonDeleteElement);
        divElement.appendChild(buttonFinishElement);
        
        articleElement.appendChild(divElement);
        inProgressDiv.appendChild(articleElement);
    }

    function deleteArticle(event) {
        let articleElement = event.currentTarget.parentNode.parentNode;
        articleElement.parentNode.removeChild(articleElement);
    }

    function moveToInComplete(event) {
        let currentTarget = event.currentTarget.parentNode.parentNode;
        let articleElement = document.createElement('article');

        articleElement.appendChild(currentTarget.querySelector('h3'));
        articleElement.appendChild(currentTarget.querySelector('p'));
        articleElement.appendChild(currentTarget.querySelector('p'));

        completeDiv.appendChild(articleElement);
        inProgressDiv.removeChild(currentTarget)
    }
}