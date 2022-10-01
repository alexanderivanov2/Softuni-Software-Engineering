function solve() {
    // Input and Values of Input
    let inputElementTask = document.getElementById('task');
    let inputElementDescription = document.getElementById('description');
    let inputElementDate = document.getElementById('date');
    
    let openSectionDivElement = document.querySelector('.wrapper section:nth-child(2) div:last-child');
    let inProgressDivElement = document.querySelector('.wrapper section:nth-child(3) div:last-child');
    let completeDivElement = document.querySelector('.wrapper section:last-child div:last-child');
    let btnAdd = document.getElementById('add');
    
   
    btnAdd.addEventListener('click', e => {
        e.preventDefault();
        let taskValue = inputElementTask.value;
        let descriptionValue = inputElementDescription.value;
        let dateValue = inputElementDate.value;
        if(taskValue && descriptionValue && dateValue) {
            let articleElement = document.createElement('article');
            let headingElement = document.createElement('h3');
            let paragraphDescriptionElement = document.createElement('p');
            let paragraphDateElement = document.createElement('p');
            let divElement = document.createElement('div');
            let buttonStartElement = document.createElement('button');
            let buttonDeleteElement = document.createElement('button');

            headingElement.textContent = `${taskValue}`
            paragraphDescriptionElement.textContent = `Description: ${descriptionValue}`;
            paragraphDateElement.textContent = `Due Date: ${dateValue}`;

            divElement.className = 'flex';
            buttonStartElement.className = 'green';
            buttonDeleteElement.className = 'red';
            buttonStartElement.textContent = 'Start';
            buttonDeleteElement.textContent = 'Delete';
            buttonDeleteElement.addEventListener('click', deleteNode);
            buttonStartElement.addEventListener('click', moveElementToInProgress);

            divElement.appendChild(buttonStartElement);
            divElement.appendChild(buttonDeleteElement);

            articleElement.appendChild(headingElement);
            articleElement.appendChild(paragraphDescriptionElement);
            articleElement.appendChild(paragraphDateElement);
            articleElement.appendChild(divElement);
            openSectionDivElement.appendChild(articleElement);
        }
        inputElementTask.value = '';
        inputElementDescription.value = '';
        inputElementDate.value = '';
    });

    function deleteNode(e) {
        let parrentNode = e.currentTarget.parentNode.parentNode;
        parrentNode.remove();
    }

    function moveElementToInProgress(e) {
        let parentNode = e.currentTarget.parentNode.parentNode;
        inProgressDivElement.appendChild(parentNode);
        let divElement =  e.currentTarget.parentNode;
        e.currentTarget.remove();

        let btnFinish = document.createElement('button');
        btnFinish.className = 'orange';
        btnFinish.textContent = 'Finish';
        btnFinish.addEventListener('click', moveToComplete);
        divElement.appendChild(btnFinish);
    }

    function moveToComplete(e) {
        let parentNode = e.currentTarget.parentNode.parentNode;
        let divElement = e.currentTarget.parentNode;
        divElement.remove();
        completeDivElement.appendChild(parentNode);
    }
}