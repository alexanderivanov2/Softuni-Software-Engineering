function needTimeForBreak (input) {
    let serialName = input[0];
    let episodeTime = Number(input[1]);
    let breakTime = Number(input[2]);
    let timeForLunch = breakTime * 1/8;
    let timeForRest = breakTime * 1/4;
    let needMinutesForBreak = episodeTime + timeForLunch + timeForRest;
    if (breakTime >= needMinutesForBreak) {
        console.log(`You have enough time to watch ${serialName} and left with ${Math.ceil(breakTime-needMinutesForBreak)} minutes free time.`)
    } else {
        console.log(`You don't have enough time to watch ${serialName}, you need ${Math.ceil(needMinutesForBreak-breakTime)} more minutes.`)
    }
}


needTimeForBreak(["Game of Thrones",
"60",
"96"]);

needTimeForBreak(["Teen Wolf",
"48",
"60"]);
