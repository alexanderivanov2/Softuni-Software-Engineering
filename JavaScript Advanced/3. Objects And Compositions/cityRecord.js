function createCityRecord(name, population, treasury) {
    let cityRecord = {
        name: name,
        population: population,
        treasury: treasury,
    }

    return cityRecord; 
}

console.log(createCityRecord('Tortuga',
7000,
15000));