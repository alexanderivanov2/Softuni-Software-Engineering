function logIn(input){
    let username = input[0];
    let password = input[1];
    let i = 2;
    while(true){
        let enteredPassword = input[i]
        if (password === enteredPassword) {
            console.log(`Welcome ${username}!`);
            break;
        }
        i++;
    }
}

logIn(["Nakov",
"1234",
"Pass",
"1324",
"1234"]);