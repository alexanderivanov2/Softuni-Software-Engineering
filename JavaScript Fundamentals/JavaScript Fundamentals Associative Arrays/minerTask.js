function minerTask(arr) {
    let obj = {};
    
    for (let i = 0; i < arr.length; i+= 2) {
        let resource = arr[i];
        let quantity = Number(arr[i + 1]);

        if (obj.hasOwnProperty(resource)) {
            obj[resource] += quantity;
        } else {
            obj[resource] = quantity;
        }
    }

    for(let key in obj) {
        console.log(`${key} -> ${obj[key]}`);
    }
}

minerTask([
    'gold',
    '155',
    'silver',
    '10',
    'copper',
    '17',
    'gold',
    '15'
    ]);