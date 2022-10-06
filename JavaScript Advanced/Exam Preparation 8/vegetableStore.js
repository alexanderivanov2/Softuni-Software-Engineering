class VegetableStore {
    constructor(owner, location) {
        this.owner = owner;
        this.location = location;
        this.availableProducts = [];
    }

    loadingVegetables(vegetables) {
        const loadedVegetables = [];
        
        for (let el of vegetables) {
            let type, quantity, price;
            [type, quantity, price] = el.split(' ');
            quantity = Number(quantity);
            price = Number(price);

            const findVegetables = this.availableProducts.find(veg => veg.type == type);
            if (findVegetables) {
                findVegetables.quantity += quantity;
                if (findVegetables.price < price) {
                    findVegetables.price = price;
                }
            } else {
                this.availableProducts.push({
                    type,
                    quantity,
                    price
                });   
            }

            if (!loadedVegetables.includes(type)){
                loadedVegetables.push(type);
            }

        }
        return `Successfully added ${loadedVegetables.join(', ')}`;
    }

    buyingVegetables(selectedProducts) {
        let totalPrice = 0;

        for (let el of selectedProducts) {
            let [type, quantity] = el.split(' ');
            quantity = Number(quantity);

            const product = this.availableProducts.find(product => product.type == type);

            if (!product) {
                throw new Error(`${type} is not available in the store, your current bill is $${totalPrice.toFixed(2)}.`);
            }

            if (product.quantity < quantity) {
                throw new Error(`The quantity ${quantity} for the vegetable ${type} is not available in the store, your current bill is $${totalPrice.toFixed(2)}.`)
            }

            totalPrice += product.price * quantity;
            product.quantity -= quantity;
        }
        return `Great choice! You must pay the following amount $${totalPrice.toFixed(2)}.`
    }

    rottingVegetable(type, quantity) {
        const product = this.availableProducts.find(el => el.type == type);

        if (!product) {
            throw new Error( `${type} is not available in the store.`);
        }

        if (product.quantity < quantity) {
            product.quantity = 0;

            return `The entire quantity of the ${type} has been removed.`;
        }

        product.quantity -= quantity;

        return `Some quantity of the ${type} has been removed.`;
    }

    revision() {
        const result = ['Available vegetables:'];
        let sortVegetables = this.availableProducts.sort((a, b) => a.price - b.price);
        for (let el of sortVegetables) {
            result.push(`${el.type}-${el.quantity}-$${el.price}`);
        }

        result.push(`The owner of the store is ${this.owner}, and the location is ${this.location}.`)


        return result.join('\n');
    }
} 


let vegStore = new VegetableStore("Jerrie Munro", "1463 Pette Kyosheta, Sofia");

console.log(vegStore.loadingVegetables(["Okra 2.5 3.5", "Beans 10 2.8", "Celery 5.5 2.2", "Celery 0.5 2.5"]));
// console.log(vegStore.rottingVegetable("Okra", 1));
// console.log(vegStore.rottingVegetable("Okra", 2.5));
console.log(vegStore.buyingVegetables(["Beans 8", "Okra 1.5"]));
console.log(vegStore.revision());
// Successfully added Okra, Beans, Celery 
// Some quantity of the Okra has been removed. 
// The entire quantity of the Okra has been removed. 
// Uncaught Error: The quantity 1.5 for the vegetable Okra is not available in the store, your current bill is $22.40.

// Unexpected error: expected 'Great choice! You must pay the following amount 3.5.' to equal 'Great choice! You must pay the following amount $3.50.'
// Unexpected error: expected 'Available vegetables:\nCelery-4.5-2.5\nBeans-2-2.8\nOkra-0-3.5\nThe owner of the store is Jerrie Munro, and the location is 1463 Pette Kyosheta, Sofia.' to equal 'Available vegetables:\nCelery-4.5-$2.5\nBeans-2-$2.8\nOkra-0-$3.5\nThe owner of the store is Jerrie Munro, and the location is 1463 Pette Kyosheta, Sofia.'