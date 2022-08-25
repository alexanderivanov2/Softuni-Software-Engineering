function getNextDay(year, month, day){
    let currDate = new Date(year, month - 1, day);
    let nextDay = currDate.setDate(currDate.getDate() + 1);
    nextDay = new Date(nextDay)
    console.log(`${nextDay.getFullYear()}-${nextDay.getMonth() + 1}-${nextDay.getDate()}`);

}

getNextDay(2016, 9, 30);