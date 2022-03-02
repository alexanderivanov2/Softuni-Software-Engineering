function traveling(input){
    let i = 0;
    while(input[i] !== 'End'){
        let destination = input[i];
        i++;
        let price = Number(input[i]);
        let savePrice = 0;
        i++;
        let action;
        while(parseInt(input[i])){
                action = Number(input[i]);
                savePrice += action;
                i++;
                action = input[i]
        }
        if (savePrice >= price){
        console.log(`Going to ${destination}!`)
        }
    }
}

traveling(["Greece",
"1000",
"200",
"200",
"300",
"100",
"150",
"240",
"Spain",
"1200",
"300",
"500",
"193",
"423",
"End"]);