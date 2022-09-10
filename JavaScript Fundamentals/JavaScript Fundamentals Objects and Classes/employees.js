function employees(inputArr) {
    function createObject(name) {
        let obj = {
            name: name,
            personalNum: name.length
        }
        return obj;
    }

    let arr = [];

    for (let el of (inputArr)) {
        arr.push(createObject(el));
    }

    for (let obj of arr) {
        console.log(`Name: ${obj.name} -- Personal Number: ${obj.personalNum}`);
    }
}


employees([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ])