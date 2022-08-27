function validatePassword(password) {
    let checkPasswordLength = x => x.length >= 6 && x.length <= 10;
    let checkOnlyLettersAndDigits = str => /^[A-Za-z0-9]*$/.test(str);
    let checkAtLeast2Digits = str => str.match(/\d+/);

    if (checkPasswordLength(password) && checkOnlyLettersAndDigits(password) && checkAtLeast2Digits(password) && checkAtLeast2Digits(password)[0].length >= 2) {
        console.log("Password is valid");
    } else {
        if (!checkPasswordLength(password)) {
            console.log("Password must be between 6 and 10 characters");
        }        
        if (!checkOnlyLettersAndDigits(password)) {
            console.log("Password must consist only of letters and digits");
        }
        if (!checkAtLeast2Digits(password) || checkAtLeast2Digits(password)[0].length < 2) {
            console.log("Password must have at least 2 digits");
        }
    }
}

validatePassword('logIn');
validatePassword('MyPass123');
validatePassword('Pa$s$s')

// console.log('MyPass123'.match(/\d+/)[0].length);
// console.log('MyPass'.match(/\d+/));