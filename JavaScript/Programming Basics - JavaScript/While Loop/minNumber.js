function minNumber(input){
    let minimum = Number.MAX_SAFE_INTEGER;
    let i = 0;
    let action = input[0];
    while(action !== 'Stop'){
        action = Number(action);
        if (action < minimum){
            minimum = action;
        }
        i++;
        action = input[i];
    }
    console.log(minimum);
}

minNumber(["100",
"99",
"80",
"70",
"Stop"]);