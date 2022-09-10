function storeProvision (inputArr1, inputArr2) {
    function createObj(product, quantity) {
        let obj = {
            product,
            quantity
        }
        
        return obj;
    }
    let inputArr = [inputArr1, inputArr2];
    let arrOfObj = [];

    for (let el of inputArr) {
        for (let i = 0; i < el.length; i+=2) {
            let inside = false;
            let product = el[i];
            let quantity = Number(el[i + 1]);

            for (let obj of arrOfObj) {
                if (obj.product === product) {
                    obj.quantity += quantity;
                    inside = true;
                    break;
                }
            }
            if (!inside) {
                arrOfObj.push(createObj(product, quantity));
            }
        }
    }

    for (let obj of arrOfObj) {
        console.log(`${obj.product} -> ${obj.quantity}`);
    }
}

storeProvision([
    'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
    'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ]);