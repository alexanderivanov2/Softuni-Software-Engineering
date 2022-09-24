function getJsonForTowns(input) {
    let result = [];
    let regEx = /[^|]+/gm;
    let [town, latitude, longtitude] = input.shift().match(regEx).map(x => x.trim());

    for (let line of input) {
        let obj = {};
        line = line.match(regEx).map(x => x.trim());
        let [name, lati, long] = line;
        lati = Number(lati);
        long = Number(long);
        obj = {
            [town]: name,
            [latitude]: Math.round(lati * 100) / 100,
            [longtitude]: Math.round(long * 100) / 100,
        }
        result.push(obj);
    }

    console.log(JSON.stringify(result));
}

getJsonForTowns(['| Town | Latitude | Longitude |',
'| Sofia | 42.696552 | 23.32601 |',
'| Beijing | 39.913818 | 116.363625 |']);

getJsonForTowns(['| Town | Latitude | Longitude |',
'| Veliko Turnovo | 43.0757 | 25.6172 |',
'| Monatevideo | 34.50 | 56.11 |']);