function rankingPoints(input){
    let numOfTournaments = Number(input[0]);
    let startingPoints = Number(input[1]);
    let winPoints = 0;
    let winTournaments = 0;
    for (let i = 2; i <= input.length; i++){
        let result = input[i];
        switch(result){
            case 'W':  winPoints += 2000; winTournaments += 1; break;
            case 'F': winPoints += 1200; break;
            case 'SF': winPoints += 720; break;
        }
    }
    console.log(`Final points: ${startingPoints + winPoints}`);
    console.log(`Average points: ${Math.trunc(winPoints / numOfTournaments)}`);
    console.log(`${(winTournaments/numOfTournaments * 100).toFixed(2)}%`);
}

rankingPoints(["5",
"1400",
"F",
"SF",
"W",
"W",
"SF"]);

rankingPoints(["7",
"1200",
"SF",
"F",
"W",
"F",
"W",
"SF",
"W"]);