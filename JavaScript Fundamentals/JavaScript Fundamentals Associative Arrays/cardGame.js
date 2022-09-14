function cardGame (arr) {
    let objArr = {};
    let objScores = {
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
        'S': 4,
        'H': 3,
        'D': 2,
        'C': 1
    }

    for (let el of arr) {
        let [name, ...cards] = el.split(': ');
        cards = cards[0].split(', ');
        if (!objArr.hasOwnProperty(name)) {
           objArr[name] = {points: 0}; 
        } 
        for (let el of cards) {
            let points = 0;
            let[firstPart, SecondPart] = el.split('');
            if (el.length === 3) {
                firstPart = el.slice(0, 2);
                SecondPart = el.slice(2);
            }

            if (objArr[name].hasOwnProperty(el)) {
                continue;
            }
            if (isNaN(firstPart)) {
                points += objScores[firstPart];
            } else {
                points += Number(firstPart);
            }
            points *= objScores[SecondPart];
            objArr[name][el] = points;
            objArr[name]['points'] += points;

        }
    }
    for (let [key, value] of Object.entries(objArr)) {
            console.log(`${key}: ${objArr[key]['points']}`);
    }
}


cardGame([
    'Peter: 2C, 4H, 9H, AS, QS',
    'Tomas: 3H, 10S, JC, KD, 5S, 10S',
    'Andrea: QH, QC, QS, QD',
    'Tomas: 6H, 7S, KC, KD, 5S, 10C',
    'Andrea: QH, QC, JS, JD, JC',
    'Peter: JD, JD, JD, JD, JD, JD'
    ]);