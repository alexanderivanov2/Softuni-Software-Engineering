function shopping (input) {
    let budget = Number(input[0]);
    let numOfVideoCards = Number(input[1]);
    let numOfCpus = Number(input[2]);
    let numOfRam = Number(input[3]);
    let videoCardsCost = numOfVideoCards * 250;
    let cpuPrice = numOfCpus * (videoCardsCost * 0.35);
    let ramPrice = numOfRam * (videoCardsCost * 0.10);
    let totalPrice = videoCardsCost + cpuPrice + ramPrice;
    if (numOfVideoCards > numOfCpus) {
        totalPrice *= 0.85;
    }
    if (budget >= totalPrice) {
        console.log(`You have ${(budget-totalPrice).toFixed(2)} leva left!`)
    } else {
        console.log(`Not enough money! You need ${(totalPrice-budget).toFixed(2)} leva more!`)
    }
}

shopping(["900",
"2",
"1",
"3"]);

shopping(["920.45",
"3",
"1",
"1"]);