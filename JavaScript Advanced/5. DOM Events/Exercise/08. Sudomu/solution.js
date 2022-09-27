function solve() {
    let buttonCheckElement = document.querySelector('tfoot tr td button:first-child');
    let buttonClearElement = document.querySelector('tfoot tr td button:last-child');

    function getSodomuResult() {
        for (let i = 1; i < 4; i += 1) {
            let row = document.querySelectorAll(`tbody tr:nth-child(${i}) td input`);
            let column = document.querySelectorAll(`tbody tr td:nth-child(${i}) input`);

            let convertRow = convertQuerryCollection(row);
            let convertColumn = convertQuerryCollection(column);
        
            if (convertRow.size != 3 || convertColumn.size != 3) {
                return false;
            }
        }

        return true;
    };

    function convertQuerryCollection(querryCollection) {
        querryCollection = Array.from(querryCollection).map(el => el.value);
        return new Set(querryCollection);

    };

    buttonCheckElement.addEventListener('click', (e) => {
        let result = getSodomuResult();
        let tableElement = document.querySelector('table');
        let checkResultElement = document.querySelector('#check p');

        if (result) {
            tableElement.style.border = '2px solid green';
            checkResultElement.textContent = "You solve it! Congratulations!";
            checkResultElement.style.color = 'green';
        } else {
            tableElement.style.border = '2px solid red';
            checkResultElement.textContent = "NOP! You are not done yet...";
            checkResultElement.style.color = 'red';
        }
    });

    buttonClearElement.addEventListener('click', (e) => {
        let inputElements = document.querySelectorAll('tbody td input');
        inputElements = Array.from(inputElements);
        let tableElement = document.querySelector('table');
        let checkResultElement = document.querySelector('#check p');

        inputElements.forEach(el => el.value = '');
        tableElement.style.border = 'none';
        checkResultElement.textContent = '';
    })
}