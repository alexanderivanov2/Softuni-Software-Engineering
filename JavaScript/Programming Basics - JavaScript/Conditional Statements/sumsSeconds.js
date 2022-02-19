function sumSeconds (times) {
    let firstTime = Number(times[0]);
    let secondTime = Number(times[1]);
    let thirdTime = Number(times[2]);
    let totalTime = firstTime + secondTime + thirdTime;
    let minutes = Math.floor(totalTime / 60);
    let seconds = totalTime % 60;
    if (seconds < 10) {
        console.log(`${minutes}:0${seconds}`);
    } else {
        console.log(`${minutes}:${seconds}`);
    }
}


sumSeconds(["35",
"45",
"44"]);

sumSeconds(["50",
"50",
"49"]);