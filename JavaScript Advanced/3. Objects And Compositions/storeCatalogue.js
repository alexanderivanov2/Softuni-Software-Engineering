function storeCatalogue(input) {
    let objCatalogue = {};
    for (let product of input) {
        let [name, price] = product.split(' : ');
        
        price = Number(price);
        let letter = name[0];

        if (objCatalogue[letter]) {
            objCatalogue[letter][name] = price;
        } else {
            objCatalogue[letter] = {
                [name]: price,
            }
        }
    }

    let keysSort = Object.keys(objCatalogue).sort((a, b) => a.localeCompare(b));

    for (let key of keysSort) {
        console.log(`${key}`);
        // console.log(objCatalogue[key]);
        let sortObjects = Object.entries(objCatalogue[key]).sort((a, b) => a[0].localeCompare(b[0]));
        for (let [key, value] of sortObjects) {
            console.log(` ${key}: ${value}`);
        }
    }
}

storeCatalogue(['Appricot : 20.4',
'Fridge : 1500',
'TV : 1499',
'Deodorant : 10',
'Boiler : 300',
'Apple : 1.25',
'Anti-Bug Spray : 15',
'T-Shirt : 10']);