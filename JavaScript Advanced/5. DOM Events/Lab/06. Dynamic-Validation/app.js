function validate() {
    let regExp = /[a-z]+\@[a-z]+\.[a-z]+/gm;

    let inputElement =document.getElementById('email');

    inputElement.addEventListener('change', (e) => {
        let valueElement = e.currentTarget.value
        let isValidate = valueElement.match(regExp);
        if (!isValidate && valueElement.length > 0) {
            e.currentTarget.className = 'error'
        } else {
            e.currentTarget.className = '';
        }
    });
}