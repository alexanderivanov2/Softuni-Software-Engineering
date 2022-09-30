class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
        Object.defineProperty(this, 'fullName', {
            get() {
                return `${this.firstName} ${this.lastName}`;
            },

            set(input) {
                let inputSplit = input.split(' ');
                if (inputSplit.length == 2) {
                    this.firstName = inputSplit[0];
                    this.lastName = inputSplit[1];
                }
            }
        })
    }
}



let person = new Person("Peter", "Ivanov");

console.log(Object.getOwnPropertyDescriptors(person));
console.log(person.fullName); //Peter Ivanov
person.firstName = "George";
console.log(person.fullName); //George Ivanov
person.lastName = "Peterson";
console.log(person.fullName); //George Peterson
person.fullName = "Nikola Tesla";
console.log(person.firstName); //Nikola
console.log(person.lastName); //Tesla

person = new Person("Albert", "Simpson");
console.log(person.fullName); //Albert Simpson
person.firstName = "Simon";
console.log(person.fullName); //Simon Simpson
person.fullName = "Peter";
console.log(person.firstName);  // Simon
console.log(person.lastName); 