 function arenaTier(arr) {
    let gladiators = {};
    let el = arr.shift();
    while (el !== "Ave Cesar") {
        if (el.includes('vs')){
            let [name1, name2] = el.split(' vs ');
            if (gladiators.hasOwnProperty(name1) && gladiators.hasOwnProperty(name2)){
                let fight = false;
                for (let skill in gladiators[name1]) {
                    if (skill !== 'total' && gladiators[name2].hasOwnProperty(skill)) {
                        fight = true;
                        break;
                    }
                }
                if (fight) {
                    let one = gladiators[name1]['total'];
                    let two = gladiators[name2]['total'];
                    letDeleteName = one > two ? name2 : name1;
                    delete gladiators[letDeleteName];
                }
            }

        } else {
            let [name, skill, points] = el.split(' -> ');
            points = Number(points)

            if (gladiators.hasOwnProperty(name)) {
                currentSkillPoints = gladiators[name][skill];
                if (gladiators[name].hasOwnProperty(skill) && points >= currentSkillPoints){
                    gladiators[name]['total'] += points - currentSkillPoints;
                } else if (gladiators[name].hasOwnProperty(skill) && points < currentSkillPoints) {
                    points = currentSkillPoints;
                } else {
                    gladiators[name][skill] = points;
                    gladiators[name]['total'] += points;
                }
            } else {
                gladiators[name] = {};
                gladiators[name]['total'] = points;
                gladiators[name][skill] = points;
            }
        }
        


        el = arr.shift();
    }

    let sortedGladiators = Object.entries(gladiators).sort((a, b) => b[1]['total'] - a[1]['total']);
    
    for (let [key, value] of sortedGladiators) {
        console.log(`${key}: ${gladiators[key]['total']} skill`);
        value = Object.entries(value).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
        for (let [key2, value2] of value) {
    
            if (key2 === 'total') {
                continue;
            }
            console.log(`- ${key2} <!> ${value2}`);
        }
    }
}


arenaTier([
    'Peter -> Duck -> 400',
    'Julius -> Shield -> 150',
    'Gladius -> Heal -> 200',
    'Gladius -> Support -> 250',
    'Gladius -> Shield -> 250',
    'Peter vs Gladius',
    'Gladius vs Julius',
    'Gladius vs Maximilian',
    'Ave Cesar'
    ]);
