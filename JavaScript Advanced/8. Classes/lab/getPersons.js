function getPersons() {
    class Person {
        constructor(firstName, lastName, age, email) {
            this.firstName = firstName;
            this.lastName = lastName;
            this.age = age;
            this.email = email;
        }
    
        toString = () => {
            return `${this.firstName} ${this.lastName} (age: ${this.age}, email: ${this.email})`;
        }
    }

    let personsDAta = [['Anna', 'Simpson', 22, 'anna@yahoo.com'], ['SoftUni'], ['Stephan', 'Johnson', 25], ['Gabriel', 'Peterson', 24, 'g.p@gmail.com']];

    let arrOfPersonInstances = personsDAta.map(arr => {
        let person = new Person(...arr);
        return person;
    });

    return arrOfPersonInstances;
}

console.log(getPersons());