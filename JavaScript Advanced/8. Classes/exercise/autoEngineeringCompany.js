function solve(inputCars) {
    // Cars - Brand: {Model: produced}
    let cars = {};

    inputCars.forEach(input => {
        let [brand, model, producedCars] = input.split(' | ');
        producedCars = Number(producedCars);
        
        if (!cars[brand]) {
            cars[brand] = {[model]: producedCars};
        } else if (!cars[brand][model]) {
            cars[brand][model] = producedCars;
        } else {
            cars[brand][model] += producedCars;
        }
    })

    Object.entries(cars).forEach(([model, modelCars]) => {
        console.log(model);

        Object.entries(modelCars).forEach(([brand, produced]) => {
            console.log(`###${brand} -> ${produced}`);
        });
    });
}

solve(['Audi | Q7 | 1000',
'Audi | Q6 | 100',
'BMW | X5 | 1000',
'BMW | X6 | 100',
'Citroen | C4 | 123',
'Volga | GAZ-24 | 1000000',
'Lada | Niva | 1000000',
'Lada | Jigula | 1000000',
'Citroen | C4 | 22',
'Citroen | C5 | 10']);