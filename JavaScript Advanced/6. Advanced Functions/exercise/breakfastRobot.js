function solution () {
    let storage = {
        protein: 0,
        carbohydrate: 0,
        fat: 0,
        flavour: 0
    }

    let recipes = {
        apple: {carbohydrate: 1, flavour: 2},
        lemonade: {carbohydrate: 10, flavour: 20},
        burger: {carbohydrate: 5, fat: 7, flavour: 3},
        eggs: {protein: 5, fat: 1, flavour: 1},
        turkey: {protein: 10, carbohydrate: 10, fat: 10, flavour: 10}
    }

    function manage(input) {
        
        function restock(microelement, quantity) {
            storage[microelement] += quantity;
            return 'Success';
        }

        function prepare(recipe, quantity) {
            let needSupplies = calcNeedSupplies(recipe, quantity);

            let checkStorageSupplies = checkStorage(needSupplies);

            if (checkStorageSupplies !== true) {
                return `Error: not enough ${checkStorageSupplies} in stock`;
            }

            removeSuppliesFromStorage(needSupplies);

            return 'Success'
        }

        function calcNeedSupplies(recipe, quantity) {
            let needForOnePortion = recipes[recipe];
            let obj = {}
            Object.keys(needForOnePortion).forEach(key => {
                obj[key] = needForOnePortion[key] * quantity;
            });
            
            return obj;
        }

        function checkStorage(needSupplies) {
            let enough = true;
            for (let key of Object.keys(needSupplies)){
                if (needSupplies[key] > storage[key]) {
                    return key;
                }
            }
            return enough;
        } 

        function removeSuppliesFromStorage(needSupplies) {
            Object.keys(needSupplies).forEach(key =>{
                storage[key] -= needSupplies[key];
            }) 
        }

        function report() {
            let storageReport = [];
            Object.entries(storage).forEach((a) => {
                storageReport.push(`${a[0]}=${a[1]}`);
            })
            return storageReport.join(' ');
        }

        // Main
        let [funcName, info, quantity] = input.split(' ');
        quantity = Number(quantity);

        let result = '';
  
        if (funcName == 'restock') {
            result = restock(info, quantity);
        } else if (funcName == 'prepare') {
            result = prepare(info, quantity);
        } else if (funcName == 'report') {
            result = report();
        }
        
        return result
    }
    return manage;
}

let manager = solution (); 
console.log (manager ("restock flavour 50")); // Success 
console.log (manager ("prepare lemonade 4")); // Error: not enough carbohydrate in stock 
console.log(manager('report'));
console.log(manager('restock carbohydrate 10'));
console.log(manager('restock flavour 10'));
console.log(manager('prepare apple 1'));
console.log(manager('restock fat 10'));
console.log(manager('prepare burger 1'));
console.log(manager('report'));