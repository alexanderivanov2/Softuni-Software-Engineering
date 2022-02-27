function calculatePorcentForPartsOfHistorgram(input){
    let lengthOfNums = Number(input[0]);
    p1 = 0;
    p2 = 0;
    p3 = 0;
    p4 = 0;
    p5 = 0;
    for (let i = 1; i <= lengthOfNums; i++){
        let num = Number(input[i]);
        if (num < 200){
            p1 += 1;
        } else if (num < 400){
            p2 += 1;
        } else if (num < 600){
            p3 += 1;
        } else if (num < 800){
            p4 += 1;
        } else if (num >= 800){
            p5 += 1;
        }
    }
    console.log(`${(p1/lengthOfNums * 100).toFixed(2)}%`);
    console.log (`${(p2/lengthOfNums*100).toFixed(2)}%`);
    console.log(`${(p3/lengthOfNums*100).toFixed(2)}%`);
    console.log(`${(p4/lengthOfNums*100).toFixed(2)}%`);
    console.log(`${(p5/lengthOfNums*100).toFixed(2)}%`);
}


calculatePorcentForPartsOfHistorgram(["3",
"1",
"2",
"999"]);

calculatePorcentForPartsOfHistorgram(["14",
"53",
"7",
"56",
"180",
"450",
"920",
"12",
"7",
"150",
"250",
"680",
"2",
"600",
"200"]);