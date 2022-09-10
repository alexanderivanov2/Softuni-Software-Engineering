function schoolRegister(jsonArr) {
    let grades = [] 
    for (let el of jsonArr) {
        allTokens = el.split(',');
        let name = allTokens[0].split('Student name: ')[1];
        let grade = Number(allTokens[1].split(' Grade: ')[1]) + 1;
        let averageScore =  Number(allTokens[2].split(': ')[1]);
        let findGrade = grades.find( gr => gr.grade === grade);
        
        if (findGrade && averageScore >= 3) {
            findGrade.names.push(name);
            findGrade.scores.push(averageScore);
        } else if (averageScore >= 3) {
            let obj = {
                names: [name],
                grade,
                scores: [averageScore]
            }

            grades.push(obj);      
        }
     }

     grades.sort((a, b) => a.grade - b.grade);

     for (let obj of grades) {
         let averageGrade = obj.scores.reduce((a, b) => a + b, 0);
         averageGrade /= obj.scores.length;
         
         console.log(`${obj.grade} Grade \nList of students: ${obj.names.join(', ')}\nAverage annual grade from last year: ${averageGrade.toFixed(2)}\n`);
     }
}


schoolRegister([
    "Student name: Mark, Grade: 8, Graduated with an average score: 4.75",
        "Student name: Ethan, Grade: 9, Graduated with an average score: 5.66",
        "Student name: George, Grade: 8, Graduated with an average score: 2.83",
        "Student name: Steven, Grade: 10, Graduated with an average score: 4.20",
        "Student name: Joey, Grade: 9, Graduated with an average score: 4.90",
        "Student name: Angus, Grade: 11, Graduated with an average score: 2.90",
        "Student name: Bob, Grade: 11, Graduated with an average score: 5.15",
        "Student name: Daryl, Grade: 8, Graduated with an average score: 5.95",
        "Student name: Bill, Grade: 9, Graduated with an average score: 6.00",
        "Student name: Philip, Grade: 10, Graduated with an average score: 5.05",
        "Student name: Peter, Grade: 11, Graduated with an average score: 4.88",
        "Student name: Gavin, Grade: 10, Graduated with an average score: 4.00"
    ]);