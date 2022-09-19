function printMoneyForFruit(fruit, weight, moneyForKg) {
    weight /= 1000;
    let moneyCost = weight * moneyForKg;
    console.log(`I need $${moneyCost.toFixed(2)} to buy ${weight.toFixed(2)} kilograms ${fruit}.`);
}

printMoneyForFruit('orange', 2500, 1.80);


