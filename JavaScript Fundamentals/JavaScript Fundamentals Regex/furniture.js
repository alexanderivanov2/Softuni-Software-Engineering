function solve(input) {
    let pattern = />>\b(?<name>[A-Za-z]+)<<(?<price>\d+|\d+\.\d+)\!(?<quantity>\d+)/g;
    let bought = [];
    let totalMoney = 0;
    
    for (let el of input) {
        if(el.match(pattern)) {
            let match = pattern.exec(el);
            let {name, price, quantity} = match.groups;
            bought.push(name);
            totalMoney += Number(price) * Number(quantity);
        }
    }

    console.log('Bought furniture:');
    if (bought.length > 0) {
        console.log(bought.join('\n'));
    }
    console.log(`Total money spend: ${totalMoney.toFixed(2)}`);
}

// solve(['>>Laptop<<312.2323!3',
// '>>TV<<300.21314!5',
// '>Invalid<<!5',
// '>>TV<<300.21314!20',
// '>>Invalid<!5',
// '>>TV<<30.21314!5',
// '>>Invalid<<!!5',
// 'Purchase']);

// solve(['>>Sofa<<312.23!3',
// '>>TV<<300!5',
// '>Invalid<<!5',
// 'Purchase']);

solve(['>Invalid<<!4',
'>Invalid<<!2',
'>Invalid<<!5',
'Purchase']);