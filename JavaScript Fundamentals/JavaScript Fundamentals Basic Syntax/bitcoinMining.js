function calculateBitcoin(input) {
    const priceForOneBitcoin = 11949.16;
    const priceForOneGramGold = 67.51;
    let golds = input;
    let dayOfFirstBoughtBitcoin = 0;
    let bitcoins = 0;
    let leva = 0;
    let day = 0;
    for (let i = 0; i < golds.length; i++){
        day += 1;
        let gold = golds[i];
        if (day % 3 === 0){
            gold *= 0.70;
        }
        leva += gold * priceForOneGramGold;
        while (leva >= priceForOneBitcoin) {
            if (dayOfFirstBoughtBitcoin === 0){
                dayOfFirstBoughtBitcoin = day;
            }
            bitcoins += 1;
            leva -= priceForOneBitcoin;
        }
    }
    console.log(`Bought bitcoins: ${bitcoins}`);
    if (dayOfFirstBoughtBitcoin !== 0){
        console.log(`Day of the first purchased bitcoin: ${dayOfFirstBoughtBitcoin}`);
    }
    console.log(`Left money: ${leva.toFixed(2)} lv.`);
}

calculateBitcoin([50, 100]);
calculateBitcoin([3124.15, 504.212, 2511.124]);