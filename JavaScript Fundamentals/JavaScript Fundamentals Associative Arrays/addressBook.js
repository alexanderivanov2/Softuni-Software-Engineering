function addressBook(arr) {
    let book = {};
    for (let el of arr) {
        let [personName, address] = el.split(':');
        book[personName] = address;
    }

    let objectEntries = Object.entries(book);

    objectEntries.sort((a, b) => {
         return a[0].localeCompare(b[0]);
        });
    
    for (let [key, value] of objectEntries) {
        console.log(`${key} -> ${value}`);
    }
}


addressBook(['Tim:Doe Crossing',
'Bill:Nelson Place',
'Peter:Carlyle Ave',
'Bill:Ornery Rd']);