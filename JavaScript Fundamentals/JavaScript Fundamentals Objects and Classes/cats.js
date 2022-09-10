function createCatsClass(input) {
    class Cat {
        constructor(name, age) {
            this.name = name,
            this.age = age
        }

        meow () {
            console.log(`${this.name}, age ${this.age} says Meow`)
        }
    }

    for (let el of input) {
        let [name, age] = el.split(' ');
        age = Number(age);
        let cat = new Cat(name, age);
        cat.meow();
    }

};

createCatsClass(['Mellow 2', 'Tom 5'])