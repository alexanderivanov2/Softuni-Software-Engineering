function carFactory(obj) {
    let currObj = obj;
    let power = currObj.power;
    let color = currObj.color;
    let carriage = currObj.carriage;
    let wheelsize = Math.floor(currObj.wheelsize);
    let car = {
        model: currObj.model,   
    }
    car.engine = {}
    if (power <= 90) {
        car.engine.power = 90;
        car.engine.volume = 1800;
        
    } else if (power <= 120) {
        car.engine.power = 120;
        car.engine.volume = 2400;
        
    } else {
        car.engine.power = 200;
        car.engine.volume = 3500;
    }

    car.carriage = {
        type: carriage,
        'color': color, 
    }

    wheelsize = wheelsize % 2 == 0 ? wheelsize - 1 : wheelsize;

    car.wheels = [wheelsize, wheelsize, wheelsize, wheelsize];

    return car;
}



/result/
// { model: 'VW Golf II',
//   engine: { power: 90,
//             volume: 1800 },
//   carriage: { type: 'hatchback',
//               color: 'blue' },
//   wheels: [13, 13, 13, 13] }

console.log(carFactory({ model: 'VW Golf II',
power: 90,
color: 'blue',
carriage: 'hatchback',
wheelsize: 14 }));