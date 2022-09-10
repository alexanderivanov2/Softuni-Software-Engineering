function personInfo(name, secondName, inputAge) {
    let person = {
        firstName: name,
        lastName: secondName,
        age: Number(inputAge)
    }
    return person;
}

console.log(personInfo("Peter", 
"Pan",
"20"));