function calculateSpices(spice) {
    let days = 0;
    let spices = spice;
    const workersConsume = 26;
    let totalSpices = 0;
    while (spices >= 100){
        days += 1;
        totalSpices += spices;
        spices -= 10;
        totalSpices -= workersConsume;
    }
    if (days > 0){
        totalSpices -= workersConsume;
    }
    console.log(days);
    console.log(totalSpices);
}

calculateSpices(111);
calculateSpices(450);