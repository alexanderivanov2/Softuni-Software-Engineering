function getMaxNumber(input){
    let maxNumber =  Number.MIN_SAFE_INTEGER;
    let i = 0;
    let action = input[i];
    while(action !== 'Stop'){
        action = Number(action);
        if (action > maxNumber){
            maxNumber = action;
        }
        i++;
        action = input[i];
    }
    console.log(maxNumber);
}


getMaxNumber(["45",
"-20",
"7",
"99",
"Stop"]);