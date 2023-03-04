let urlArticles = 'http://localhost:3030/jsonstore/advanced/articles/list';
let urlDetails = 'http://localhost:3030/jsonstore/advanced/articles/details/';
let sectionElement = document.getElementById('main');

function solution() {
    fetch(urlArticles)
        .then(response => {
            if (response.status != 200) {
                throw new Error('Error');
            }

            return response.json();
        })
        .then(data => {
            data.forEach(el => {
                let divAccordion = createElement('div', sectionElement, '', ['accordion']);
                let divHead = createElement('div', divAccordion, '', ['head']);
                createElement('span', divHead, el.title);
                let btn = createElement('button', divHead, 'More', ['button'], el._id);

                btn.addEventListener('click', accordionManage);
            });
        })
        .catch(error => console.log(error.message));
}



function createElement(type, parentEl, content, classes, id) {
    let element = document.createElement(type);
    parentEl.appendChild(element);

    if (content) {
        element.textContent = content;
    }

    if (classes) {
        while (classes.length > 0) {
            element.classList.add(classes.shift());
        }
    }
   
    if (id) {
        element.id = id;
    }

    return element;
}


function accordionManage(event) {
    let id = event.currentTarget.id;
    let parentEl = event.currentTarget.parentNode.parentNode;
    let divExtraElement = parentEl.querySelector('.extra');

    if (event.currentTarget.textContent == 'More') {
        event.currentTarget.textContent = 'Less';

        fetch(urlDetails + id)
        .then(response => {
            if (response.status != 200) {
                throw new Error('Error');
            }

            return response.json();
        })
        .then(data => {
            console.log(data.content);
            let divExtra = createElement('div', parentEl, '', ['extra']);
            divExtra.style.display = 'block';
            createElement('p', divExtra, data.content);
        })
        .catch(error => console.log(error.message));
    } else {
        
        event.currentTarget.textContent = 'More';
        divExtraElement.style.display = 'none';
        divExtraElement.remove();

    }
    
}

solution();