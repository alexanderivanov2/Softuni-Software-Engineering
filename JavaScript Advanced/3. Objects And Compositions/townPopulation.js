function getTownsPopulation(arrTowns) {
    let townsPopulation = {};

    for (let data of arrTowns) {
        let [town, population] = data.split(' <-> ');
        population = Number(population);

        if (townsPopulation[town]) {
            townsPopulation[town] = population;
        } else {
            townsPopulation[town] += population
        }
    }

    Object.keys(townsPopulation).forEach((x) =>{
        console.log(`${x} : ${townsPopulation[x]}`)
    });
}


getTownsPopulation(['Sofia <-> 1200000',
'Montana <-> 20000',
'New York <-> 10000000',
'Washington <-> 2345000',
'Las Vegas <-> 1000000']);


getTownsPopulation(['Istanbul <-> 100000',
'Honk Kong <-> 2100004',
'Jerusalem <-> 2352344',
'Mexico City <-> 23401925',
'Istanbul <-> 1000']);