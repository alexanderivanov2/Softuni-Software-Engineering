function city (city) {    
    let cityKeys = Object.keys(city);

    for (let key of cityKeys) {
        console.log(`${key} -> ${city[key]}`);
    }
}

console.log(city({
    name: "Sofia",
    area: 492,
    population: 1238438,
    country: "Bulgaria",
    postCode: "1000"
}));