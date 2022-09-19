function printRoadRadar(speed, area) {
    function getStatus(overSpeed) {
        if (overSpeed <= 20) {
            return 'speeding'
        } else if (overSpeed <= 40) {
            return 'excessive speeding'
        } else {
            return 'reckless driving'
        }
    }

    if (area === 'residential') {
        if (speed <= 20) {
            console.log(`Driving ${speed} km/h in a 20 zone`)
        } else {
            let overSpeed = speed - 20;
            let status = getStatus(overSpeed);
            console.log(`The speed is ${overSpeed} km/h faster than the allowed speed of 20 - ${status}`)
        }
    } else if (area === 'city') {
        if (speed <= 50) {
            console.log(`Driving ${speed} km/h in a 50 zone`)
        } else {
            let overSpeed = speed - 50;
            let status = getStatus(overSpeed);
            console.log(`The speed is ${overSpeed} km/h faster than the allowed speed of 50 - ${status}`)
        }
    } else if (area === 'interstate') {
        if (speed <= 90) {
            console.log(`Driving ${speed} km/h in a 90 zone`)
        } else {
            let overSpeed = speed - 90;
            let status = getStatus(overSpeed);
            console.log(`The speed is ${overSpeed} km/h faster than the allowed speed of 90 - ${status}`)
        }
    } else  if (area === 'motorway') {
        if (speed <= 130) {
            console.log(`Driving ${speed} km/h in a 130 zone`)
        } else {
            let overSpeed = speed - 130;
            let status = getStatus(overSpeed);
            console.log(`The speed is ${overSpeed} km/h faster than the allowed speed of 130 - ${status}`)
        }
    }
}

printRoadRadar(40, 'city');
printRoadRadar(21, 'residential');
printRoadRadar(120, 'interstate');
printRoadRadar(200, 'motorway');