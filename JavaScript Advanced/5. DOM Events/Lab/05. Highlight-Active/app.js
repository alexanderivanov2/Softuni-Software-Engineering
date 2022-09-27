function focused() {
    let divElements = document.querySelectorAll('input')
    divElements = Array.from(divElements);

    divElements.forEach(el => {
        el.addEventListener('focus', (e) => {
            el.parentNode.className = 'focused';
        })

        el.addEventListener('blur', (e) => {
            el.parentNode.className = '';
        })
    });
}