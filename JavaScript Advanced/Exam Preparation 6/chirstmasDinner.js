class ChristmasDinner {
    constructor(budget) {
        this.budget = budget;
        this.dishes = [];
        this.products = [];
        this.guests = {};
    }

    get budget() {
        return this._budget
    }

    set budget(value) {
        if (value < 0) {
            throw new Error("The budget cannot be a negative number");
        }

        this._budget = value;
    }

    shopping(productArr) {
        let [product, price] = [...productArr];
        price = Number(price);
        if (price > this.budget) {
            throw new Error('Not enough money to buy this product');
        }

        this.budget -= price;
        this.products.push(product);

        return `You have successfully bought ${product}!`;
    }

    recipes(recipeObj) {
        // {recipeName: string, productList: array of strings}
        recipeObj.productsList.forEach(product => {
            if (!this.products.includes(product)) {
                throw new Error('We do not have this product');
            }
        })
        this.dishes.push(recipeObj);

        return `${recipeObj.recipeName} has been successfully cooked!`;
    }

    inviteGuests(name, dish) {
        ;
        const dishes = Object
            .values(this.dishes)
            .map(obj => obj.recipeName)
            .find(k => k === dish); 
        if (!dishes) {
            throw new Error('We do not have this dish');
        }

        const guest = Object.keys(this.guests).find(k => k == name);

        if (guest) {
            throw new Error('This guest has already been invited');
        }

        this.guests[name] = dish;

        return `You have successfully invited ${name}!`
    }

    showAttendance() {
        const result = [];
        Object.keys(this.guests)
            .forEach(name => {
                const dish = this.guests[name];
                const products = Object
                .values(this.dishes)
                .find(obj => obj.recipeName === dish)
                .productsList;
                
                result.push(`${name} will eat ${dish}, which consists of ${products.join(', ')}`);
            });

        return result.join('\n');
    }
}


let dinner = new ChristmasDinner(300);

console.log(dinner.budget);

dinner.shopping(['Salt', 1]);
dinner.shopping(['Beans', 3]);
dinner.shopping(['Cabbage', 4]);
dinner.shopping(['Rice', 2]);
dinner.shopping(['Savory', 1]);
dinner.shopping(['Peppers', 1]);
dinner.shopping(['Fruits', 40]);
dinner.shopping(['Honey', 10]);

dinner.recipes({
    recipeName: 'Oshav',
    productsList: ['Fruits', 'Honey']
});
dinner.recipes({
    recipeName: 'Folded cabbage leaves filled with rice',
    productsList: ['Cabbage', 'Rice', 'Salt', 'Savory']
});
dinner.recipes({
    recipeName: 'Peppers filled with beans',
    productsList: ['Beans', 'Peppers', 'Salt']
});

dinner.inviteGuests('Ivan', 'Oshav');
dinner.inviteGuests('Petar', 'Folded cabbage leaves filled with rice');
dinner.inviteGuests('Georgi', 'Peppers filled with beans');

console.log(dinner.showAttendance());

// Ivan will eat Oshav, which consists of Fruits, Honey
// Petar will eat Folded cabbage leaves filled with rice, which consists of Cabbage, Rice, Salt, Savory
// Georgi will eat Peppers filled with beans, which consists of Beans, Peppers, Salt