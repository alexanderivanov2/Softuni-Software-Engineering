function calculatePriceForVacantion(students, group, whichDay){
    let numOfStudents = students;
    let typeOfGroup = group;
    let day = whichDay;
    let costPerPerson = 0;
    switch(day){
        case 'Friday':
            switch(typeOfGroup){
                case 'Students': costPerPerson = 8.45; break;
                case 'Business': costPerPerson = 10.90; break;
                case 'Regular': costPerPerson = 15; break;
            }; break;
        case 'Saturday':
            switch(typeOfGroup){
                case 'Students': costPerPerson = 9.80; break;
                case 'Business': costPerPerson = 15.60; break;
                case 'Regular': costPerPerson = 20; break;              
            }; break;
        case 'Sunday':
            switch(typeOfGroup){
                case 'Students': costPerPerson = 10.46; break;
                case 'Business': costPerPerson = 16; break;
                case 'Regular': costPerPerson = 22.50; break;
            }; break;
    }

    let totalCost = numOfStudents * costPerPerson;
    if(typeOfGroup === 'Students' && numOfStudents >= 30) {
        totalCost *= 0.85;
    } else if (typeOfGroup === 'Business' && numOfStudents >= 100) {
        totalCost -= 10 * costPerPerson;
    } else if(typeOfGroup === 'Regular' && numOfStudents >= 10 && numOfStudents <= 20) {
        totalCost *= 0.95;
    }

    console.log(`Total price: ${totalCost.toFixed(2)}`);
}

calculatePriceForVacantion(30,'Students', 'Sunday');
calculatePriceForVacantion(40,
    "Regular",
    "Saturday");