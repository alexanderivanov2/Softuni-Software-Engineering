function travelTime(arr) {
    let travels = {};

    for (let el of arr) {
        let[country, town, cost] = el.split(' > ');
            cost = Number(cost);
        if (travels.hasOwnProperty(country)) {
            let savedCost = travels[country][town];
            if (travels[country].hasOwnProperty(town) && savedCost < cost) {
                travels[country][town] = savedCost;
            } else {
                travels[country][town] = cost;
            }
        } else {
            travels[country] = {}
            travels[country][town] = cost;
            
        }
    }

    let sortKeys = Object.keys(travels).sort((a, b) => a.localeCompare(b)); 

    for (let key of sortKeys) {
        let result = `${key} ->`;
        let sortTowns = Object.entries(travels[key]).sort((a, b) => a[1] - b[1]);
        for (let [key, value] of sortTowns){
            result += ` ${key} -> ${value}`;
        }

        console.log(result);
    }
}

travelTime([
'Bulgaria > Sofia > 25000',
'Bulgaria > Sofia > 25000',
'Kalimdor > Orgrimar > 25000',
'Albania > Tirana > 25000',
'Bulgaria > Varna > 25010',
'Bulgaria > Lukovit > 10'
]);