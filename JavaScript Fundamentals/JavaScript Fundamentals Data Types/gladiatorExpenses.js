function gladiatorExpenses(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice){
    let expenses = 0;
    shieldsBrakes = 0;
    for (let i = 1; i <= lostFights; i++){
        if (i % 2 === 0 && i % 3 === 0){
            expenses += helmetPrice + swordPrice + shieldPrice;
            shieldsBrakes += 1;
            if (shieldsBrakes % 2 === 0){
                expenses += armorPrice;
            }
        } else if(i % 2 === 0){
            expenses += helmetPrice;
        } else if(i % 3 === 0){
            expenses += swordPrice;
        } 
    }
    console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`);
}

gladiatorExpenses(7,
    2,
    3,
    4,
    5);

gladiatorExpenses(23,
    12.50,
    21.50,
    40,
    200);