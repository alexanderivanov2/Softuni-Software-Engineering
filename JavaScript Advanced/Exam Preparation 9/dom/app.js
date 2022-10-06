function solve() {
    console.log('hi');
    const tbodyElement = document.getElementById('tbody');
    const spanBudget = document.getElementById('sum');

    const firstName = document.getElementById('fname');
    const lastName = document.getElementById('lname');
    const email = document.getElementById('email');
    const birth = document.getElementById('birth');
    const position = document.getElementById('position');
    const salary = document.getElementById('salary');
    
    const buttonAddWorker = document.getElementById('add-worker');

    buttonAddWorker.addEventListener('click', onSubmit);

    function onSubmit(e) {
        e.preventDefault();
        if (firstName.value && lastName.value && email.value && birth.value && position.value && salary.value) {
            const obj = {
                firstName: firstName.value,
                lastName: lastName.value,
                email: email.value,
                birth: birth.value,
                position: position.value,
                salary: salary.value
            }
            createTableRow(obj);
            addBudget(salary.value);
            document.querySelector('form').reset();
        }
    }

    function addBudget(value) {
        spanBudget.textContent = (Number(spanBudget.textContent) + Number(value)).toFixed(2);
    }

    function reduceBudget(value) {
        spanBudget.textContent = (Number(spanBudget.textContent) - Number(value)).toFixed(2);
    }

    function createTableRow(data) {
        const trElement = createElement('tr', tbodyElement);
        createElement('td', trElement, data.firstName);
        createElement('td', trElement, data.lastName);
        createElement('td', trElement, data.email);
        createElement('td', trElement, data.birth);
        createElement('td', trElement, data.position);
        createElement('td', trElement, data.salary);
        const tdBtns = createElement('td', trElement);
        const btnFired = createElement('button', tdBtns, 'Fired', ['class', 'fired']);
        const btnEdit = createElement('button', tdBtns, 'Edit', ['class', 'edit'] );

        btnFired.addEventListener('click', (e) => {
            e.preventDefault();
            const tdSalary = e.target.parentNode.previousSibling;
            reduceBudget(tdSalary.textContent);
            e.target.parentNode.parentNode.remove();
        });

        btnEdit.addEventListener('click', (e) => editWorker(e, data));
    }

    function editWorker(e, data) {
        e.preventDefault();const tdSalary = e.target.parentNode.previousSibling;
        reduceBudget(tdSalary.textContent);
        e.target.parentNode.parentNode.remove();
        firstName.value = data.firstName;
        lastName.value = data.lastName;
        email.value = data.email;
        birth.value = data.birth;
        position.value = data.position;
        salary.value = data.salary;
    }
    
    function createElement(type, parent='', context='', attributes=[]){
        const el = document.createElement(type);

        if(context) {
            el.textContent = context;
        }

        for(let i = 0; i < attributes.length; i+=2) {
            el.setAttribute(attributes[i], attributes[i + 1]);
        }

        if(parent) {
            parent.appendChild(el);
        }

        return el;
    }
}

solve()