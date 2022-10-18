function validate() {
    let inputElement = document.getElementById('email');
    let emailRegEx = /\b[a-z]+\@[a-z]+\.[a-z]+\b/gm
    inputElement.addEventListener('change', (e) => {
        let valueOfInput = inputElement.value;

        if (!valueOfInput.match(emailRegEx)) {
            inputElement.className = 'error';
        } else {
            inputElement.className = '';
        }
    });
}