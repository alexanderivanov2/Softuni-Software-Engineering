function validate() {
    let buttonElement = document.getElementById('submit');
    let usernameInput = document.getElementById('username');
    let emailInput = document.getElementById('email');
    let passwordInput = document.getElementById('password');
    let confirmPasswordInput = document.getElementById('confirm-password');
    let companyCheckboxInput = document.getElementById('company');
    let filedsetElement = document.getElementById('companyInfo');
    let companyNumberInput = document.getElementById('companyNumber');
    let divValidElement = document.getElementById('valid');

    buttonElement.addEventListener('click', validateInputs);
    companyCheckboxInput.addEventListener('change', showCompanyInputs);
   
    function showCompanyInputs() {

        if (companyCheckboxInput.checked) {
            filedsetElement.style.display = 'block';
        } else {
            filedsetElement.style.display = 'none';
        }
    }

    function validateInputs(e) {
        e.preventDefault();
        let validOut = [];
        let patternUsernameRegEx = /^[a-zA-Z0-9]{3,20}$/gm;
        let patternPasswordRegEx = /^[\w]{5,15}$/gm;
        let patternEmailRegEx = /^[^@.]+@[^@]*\.[^@]*$/gm;

        if (usernameInput.value.match(patternUsernameRegEx)) {
            validOut.push(true);
            usernameInput.style.borderColor = '';
        } else {
            validOut.push(false);
            usernameInput.style.borderColor = 'red';
        }
        
        if (emailInput.value.match(patternEmailRegEx)) {
            validOut.push(true);
            emailInput.style.borderColor = '';
        } else {
            validOut.push(false);
            emailInput.style.borderColor = 'red';
        }

        if (passwordInput.value.match(patternPasswordRegEx) && confirmPasswordInput.value.match(patternPasswordRegEx) && passwordInput.value === confirmPasswordInput.value) {
            validOut.push(true);
            passwordInput.style.borderColor = '';
            confirmPasswordInput.style.borderColor = '';
        } else {
            validOut.push(false);
            passwordInput.style.borderColor = 'red';
            confirmPasswordInput.style.borderColor = 'red';
        }

        if (companyCheckboxInput.checked) {
            if (Number(companyNumberInput.value) >= 1000 && Number(companyNumberInput.value) <= 9999) {
                validOut.push(true);
                companyNumberInput.style.borderColor = '';
            } else {
                validOut.push(false);
                companyNumberInput.style.borderColor = 'red'
            }
        }
       
    
        if (!validOut.includes(false)) {
            divValidElement.style.display = 'block';
        } else {
            divValidElement.style.display = 'none'
        }
    };
}