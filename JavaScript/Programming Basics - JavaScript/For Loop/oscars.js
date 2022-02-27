function oscars(input){
    let name = input[0];
    let pointFromAcademy = Number(input[1]);
    let numOfJudges = Number(input[2]);
    for (let i = 3; i < input.length; i+=2){
        let VoteName = input[i];
        let points = Number(input[i+1]);
        pointFromAcademy += (VoteName.length * points) / 2;
        if (pointFromAcademy > 1250.5) {
            console.log(`Congratulations, ${name} got a nominee for leading role with ${pointFromAcademy.toFixed(1)}!`);
            return;
        }
    }
    console.log(`Sorry, ${name} you need ${(1250.5-pointFromAcademy).toFixed(1)} more!`);
}

oscars(["Zahari Baharov",
"205",
"4",
"Johnny Depp",
"45",
"Will Smith",
"29",
"Jet Lee",
"10",
"Matthew Mcconaughey",
"39"]);

oscars(["Sandra Bullock",
"340",
"5",
"Robert De Niro",
"50",
"Julia Roberts",
"40.5",
"Daniel Day-Lewis",
"39.4",
"Nicolas Cage",
"29.9",
"Stoyanka Mutafova",
"33"]);