function isLeapYear(inputYear) {
    let year = inputYear;
    if (year % 4 === 0  && (year % 400 === 0 || year % 100 !== 0)){
        console.log('yes');
    } else {
        console.log('no');
    }
}

isLeapYear(1984);
isLeapYear(2003);
isLeapYear(4);
isLeapYear(2000);