class Restaurant {
    constructor(budgetMoney) {
        this.budgetMoney = budgetMoney;
        this.menu = {};
        this.stockProducts = {};
        this.history = [];
    }

    loadProducts(products = []) {
        for (let i = 0; i < products.length; i++) {
            let [product, prQuantity, prPrice] = products[i].split(' ');
            prQuantity = Number(prQuantity)
            prPrice = Number(prPrice);

            if (prPrice <= this.budgetMoney) {
                if (!this.stockProducts.hasOwnProperty(product)) {
                    this.stockProducts[product] = 0;
                }

                this.stockProducts[product] += prQuantity;
                this.budgetMoney -= prPrice;
                this.history.push(`Successfully loaded ${prQuantity} ${product}`);

            } else {
                this.history.push(`There was not enough money to load ${prQuantity} ${product}`);
            }
        }

        return this.history.join('\n').trim();
    }

    // addToMenu(meal, neededProducts = [], price) {
    //     let products = [];

    //     for (let info of neededProducts) {
    //         let [product, quantity] = info.split(' ');
    //         quantity = Number(quantity);

    //         products.push([product, quantity]);
    //     }

    //     if (!this.menu.hasOwnProperty(meal)) {
    //         this.menu[meal] = {
    //             products: products,
    //             price: Number(price)
    //         };
    //         let mealCount = Object.keys(this.menu).length;

    //         return mealCount == 1 ? `Great idea! Now with the ${meal} we have 1 meal in the menu, other ideas?` :
    //             `Great idea! Now with the ${meal} we have ${mealCount} meals in the menu, other ideas?`;
    //     }

    //     return `The ${meal} is already in the our menu, try something different.`;
    // }

    makeTheOrder(meal) {
        let targetMeal = this.menu[meal];

        if (targetMeal) {
            for (let [product, quantity] of targetMeal.products) {
                if (!this.stockProducts[product]) {
                    return `For the time being, we cannot complete your order (${meal}), we are very sorry...`

                } else {
                    if (this.stockProducts[product] < quantity) {
                        return `For the time being, we cannot complete your order (${meal}), we are very sorry...`
                    }
                    else {
                        this.stockProducts[product] -= quantity;
                    }
                }
            }
            this.budgetMoney += targetMeal.price;

            return `Your order (${meal}) will be completed in the next 30 minutes and will cost you ${targetMeal.price}.`;
        }

        return `There is not ${meal} yet in our menu, do you want to order something else?`;
    }

    // loadProducts(products) {
    //     products.forEach(product => {
    //         let [productName, productQuantity, productTotalPrice] = product.split(' ');
    //         productQuantity = Number(productQuantity);
    //         productTotalPrice = Number(productTotalPrice);
            
    //         if (productTotalPrice <= this.budgetMoney) {
    //             if(this.stockProducts.hasOwnProperty(productName)) {
    //                 this.stockProducts[productName] = 0;
    //             }
    //             this.budgetMoney -= productTotalPrice;
    //             this.stockProducts[productName] += productQuantity;
    //             this.history.push(`Successfully loaded ${productQuantity} ${productName}`);
    
    //         } else {
    //             this.history.push(`There was not enough money to load ${productQuantity} ${productName}`);
            
    //         }
    //     });

    //     return this.history.join('\n').trim();
    // }

    addToMenu(meal, neededProducts, price) {
        if(this.menu.hasOwnProperty(meal)) {
            return `The ${meal} is already in the our menu, try something different.`;
        }

        let products = [];
        
        neededProducts.forEach(product => {
            let [productName, productQuantity] = product.split(' ');
            productQuantity = Number(productQuantity);
            products.push([productName, productQuantity]);
        });

        this.menu[meal] = {};
        this.menu[meal]['products'] = products;
        this.menu[meal]['price'] = Number(price);

        let lengthOfMenu = Object.keys(this.menu).length;
        if( lengthOfMenu == 1) {
            return `Great idea! Now with the ${meal} we have 1 meal in the menu, other ideas?`;
        }

        return `Great idea! Now with the ${meal} we have ${lengthOfMenu} meals in the menu, other ideas?`;
    }

    showTheMenu() {
        let menuKeys = Object.keys(this.menu);
        if(menuKeys.length == 0) {
            return `Our menu is not ready yet, please come later...`;
        }

        let result = []
        menuKeys.forEach(meal => {
            result.push((`${meal} - $ ${this.menu[meal].price}`));
        });

        return result.join('\n');
    }

    // makeTheOrder(meal) {
    //     if(!this.menu.hasOwnProperty(meal)){
    //         return `There is not ${meal} yet in our menu, do you want to order something else?`
    //     }

    //     Object.entries(this.menu[meal].products).forEach(product => {
    //         let productName = product[0];
    //         let productQuantity = product[1];
    //         if (!this.stockProducts.hasOwnProperty(productName) || this.stockProducts[productName] < productQuantity) {
    //             return `For the time being, we cannot complete your order (${meal}), we are very sorry...`;
    //         }
    //         this.stockProducts[productName] -= productQuantity;
    //     });

    //     // Object.entries(this.menu[meal].products).forEach(product => {
    //     //     let productName = product[0];
    //     //     let productQuantity = product[1];

    //     //     this.stockProducts[productName] -= productQuantity;
    //     // });

    //     this.budgetMoney += this.menu[meal].price;

    //     return `Your order (${meal}) will be completed in the next 30 minutes and will cost you ${this.menu[meal].price}.`
    // }
}

// let kitchen = new Restaurant(1000);
// console.log(kitchen.loadProducts(['Banana 10 5', 'Banana 20 10', 'Strawberries 50 30', 'Yogurt 10 10', 'Yogurt 500 1500', 'Honey 5 50']));

// let kitchen = new Restaurant(1000);
// console.log(kitchen.addToMenu('frozenYogurt', ['Yogurt 1', 'Honey 1', 'Banana 1', 'Strawberries 10'], 9.99));
// console.log(kitchen.addToMenu('Pizza', ['Flour 0.5', 'Oil 0.2', 'Yeast 0.5', 'Salt 0.1', 'Sugar 0.1', 'Tomato sauce 0.5', 'Pepperoni 1', 'Cheese 1.5'], 15.55));

// console.log(kitchen.showTheMenu());
let kitchen = new Restaurant(1000);
kitchen.loadProducts(['Yogurt 30 3', 'Honey 50 4', 'Strawberries 20 10', 'Banana 5 1']);
kitchen.addToMenu('frozenYogurt', ['Yogurt 1', 'Honey 1', 'Banana 1', 'Strawberries 10'], 9.99);
console.log(kitchen.makeTheOrder('frozenYogurt'));