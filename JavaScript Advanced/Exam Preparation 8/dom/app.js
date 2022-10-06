window.addEventListener('load', solve);

function solve() {
    const form = document.querySelector('form');
    const sectionReciveOrders = document.getElementById('received-orders');
    const sectionCompletedOrders = document.getElementById('completed-orders');

    form.querySelector('button').addEventListener('click', (e) => onSubmit(e));

    function onSubmit(e) {
        e.preventDefault();

        const select = form.querySelector('#type-product').value;
        const description = form.querySelector('#description').value;
        const clientName = form.querySelector('#client-name').value;
        const clientPhone = form.querySelector('#client-phone').value;

        console.log(select, description, clientName, clientPhone);
        if (description && clientName && clientPhone) {
            reciveProduct({select, description, clientName, clientPhone});
            form.reset();
        }
    }

    function reciveProduct(formDataObj) {
        const divContainer = createElement('div', sectionReciveOrders, '', ['class', 'container']);
        createElement('h2', divContainer, `Product type for repair: ${formDataObj.select}`);
        createElement('h3', divContainer, `Client information: ${formDataObj.clientName}, ${formDataObj.clientPhone}`);
        createElement('h4', divContainer, `Description of the problem: ${formDataObj.description}`);
        const btnStart = createElement('button', divContainer, 'Start repair', ['class', 'start-btn']);
        const btnFinish = createElement('button', divContainer, 'Finish repair', ['class', 'finish-btn', 'disabled', 'true']);

        btnStart.addEventListener('click', (e) => {
            e.preventDefault();
            e.currentTarget.setAttribute('disabled', 'true');
            e.currentTarget.nextSibling.removeAttribute('disabled', 'false');
        });

        btnFinish.addEventListener('click', (e) => {
            e.preventDefault();
            const product = e.currentTarget.parentNode;
            e.currentTarget.previousSibling.remove();
            e.currentTarget.remove();
            sectionCompletedOrders.appendChild(product);
        });
    }

    sectionCompletedOrders.querySelector('button').addEventListener('click', (e) => {
        e.preventDefault();
        Array.from(sectionCompletedOrders.querySelectorAll('.container')).forEach(div => div.remove());
    })

    function createElement(type, parent='', content='', attributes=[]) {
        const el = document.createElement(type);

        if (parent) {
            parent.appendChild(el);
        }

        if (content) {
            el.textContent = content;
        }

        for (let i = 0; i < attributes.length; i+=2) {
            el.setAttribute(attributes[i], attributes[i + 1]);
        }

        return el;
    }
}