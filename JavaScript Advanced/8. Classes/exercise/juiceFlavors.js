function solve(input) {
    let juiceQuanity = {};
    let juiceBottles = {};

    input.forEach(element => {
        let [name, quantity] = element.split(' => ');
        quantity = Number(quantity);
        
        if (!juiceQuanity[name]) {
            juiceQuanity[name] = 0;
        }
        juiceQuanity[name] += quantity;

        while(juiceQuanity[name] >= 1000) {
            if (!juiceBottles[name]) {
                juiceBottles[name] = 0;
            }
            juiceBottles[name] += 1;
            juiceQuanity[name] -= 1000;
        }
    });

    Object.entries(juiceBottles).forEach(([name, bottles]) => {
        console.log(`${name} => ${bottles}`);
    });
}


solve(['Orange => 2000',
'Peach => 1432',
'Banana => 450',
'Peach => 600',
'Strawberry => 549']);

solve(['Kiwi => 234',
'Pear => 2345',
'Watermelon => 3456',
'Kiwi => 4567',
'Pear => 5678',
'Watermelon => 6789']);