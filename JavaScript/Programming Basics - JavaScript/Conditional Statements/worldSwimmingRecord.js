function calculateWorldRecord (input) {
    let worldRecord = Number(input[0]);
    let distanceInMeters = Number(input[1]);
    let timeInSecondsForOneMeter = Number(input[2]);
    let totalTime = distanceInMeters * timeInSecondsForOneMeter;
    totalTime += Math.floor(distanceInMeters / 15) * 12.5;
    if (worldRecord <= totalTime) {
        console.log(`No, he failed! He was ${(totalTime-worldRecord).toFixed(2)} seconds slower.`)
    } else {
        console.log(` Yes, he succeeded! The new world record is ${totalTime.toFixed(2)} seconds.`)
    }
}

calculateWorldRecord(["10464",
"1500",
"20"]);

calculateWorldRecord(["55555.67",
"3017",
"5.03"]);