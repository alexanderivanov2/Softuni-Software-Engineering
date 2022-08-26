function dayOfWeek(num){
    let days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
    let currIndex = num - 1;
    let result = num >= 1 && num <= 7 ? days[currIndex] : 'Invalid day!';
    console.log(result);
}

dayOfWeek(3);
dayOfWeek(11);