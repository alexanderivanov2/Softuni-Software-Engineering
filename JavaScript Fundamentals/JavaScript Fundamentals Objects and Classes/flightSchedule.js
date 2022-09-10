function flightSchedule(inputArr) {
    let arrAllFlights = inputArr[0];
    let changedFlights = inputArr[1];
    let status = inputArr[2][0];
    let flights = [];

    for (let flight of arrAllFlights) {
        let tokens = flight.split(' ');
        flightID = tokens.shift();
        Destination = tokens.join(' ');
        let obj = {
            flightID,
            Destination,
            Status: 'Ready to fly'
        }

        flights.push(obj);
    }

    for (let changeFlight of changedFlights) {
        let [flightID, newStatus] = changeFlight.split(' ');
        let foundFlight = flights.find(element => element.flightID === flightID);
        if (foundFlight) {
            foundFlight.Status = newStatus;
        }
    }
    
    for (let obj of flights) {
        // console.log(obj.status);
        // console.log(status);
        if (obj.Status === status) {
            delete obj.flightID;
            console.log(obj);
        }
    }
}

flightSchedule([['WN269 Delaware',
'FL2269 Oregon',
 'WN498 Las Vegas',
 'WN3145 Ohio',
 'WN612 Alabama',
 'WN4010 New York',
 'WN1173 California',
 'DL2120 Texas',
 'KL5744 Illinois',
 'WN678 Pennsylvania'],
 ['DL2120 Cancelled',
 'WN612 Cancelled',
 'WN1173 Cancelled',
 'SK430 Cancelled'],
 ['Cancelled']
]);