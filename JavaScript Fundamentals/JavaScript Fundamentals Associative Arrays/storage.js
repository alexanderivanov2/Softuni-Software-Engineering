function storage(arr) {
    let mapper = new Map();

    for (let el of arr) {
        let [name, quantity] = el.split(' ');
        quantity = Number(quantity);

        if (mapper.has(name)) {
            let n = mapper.get(name) + quantity; 
            mapper.set(name, n);
        } else {
            mapper.set(name, quantity);
        }
    }

    for (let [mapKey, mapValue] of mapper.entries()) {
        console.log(`${mapKey} -> ${mapValue}`)
    }
}

storage(['tomatoes 10',
'coffee 5',
'olives 100',
'coffee 40']);