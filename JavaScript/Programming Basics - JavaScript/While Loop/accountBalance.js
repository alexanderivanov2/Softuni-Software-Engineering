function updateBalance(input){
    let balance = 0;
    let i = 0;
    let action = input[i];
    while(action !== 'NoMoreMoney'){
        action = Number(action);
        if (action < 0){
            console.log('Invalid operation!');
            break;
        }
        balance += action;
        console.log(`Increase: ${action.toFixed(2)}`);
        i++;
        action = input[i];
    }
    console.log(`Total: ${balance.toFixed(2)}`);
}

updateBalance(["120",
"45.55",
"-150"]);