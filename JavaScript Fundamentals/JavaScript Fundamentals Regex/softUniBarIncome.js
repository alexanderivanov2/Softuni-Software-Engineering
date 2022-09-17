function solve(input) {
    let pattern = /%(?<name>[A-Z][a-z]+)%[^\%\.\$\|]*<(?<product>\w+)>[^\%\.\$\|]*\|(?<count>\d+)\|[^\%\.\$\|\d]*(?<price>\d+|\d+\.\d+)\$/g;
    let totalIncome = 0;

    let txt = input.shift();

    while(txt !== 'end of shift') {
        if (txt.match(pattern)) {
            let match = pattern.exec(txt);
            let {name, product, count, price} = match.groups;
            let cost = Number(count) * Number(price);
            console.log(`${name}: ${product} - ${cost.toFixed(2)}`);
            totalIncome += cost;
        }

        txt = input.shift();

    }

    console.log(`Total income: ${totalIncome.toFixed(2)}`);
}

solve(['%George%<Croissant>|2|10.3$',
'%Peter%<Gum>|1|1.3$',
'%Maria%<Cola>|1|2.4$',
'end of shift']);

solve(['%InvalidName%<Croissant>|2|10.3$',
'%Peter%<Gum>1.3$',
'%Maria%<Cola>|1|2.4',
'%Valid%<Valid>valid|10|valid20$',
'end of shift']);