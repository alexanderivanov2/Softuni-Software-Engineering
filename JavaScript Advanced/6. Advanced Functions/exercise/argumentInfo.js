function printArgumentInfo(...args) {
    let obj = {};

    for (let arg of args) {
        let typeArg = typeof arg;
        console.log(`${typeArg}: ${arg}`);

        if (!obj[typeArg]) {
            obj[typeArg] = 0;
        }
        obj[typeArg] += 1;
    }

    Object
    .entries(obj)
    .sort((a, b) => b[1] - a[1])
    .forEach(el => {
        console.log(`${el[0]} = ${el[1]}`);        
    });
}

printArgumentInfo('cat', 42, function () { console.log('Hello world!'); })

printArgumentInfo({ name: 'bob'}, 3.333, 9.999);