function schoolGrades(arr) {
    let students = {};
    for (let el of arr) {
        let [name, ...grades] = el.split(' ');
        
        if (students.hasOwnProperty(name)) {
            students[name] = students[name].concat(grades);
        } else {
            students[name] = grades; 
        }
    }

    let sortStudents = Object.keys(students).sort((a, b) => a.localeCompare(b));

    for (let key of sortStudents) {
        let currentGrade = students[key].reduce((a, b) => Number(a) + Number(b));
        currentGrade /= students[key].length;
        console.log(`${key}: ${currentGrade.toFixed(2)}`);
    }
}


schoolGrades(['Lilly 4 6 6 5',
'Tim 5 6',
'Tammy 2 4 3',
'Tim 6 6']);