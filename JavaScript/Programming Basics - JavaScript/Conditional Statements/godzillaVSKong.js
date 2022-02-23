function movieCalculations (input) {
    let budget = Number(input[0]);
    let numOfPeople = Number(input[1]);
    let priceForClothes = Number(input[2]);
    if (numOfPeople > 150) {
        priceForClothes *= 0.90;
    }
    let priceForDecorations = budget * 0.10;
    let totalCost = priceForDecorations + (priceForClothes * numOfPeople);
    if (totalCost > budget) {
        console.log(`Not enough money!\nWingard needs ${(totalCost-budget).toFixed(2)} leva more.`);
    } else {
        console.log(`Action!\nWingard starts filming with ${(budget-totalCost).toFixed(2)} leva left.`);
    }
}

movieCalculations(["20000",
"120",
"55.5"]);

movieCalculations(["15437.62",
"186",
"57.99"]);

movieCalculations(["9587.88",
"222",
"55.68"]);