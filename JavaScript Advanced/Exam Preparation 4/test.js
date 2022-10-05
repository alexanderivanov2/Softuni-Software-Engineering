class Restaurant {
    constructor(budgetMoney) {
        this.budgetMoney = budgetMoney;
        this.menu = {};
        this.stockProducts = {};
        this.history = [];
    }

    loadProducts(products) {
        products.forEach(product => {
            let [productName, productQuantity, productTotalPrice] = product.split(' ');
            productQuantity = Number(productQuantity);
            productTotalPrice = Number(productTotalPrice);
            
            if (productTotalPrice <= this.budgetMoney) {
                if(!this.stockProducts.hasOwnProperty(productName)) {
                    this.stockProducts[productName] = 0;
                }
                this.budgetMoney -= productTotalPrice;
                this.stockProducts[productName] += productQuantity;
                this.history.push(`Successfully loaded ${productQuantity} ${productName}`);
    
            } else {
                this.history.push(`There was not enough money to load ${productQuantity} ${productName}`);
            
            }
        });

        return this.history.join('\n').trim();
    }

    addToMenu(meal, neededProducts, price) {
        if(this.menu.hasOwnProperty(meal)) {
            return `The ${meal} is already in the our menu, try something different.`;
        }

        let products = [];
        
        neededProducts.forEach(product => {
            let [productName, productQuantity] = product.split(' ');
            productQuantity = Number(productQuantity);
            products.push(productName, productQuantity);
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

    makeTheOrder(meal) {
        if(!this.menu.hasOwnProperty(meal)){
            return `There is not ${meal} yet in our menu, do you want to order something else?`
        }

        Object.entries(this.menu[meal].products).forEach(product => {
            let productName = product[0];
            let productQuantity = product[1];
            if (!this.stockProducts.hasOwnProperty(productName) || this.stockProducts[productName] < productQuantity) {
                return `For the time being, we cannot complete your order (${meal}), we are very sorry...`;
            }
            this.stockProducts[productName] -= productQuantity;
        });

        this.budgetMoney += this.menu[meal].price;

        return `Your order (${meal}) will be completed in the next 30 minutes and will cost you ${this.menu[meal].price}.`
    }
}