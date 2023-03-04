let mainElement = document.getElementById('main');
let url = 'http://localhost:3030/jsonstore/advanced/profiles';

function lockedProfile() {
    mainElement.replaceChildren();
    
    fetch(url)
        .then(response => {
            if (response.status != 200) {
                throw new Error('Error');
            }

            return response.json();
        })
        .then(data => {
            for (let obj of Object.values(data)) {
                // div
                let divProfile = createElement(mainElement, 'div', ['profile']);
                // img
                let img = createElement(divProfile, 'img', ['userIcon']);
                img.src = "./iconProfile2.png";
                // radio buttons
                createElement(divProfile, 'label', [], 'Lock');
                let lockRadio = createElement(divProfile, 'input', [], '', 'radio', 'user1Locked', 'lock');
                createElement(divProfile, 'label', [], 'Unlock');
                createElement(divProfile, 'input', [], '', 'radio', 'user1Locked', 'unlock');
                // username
                createElement(divProfile, 'label', [], 'Username');
                
                let username = createElement(divProfile, 'input', [], '', 'text', 'user1Locked', obj.username);
                username.disabled = 'true';
                username.readonly = 'true';
                // div hidden info
                let divHiddenInfo = createElement(divProfile, 'div', ['hiddenInfo']);
                // createElement(divHiddenInfo, 'hr');
                createElement(divHiddenInfo, 'label', [], 'Email:');
                let inputEmail = createElement(divHiddenInfo, 'input', [], '', 'email', 'user1Email', obj.email);
                inputEmail.disabled = 'true';
                inputEmail.readonly = 'true';
                // Age
                createElement(divHiddenInfo, 'label', [], 'Age:');
                let inputAge = createElement(divHiddenInfo, 'input', [], '', 'number', 'user1Age', obj.age);
                inputAge.disabled = 'true';
                inputAge.readonly = 'true';
                // button
                let btn = createElement(divProfile, 'button', [], 'Show more');

                btn.addEventListener('click', infoManage);
                
            }
        })
        .catch(err => {
            console.log(err);
        })
}


function createElement(parrent, type, classes, content, inputType, inputName, inputValue) {
    let element = document.createElement(type);
    parrent.appendChild(element);
    
    while(classes.length > 0) {
        element.classList.add(classes.shift());
    }

    if (content) {
        element.textContent = content;
    }

    if (inputType) {
        element.type = inputType;
    }

    if (inputName) {
        element.name = inputName;
    }

    if (inputValue) {
        element.value = inputValue
    }

    if (inputValue == 'lock') {
        element.setAttribute('checked', 'true');
    }

    return element;
}

function infoManage(event) {
    let parent = event.currentTarget.parentNode;
    let divHidden = event.currentTarget.previousSibling;
    let lock = parent.querySelector('input');

    if (!lock.checked) {
        if(event.currentTarget.textContent == 'Show more') {
            event.currentTarget.textContent = 'Hide it';
            divHidden.classList.remove('hiddenInfo');
            
        } else {
            event.currentTarget.textContent = 'Show more';
            divHidden.classList.add('hiddenInfo');
        }
    }
}