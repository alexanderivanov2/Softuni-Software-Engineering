function sumTable() {
    let tdSecondElements = document.querySelectorAll('tr td:last-child');
    // let result = Array.from(tdSecondElements).reduce((a, x) => {
    //     let sum = Number(x.textContent) || 0;
    //     return a + sum;
    // }, 0);
    // let totalElement = document.getElementById('sum');
    // totalElement.textContent = result; 
    
    let tdElements = Array.from(tdSecondElements);
    let sum = tdElements.pop();
    let result = 0;
    for (let el of tdElements) {
        result += Number(el.textContent);
    }

    sum.textContent = result;
}