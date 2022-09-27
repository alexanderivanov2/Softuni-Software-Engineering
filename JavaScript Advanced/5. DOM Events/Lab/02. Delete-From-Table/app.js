function deleteByEmail() {
    let tdEmailsElements = document.querySelectorAll('tbody tr td:last-child');
    let tbodyElement = document.querySelector('tbody');
    let divResultElement = document.getElementById('result');
    let inputElement = document.querySelector('input');
    let result = 'Not found.';
    let found = false;
    let searchElement = null;

    for (let td of tdEmailsElements) {
        if (td.textContent == inputElement.value) {
            let parrentElementForDelete = td.parentNode;
            tbodyElement.removeChild(parrentElementForDelete);
            result = 'Deleted.';
            found = true;
            break;
        }
    }

    divResultElement.textContent = result;
}