function calculateGraduation(input){
    let name = input[0];
    let i = 1
    let end = input.length;
    let fails = false;
    let sumOfgrades = 0;
    while (i < end){
        grade = Number(input[i]);
        if (grade < 4.00){
            if (fails){
                console.log(`${name} has been excluded at ${i - 1} grade`);
                return;
            }
            fails = true;
        }
        sumOfgrades += grade;
        i++;
    }
    let averageGrade = sumOfgrades / (end-1);
    console.log(`${name} graduated. Average grade: ${averageGrade.toFixed(2)}`)
}

calculateGraduation(["Gosho", 
"5",
"5.5",
"6",
"5.43",
"5.5",
"6",
"5.55",
"5",
"6",
"6",
"5.43",
"5"]);

calculateGraduation(["Mimi", 
"5",
"6",
"5",
"6",
"5",
"6",
"6",
"2",
"3"]);