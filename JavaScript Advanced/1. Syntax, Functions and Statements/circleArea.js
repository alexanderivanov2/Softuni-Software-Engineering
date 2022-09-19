function getCircleArea(arg) {
    let typeArg = typeof(arg);
    
    if (typeArg === 'number') {
        let area = Math.PI * (arg**2);
        console.log(area.toFixed(2));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${typeArg}.`);
    }
}

getCircleArea(5);
getCircleArea('name');