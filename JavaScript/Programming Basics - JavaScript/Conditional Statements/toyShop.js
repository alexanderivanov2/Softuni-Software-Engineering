function toyShopTravel (input) {
    let profit = 0;
    let priceForTravel = Number(input[0]);
    let numPuzzles = Number(input[1]);
    let numTalkingDolls = Number(input[2]);
    let numTeddyBear = Number(input[3]);
    let numMinnions = Number(input[4]);
    let numTrucks = Number(input[5]);
    let totalToys = numPuzzles + numTalkingDolls + numTeddyBear + numMinnions + numTrucks;
    profit += numPuzzles * 2.60;
    profit += numTalkingDolls * 3;
    profit += numTeddyBear * 4.10;
    profit += numMinnions * 8.20;
    profit += numTrucks * 2;
    if (totalToys >= 50) {
        profit *= 0.75
    }
    profit *= 0.90;
    if (profit >= priceForTravel) {
        console.log(`Yes! ${(profit-priceForTravel).toFixed(2)} lv left.`);
    } else {
        console.log(`Not enough money! ${(priceForTravel - profit).toFixed(2)} lv needed.`)
    }
}


// toyShopTravel(["40.8",
// "20",
// "25",
// "30",
// "50",
// "10"]);

toyShopTravel(["320",
"8",
"2",
"5",
"5",
"1"]);