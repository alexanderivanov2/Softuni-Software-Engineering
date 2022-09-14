function meetings(arr) {
    let schedule = {};

    for (let el of arr) {
        let [day, personName] = el.split(' ');
        
        if (schedule.hasOwnProperty(day)) {
            console.log(`Conflict on ${day}!`);
        } else {
            console.log(`Scheduled for ${day}`);
            schedule[day] = personName;
        }
    }

    for (let [key, value] of Object.entries(schedule)) {
        console.log(`${key} -> ${value}`);
    }
}


meetings(['Monday Peter',
'Wednesday Bill',
'Monday Tim',
'Friday Tim']);