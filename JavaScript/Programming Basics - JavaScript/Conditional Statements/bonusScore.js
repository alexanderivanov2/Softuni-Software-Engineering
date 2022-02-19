function getBonusPoints (input) {
    let points = Number(input[0]);
    let bonusPoints = 0;

    if (points <= 100) {
        bonusPoints += 5;
    } else if (points > 1000) {
        bonusPoints = points * 0.10;
    } else {
        bonusPoints = points * 0.20
    }
    
    if (points % 2 === 0) {
        bonusPoints += 1;
    }
    if (points % 10 === 5) {
        bonusPoints += 2;
    }

    console.log(bonusPoints);
    console.log(points + bonusPoints);
}

getBonusPoints(["20"]);
getBonusPoints(["175"]);
getBonusPoints(["2703"]);
getBonusPoints(["15875"]);