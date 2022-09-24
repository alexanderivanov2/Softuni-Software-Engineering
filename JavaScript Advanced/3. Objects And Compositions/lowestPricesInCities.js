function getLowestPrices(input) {
    let objects = {}
    for (let el of input) {
        let [townName, productName, price] = el.split(" | ")
        price = Number(price);
        if (objects[productName]) {
            if (objects[productName]['price'] > price){
                objects[productName].price = price;
                objects[productName].townName = townName;
            }
        } else {
            objects[productName] = {
                price: price,
                townName: townName,
            }
        }
    } 
    for (obj in objects){
        console.log(`${obj} -> ${objects[obj].price} (${objects[obj].townName})`);
    }
}

getLowestPrices(['New York | Sample Product | 1000.1', 'Sample Town | Sample Product | 1000',
'Sample Town | Orange | 2',
'Sample Town | Peach | 1',
'Sofia | Orange | 3',
'Sofia | Peach | 2',
'New York | Burger | 10']);