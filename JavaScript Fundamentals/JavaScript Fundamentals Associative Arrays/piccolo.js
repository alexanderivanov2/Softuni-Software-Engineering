function piccolo(arr) {
    let obj = [];

    for (let el of arr) {
        let [action, number] = el.split(', ');
        if (action === "IN" && !obj.includes(number)) {
            obj.push(number)
        } else if (action === "OUT" && obj.includes(number)) {
            obj.splice(obj.indexOf(number), 1);
        }
    }

    if (obj.length > 0){
        obj.sort((a, b) => a.localeCompare(b));
        console.log(obj.join('\n'));
    } else {
        console.log('Parking Lot is Empty');
    }
}

piccolo(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU']);