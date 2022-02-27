function histogramOfGroups(input){
    let numOfGroups = Number(input[0]);
    let people = 0;
    let p1 = 0;
    let p2 = 0;
    let p3 = 0;
    let p4 = 0;
    let p5 = 0;
    for (let i = 1; i < input.length; i++){
        let num = Number(input[i]);
        people += num;
        if (num < 6){
            p1 += num;
        } else if (num < 13){
            p2 += num;
        } else if (num < 26){
            p3 += num;
        } else if (num < 41){
            p4 += num;
        } else {
            p5 += num;
        }
    }
    console.log(`${(p1/people*100).toFixed(2)}%`);
    console.log(`${(p2/people*100).toFixed(2)}%`);
    console.log(`${(p3/people*100).toFixed(2)}%`);
    console.log(`${(p4/people*100).toFixed(2)}%`);
    console.log(`${(p5/people*100).toFixed(2)}%`);
}


histogramOfGroups(["10",
"10",
"5",
"1",
"100",
"12",
"26",
"17",
"37",
"40",
"78"]);