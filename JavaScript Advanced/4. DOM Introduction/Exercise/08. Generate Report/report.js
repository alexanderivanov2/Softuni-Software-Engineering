function generateReport() {
    
    function getCheckedTHeadings(theaderElements) {
        let result = []
        for (let theadElements of theaderElements) {
            let name = theadElements.textContent.trim().toLowerCase();
            let isChecked = theadElements.getElementsByTagName('input')[0].checked;
            if (isChecked) {
                result.push(name);
            }
        }
        return result;
    }

    function getCheckedColumns() {
        let result = [];

        for (let check of checked) {
            let column = document.querySelectorAll(`tbody td:nth-child(${mapper[check]})`);
            result.push(column);
        }
        return result;
    }

    let mapper = {
        employee: 1,
        department: 2,
        status: 3,
        'date hired': 4,
        benefits: 5,
        compensation: 6,
        rating: 7
    }
    
    let getTHeaderElements = document.querySelectorAll('thead tr th');
    let checked = getCheckedTHeadings(getTHeaderElements);
    let columns = getCheckedColumns(checked);
    let columnLength = columns[0].length;

    let generateElements = [];
    
    for (let i = 0; i < columnLength; i++) {
        let obj = {};
        for (let j = 0; j < checked.length; j++) {
            let name = checked[j];
            let tdValue = columns[j][i].textContent;
            obj[name] = tdValue;
        }
        generateElements.push(obj);
    }

    // console.log(JSON.stringify(generateElements));
    let outputElement = document.getElementById('output');
    let outputResult = JSON.stringify(generateElements);

    outputElement.value = outputResult;
    // console.log(outputResult);
}

// function generateReport() {
//     const checkButtons = document.querySelectorAll('thead tr th input');
//     const table = document.querySelectorAll('tbody tr');

//     const buttons = [];
//     Array.from(checkButtons).forEach((btn, i) => {
//         buttons.push({ [btn.name]: btn.checked });
//     });

//     const result = [];
//     for (let row = 0; row < table.length; row++) {
//         const obj = {};
//         for (let col = 0; col < table[row].children.length; col++) {
//             const [type, bool] = Object.entries(buttons[col])[0];
//             if (bool) {
//                 obj[type] = table[row].children[col].textContent;
//             }
//         }
//         result.push(obj);
//     }
//     document.getElementById('output').value = JSON.stringify(result);
// }
