function login(input) {
    let username = input[0];
    let passwords = input;
    let password = '';
    for (let i = username.length - 1; i >= 0; i--){
        password += username[i];
    }

    for (let i = 1; i <= input.length - 1; i++){
        if (passwords[i] === password){
            console.log(`User ${username} logged in.`);
            return;
        } else if(i === input.length - 1){
            console.log(`User ${username} blocked!`);
            return;
        }
        console.log('Incorrect password. Try again.')
    }  
}


login(['Acer','login','go','let me in','recA']);
login(['sunny','rainy','cloudy','sunny','not sunny']);