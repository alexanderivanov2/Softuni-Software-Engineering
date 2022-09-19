function solve(steps, lenghtFoot, speed) {
    let distance = steps * lenghtFoot
    let speeding = speed 
    let minutesRest = Math.floor(distance / 500)
    let timeTakeing = (distance / speeding) / 1000
    let hh =Math.floor(timeTakeing);
    let mm = Math.floor(timeTakeing * 60);
    let ssCalc = timeTakeing * 60 - mm;
    let ss = Math.round(ssCalc * 60);
    mm += minutesRest
    if (mm > 59){
        hh += 1
        mm -= 60
    }
    if (hh < 10){
        hh = `0${hh}`;
    }
    if (mm < 10) {
        mm = `0${mm}`;
    }
    if (ss < 10) {
        ss = `0${ss}`
    } 
    console.log(`${hh}:${mm}:${ss}`);
}

solve(4000, 0.60, 5);